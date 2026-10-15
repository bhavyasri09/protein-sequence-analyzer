import unittest

from analyzer import clean_sequence, analyze_sequence


class TestProteinAnalyzer(unittest.TestCase):

    def test_clean_sequence(self):
        result = clean_sequence(
            ">Protein 1\nACD\nEFG"
        )
        self.assertEqual(result, "ACDEFG")

    def test_sequence_length(self):
        result = analyze_sequence("ACDEFG")
        self.assertEqual(result["length"], 6)

    def test_unique_amino_acids(self):
        result = analyze_sequence("AAACCG")
        self.assertEqual(result["unique_amino_acids"], 3)

    def test_invalid_characters(self):
        result = analyze_sequence("ACDX*")
        self.assertEqual(
            result["invalid_characters"],
            ["*", "X"]
        )

    def test_valid_sequence(self):
        result = analyze_sequence("ACDEFG")
        self.assertEqual(result["invalid_characters"], [])
        self.assertIsNotNone(result["molecular_weight"])

    def test_empty_sequence(self):
        result = analyze_sequence("")
        self.assertEqual(result["length"], 0)
        self.assertIsNone(result["molecular_weight"])

    def test_fasta_header_is_removed(self):
        result = analyze_sequence(
            ">Test Protein\nACDE"
        )
        self.assertEqual(result["sequence"], "ACDE")
        self.assertEqual(result["length"], 4)

    def test_molecular_weight_not_calculated_for_invalid_sequence(self):
        result = analyze_sequence("ACDX")
        self.assertIsNone(result["molecular_weight"])


if __name__ == "__main__":
    unittest.main()
