
import streamlit as st
import pandas as pd
import plotly.express as px

from analyzer import analyze_sequence


st.set_page_config(
    page_title="Protein Sequence Analyzer",
    page_icon="🧬",
    layout="wide"
)

st.title("🧬 Protein Sequence Analyzer")
st.caption(
    "Analyze amino acid composition, sequence validity, "
    "and estimated molecular weight."
)

st.divider()

# Sidebar
st.sidebar.header("About")
st.sidebar.write(
    "Upload a protein sequence in FASTA or TXT format, "
    "or paste a sequence directly."
)
st.sidebar.info(
    "The analyzer supports the 20 standard amino acids."
)

# Sequence input
st.subheader("Input Protein Sequence")

uploaded_file = st.file_uploader(
    "Upload a FASTA or TXT file",
    type=["fasta", "fa", "txt"]
)

pasted_sequence = st.text_area(
    "Or paste your sequence here",
    placeholder="Paste a sequence or FASTA record...",
    height=150
)


raw_sequence = pasted_sequence

if uploaded_file is not None:
    try:
        raw_sequence = uploaded_file.getvalue().decode("utf-8")
    except UnicodeDecodeError:
        raw_sequence = ""
        st.error("Please upload a valid text-based sequence file.")

if st.button("Analyze Sequence", type="primary"):
    if not raw_sequence.strip():
        st.warning("Please enter or upload a protein sequence.")
    else:
        result = analyze_sequence(raw_sequence)

        if not result["sequence"]:
            st.warning("No protein sequence was found.")
        else:
            st.session_state["analysis_result"] = result

# Display analysis
if "analysis_result" in st.session_state:
    result = st.session_state["analysis_result"]

    st.divider()
    st.subheader("Analysis Summary")

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Sequence Length", result["length"])
    col2.metric(
        "Amino Acid Types",
        result["unique_amino_acids"]
    )

    if result["molecular_weight"] is not None:
        col3.metric(
            "Molecular Weight",
            f'{result["molecular_weight"]:,.2f} Da'
        )
    else:
        col3.metric("Molecular Weight", "Unavailable")

    if result["invalid_characters"]:
        col4.metric("Sequence Status", "Invalid")
    else:
        col4.metric("Sequence Status", "Valid")

    # Validation report
    st.subheader("Sequence Validation")

    if result["invalid_characters"]:
        st.error(
            "Invalid characters found: "
            + ", ".join(result["invalid_characters"])
        )
        st.write(
            "Molecular weight is not calculated until "
            "the sequence contains only standard amino acids."
        )
    else:
        st.success("All characters are valid standard amino acids.")

    # Composition table
    df = pd.DataFrame(result["composition"])
    present_df = df[df["Count"] > 0].copy()

    st.subheader("Amino Acid Composition")
    st.dataframe(
        present_df,
        hide_index=True,
        use_container_width=True
    )

    # Charts
    if not present_df.empty:
        chart_col1, chart_col2 = st.columns(2)

        with chart_col1:
            st.subheader("Amino Acid Frequency")
            frequency_chart = px.bar(
                present_df,
                x="Amino Acid",
                y="Count",
                title="Count of Each Amino Acid"
            )
            st.plotly_chart(
                frequency_chart,
                use_container_width=True
            )

        with chart_col2:
            st.subheader("Amino Acid Percentage")
            percentage_chart = px.pie(
                present_df,
                names="Amino Acid",
                values="Count",
                hole=0.4,
                title="Composition of the Protein"
            )
            st.plotly_chart(
                percentage_chart,
                use_container_width=True
            )

    # Download results
    st.subheader("Export Results")

    csv_data = df.to_csv(index=False).encode("utf-8")

    st.download_button(
        label="Download Composition as CSV",
        data=csv_data,
        file_name="amino_acid_composition.csv",
        mime="text/csv"
    )

    with st.expander("View cleaned protein sequence"):
        st.code(result["sequence"], language=None)
