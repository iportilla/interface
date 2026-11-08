"""
simple.py — Simple Lab: Basic Inputs
=====================================
Demonstrates the three most fundamental Streamlit input widgets:

- st.text_input  : single-line text entry
- st.multiselect : checklist allowing multiple independent selections
- st.text_area   : multi-line text entry with live word/character count

Run with:
    streamlit run simple.py
"""

import streamlit as st

st.set_page_config(page_title="Simple Lab — Basic Inputs", page_icon="📝")

st.title("Simple Lab — Basic Inputs")
st.caption("This lab covers the three most fundamental HTML form elements: a text field, a checklist, and a multi-line text area.")

st.divider()

# --- Text Field ---
st.subheader("Text Field")
st.markdown("A single-line input for short text entry.")
username = st.text_input("Username", placeholder="Enter your username")
if username:
    st.success(f"Hello, **{username}**!")

st.divider()

# --- Checklist ---
st.subheader("Checklist")
st.markdown("Checkboxes let users select multiple options independently.")
interests = st.multiselect(
    "Select your interests:",
    options=["Coding", "Design", "Data Science", "DevOps"],
)
if interests:
    st.info(f"You selected: {', '.join(interests)}")

st.divider()

# --- Multi-line Text Area ---
st.subheader("Multi-line Text Area")
st.markdown("A text area accepts longer, multi-line text input.")
comments = st.text_area("Comments", placeholder="Enter your comments here...", height=140)
if comments:
    word_count = len(comments.split())
    st.caption(f"{word_count} word{'s' if word_count != 1 else ''} · {len(comments)} characters")
