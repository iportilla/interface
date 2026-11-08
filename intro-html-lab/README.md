# Intro HTML Lab

Four HTML pages that teach core HTML form elements, progressing from a landing page through three hands-on labs.

## Pages

| File | Difficulty | What it covers |
|---|---|---|
| `index.html` | — | Landing page with cards linking to each lab |
| `simple.html` | Simple | Text field, checklist, multi-line text area |
| `medium.html` | Medium | Radio buttons with live JavaScript background-color change |
| `advanced.html` | Advanced | Countries and sales tables with single-select drill-down and multi-select comparison |

## Getting Started

No build step or server required. Open any file directly in your browser:

```bash
open index.html        # macOS
start index.html       # Windows
xdg-open index.html    # Linux
```

Or serve locally with any static server:

```bash
npx serve .
# then visit http://localhost:3000
```

## Lab Descriptions

### Simple — Basic Inputs (`simple.html`)

Covers the three most fundamental HTML form elements with no JavaScript:

- **Text field** — `<input type="text">` for short single-line entry
- **Checklist** — `<input type="checkbox">` for independent multi-option selection
- **Multi-line text area** — `<textarea>` for longer freeform input

### Medium — Radio Buttons and JavaScript (`medium.html`)

Introduces radio buttons and connects them to a JavaScript event listener:

- **Radio buttons** — `<input type="radio">` with 11 color options (mutually exclusive)
- **Live background** — `change` event updates `document.body.style.backgroundColor` on every selection
- **Smooth transition** — CSS `transition: background-color 0.3s` provides a gentle fade

### Advanced — Interactive Tables (`advanced.html`)

Demonstrates JavaScript-driven table interactions:

- **Single select** — radio button in the first column; selecting a row populates a quarterly sales breakdown table below
- **Multi select** — checkboxes allow selecting multiple countries simultaneously; a live comparison table and chip-tag summary update on every change
- **Pure HTML/CSS/JS** — no frameworks or libraries required

## Project Structure

```
intro-html-lab/
├── index.html      # Landing page — links to all three labs
├── simple.html     # Basic inputs lab
├── medium.html     # Radio buttons + JS background color lab
└── advanced.html   # Interactive tables lab
```

## Concepts Covered

| Concept | Lab |
|---|---|
| `<input type="text">` | Simple |
| `<input type="checkbox">` | Simple, Advanced |
| `<textarea>` | Simple |
| `<input type="radio">` | Medium, Advanced |
| DOM event listeners (`addEventListener`) | Medium, Advanced |
| Dynamic CSS via JavaScript | Medium |
| HTML `<table>` with `<thead>` and `<tbody>` | Advanced |
| Dynamic row generation (`createElement`) | Advanced |
