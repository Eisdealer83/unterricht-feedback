import streamlit as st
import csv, os, pandas as pd, re
from datetime import datetime
from collections import Counter
from openai import OpenAI
from io import BytesIO
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet

# ============ KONFIGURATION ============
DATA_FILE = "feedback_moodle_ki.csv"
KLASSEN = ["", "11BG", "12BG", "13BG", "BÜA", "FOS", "Andere"]
client = OpenAI(api_key=st.secrets.get("OPENAI_API_KEY", None))

# ============ DATEN SCHREIBEN ============
def write_row(row):
    file_exists = os.path.exists(DATA_FILE)
    with open(DATA_FILE, "a", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["timestamp","klasse","verstaendnis","motivation","hilfreich","verbesserung"])
        if not file_exists:
            writer.writeheader()
        writer.writerow(row)

# ============ KI-ZUSAMMENFASSUNG ============
def summarize_with_ai(texts):
    if not client or len(" ".join(texts).strip()) == 0:
        return "Keine Daten zur Zusammenfassung vorhanden."
    try:
        prompt = (
            "Fasse die folgenden anonymen Schülerfeedbacks zu einem Unterrichtstag in 3-4 Sätzen zusammen. "
            "Beschreibe Verständnis, Motivation, positive Aspekte und Verbesserungsvorschläge:\n\n"
            + "\n".join(texts)
        )
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=250,
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"Fehler bei der KI-Auswertung: {e}"

# ============ PDF GENERIERUNG ============
def create_pdf(summary, stats, top_words):
    buffer = BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=A4)
    styles = getSampleStyleSheet()
    elements = []

    elements.append(Paragraph("<b>Unterrichts-Feedback – KI-Zusammenfassung</b>", styles["Title"]))
    elements.append(Spacer(1, 12))
    elements.append(Paragraph(datetime.now().strftime("Erstellt am: %d.%m.%Y, %H:%M Uhr"), styles["Normal"]))
    elements.append(Spacer(1, 20))

    # Statistiken
    elements.append(Paragraph("<b>📊 Durchschnittswerte:</b>", styles["Heading3"]))
    data = [["Kriterium", "Durchschnitt"]] + [[k, f"{v:.2f}"] for k, v in stats.items()]
    t = Table(data)
    t.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (-1,0), colors.lightgrey),
        ("GRID", (0,0), (-1,-1), 0.5, colors.grey),
        ("FONTNAME", (0,0), (-1,0), "Helvetica-Bold")
    ]))
    elements.append(t)
    elements.append(Spacer(1, 20))

    # Häufige Begriffe
    if top_words:
        elements.append(Paragraph("<b>🔤 Häufig genannte Begriffe:</b>", styles["Heading3"]))
        word_text = ", ".join([f"{w} ({c}×)" for w, c in top_words])
        elements.append(Paragraph(word_text, styles["Normal"]))
        elements.append(Spacer(1, 20))

    # KI-Zusammenfassung
    elements.append(Paragraph("<b>🧠 Automatische KI-Zusammenfassung:</b>", styles["Heading3"]))
    elements.append(Paragraph(summary, styles["Normal"]))

    doc.build(elements)
    buffer.seek(0)
    return buffer

# ============ APP ============
st.set_page_config(page_title="KI-Feedback-Agent", layout="centered")
st.markdown("<h2 style='text-align:center;'>🧠 KI-Feedback-Agent zum Unterricht</h2>", unsafe_allow_html=True)

with st.form("feedback_form"):
    klasse = st.selectbox("Klasse (optional)", KLASSEN)
    verstaendnis = st.slider("Ich habe den Unterricht heute gut verstanden.", 1, 5, 3)
    motivation = st.slider("Der Unterricht war motivierend und interessant.", 1, 5, 3)
    hilfreich = st.text_area("Was hat dir heute besonders geholfen?", height=80)
    verbesserung = st.text_area("Was sollte beim nächsten Mal anders sein?", height=80)
    absenden = st.form_submit_button("✅ Feedback absenden")

if absenden:
    write_row({
        "timestamp": datetime.now().isoformat(),
        "klasse": klasse,
        "verstaendnis": verstaendnis,
        "motivation": motivation,
        "hilfreich": hilfreich.strip(),
        "verbesserung": verbesserung.strip(),
    })
    st.success("Danke für dein Feedback! 🙌")
    st.balloons()

st.divider()

# ============ ADMIN-BEREICH ============
if st.checkbox("🔑 Admin-Zusammenfassung anzeigen"):
    if not os.path.exists(DATA_FILE):
        st.warning("Noch keine Rückmeldungen vorhanden.")
    else:
        df = pd.read_csv(DATA_FILE)
        st.write("**Letzte Rückmeldungen:**")
        st.dataframe(df.tail(10))
        st.write("**Durchschnittswerte:**")
        stats = df[["verstaendnis","motivation"]].mean().round(2).to_dict()
        st.write(stats)
        st.write("Gesamtanzahl Rückmeldungen:", len(df))

        # Häufige Begriffe
        all_text = " ".join(df["hilfreich"].fillna("") + " " + df["verbesserung"].fillna(""))
        words = re.findall(r"\b\w{4,}\b", all_text.lower())
        top_words = Counter(words).most_common(10)
        st.write("**Häufig genannte Begriffe:**")
        st.write(", ".join([f"{w} ({c}×)" for w,c in top_words]))

        # KI-Zusammenfassung
        if st.button("🧠 KI-Zusammenfassung erstellen"):
            texts = (df["hilfreich"].fillna("").tolist() + df["verbesserung"].fillna("").tolist())
            summary = summarize_with_ai(texts)
            st.subheader("KI-Zusammenfassung:")
            st.info(summary)

            # PDF-Export
            pdf = create_pdf(summary, stats, top_words)
            st.download_button(
                label="📄 PDF herunterladen",
                data=pdf,
                file_name="feedback_zusammenfassung.pdf",
                mime="application/pdf"
            )

st.divider()
st.markdown("""
<p style="font-size:0.9em; text-align:center; color:gray;">
<b>Datenschutz:</b> Keine personenbezogenen Daten. Rückmeldungen dienen ausschließlich der Unterrichtsentwicklung.
</p>
""", unsafe_allow_html=True)
