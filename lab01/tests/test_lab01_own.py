import pytest
from src.basics import gc_percent, format_report, parse_counts

def test_gc_percent_valid():
    assert gc_percent(18, 12, 10, 20) == pytest.approx(36.6666, rel=1e-3)

def test_gc_percent_negative():
    with pytest.raises(ValueError):
        gc_percent(-1, 5, 5, 5)

def test_gc_percent_zero_total():
    with pytest.raises(ValueError):
        gc_percent(0, 0, 0, 0)

def test_format_report():
    text = format_report("Amplicon_01", 60, 36.6667)
    assert text == "Amplicon_01: 60 bases, GC 36.7%"

def test_parse_counts_spaces():
    assert parse_counts("18 12 10 20") == (18, 12, 10, 20)

def test_parse_counts_commas():
    assert parse_counts("18,12,10,20") == (18, 12, 10, 20)

def test_parse_counts_invalid():
    with pytest.raises(ValueError):
        parse_counts("18,12,10")  # kurang satu
