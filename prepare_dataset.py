#!/usr/bin/env python3
from __future__ import annotations

import logging
import urllib.request
from pathlib import Path


DEFAULT_URL = "https://zenodo.org/records/12805484/files/Promise+.arff?download=1"
DEFAULT_INPUT = "Promise+.arff"
DEFAULT_OUTPUT = "output.txt"
DEFAULT_START_LINE = 10

logger = logging.getLogger(__name__)


def download_file(url: str, output_path: Path) -> None:
    logger.info("Downloading ARFF file from %s to %s", url, output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with urllib.request.urlopen(url) as response:
        data = response.read()
    output_path.write_bytes(data)
    logger.info("Download completed: %s", output_path)


def transform_arff_to_txt(input_path: Path, output_path: Path, start_line: int) -> int:
    logger.info(
        "Transforming ARFF file %s into %s (start line: %d)",
        input_path,
        output_path,
        start_line,
    )
    written = 0
    output_path.parent.mkdir(parents=True, exist_ok=True)

    with input_path.open("r", encoding="utf-8") as f_in, output_path.open(
        "w", encoding="utf-8"
    ) as f_out:
        for i, line in enumerate(f_in, start=1):
            if i < start_line:
                continue

            first_quote = line.find("'")
            if first_quote == -1:
                continue
            second_quote = line.find("'", first_quote + 1)
            if second_quote == -1:
                continue

            text = line[first_quote + 1 : second_quote]
            f_out.write(text + "\n")
            written += 1

    logger.info("Transformation completed: %d lines written to %s", written, output_path)
    return written


def ensure_data_ready(
    input_path: Path = Path(DEFAULT_INPUT),
    output_path: Path = Path(DEFAULT_OUTPUT),
    url: str = DEFAULT_URL,
    start_line: int = DEFAULT_START_LINE,
) -> int:
    if output_path.exists():
        logger.info("Output file already exists, skipping preparation: %s", output_path)
        return 0

    logger.info("Output file is missing, preparing dataset: %s", output_path)
    download_file(url, input_path)
    return transform_arff_to_txt(input_path, output_path, start_line)
