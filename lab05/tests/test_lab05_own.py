import pytest

from src.sequence_utils import reverse_complement
from src.normalize import cpm, proportions


def test_reverse_complement_valid():
    assert reverse_complement("ACGTCCAT") == "ATGGACGT"


def test_proportions_does_not_change_input():
    counts = [40, 180, 60]
    original = counts.copy()

    proportions(counts)

    assert counts == original


def test_proportions_zero_total():
    with pytest.raises(ValueError):
        proportions([0, 0, 0])


def test_cpm_default_library_size():
    assert cpm([10, 20]) == pytest.approx(
        [333333.3333333333, 666666.6666666666]
    )