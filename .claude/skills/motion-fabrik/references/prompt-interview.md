# Teil 2: Prompt bauen

Ziel: ein kurzer Prompt, der dem Agenten sagt, **was** am Ende stehen soll und
**woran man erkennt, dass es gut ist**. Nicht, wie er es bauen soll. Die Person
muss dafür nichts über Code oder Motion Design wissen.

## Die Fragen

Stelle sie in dieser Reihenfolge. Mit einem Auswahl-Werkzeug dürfen bis zu vier
kurze Fragen auf einmal kommen (Länge, Format, Ton). Offene Fragen (Thema,
Kriterium) einzeln stellen. Was die Person schon erzählt hat, nicht noch einmal
fragen.

1. **Worum geht es?** Thema, Produkt, Link zu einer Webseite oder einem Artikel,
   oder ein Text. Soll ein fertiges Video bearbeitet werden (Longform → Short,
   Schnitt, Untertitel), dann den Pfad zur Datei. Siehe „Fertige Videos“ unten.
2. **Was ist das Ziel, und wer schaut zu?** Zum Beispiel: Erklärvideo für Kunden,
   Werbespot für Social Media, Schulung für Mitarbeitende, Intro für YouTube.
3. **Wie lang?** Vorschläge: 15 s, 30 s, 60 s, frei. Bei Code-Videos geht auch
   länger, es gibt keine Clip-Grenze wie bei Videomodellen.
4. **Welches Format?** 16:9 (YouTube, Präsentation), 9:16 (Shorts, Reels, TikTok),
   1:1 oder 4:5 (Feed).
5. **Farben, Muster, Branding?** Optionen: eigenes Branding (Logo, Farben, Schrift,
   Brand Guide hochladen oder Pfad nennen) · Look einer Webseite übernehmen (Link)
   · ein bestimmter Stil (z. B. Papier, Risograph, flach und minimal, verspielt mit
   2D-Figuren) · freie Hand.
6. **Gibt es schon eine Referenz, die dir gefällt?** Ein Video, ein Bild, ein
   Screenshot oder ein Link. Wenn ja: Datei in den Projektordner legen lassen oder
   den Link notieren und im Prompt sagen, was daran gefällt (Tempo, Farben,
   Übergänge, Typo).
7. **Ton?** Sprecherstimme ja/nein und in welcher Sprache · Musik ja/nein ·
   Soundeffekte ja/nein. Mit Higgsfield: Stimmen über ElevenLabs v4, Hörproben
   anbieten, bevor das ganze Video vertont wird. Ohne Higgsfield: eigene Dateien
   oder freie Sounds.
8. **Wann ist das Video gut?** Das ist die wichtigste Frage. Ein Satz, an dem man
   das Ergebnis messen kann. Wenn der Person nichts einfällt, Beispiele anbieten:
   - „Ein Designer würde sagen: wow.“
   - „Jemand ohne Vorwissen versteht nach dem Video, was X macht.“
   - „Das Video kann so, wie es ist, auf Social Media live gehen.“
   - „Mein Logo, meine Farben und meine Schrift sind exakt drin.“

## Die Vorlage

Baue den Prompt in der Sprache der Person, ungefähr so. Weglassen, was nicht
gefragt wurde, nichts erfinden.

```text
Du bist Motion Designer. Mach mit <Framework> ein <Länge> langes Video im Format
<Seitenverhältnis> über <Thema/Link>.

Ziel: <Ziel>. Zielgruppe: <wer schaut zu>.
Look: <Branding / Stil / Webseite als Vorbild>. <Referenz und was daran gefällt>.
Ton: <Stimme, Sprache> · <Musik> · <Soundeffekte>. <Higgsfield für Bilder/Video/Stimme, falls gewählt>.

Ziel erreicht, wenn <Kriterium>.

Sei kreativ. Prüf deine Zwischenstände selbst, bevor du fertig meldest.
<Wenn Higgsfield: Zeig mir vor dem Generieren, was es kostet.>
```

Keine Schrittlisten („erst Szene 1, dann …“), keine Pixelangaben, keine
Animationsvorgaben, außer die Person wünscht sie ausdrücklich. Geschmack gehört
rein (Look, Tempo, Stimmung), Arbeitsanweisungen nicht.

## Beispiele: so kurz dürfen Prompts sein

Diese Prompts haben im Video zum Skill funktioniert:

> Erstelle ein dynamisches 15-Sekunden-Motion-Graphics-Video, das zeigt, was für
> ein Beast du im Motion Design bist. Ziel erreicht, wenn ein professioneller
> Designer sich denkt: „Das ist krass.“ Sei kreativ und überrasch mich.

> Mach ein beeindruckendes Werbe- und Erklärvideo für die Plattform n8n.io. Nimm
> HyperFrames, halte dich an das Branding von n8n und mach es so, dass ein Designer
> „wow“ sagen würde. Vertone das Ganze mit der realistischsten deutschen
> ElevenLabs-Stimme (v4) über Higgsfield. Auftrag erfüllt, wenn das Video als
> Erklärvideo auf Social Media live gehen könnte. 16:9, 30 Sekunden reichen.

> Mach ein Motion-Design-Video, das unglaublich schön ist. Ein Designer würde
> sagen: „Krass.“ Nimm HyperFrames, 15 Sekunden. Bau Bilder aus GPT Image ein,
> damit die Animationen schöner sind, und eine deutsche ElevenLabs-v4-Stimme, beides
> über Higgsfield. Im Video erklärst du ganz einfach, was Glukoneogenese ist.

## Fertige Videos bearbeiten (Longform → Short)

Zusätzlich fragen: Wie viele Shorts? Wie lang (Shorts dürfen bis 3 Minuten
lang sein, 60–90 s ist üblich)? Untertitel ja und in welcher Farbe?

Ein Short muss für sich allein verständlich sein: **Hook, Kontext, Erklärung,
Abschluss.** Ausschnitte, die nur aus dem Zusammenhang gerissen sind, funktionieren
schlecht. Deshalb: erst das Video transkribieren (mit Wortzeiten, siehe
troubleshooting.md), dann Storylines vorschlagen und absegnen lassen, erst danach
schneiden.

## Tipps für danach

Nenne sie am Ende, kurz:

- **Aufwand:** Medium reicht fast immer, höchstens High. Alles darüber kostet
  vor allem Zeit und Limit.
- **Neuer Chat pro Video:** Ein voller Kontext mit dem letzten Video lenkt ab und
  zieht alte Ideen ins neue Video.
- **Konkretes Feedback:** „Die Musik ist zu laut“, „Das Wort X wird falsch
  ausgesprochen“, „Szene 3 ist zu lang“. Weil alles Code ist, ändert der Agent nur
  diese Stelle und der Rest bleibt.
- **Eigene Assets schlagen generierte:** echtes Logo, echte Screenshots, eigene
  Musik, wenn vorhanden.
