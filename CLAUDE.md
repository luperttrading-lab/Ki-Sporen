# Ki-Sporen

## Steckbrief

- **Ziel:** Die Labore aus dem YouTube-Video „KI repliziert sich selbst – Anthropic warnt vor
  Katastrophe“ (LPIndie, https://youtu.be/M7zLg-YNcyU) nachbauen, um zu verstehen, was dort
  tatsächlich erklärt wird. Vom Video gibt es nur Screenshots, keine HTML-Dateien.
- **These des Videos:** Ein 50–100-KB-Startcode („KI-Spore“, aus dem früheren Video „GPT-5.6 bricht
  aus … Das AI-Spore-Theorem“, https://youtu.be/t3Tb9HOiwSw) brauche zum stabilen Kopieren eine
  Fehlerkorrektur; ein „parallel rekursiver Loop“ setze sich auf einen Urzustand zurück und repariere
  sich nach Störungen selbst. Labore 1, 2, 4 sollen das zeigen; die Nachbauten zeigen: alles Mitteln.
- **Transkript holen** (normaler YouTube-Abruf scheitert an der Bot-Prüfung, dieser Client nicht):
  `yt-dlp --skip-download --ignore-no-formats-error --write-auto-subs --sub-langs de-orig --sub-format vtt --extractor-args "youtube:player_client=web_embedded" <URL>`
  Transkripte nicht committen (fremder Inhalt, Repo ist öffentlich).
- **Online:** https://luperttrading-lab.github.io/Ki-Sporen/ (GitHub Pages, Startseite `index.html`).
- **Methode:** Regeln aus den Screenshots rekonstruieren, gegen die im Video sichtbaren Zahlen
  prüfen, jede Annahme kennzeichnen (rekonstruiert / angenommen) und Gegenproben einbauen, die die
  Behauptung des Videos testen.
- **Hintergrund:** Anthropic-Artikel „AI models may be capable of self-replicating without access
  to a datacenter“ (12.10.2026).

## Dateien

| Datei | Inhalt |
|---|---|
| `index.html` | Startseite mit Links und Info-Knöpfen zu allen Laboren |
| `nachbau_1_loop_labor.html` | Video-Labor 1: genetischer Algorithmus mit Ziel (Start exakt wie im Video, Seed 44); Sinus-Layer an die digitalisierte rote Videokurve angepasst (A 0,126, P 245, Abweichung 0,013), logistisch umschaltbar |
| `nachbau_2_ohne_ziel.html` | Video-Labor 2: Ring-Mittelung + logistische Abbildung, mit Theoriekurve |
| `nachbau_4_gedaechtnis.html` | Video-Labor 4: Oberfläche wie im Video, Parameter an Video angepasst (Seed 359: Gen 0 und 630 exakt; Mischrate Farbe 0,0258, Größe 0,15; ε 0,47); Gegenproben und Versuche A–F getrennt darunter |
| `ausbreitungs_labor_sir.html` | eigene Erweiterung zum Artikel: SEIQ-Modell (Mean-Field) |
| `netzwerk_labor_cluster.html` | eigene Erweiterung zum Artikel: SEIQ auf geclustertem Graphen |

Video-Labor 3 kommt im Video nicht vor (geprüft mit Standbildern alle 5 s und dem Transkript).

Zeitleiste des Videos (aus den Storyboard-Standbildern, `sb0` in der yt-dlp-Info-JSON): 0:00 Artikel ·
1:14 KI-Spore-Folie · 2:14 Artikel · 3:03 Loop-Diagramm · 4:53 Labor 1 · 5:42 Labor 2 · 6:27 Labor 4 ·
9:16 Diagramm · 9:46 Artikel · 10:16 Labor 4 (Anomalie 10:43) · 11:30 Artikel · 11:50 Folien · 14:24 Abspann.
Schlüsselsätze: 5:33 „Urzustand“ · 6:08 „Sinuskurve“ (Labor 2) · 7:11/7:52 „zurückverfolgen“ (Labor 4) ·
8:32 „feste Verbindungen, also Kontrolle“ · 8:50 „Urfassung … Selbstreparatur“ · 9:30 „Angleichungssystem“.

## Git-Arbeitsweise

Direkt auf `main` committen und pushen, keine Feature-Branches. Grund: Das Löschen
von Remote-Branches ist in den Cloud-Sitzungen gesperrt (403), sonst bleiben leere
Branches liegen.

## Kostenzeile

Das Skript liegt in der Kostenzeilen-Skill, nicht im Repo. Nicht nach `tools/` kopieren,
sondern direkt von dort ausführen:

    python3 ~/.claude/skills/synced/*/kostenzeile/kosten.py
