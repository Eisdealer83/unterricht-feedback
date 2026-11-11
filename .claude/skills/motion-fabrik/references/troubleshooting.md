# Wenn etwas klemmt

**Neu installierte Skills oder Plugins tauchen nicht auf.**
Die Liste wird beim Start einer Sitzung gelesen. Neue Sitzung starten.

**`higgsfield` wird nicht gefunden.**
Das globale npm-Verzeichnis liegt nicht im Pfad. `npm prefix -g` zeigt, wohin
installiert wurde. Unter Windows hilft oft schon ein neues Terminal.

**Higgsfield: „Authorization with the MCP server failed“ oder „Session expired“.**
Token abgelaufen. CLI: `higgsfield auth login` wiederholen. Connector: in den
Einstellungen trennen und neu verbinden.

**`npx skills add` findet nichts oder fragt endlos.**
Mit `-l` statt `-y` listet der Befehl auf, was im Repo liegt. Liegt ein Skill tief
in Unterordnern, hilft `--full-depth`.

**HyperFrames rendert nicht.**
`node --version` muss mindestens 22 sein, und `ffmpeg` muss im Pfad liegen.
`npx hyperframes check` im Projekt zeigt Fehler im Video selbst.

**Transkription für fertige Videos (Stufe 4).**
`hyperframes transcribe` braucht whisper-cpp und kann ohne das stillschweigend
scheitern. Zuverlässiger Weg ist faster-whisper über uv (Python):

```bash
pip install uv          # einmalig, falls uv fehlt
uv run --with faster-whisper --with "av<14" python transcribe.py video.mp4
```

Das Skript lässt du den Agenten schreiben: Modell `medium`, `word_timestamps=True`,
Sprache passend zum Video, Ausgabe als JSON mit Wörtern und Zeiten. Scheitert das
Einlesen der Datei an PyAV, den Ton erst mit ffmpeg als 16-kHz-Mono-WAV
herausziehen und als Array übergeben.

**Generierte Soundeffekte sind kaum hörbar.**
Manche Modelle liefern sehr leise Dateien. Mit ffmpeg normalisieren
(`-af loudnorm=I=-16`) oder freie Sounds nehmen.

**Die Stimme spricht ein Wort falsch aus.**
Das Wort im Sprechtext lautmalerisch schreiben (z. B. „n-eight-n“ statt „n8n“)
und nur diesen Satz neu generieren.

**Das Video wirkt wie eine Präsentation mit Standbildern.**
Im Feedback sagen: „Auf jeder Ebene soll sich etwas bewegen, Animationen sollen
auf dem gesprochenen Wort sitzen.“
