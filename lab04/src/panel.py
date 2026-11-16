"""Lab 4 - lists and tuples for a gene panel and variant records."""
from typing import NamedTuple


class Variant(NamedTuple):
    """One variant coordinate: an immutable record with named fields."""

    chrom: str
    pos: int
    ref: str
    alt: str


def filter_panel(genes: list[str], priority: set[str]) -> list[str]:
    """Keep the genes that are in priority, preserving the original order."""
    return [gene for gene in genes if gene in priority]



def sorted_copy(items: list) -> list:
    """Return a sorted copy; the original list is not changed."""
    return sorted(items)


def _chrom_key(chrom: str) -> tuple:
    chrom = chrom.removeprefix("chr")
    if chrom.isdigit():
        return (0, int(chrom))

    if chrom == "X":
        return (1, 23)

    if chrom == "Y":
        return (1, 24)

    if chrom == "M":
        return (1, 25)

    raise ValueError(f"Unknown chromosome: {chrom}")


def sort_variants(variants: list[Variant]) -> list[Variant]:
    """Sort by chromosome (1-22, X, Y, M) and then by position."""
    return sorted(
        variants,
        key=lambda v: (_chrom_key(v.chrom), v.pos)
    )
