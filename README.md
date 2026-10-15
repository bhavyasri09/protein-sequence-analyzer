# Protein Sequence Analyzer

A Python-based bioinformatics project developed as part of my technical learning in data analytics. This project analyzes protein sequences and presents key biological information through an interactive Streamlit dashboard.

## Project Overview

The Protein Sequence Analyzer processes protein sequences to calculate sequence length, amino acid frequency, amino acid composition percentages, and estimated molecular weight. It also validates input sequences and identifies invalid characters.

The application combines Python programming, data processing, and visualization to make protein sequence analysis simple and accessible.

## Features

- **Sequence Analysis:** Calculates the total length of a protein sequence.
- **Amino Acid Frequency:** Counts the occurrences of each standard amino acid.
- **Composition Analysis:** Calculates amino acid percentages and displays the results in a table.
- **Molecular Weight Estimation:** Estimates the molecular weight of valid linear protein sequences.
- **Sequence Validation:** Detects characters outside the 20 standard amino acid letters.
- **Interactive Visualizations:** Displays amino acid composition using charts.
- **File Upload:** Accepts FASTA and TXT sequence files.
- **CSV Export:** Allows users to download amino acid composition results.
- **Unit Testing:** Tests the core analysis functions.

## Technologies Used

- Python
- Streamlit
- Pandas
- Plotly
- Unittest

## Project Structure

```text
protein-sequence-analyzer/
├── app.py
├── analyzer.py
├── requirements.txt
├── README.md
├── .gitignore
├── data/
│   └── insulin.fasta
└── tests/
    └── test_analyzer.py
```

## Installation and Execution

**1. Clone the repository**

```bash
git clone https://github.com/YOUR-USERNAME/protein-sequence-analyzer.git
cd protein-sequence-analyzer
```

**2. Create and activate a virtual environment**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

**3. Install the required libraries**

```bash
python -m pip install -r requirements.txt
```

**4. Run the application**

```bash
streamlit run app.py
```

Open the local URL displayed in the terminal to access the dashboard.

## Running Tests

Execute the following command from the project directory:

```bash
python -m unittest discover -s tests -v
```

## Sample Dataset

The project uses the human insulin precursor protein sequence from UniProt.

- **Accession ID:** P01308
- **Data source:** [UniProt – Human Insulin](https://www.uniprot.org/uniprotkb/P01308/entry)
- **File format:** FASTA

Users can also upload their own protein sequence files or enter sequences directly into the dashboard.

## Limitations

Molecular weight is an estimate based on average amino acid residue masses for a linear protein chain. The calculation does not account for protein processing, post-translational modifications, or disulfide bonds. The current validator accepts only the 20 standard amino acid letters.

## Future Scope

- Protein sequence similarity analysis.
- Support for additional amino acid codes.
- More protein statistics and visualizations.
- Exportable analysis reports.

## Author

**Bhavya Sri Pattapu**  

---

*An academic project exploring Python-based data analysis, bioinformatics, and interactive visualization.*
