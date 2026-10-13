# Ki-Sporen

## Steckbrief

- **Ziel:** Die Labore aus dem YouTube-Video „KI repliziert sich selbst – Anthropic warnt vor
  Katastrophe“ (LPIndie, https://youtu.be/M7zLg-YNcyU) nachbauen, um zu verstehen, was dort
  tatsächlich erklärt wird. Vom Video gibt es nur Screenshots, keine HTML-Dateien. YouTube blockt
  den Abruf aus der Cloud (Bot-Prüfung), das Transkript muss der Nutzer liefern.
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
| `nachbau_1_loop_labor.html` | Video-Labor 1: genetischer Algorithmus mit Ziel (Start exakt wie im Video, Seed 44) |
| `nachbau_2_ohne_ziel.html` | Video-Labor 2: Ring-Mittelung + logistische Abbildung, mit Theoriekurve |
| `nachbau_4_gedaechtnis.html` | Video-Labor 4: adaptives Netz, Störungstest, Zufallserwartung |
| `ausbreitungs_labor_sir.html` | eigene Erweiterung zum Artikel: SEIQ-Modell (Mean-Field) |
| `netzwerk_labor_cluster.html` | eigene Erweiterung zum Artikel: SEIQ auf geclustertem Graphen |

Video-Labor 3 fehlt, dazu gibt es keinen Screenshot.

## Git-Arbeitsweise

Direkt auf `main` committen und pushen, keine Feature-Branches. Grund: Das Löschen
von Remote-Branches ist in den Cloud-Sitzungen gesperrt (403), sonst bleiben leere
Branches liegen.

## Kostenzeile

Das Skript liegt in der Kostenzeilen-Skill, nicht im Repo. Nicht nach `tools/` kopieren,
sondern direkt von dort ausführen:

    python3 ~/.claude/skills/synced/*/kostenzeile/kosten.py
