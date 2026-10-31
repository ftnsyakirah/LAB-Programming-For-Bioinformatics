"""Lab 2 - biological sequences as strings (becomes sequence_utils.py in Week 5)."""

DNA_BASES = frozenset("ACGT")


def clean_sequence(raw: str) -> str:
    """Upper-case raw text and drop spaces, digits and newlines."""
    result = ""

    for char in raw.upper():
        if char.isalpha():
            result += char

    return result


def is_valid_dna(seq: str, allow_n: bool = False) -> bool:
    """True for a non-empty string of A, C, G, T (and N when allowed)."""
    #raise NotImplementedError("TODO: implement is_valid_dna")
    seq = seq.upper()

    if not seq:
        return False

    allowed = set(DNA_BASES)

    if allow_n:
        allowed.add("N")
    
    return all(char in allowed for char in seq)


def gc_content(seq: str) -> float:
    """Return GC percentage (0-100); ValueError if empty or not A/C/G/T."""
    #raise NotImplementedError("TODO: implement gc_content")
    seq = seq.upper()

    if not is_valid_dna(seq):
        raise ValueError("Invalid DNA sequence")

    gc_count = seq.count("G") + seq.count("C")
    return (gc_count / len(seq)) * 100

def transcribe(dna: str) -> str:
    """Return the RNA copy of a DNA sequence (T becomes U)."""
    #raise NotImplementedError("TODO: implement transcribe")
    dna = dna.upper()

    if not is_valid_dna(dna):
        raise ValueError("Invalid DNA sequence")

    return dna.replace("T", "U")


def find_motif(seq: str, motif: str) -> list[int]:
    """Return every 0-based start of motif in seq (overlaps allowed)."""
    #raise NotImplementedError("TODO: implement find_motif")
    if not motif:
        raise ValueError("Motif cannot be empty")

    seq = seq.upper()
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