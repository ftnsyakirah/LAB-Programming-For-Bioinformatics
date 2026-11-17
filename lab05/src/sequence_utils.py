"""Reusable DNA sequence utilities for BioPyLearn."""

DNA_BASES = frozenset("ACGT")
COMPLEMENT = str.maketrans("ACGT", "TGCA")


def clean_sequence(raw: str) -> str:
    """Upper-case raw text and drop spaces, digits and newlines."""
    return "".join(c.upper() for c in raw if c.isalpha())


def is_valid_dna(sequence: str, allow_n: bool = False) -> bool:
    """True for a non-empty string of A, C, G, T (N if allowed)."""
    if not sequence:
        return False
    sequence = sequence.upper()
    if allow_n:
        return all(c in DNA_BASES or c == "N" for c in sequence)
    return all(c in DNA_BASES for c in sequence)


def gc_content(sequence: str) -> float:
    """Return GC percentage (0-100); ValueError if invalid."""
    if not is_valid_dna(sequence):
        raise ValueError("Invalid DNA sequence")
    return 100 * (sequence.upper().count("G") + sequence.upper().count("C")) / len(sequence)


def reverse_complement(sequence: str) -> str:
    """Return the reverse complement; ValueError if invalid."""
    if not is_valid_dna(sequence):
        raise ValueError("Invalid DNA sequence")
    sequence = sequence.upper()
    return sequence.translate(COMPLEMENT)[::-1]

def find_motif(sequence: str, motif: str) -> list[int]:
    """Return every 0-based start of motif (overlaps allowed)."""
    if not motif:
        raise ValueError("Empty motif")
    sequence = sequence.upper()
    motif = motif.upper()
    return [i for i in range(len(sequence) - len(motif) + 1) if sequence[i:i + len(motif)] == motif]