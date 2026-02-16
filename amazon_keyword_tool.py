import streamlit as st
import pandas as pd
import itertools
import random

st.set_page_config(page_title="Amazon Logical 2-Word Combos", layout="wide")
st.title("Amazon 2-Word Logical Combination Generator (100k ready)")

# Liste pe categorii pentru combinatii logice
categories = {
    "Electronics": ["phone","tablet","laptop","charger","usb","hd","4k","led","bluetooth","smart","wireless","speaker","headphones","camera","drone","gopro","smartwatch","fitbit","airpods","earbuds"],
    "Kitchen/Home": ["knife","pan","pot","toaster","blender","coffee","tea","spatula","oven","kettle","plate","cup","mug"],
    "Fitness/Sport": ["mat","dumbbell","band","resistance","yoga","helmet","gloves","sneakers"],
    "Fashion": ["shirt","pants","dress","skirt","jacket","coat","hoodie","shoes","sandals","boots","scarf","hat","socks"],
    "Baby/Toys": ["baby","stroller","crib","diaper","bottle","pacifier","toy","puzzle","doll","lego","action","figure"],
    "Beauty": ["makeup","skincare","shampoo","conditioner","lotion","perfume","brush","comb","nailpolish","foundation","mascara","eyeliner","lipstick"],
    "Office": ["pen","pencil","notebook","planner","sticky","calendar","envelope","stapler","scissors","folder"],
    "Home Decor": ["rug","curtain","mat","lamp","bulb","blanket","pillow","shelf","basket","box","candle"]
}

# Textarea pentru modificari
word_input = st.text_area("Keywords by category (comma separated, optional)", height=300)

num_combinations = st.number_input("How many combinations?", min_value=10, max_value=100000, value=5000, step=100)
shuffle_option = st.checkbox("Shuffle results")

if st.button("Generate Logical Combinations"):
    combos = []

    # Folosim lista din text area daca este completata
    if word_input.strip():
        user_words = [w.strip() for w in word_input.split(",") if w.strip()]
        # Combinații logice: permutări între fiecare pereche de cuvinte
        combos = list(itertools.permutations(user_words, 2))
    else:
        # Combinații logice: permutări în interiorul fiecarei categorii
        for cat_words in categories.values():
            cat_combos = list(itertools.permutations(cat_words, 2))
            combos.extend(cat_combos)

    if shuffle_option:
        random.shuffle(combos)

    # Limităm la numărul cerut
    combos = combos[:num_combinations]

    df = pd.DataFrame({"combination": [f"{a} {b}" for a, b in combos]})
    st.success(f"Generated {len(df)} logical combinations.")
    st.dataframe(df)

    csv = df.to_csv(index=False).encode('utf-8')
    st.download_button("Download CSV", data=csv, file_name="amazon_logical_combinations.csv", mime="text/csv")
