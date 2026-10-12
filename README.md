# convert-rb2
Info to convert RB3 custom song packages to RB2.

This repo contains the workflow notes used to rebuild RB3 songs for RB2, plus a small helper for converting RB3 genre and subgenre metadata to the values RB2 accepts.

## Quick start

Use the genre conversion helper when translating a song entry from RB3 data to RB2 data:

```bash
python convert_genre.py popdanceelectronic subgenre_breakbeat
python convert_genre.py "hiphoprap" --json
```

Example output:

```text
other / subgenre_breakbeat
{"genre":"urban","subgenre":"subgenre_other"}
```

## Included reference files

- `convert-rb2.txt` — step-by-step RB3-to-RB2 conversion checklist for the MIDI, MOGG, `songs.dta`, and package assembly workflow.
- `convert-genre.txt` — explicit RB3-to-RB2 genre and subgenre mapping table.
- `convert_genre.py` — executable version of the genre conversion rules for easier reuse.

## Notes

The conversion process is still a manual workflow in many cases, especially around MIDI cleanup and package assembly. The most reliable approach is to preserve the original RB3 assets where possible, fix the RB3-only note data, then rebuild the RB2 song entry and package with the RB2-compatible metadata values.
