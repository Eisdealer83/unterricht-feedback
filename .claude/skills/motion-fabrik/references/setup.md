# Teil 1: Einrichten

## 1. Voraussetzungen prüfen

Führe die Prüfungen aus und zeig eine kurze Tabelle: was da ist, was fehlt, wofür
es gebraucht wird.

```bash
node --version      # HyperFrames braucht v22+, Remotion und Higgsfield CLI v18+
npm --version
ffmpeg -version     # Video schneiden und kodieren, für fast alles nötig
git --version       # Projekte versionieren, Skills laden
python --version    # oder python3; nur für Stufe 4 (Transkription) nötig
```

Stell außerdem das Betriebssystem fest (Windows, macOS, Linux), damit du die
richtigen Installationsbefehle nennst.

| Fehlt | Was dann nicht geht | Nachinstallieren (nach Rückfrage) |
|---|---|---|
| Node.js (zu alt) | HyperFrames, Remotion, Higgsfield CLI, Skill-Installation | Windows `winget install OpenJS.NodeJS.LTS` · macOS `brew install node` · Linux über nodejs.org oder den Paketmanager |
| ffmpeg | Rendern, Schneiden, Ton | Windows `winget install Gyan.FFmpeg` · macOS `brew install ffmpeg` · Linux `sudo apt install ffmpeg` |
| git | Skills laden, Projekte versionieren | Windows `winget install Git.Git` · macOS `xcode-select --install` · Linux `sudo apt install git` |
| Python | nur Transkription für Stufe 4 | Windows `winget install Python.Python.3.12` · macOS `brew install python` |

Nach einer Installation unter Windows ist das neue Programm oft erst in einem
neuen Terminal im Pfad. Sag das, statt einen Fehler zu melden.

## 2. Framework wählen

Frage (eine Auswahl, Empfehlung zuerst):

| Option | Ein Satz dazu |
|---|---|
| **HyperFrames (Empfohlen)** | Open Source (Apache-2.0), baut Videos aus HTML und bringt fertige Bausteine und Anleitungen für den Agenten mit. |
| **Remotion** | Baut Videos aus React-Code. Kostenlos für Einzelpersonen und Firmen bis 3 Mitarbeitende, größere Firmen brauchen eine Lizenz. |
| **Tesseract** | Neue Creative Suite von Mirage mit eigenem Editor im Browser. Für Claude Code gibt es noch kein Plugin, die Skills funktionieren aber. |
| **Nichts** | Claude baut alles selbst aus reinem Code. Geht, ist aber mehr Arbeit für den Agenten und klingt beim Ton künstlicher. |

Hinweis dazu, ohne eigene Option: **Claude Motion** läuft direkt in der Claude-App
und braucht keine Installation, ist aber zurzeit nur in der Beta für Team- und
Enterprise-Pläne. Wer das hat, kann es zusätzlich nutzen.

### HyperFrames

Claude Code:

```bash
claude plugin marketplace add heygen-com/hyperframes
claude plugin install hyperframes@hyperframes
```

Codex und andere Agenten:

```bash
npx skills add heygen-com/hyperframes --all -g -y
```

Ein Projekt legt man später mit `npx hyperframes init <name>` an. Vorschau:
`npx hyperframes preview`, Rendern: `npx hyperframes render`.

### Remotion

```bash
npx skills add remotion-dev/skills -g -y
```

Ein Projekt entsteht später mit `npx create-video@latest`. Die Lizenzfrage
einmal ansprechen: Wer in einer Firma mit mehr als 3 Mitarbeitenden arbeitet,
braucht eine Firmenlizenz (remotion.pro/license).

### Tesseract

```bash
npx skills add mirage-hq/Tesseract
```

Der Befehl öffnet eine Auswahl. Die Skills führen danach selbst durch die
Installation der Tesseract-CLI (mit Prüfsumme). Projekte sind `.tsrct`-Dateien
mit einem Editor im Browser, gerendert wird lokal.

### Nichts

Nichts installieren. Beim Bauen schreibt der Agent dann eine HTML-/Canvas-Animation
und nimmt sie mit Playwright und ffmpeg Bild für Bild auf. Das funktioniert,
dauert aber länger.

## 3. Higgsfield verbinden

Frage: „Willst du Higgsfield verbinden, um Bilder, Videoclips, Stimmen, Musik und
Soundeffekte zu generieren?“ Ja (Empfohlen) / Nein.

**Bei Ja** zuerst fragen: „Hast du schon ein Higgsfield-Konto?“ Nur wenn nicht,
diesen Text zeigen, inklusive Kennzeichnung:

> Hier kannst du dich anmelden: https://higgsfield.ai/s/mcp-arnold-oberleiter-Lrbecz
> (Affiliate-Link: Wenn du darüber ein Abo abschließt, bekommt der Autor dieses
> Skills eine Provision. Für dich ändert sich am Preis nichts.)

Die Kennzeichnung bleibt immer dabei. Wer schon ein Konto hat, bekommt den Link
nicht zu sehen. Dränge niemanden zu einem Abo: Generieren kostet Credits, alles
andere funktioniert auch ohne.

**Weg A: CLI (Empfohlen für Claude Code und Codex im Terminal)**

```bash
npm i -g @higgsfield/cli
higgsfield auth login                    # öffnet den Browser, blockiert bis zur Anmeldung
npx skills add higgsfield-ai/skills -g -y
higgsfield account status                # zeigt Konto und Guthaben
```

Warte bei `auth login`, bis die Anmeldung bestätigt ist. Steht bei
`account status` „Not authenticated“ oder „Session expired“: Login wiederholen.
Die CLI kann vor dem Generieren die Kosten berechnen (`higgsfield generate cost`),
das ist der Hauptgrund für diesen Weg.

**Weg B: MCP-Verbindung** (für Claude Desktop und claude.ai, oder wenn die CLI nicht will)

```bash
# Claude Code
claude mcp add --transport http -s user higgsfield https://mcp.higgsfield.ai/mcp
# Codex
codex mcp add higgsfield --url https://mcp.higgsfield.ai/mcp
```

Claude Desktop oder claude.ai: Einstellungen → Connectors → Add custom connector,
Name `Higgsfield`, URL `https://mcp.higgsfield.ai/mcp`, verbinden, im Browser
anmelden. In Chats muss der Connector eingeschaltet sein.

**Bei Nein:** Kurz sagen, was dann geht: eigene Bilder, Logos, Musik und Sounds in
einen `assets/`-Ordner im Projekt legen, oder freie Sounds und Musik von Seiten
wie Pixabay herunterladen. Selbst berechnete Sounds aus Code klingen künstlich,
eine Sprecherstimme gibt es ohne Stimmen-Dienst nicht.

## 4. Speichern und abschließen

`~/.motion-fabrik.json` schreiben (Format in SKILL.md). Dann in wenigen Zeilen:

- welche Voraussetzungen da sind und was fehlt
- welches Framework installiert wurde und wie
- ob Higgsfield verbunden ist und wie viel Guthaben da ist

Wenn Skills oder Plugins installiert wurden: „Starte eine neue Sitzung (in Claude
Code `/exit` und neu starten, oder ein neues Chatfenster) und schreib dort ‚Motion
Fabrik‘. Dann bauen wir deinen ersten Prompt.“
