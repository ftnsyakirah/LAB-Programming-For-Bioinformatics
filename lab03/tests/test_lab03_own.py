from qc import classify_read, trim_low_quality


def test_length_499_is_reject():
    assert classify_read(499, 0, 50.0) == "reject"


def test_gc_70_is_pass():
    assert classify_read(500, 0, 70.0) == "pass"


def test_trim_all_low_returns_zero():
    assert trim_low_quality([5, 6, 7], 20) == 0