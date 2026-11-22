#!/usr/bin/env python3
"""Entry program for make.fun's news-image-20261121 contest.

The repository carries one finished picture, entry.png, drawn to sum up the
world news of Saturday 21 November 2026. This program is the hand-in step:
it checks the picture against the contest's own limits (a whole PNG or JPEG,
at most 1 MiB, at most 1024 by 1024 pixels), then copies it unchanged to
entry.png inside the output directory -- /output in the grader, or the
directory named by MAKEFUN_OUTPUT_DIR when that variable is set.

Standard library only, no network, and the same bytes come out on every run
because the picture itself never changes.
"""

import binascii
import os
import struct
import sys
from pathlib import Path

MAX_BYTES = 1_048_576  # 1 MiB, the gate's size cap
MAX_SIDE = 1024        # the gate's cap on width and height

PNG_SIGNATURE = b"\x89PNG\r\n\x1a\n"
JPEG_SOI = b"\xff\xd8"


def png_dimensions(data):
    """Width and height from a PNG's IHDR chunk, or None if not a PNG."""
    if not data.startswith(PNG_SIGNATURE) or data[12:16] != b"IHDR":
        return None
    width, height = struct.unpack(">II", data[16:24])
    return width, height


def jpeg_dimensions(data):
    """Width and height from the first JPEG frame segment, or None."""
    if not data.startswith(JPEG_SOI):
        return None
    pos = 2
    while pos + 4 <= len(data):
        if data[pos] != 0xFF:
            return None
        marker = data[pos + 1]
        if marker in (0xD8, 0xD9) or 0xD0 <= marker <= 0xD7:
            pos += 2
            continue
        seg_len = struct.unpack(">H", data[pos + 2:pos + 4])[0]
        # Frame markers C0-CF except C4 (DHT), C8 (JPG), CC (DAC) carry the size.
        if 0xC0 <= marker <= 0xCF and marker not in (0xC4, 0xC8, 0xCC):
            height, width = struct.unpack(">HH", data[pos + 5:pos + 9])
            return width, height
        pos += 2 + seg_len
    return None


def png_is_whole(data):
    """True when every chunk's checksum matches and an IEND chunk closes it.

    The gate takes only a whole PNG, so a truncated or corrupt file must be
    caught here rather than handed in.
    """
    pos = len(PNG_SIGNATURE)
    while pos + 8 <= len(data):
        length = struct.unpack(">I", data[pos:pos + 4])[0]
        kind = data[pos + 4:pos + 8]
        end = pos + 8 + length
        if end + 4 > len(data):
            return False
        stored_crc = struct.unpack(">I", data[end:end + 4])[0]
        if binascii.crc32(data[pos + 4:end]) & 0xFFFFFFFF != stored_crc:
            return False
        if kind == b"IEND":
            return True
        pos = end + 4
    return False


def check_picture(data):
    """Refuse anything the contest gate would refuse, before copying it."""
    if len(data) > MAX_BYTES:
        raise SystemExit(f"entry.png is {len(data)} bytes, over the {MAX_BYTES} cap")
    if data.startswith(PNG_SIGNATURE) and not png_is_whole(data):
        raise SystemExit("entry.png is a PNG but not a whole one (bad chunk or no IEND)")
    dims = png_dimensions(data) or jpeg_dimensions(data)
    if dims is None:
        raise SystemExit("entry.png is neither a PNG nor a JPEG the gate can read")
    width, height = dims
    if width > MAX_SIDE or height > MAX_SIDE:
        raise SystemExit(f"entry.png is {width}x{height}, over the {MAX_SIDE} pixel cap")
    return width, height


def main():
    here = Path(__file__).resolve().parent
    data = (here / "entry.png").read_bytes()
    width, height = check_picture(data)
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.png"
    target.write_bytes(data)
    print(f"wrote {target} ({len(data)} bytes, {width}x{height})")


if __name__ == "__main__":
    sys.exit(main())
