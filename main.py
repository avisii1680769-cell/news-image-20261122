#!/usr/bin/env python3
"""Copy entry.png to MAKEFUN_OUTPUT_DIR after validating it.

The image is a 1024x1024 PNG of Sunday 22 November 2026 world news,
drawn as a newspaper front page. This program uses only the standard
library, performs no network access, and writes identical bytes on
every run because it copies the bundled file unchanged.
"""
import os
import struct
import sys
import zlib

MAX_BYTES = 1048576
EXPECTED_WIDTH = 1024
EXPECTED_HEIGHT = 1024
PNG_SIGNATURE = b"\x89PNG\r\n\x1a\n"


def fail(message):
    print(f"error: {message}", file=sys.stderr)
    raise SystemExit(1)


def read_png(path):
    with open(path, "rb") as handle:
        data = handle.read()
    if len(data) > MAX_BYTES:
        fail(f"entry.png is {len(data)} bytes, over the 1048576 byte limit")
    if len(data) < 8 or data[:8] != PNG_SIGNATURE:
        fail("entry.png does not start with the PNG signature")
    offset = 8
    seen_ihdr = False
    seen_iend = False
    width = height = None
    while offset < len(data):
        if offset + 8 > len(data):
            fail("entry.png ends in the middle of a chunk header")
        length, chunk_type = struct.unpack(">I4s", data[offset:offset + 8])
        chunk_end = offset + 8 + length + 4
        if chunk_end > len(data):
            fail(f"entry.png ends in the middle of chunk {chunk_type!r}")
        payload = data[offset + 8:offset + 8 + length]
        stored_crc = struct.unpack(">I", data[offset + 8 + length:chunk_end])[0]
        actual_crc = zlib.crc32(chunk_type + payload) & 0xFFFFFFFF
        if stored_crc != actual_crc:
            fail(f"entry.png chunk {chunk_type!r} has a bad CRC")
        if chunk_type == b"IHDR":
            if seen_ihdr or length != 13:
                fail("entry.png has a malformed IHDR chunk")
            width, height = struct.unpack(">II", payload[:8])
            bit_depth, color_type = payload[8], payload[9]
            if bit_depth != 8 or color_type not in (2, 6):
                fail(f"entry.png uses bit depth {bit_depth} color type "
                     f"{color_type}, expected 8-bit RGB/RGBA")
            seen_ihdr = True
        if chunk_type == b"IEND":
            seen_iend = True
            if chunk_end != len(data):
                fail("entry.png has trailing bytes after IEND")
            break
        offset = chunk_end
    if not seen_ihdr:
        fail("entry.png has no IHDR chunk")
    if not seen_iend:
        fail("entry.png has no IEND chunk")
    if width != EXPECTED_WIDTH or height != EXPECTED_HEIGHT:
        fail(f"entry.png is {width}x{height}, expected 1024x1024")
    return data


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    source = os.path.join(here, "entry.png")
    if not os.path.isfile(source):
        fail("entry.png is missing next to main.py")
    data = read_png(source)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    target = os.path.join(out_dir, "entry.png")
    with open(target, "wb") as handle:
        handle.write(data)
    print(f"wrote {target} ({len(data)} bytes, 1024x1024 PNG)")


if __name__ == "__main__":
    main()
