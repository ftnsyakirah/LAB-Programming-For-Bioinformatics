import pytest

from src.batch import main, process_directory
from src.bio_io import FastaFormatError, read_fasta

def test_bad_file_does_not_stop_batch(tmp_path):
    """A bad file should be logged and the batch should continue."""
    # Create a good FASTA file
    good_fasta = tmp_path / "good.fasta"
    good_fasta.write_text(">seq1\nACGT\n>seq2\nTGCA\n")

    # Create a bad FASTA file (empty)
    bad_fasta = tmp_path / "bad.fasta"
    bad_fasta.write_text("")

    # Process the directory
    summary = process_directory(tmp_path, tmp_path / "out.csv", tmp_path / "log.txt")

    # Check that the summary reflects one processed and one rejected file
    assert summary["processed"] == 1
    assert summary["rejected"] == 1
    assert summary["records"] == 2

    # Check that the log file contains a warning about the bad file
    log_content = (tmp_path / "log.txt").read_text()
    assert "rejected bad.fasta" in log_content
 
 
def test_every_record_is_read():    #be sure that every record in a FASTA file is read correctly
    recs = dict(read_fasta("data/amplicons.fasta"))
    assert list(recs) == [f"ISO_00{i}" for i in range(1, 7)]

@pytest.mark.parametrize("text, msg", [
    ("ATGC\n>a\nATGC\n", "before the first header"),
    (">\nATGC\n", "empty header"),
    (">a\n>b\nATGC\n", "no sequence"),
])


def test_format_errors(tmp_path, text, msg):    #test that the read_fasta function raises FastaFormatError for various malformed FASTA files
    bad = tmp_path / "bad.fasta"
    bad.write_text(text)
    with pytest.raises(FastaFormatError, match=msg):
        list(read_fasta(bad))


def test_main_missing_folder(tmp_path):
    assert main([str(tmp_path / "missing_folder")]) == 2