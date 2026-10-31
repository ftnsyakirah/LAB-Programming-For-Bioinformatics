"""Lab 1 - Python fundamentals for biological calculations."""


def gc_percent(a: int, c: int, g: int, t: int) -> float:
    """Return the GC percentage from the four base counts.

    Raises:
        ValueError: if any count is negative or the total is zero.
    """
    if any(x < 0 for x in (a, c, g, t)):
        raise ValueError("Counts must be non-negative")
    total = a + c + g + t
    if total == 0:
        raise ValueError("Total bases cannot be zero")
    return (g + c) / total * 100


def format_report(sample: str, length: int, gc: float) -> str:
    """Return a one-line report with units, e.g. 'S1: 60 bases, GC 46.7%'."""
    return f"{sample}: {length} bases, GC {gc:.1f}%"


def parse_counts(text: str) -> tuple[int, int, int, int]:
    """Parse 'A C G T' counts separated by spaces or commas.

    Raises:
        ValueError: if there are not exactly four non-negative integers.
    """
    parts = text.replace(",", " ").split()
    if len(parts) != 4:
        raise ValueError("Must provide exactly four counts")
    try:
        counts = tuple(int(x) for x in parts)
    except ValueError:
        raise ValueError("Counts must be integers")
    if any(x < 0 for x in counts):
        raise ValueError("Counts must be non-negative")
    return counts
