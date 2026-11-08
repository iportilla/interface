# Interface Labs

A collection of hands-on UI labs that teach web interface development using HTML and Python (Streamlit), progressing from basic form elements to interactive data-driven applications.

## 📁 Labs

| Folder | Stack | Difficulty range | README |
|---|---|---|---|
| [`intro-html-lab/`](intro-html-lab/) | HTML · CSS · JavaScript | Simple → Advanced | [intro-html-lab/README.md](intro-html-lab/README.md) |
| [`intro-streamlit-lab/`](intro-streamlit-lab/) | Python · Streamlit · pandas | Simple → Advanced | [intro-streamlit-lab/README.md](intro-streamlit-lab/README.md) |

Both lab sets cover the same three difficulty levels side-by-side, making it easy to compare how the same UI concepts translate between plain HTML and a Python framework.

---

## 🧪 intro-html-lab

Four static HTML pages — no build step, no server required.

| Page | What it covers |
|---|---|
| `index.html` | Landing page linking to all three labs |
| `simple.html` | Text field, checklist, multi-line textarea |
| `medium.html` | Radio buttons + live JS background-color change |
| `advanced.html` | Country sales tables with single-select drill-down and multi-select comparison |

**Quick start:**
```bash
open intro-html-lab/index.html
```

➡️ Full details: [intro-html-lab/README.md](intro-html-lab/README.md)

---

## 🐍 intro-streamlit-lab

Three Python apps built with [Streamlit](https://streamlit.io).

| App | What it covers |
|---|---|
| `simple.py` | `st.text_input`, `st.multiselect`, `st.text_area` |
| `medium.py` | `st.radio` + CSS injection for live background color |
| `advanced.py` | `st.dataframe` with single-select drill-down, multi-select comparison, and bar chart |

**Quick start:**
```bash
cd intro-streamlit-lab
pip install -r requirements.txt
streamlit run simple.py
```

➡️ Full details: [intro-streamlit-lab/README.md](intro-streamlit-lab/README.md)

---

## 🗺️ Concept Coverage

| Concept | HTML lab | Streamlit lab |
|---|---|---|
| Text input | `simple.html` | `simple.py` |
| Multi-select checklist | `simple.html` | `simple.py` |
| Multi-line text area | `simple.html` | `simple.py` |
| Radio buttons | `medium.html` | `medium.py` |
| Dynamic background color | `medium.html` | `medium.py` |
| Data table — single select | `advanced.html` | `advanced.py` |
| Data table — multi select | `advanced.html` | `advanced.py` |
| Bar chart | — | `advanced.py` |

## 📄 License

MIT
