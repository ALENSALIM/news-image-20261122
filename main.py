#!/usr/bin/env python3
"""Entry point for the make.fun bounty news-image-20261122.

Copies the bundled front-page image (entry.png) to the output
directory given by MAKEFUN_OUTPUT_DIR (default /output), verifies
the copy matches the bundled file byte for byte (same size and
same SHA-256 digest), and prints the byte count and SHA-256 hash
of the copy. Standard library only; no network access.
"""

import hashlib
import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "entry.png")


def _sha256(path):
    digest = hashlib.sha256()
    with open(path, "rb") as fh:
        for chunk in iter(lambda: fh.read(65536), b""):
            digest.update(chunk)
    return digest.hexdigest()


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    dst = os.path.join(out_dir, "entry.png")
    shutil.copyfile(SRC, dst)

    src_size = os.path.getsize(SRC)
    dst_size = os.path.getsize(dst)
    if dst_size != src_size:
        print("error: size mismatch: bundled %d bytes, copy %d bytes"
              % (src_size, dst_size), file=sys.stderr)
        sys.exit(1)

    src_digest = _sha256(SRC)
    dst_digest = _sha256(dst)
    if src_digest != dst_digest:
        print("error: sha256 mismatch: bundled %s, copy %s"
              % (src_digest, dst_digest), file=sys.stderr)
        sys.exit(1)

    print("entry.png: %d bytes" % dst_size)
    print("sha256: %s" % dst_digest)
    print("wrote %s" % dst)


if __name__ == "__main__":
    main()
