#!/usr/bin/env python3

from pathlib import Path
import csv
import hashlib


DATASET_DIR = Path("datasets/wheat-research-sample")
OUTPUT_FILE = DATASET_DIR / "manifest.csv"


def calculate_sha256(path: Path) -> str:
    sha256 = hashlib.sha256()

    with path.open("rb") as file:
        for chunk in iter(lambda: file.read(8192), b""):
            sha256.update(chunk)

    return sha256.hexdigest()


def main() -> int:
    if not DATASET_DIR.exists():
        print(f"ERROR: dataset directory not found: {DATASET_DIR}")
        return 1

    files = [
        path
        for path in DATASET_DIR.rglob("*")
        if path.is_file()
        and path.name != OUTPUT_FILE.name
        and path.suffix in [".csv", ".tsv", ".json", ".txt"]
    ]
    if not files:
        print(f"ERROR: no files found in {DATASET_DIR}")
        return 1

    with OUTPUT_FILE.open("w", newline="", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["path", "size_bytes", "sha256"])

        for path in sorted(files):
            writer.writerow(
                [
                    str(path),
                    path.stat().st_size,
                    calculate_sha256(path),
                ]
            )

    print(f"OK: manifest generated: {OUTPUT_FILE}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
