import streamlit as st
import pandas as pd
import itertools
import random

st.set_page_config(page_title="Amazon 2-Word Combo Generator", layout="wide")
st.title("Amazon 2-Word Combination Generator (100k ready)")

default_words = """
... (lista extinsă de cuvinte ~320)
"""
word_input = st.text_area("Keywords (comma separated)", default_words, height=250)
num_combinations = st.number_input("How many combinations?", min_value=10, max_value=100000, value=5000, step=100)
shuffle_option = st.checkbox("Shuffle results")

if st.button("Generate Combinations"):
    words = [w.strip() for w in word_input.split(",") if w.strip()]
    if len(words) < 2:
        st.error("Please enter at least 2 words.")
    else:
        combos = list(itertools.permutations(words, 2))
        if shuffle_option:
            random.shuffle(combos)
        combos = combos[:num_combinations]
        df = pd.DataFrame({"combination": [f"{a} {b}" for a, b in combos]})
        st.success(f"Generated {len(df)} combinations.")
        st.dataframe(df)
        csv = df.to_csv(index=False).encode('utf-8')
        st.download_button(label="Download CSV", data=csv, file_name="amazon_combinations.csv", mime="text/csv")
