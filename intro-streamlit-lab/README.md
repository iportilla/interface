# Intro Streamlit Lab

Three hands-on Streamlit apps that mirror the [HTML form labs](../intro-html-lab/), progressing from basic inputs to interactive data tables.

## Labs

| App | Difficulty | What it covers |
|---|---|---|
| `simple.py` | Simple | Text field, checklist (multi-select), multi-line text area |
| `medium.py` | Medium | Radio buttons with live CSS background-color injection |
| `advanced.py` | Advanced | Single-select drill-down table + multi-select comparison table with bar chart |

## Getting Started

### Prerequisites

- Python 3.9+
- pip

### Install dependencies

```bash
pip install -r requirements.txt
```

### Run a lab

```bash
streamlit run simple.py
streamlit run medium.py
streamlit run advanced.py
```

Each command opens the app in your browser at `http://localhost:8501`.

## Lab Descriptions

### Simple — Basic Inputs (`simple.py`)

Covers the three most fundamental form elements:

- **Text field** — `st.text_input` with a live greeting
- **Checklist** — `st.multiselect` showing selected interests
- **Multi-line text area** — `st.text_area` with word and character count

### Medium — Radio Buttons & JS (`medium.py`)

Demonstrates radio button groups and dynamic styling:

- **Radio buttons** — `st.radio` (horizontal layout) with 11 color choices
- **Live background** — injects a `<style>` block via `st.markdown(unsafe_allow_html=True)` to change the app background color instantly
- **Color swatch** — displays a preview tile and hex code for the chosen color

### Advanced — Interactive Tables (`advanced.py`)

Shows how to drive table interactions with Streamlit widgets:

- **Single select** — radio buttons select a country; a quarterly sales breakdown table appears immediately below
- **Multi select** — `st.multiselect` picks multiple countries; a comparison table and bar chart update in real time
- **Formatted numbers** — `st.column_config.NumberColumn` renders sales figures as `$` values

## Project Structure

```
intro-streamlit-lab/
├── simple.py          # Basic inputs lab
├── medium.py          # Radio buttons + background color lab
├── advanced.py        # Interactive tables lab
└── requirements.txt   # Python dependencies
```

## Dependencies

| Package | Version | Purpose |
|---|---|---|
| `streamlit` | ≥ 1.32.0 | UI framework |
| `pandas` | ≥ 2.0.0 | DataFrame handling (advanced lab) |
