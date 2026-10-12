#!/usr/bin/env python3
"""Convert RB3 genre/subgenre values to RB2 equivalents.

This mirrors the mappings described in convert-genre.txt, making the conversion
workflow easier to apply to a larger batch of songs.
"""

from __future__ import annotations

import argparse
import json
import sys
from typing import Iterable, Tuple

UNCHANGED = {
    "alternative",
    "blues",
    "classicrock",
    "country",
    "emo",
    "fusion",
    "glam",
    "grunge",
    "indierock",
    "jazz",
    "metal",
    "newwave",
    "novelty",
    "numetal",
    "poprock",
    "prog",
    "punk",
    "rock",
    "southernrock",
    "other",
}

GENRE_DEFAULTS = {
    "classical": ("other", "subgenre_other"),
    "inspirational": ("other", "subgenre_other"),
    "latin": ("other", "subgenre_other"),
    "jrock": ("rock", "subgenre_rock"),
    "world": ("other", "subgenre_other"),
    "hiphoprap": ("urban", "subgenre_other"),
}

SUBGENRE_MAPS = {
    "popdanceelectronic": {
        "subgenre_ambient": ("other", "subgenre_ambient"),
        "subgenre_breakbeat": ("other", "subgenre_breakbeat"),
        "subgenre_chiptune": ("other", "subgenre_chiptune"),
        "subgenre_dance": ("other", "subgenre_dance"),
        "subgenre_downtempo": ("other", "subgenre_electronica"),
        "subgenre_dub": ("rock", "subgenre_reggae"),
        "subgenre_drumandbass": ("other", "subgenre_drumandbass"),
        "subgenre_electronica": ("other", "subgenre_electronica"),
        "subgenre_garage": ("urban", "subgenre_garage"),
        "subgenre_hardcoredance": ("urban", "subgenre_hardcoredance"),
        "subgenre_house": ("other", "subgenre_house"),
        "subgenre_industrial": ("urban", "subgenre_industrial"),
        "subgenre_techno": ("other", "subgenre_techno"),
        "subgenre_trance": ("other", "subgenre_trance"),
        "subgenre_other": ("other", "subgenre_electronica"),
    },
    "rbsoulfunk": {
        "subgenre_disco": ("poprock", "subgenre_disco"),
        "subgenre_funk": ("rock", "subgenre_funk"),
        "subgenre_motown": ("poprock", "subgenre_motown"),
        "subgenre_rhythmandblues": ("poprock", "subgenre_rhythmandblues"),
        "subgenre_soul": ("poprock", "subgenre_soul"),
        "subgenre_other": ("poprock", "subgenre_rhythmandblues"),
    },
}


def convert_rb3_genre(genre: str, subgenre: str | None = None) -> Tuple[str, str]:
    """Return the RB2-compatible (genre, subgenre) pair for the given RB3 values."""
    normalized_genre = (genre or "").strip().lower()
    normalized_subgenre = (subgenre or "").strip().lower()

    if not normalized_genre:
        return ("other", "subgenre_other")

    if normalized_genre in UNCHANGED:
        return (normalized_genre, normalized_subgenre or "subgenre_other")

    if normalized_genre in GENRE_DEFAULTS:
        default_genre, default_subgenre = GENRE_DEFAULTS[normalized_genre]
        return (default_genre, normalized_subgenre or default_subgenre)

    if normalized_genre == "reggaeska":
        if normalized_subgenre == "subgenre_ska":
            return ("rock", "subgenre_ska")
        return ("rock", "subgenre_reggae")

    if normalized_subgenre:
        mapped = SUBGENRE_MAPS.get(normalized_genre, {}).get(normalized_subgenre)
        if mapped:
            return mapped

    if normalized_genre == "hiphoprap":
        return ("urban", normalized_subgenre or "subgenre_other")

    return ("other", "subgenre_other")


def _parse_args(argv: Iterable[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Map RB3 music genres to RB2-compatible values.")
    parser.add_argument("genre", help="RB3 genre, such as 'popdanceelectronic'")
    parser.add_argument("subgenre", nargs="?", default=None, help="Optional RB3 subgenre")
    parser.add_argument("--json", action="store_true", help="Print JSON instead of a plain string")
    return parser.parse_args(list(argv) if argv is not None else None)


def main(argv: Iterable[str] | None = None) -> int:
    args = _parse_args(argv)
    genre, subgenre = convert_rb3_genre(args.genre, args.subgenre)
    result = {"genre": genre, "subgenre": subgenre}
    if args.json:
        print(json.dumps(result, separators=(",", ":")))
    else:
        print(f"{genre} / {subgenre}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
