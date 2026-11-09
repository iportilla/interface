# Intro Streamlit Lab

Three hands-on Streamlit apps that mirror the [HTML form labs](../intro-html-lab/), progressing from basic inputs to interactive data tables.

## Apps

| File | Difficulty | What it covers |
|---|---|---|
| `simple.py` | Simple | Text field, checklist, multi-line text area |
| `medium.py` | Medium | Radio buttons with live CSS background-color injection |
| `advanced.py` | Advanced | Single-select drill-down table + multi-select comparison table with bar chart |

---

## New to Python?

Python is the programming language used in these labs. Before running anything, make sure Python is installed on your machine.

### Check if Python is installed

```bash
python --version
# or
python3 --version
```

If you see something like `Python 3.11.2` you are ready. If not, download Python from [https://www.python.org/downloads/](https://www.python.org/downloads/) and follow the installer for your operating system. Install version **3.9 or newer**.

### What is pip?

`pip` is Python's package manager — it downloads and installs libraries for you. It comes bundled with Python. Verify it is available:

```bash
pip --version
# or
pip3 --version
```

---

## Setting Up a Virtual Environment

A virtual environment keeps these lab dependencies isolated from the rest of your system. This is the recommended approach. Choose either **venv** (built into Python) or **conda** (if you use Anaconda/Miniconda).

### Option A — venv (recommended for most students)

```bash
# 1. Create the environment (run once)
python -m venv venv

# 2. Activate it
source venv/bin/activate        # macOS / Linux
venv\Scripts\activate           # Windows

# 3. Install dependencies
pip install -r requirements.txt

# 4. When you are done, deactivate
deactivate
```

> Every time you open a new terminal to work on the labs, run the **activate** step again before running `streamlit run`.

### Option B — conda (if you have Anaconda or Miniconda)

```bash
# 1. Create the environment (run once)
conda create -n interface-labs python=3.11

# 2. Activate it
conda activate interface-labs

# 3. Install dependencies
pip install -r requirements.txt

# 4. When you are done, deactivate
conda deactivate
```

---

## Running the Labs

After activating your environment and installing dependencies:

```bash
streamlit run simple.py
streamlit run medium.py
streamlit run advanced.py
```

Each command opens the app automatically in your browser at `http://localhost:8501`. Press `Ctrl+C` in the terminal to stop the app.

---

## Lab Descriptions

### Simple — Basic Inputs (`simple.py`)

Covers the three most fundamental form elements:

- **Text field** — `st.text_input` with a live greeting response
- **Checklist** — `st.multiselect` showing selected interests
- **Multi-line text area** — `st.text_area` with live word and character count

### Medium — Radio Buttons (`medium.py`)

Demonstrates radio button groups and dynamic styling:

- **Radio buttons** — `st.radio` (horizontal layout) with 11 color choices
- **Live background** — injects a `<style>` block via `st.markdown(unsafe_allow_html=True)` to change the app background color instantly
- **Color swatch** — displays a preview tile and the selected hex code

### Advanced — Interactive Tables (`advanced.py`)

Shows how to drive table interactions with Streamlit widgets:

- **Single select** — `st.radio` selects one country; a quarterly sales breakdown table renders immediately below
- **Multi select** — `st.multiselect` picks multiple countries; a comparison table and bar chart update in real time
- **Formatted numbers** — `st.column_config.NumberColumn` renders all sales figures as `$` values

---

## Project Structure

```
intro-streamlit-lab/
├── simple.py          # Basic inputs lab
├── medium.py          # Radio buttons + background color lab
├── advanced.py        # Interactive tables lab
├── requirements.txt   # Python dependencies
└── README.md          # This file
```

## Dependencies

| Package | Version | Purpose |
|---|---|---|
| `streamlit` | >= 1.49.0 | UI framework |
| `pandas` | >= 2.0.0 | DataFrame handling (advanced lab) |
