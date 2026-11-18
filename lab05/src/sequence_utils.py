"""Reusable DNA sequence utilities for BioPyLearn."""

DNA_BASES = frozenset("ACGT")
COMPLEMENT = str.maketrans("ACGT", "TGCA")


def clean_sequence(raw: str) -> str:
    """Upper-case raw text and drop spaces, digits and newlines."""
    result = ""

    for char in raw.upper():
        if char.isalpha():
            result += char

    return result


def is_valid_dna(sequence: str, allow_n: bool = False) -> bool:
    """True for a non-empty string of A, C, G, T (N if allowed)."""
    seq = sequence.upper()
    if not seq:
        return False

    allowed = set(DNA_BASES)

    if allow_n:
        allowed.add("N")

    return all(char in allowed for char in seq)


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
        raise ValueError("Motif cannot be empty")

    seq = sequence.upper()
    motif = motif.upper()

    positions = []
    start = 0
    while True:
        pos = seq.find(motif, start)
        if pos == -1:
            break

        positions.append(pos)
        start = pos + 1

    return positions

if __name__ == "__main__":
    print(clean_sequence("3e2r fAtiNnAkiraA"))
    print(is_valid_dna("Acgt",True))
    print(gc_content("gctaggcctaaatcg"))
    print(reverse_complement("agctgtaacc"))
    print(find_motif("AAAA", "aa"))