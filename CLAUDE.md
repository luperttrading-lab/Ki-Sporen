# Ki-Sporen

Material zu selbstreplizierender KI (Anthropic-Artikel „AI models may be capable of
self-replicating without access to a datacenter“, 12.10.2026) und zu den Emergenz-Laboren.

Steckbrief: noch offen.

## Git-Arbeitsweise

Direkt auf `main` committen und pushen, keine Feature-Branches. Grund: Das Löschen
von Remote-Branches ist in den Cloud-Sitzungen gesperrt (403), sonst bleiben leere
Branches liegen.

## Kostenzeile

Das Skript liegt in der Kostenzeilen-Skill, nicht im Repo. Nicht nach `tools/` kopieren,
sondern direkt von dort ausführen:

    python3 ~/.claude/skills/synced/*/kostenzeile/kosten.py
