"""Regenerate the bundled emoji data files under ``charguana/data/emoji/``.

Usage:
    python scripts/refresh_emoji.py                    # latest Unicode version
    python scripts/refresh_emoji.py --version 16.0     # pin a version

Pulls the four Unicode source files (emoji-data, emoji-variation-sequences,
emoji-sequences, emoji-zwj-sequences), parses them via
:func:`charguana.emoji.fetch_emoji`, and writes distilled one-per-line files.
The raw Unicode files are discarded — only the parsed payload is committed.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT))

from charguana.emoji import emoji_dir as _DEFAULT_OUT, fetch_emoji  # noqa: E402

DATA_DIR = Path(_DEFAULT_OUT)


def write_bundle(parsed: dict[str, object], out_dir: Path = DATA_DIR) -> None:
    out_dir.mkdir(parents=True, exist_ok=True)

    # Emoji_Presentation: those rendered as emoji by default (without VS16).
    # Extended_Pictographic is a superset that includes text-default chars
    # like © — skip for the default "is this an emoji?" list.
    presentation = parsed['data_properties'].get('Emoji_Presentation', set())
    (out_dir / 'emoji_chars.txt').write_text(
        '\n'.join(sorted(presentation)) + '\n', encoding='utf-8'
    )
    (out_dir / 'emoji_sequences.txt').write_text(
        '\n'.join(parsed['sequences']) + '\n', encoding='utf-8'
    )
    (out_dir / 'emoji_zwj_sequences.txt').write_text(
        '\n'.join(parsed['zwj_sequences']) + '\n', encoding='utf-8'
    )

    props_by_char: dict[str, set[str]] = {}
    for prop, chars in parsed['data_properties'].items():
        for ch in chars:
            props_by_char.setdefault(ch, set()).add(prop)
    lines = [
        f"{ch}\t{','.join(sorted(props))}"
        for ch, props in sorted(props_by_char.items())
    ]
    (out_dir / 'emoji_properties.txt').write_text(
        '\n'.join(lines) + '\n', encoding='utf-8'
    )


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--version', default='latest',
                    help='Unicode emoji version to pull (default: latest).')
    ap.add_argument('--out', type=Path, default=DATA_DIR,
                    help=f'Output directory (default: {DATA_DIR}).')
    args = ap.parse_args(argv)

    print(f"Fetching emoji data for version {args.version!r}...")
    parsed = fetch_emoji(args.version)

    presentation = parsed['data_properties'].get('Emoji_Presentation', set())
    print(
        f"  Emoji_Presentation chars:          {len(presentation)}\n"
        f"  emoji-sequences entries:           {len(parsed['sequences'])}\n"
        f"  emoji-zwj-sequences:               {len(parsed['zwj_sequences'])}\n"
        f"  variation-sequences (emoji style): {len(parsed['variation_sequences'])}"
    )

    write_bundle(parsed, args.out)
    print(f"Wrote distilled data files to {args.out}")
    return 0


if __name__ == '__main__':
    sys.exit(main())
