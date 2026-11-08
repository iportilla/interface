"""
medium.py — Medium Lab: Radio Buttons & Dynamic Styling
=========================================================
Demonstrates radio button groups and CSS injection in Streamlit:

- st.radio           : mutually exclusive option picker (horizontal layout)
- st.markdown(unsafe_allow_html=True) : injects a <style> block to change
                       the app background color based on the selected option
- Color swatch       : renders an inline HTML div as a live color preview

Run with:
    streamlit run medium.py
"""

import streamlit as st

st.set_page_config(page_title="Medium Lab — Radio Buttons", page_icon="🎨")

st.title("Medium Lab — Radio Buttons")
st.caption("Radio buttons let users pick exactly one option from a group. Here they control the page background color via custom CSS.")

st.divider()

# Color options: label -> hex
COLOR_OPTIONS = {
    "Gray":       "#f4f5f7",
    "White":      "#ffffff",
    "Light Blue": "#eaf4fb",
    "Red":        "#ff6b6b",
    "Green":      "#51cf66",
    "Blue":       "#74c0fc",
    "Yellow":     "#ffd43b",
    "Orange":     "#ff922b",
    "Purple":     "#cc5de8",
    "Pink":       "#f783ac",
    "Teal":       "#20c997",
}

st.subheader("Favorite Color")
st.markdown("Pick your favorite color to change the page background:")

selected_label = st.radio(
    "Color",
    options=list(COLOR_OPTIONS.keys()),
    index=2,  # Light Blue default
    horizontal=True,
    label_visibility="collapsed",
)

selected_hex = COLOR_OPTIONS[selected_label]

# Inject CSS to change the Streamlit app background
st.markdown(
    f"""
    <style>
        .stApp {{
            background-color: {selected_hex};
        }}
    </style>
    """,
    unsafe_allow_html=True,
)

# Show a color swatch and the chosen hex
col1, col2 = st.columns([1, 5])
with col1:
    st.markdown(
        f'<div style="width:48px;height:48px;border-radius:8px;'
        f'background:{selected_hex};border:1px solid #ccc;"></div>',
        unsafe_allow_html=True,
    )
with col2:
    st.markdown(f"**{selected_label}** — `{selected_hex}`")
