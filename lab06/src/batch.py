"""Week 6 extension - batch processing, logging, FASTQ and a command-line tool."""
import argparse
import logging
import sys
from collections.abc import Iterator
from pathlib import Path

from bio_io import FastaFormatError, read_fasta, write_csv

LOG = logging.getLogger("batch")


class FastqFormatError(ValueError):
    """Raised when a FASTQ file is malformed."""


def process_directory(in_dir, out_csv, log_path=None) -> dict[str, int]:
    """Read every *.fasta file in in_dir; one bad file never stops the batch.

    Writes one row per file (file, records, status, reason) to out_csv and
    returns {'processed': ..., 'rejected': ..., 'records': ...}.
    """
    handler = None  #keep handler log so can remove it later
    if log_path is not None:    #create the log file and its parent folder if needed
        Path(log_path).parent.mkdir(    #create the parent folder if needed
            parents=True, exist_ok=True)
        handler = logging.FileHandler(  #open the log file for writing with utf-8 encoding
            log_path, mode="w", encoding="utf-8")
        handler.setFormatter(
            logging.Formatter("%(levelname)s %(message)s"))
        LOG.addHandler(handler)
        LOG.setLevel(logging.INFO)
    rows: list[dict] = []
    summary = {"processed": 0, "rejected": 0, "records": 0}
    try:
        for path in sorted(Path(in_dir).glob("*.fasta")):   #read all *.fasta files in the input folder, sorted by name
            try:
                count = sum(1 for _ in read_fasta(path))    #count the number of records in the FASTA file
                if count == 0:  
                    raise FastaFormatError("empty file")
            except (OSError, UnicodeDecodeError, FastaFormatError) as err:
                LOG.warning("rejected %s: %s", path.name, err)
                rows.append({"file": path.name, "records": 0,
                             "status": "rejected", "reason": str(err)})
                summary["rejected"] += 1
            else:
                LOG.info("processed %s (%d records)", path.name, count)
                rows.append({"file": path.name, "records": count,
                             "status": "processed", "reason": ""})
                summary["processed"] += 1
                summary["records"] += count
        write_csv(rows, out_csv,    #write the results to the output CSV file
                  ["file", "records", "status", "reason"])
    finally:
        if handler is not None:
            LOG.removeHandler(handler)
            handler.close()
    return summary


def read_fastq(path) -> Iterator[tuple[str, str, str]]:
    """Yield (read_id, sequence, quality) for each 4-line FASTQ record."""
    with open(path, encoding="utf-8") as handle:
        while True:
            header = handle.readline()  #read the header line
            if not header:  #until end of file (EOF)
                return
            if not header.strip():  #skip blank lines
                continue
            seq = handle.readline().strip()
            plus = handle.readline().strip()
            qual = handle.readline().strip()    #read the 4 lines of a FASTQ record
            if not header.startswith("@") or not plus.startswith("+"):
                raise FastqFormatError(
                    f"{path}: malformed record near {header.strip()!r}")
            if len(seq) != len(qual):
                raise FastqFormatError(
                    f"{path}: sequence and quality lengths differ "
                    f"for {header.strip()!r}")
            yield header[1:].split()[0], seq, qual


def mean_phred(quality: str, offset: int = 33) -> float:
    """Mean Phred score of a quality string (Phred+33 by default)."""
    if not quality:
        raise ValueError("quality string is empty")
    return sum(ord(ch) - offset for ch in quality) / len(quality)


def main(argv: list[str] | None = None) -> int:
    """Command-line entry point. Exit code 0 = all good, 1 = some files rejected, 2 = bad input."""
    parser = argparse.ArgumentParser(
        description="Summarise every FASTA file in a folder.")
    parser.add_argument("in_dir", help="folder containing *.fasta files")   #folder containing the input FASTA files
    parser.add_argument("--out", default="results", #folder for output files (default: results)")
                        help="output folder (default: results)")
    args = parser.parse_args(argv)
    if not Path(args.in_dir).is_dir():  #make sure the input folder exists and is a directory
        print(f"error: {args.in_dir} is not a folder", file=sys.stderr)
        return 2
    out = Path(args.out)
    summary = process_directory(    #process the input folder and write the results to a CSV file and a log file
        args.in_dir, out / "processing_log.csv", out / "batch.log")
    print(f"processed={summary['processed']} "
          f"rejected={summary['rejected']} "
          f"records={summary['records']}")
    return 1 if summary["rejected"] else 0


if __name__ == "__main__":
    sys.exit(main())