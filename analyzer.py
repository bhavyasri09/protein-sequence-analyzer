from collections import Counter
VALID_AMINO_ACIDS = "ACDEFGHIKLMNPQRSTVWY"

# Average amino acid residue masses in Daltons
RESIDUE_WEIGHTS = {
    "A": 71.08, "C": 103.14, "D": 115.09,
    "E": 129.12, "F": 147.18, "G": 57.05,
    "H": 137.14, "I": 113.16, "K": 128.17,
    "L": 113.16, "M": 131.20, "N": 114.10,
    "P": 97.12, "Q": 128.13, "R": 156.19,
    "S": 87.08, "T": 101.11, "V": 99.13,
    "W": 186.21, "Y": 163.18
}

WATER_WEIGHT = 18.015


def clean_sequence(raw_sequence):
    """Remove FASTA headers and whitespace."""
    lines = raw_sequence.splitlines()
    sequence_lines = [
        line.strip()
        for line in lines
        if not line.strip().startswith(">")
    ]

    return "".join(sequence_lines).replace(" ", "").upper()


def analyze_sequence(raw_sequence):
    """Analyze a protein sequence and return its properties."""
    sequence = clean_sequence(raw_sequence)

    # Identify invalid characters
    invalid_characters = sorted(
        set(
            letter for letter in sequence
            if letter not in VALID_AMINO_ACIDS
        )
    )

    # Count amino acids
    counts = Counter(
        letter for letter in sequence
        if letter in VALID_AMINO_ACIDS
    )

    total_length = len(sequence)

    # Calculate frequency and percentage
    composition = []

    for amino_acid in VALID_AMINO_ACIDS:
        count = counts.get(amino_acid, 0)

        percentage = (
            count / total_length * 100
            if total_length > 0 else 0
        )

        composition.append({
            "Amino Acid": amino_acid,
            "Count": count,
            "Percentage": round(percentage, 2)
        })

    # Calculate molecular weight only for a valid sequence
    molecular_weight = None

    if total_length > 0 and not invalid_characters:
        molecular_weight = (
            sum(RESIDUE_WEIGHTS[letter] for letter in sequence)
            + WATER_WEIGHT
        )

    return {
        "sequence": sequence,
        "length": total_length,
        "unique_amino_acids": len(counts),
        "invalid_characters": invalid_characters,
        "composition": composition,
        "molecular_weight": (
            round(molecular_weight, 2)
            if molecular_weight is not None else None
        )
    }
