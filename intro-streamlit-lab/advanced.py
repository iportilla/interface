"""
advanced.py — Advanced Lab: Interactive Tables
===============================================
Demonstrates widget-driven table interactions using Streamlit and pandas:

Single Select (radio -> quarterly drill-down):
- st.radio        : select one country from a horizontal list
- st.dataframe    : render the full summary table, then the quarterly breakdown
                    for the selected country

Multi Select (checkboxes -> live comparison):
- st.multiselect  : pick one or more countries
- st.dataframe    : comparison table of selected countries
- st.bar_chart    : auto-updating bar chart of total sales

NumberColumn config formats all sales figures as "$" values.

Run with:
    streamlit run advanced.py
"""

import streamlit as st
import pandas as pd

st.set_page_config(page_title="Advanced Lab — Interactive Tables", page_icon="🌍", layout="wide")

st.title("Advanced Lab — Interactive Tables")
st.caption(
    "Single-select (radio) drills into quarterly sales data. "
    "Multi-select (checkboxes) builds a live comparison table."
)

# --- Shared data ---
COUNTRY_META = {
    "usa":       {"name": "United States",  "capital": "Washington D.C.", "total": 1_240_500},
    "uk":        {"name": "United Kingdom", "capital": "London",          "total":   876_300},
    "germany":   {"name": "Germany",        "capital": "Berlin",          "total":   934_750},
    "japan":     {"name": "Japan",          "capital": "Tokyo",           "total": 1_105_200},
    "brazil":    {"name": "Brazil",         "capital": "Brasília",        "total":   612_400},
    "australia": {"name": "Australia",      "capital": "Canberra",        "total":   748_900},
    "canada":    {"name": "Canada",         "capital": "Ottawa",          "total":   819_600},
    "india":     {"name": "India",          "capital": "New Delhi",       "total":   990_100},
}

SALES_DATA = {
    "usa":       [("Q1","Widgets",4200,310_000),("Q2","Gadgets",3800,295_000),("Q3","Widgets",5100,381_500),("Q4","Services",3500,254_000)],
    "uk":        [("Q1","Gadgets",2900,218_000),("Q2","Widgets",2400,187_000),("Q3","Services",2800,210_000),("Q4","Gadgets",3500,261_300)],
    "germany":   [("Q1","Widgets",3100,234_000),("Q2","Services",2700,202_500),("Q3","Gadgets",3300,248_000),("Q4","Widgets",3350,250_250)],
    "japan":     [("Q1","Gadgets",4100,307_000),("Q2","Widgets",3700,277_500),("Q3","Services",3900,292_500),("Q4","Gadgets",3050,228_200)],
    "brazil":    [("Q1","Widgets",2100,157_500),("Q2","Gadgets",1900,142_500),("Q3","Widgets",2300,172_500),("Q4","Services",1870,139_900)],
    "australia": [("Q1","Services",2500,187_500),("Q2","Gadgets",2200,165_000),("Q3","Widgets",2600,195_000),("Q4","Services",2700,201_400)],
    "canada":    [("Q1","Widgets",2700,202_500),("Q2","Services",2400,180_000),("Q3","Gadgets",2900,217_500),("Q4","Widgets",2920,219_600)],
    "india":     [("Q1","Gadgets",3400,255_000),("Q2","Widgets",3200,240_000),("Q3","Services",3600,270_000),("Q4","Gadgets",3100,225_100)],
}

country_names = {k: v["name"] for k, v in COUNTRY_META.items()}
name_to_key = {v: k for k, v in country_names.items()}

st.divider()

# -------------------------------------------------------
# Section 1: Single Select (radio)
# -------------------------------------------------------
st.subheader("Countries, Capitals & Sales — Single Select")
st.markdown("Select a country to see its quarterly sales breakdown:")

# Summary table
summary_df = pd.DataFrame([
    {"Country": m["name"], "Capital": m["capital"], "Total Sales ($)": m["total"]}
    for m in COUNTRY_META.values()
])

selected_name = st.radio(
    "Country",
    options=list(country_names.values()),
    horizontal=True,
    label_visibility="collapsed",
)

st.dataframe(
    summary_df,
    width='stretch',
    hide_index=True,
    column_config={"Total Sales ($)": st.column_config.NumberColumn(format="$%d")},
)

# Detail breakdown for selected country
key = name_to_key[selected_name]
detail_rows = SALES_DATA[key]
detail_df = pd.DataFrame(detail_rows, columns=["Quarter", "Product", "Units Sold", "Revenue ($)"])

st.markdown(f"#### {selected_name} — Sales Breakdown")
st.dataframe(
    detail_df,
    width='stretch',
    hide_index=True,
    column_config={"Revenue ($)": st.column_config.NumberColumn(format="$%d")},
)

st.divider()

# -------------------------------------------------------
# Section 2: Multi Select (checkboxes)
# -------------------------------------------------------
st.subheader("Countries, Capitals & Sales — Multi Select")
st.markdown("Select multiple countries to compare their total sales:")

selected_names = st.multiselect(
    "Countries",
    options=list(country_names.values()),
    default=["United States", "Japan"],
    label_visibility="collapsed",
)

if selected_names:
    comparison_rows = [
        {
            "Country": COUNTRY_META[name_to_key[n]]["name"],
            "Capital": COUNTRY_META[name_to_key[n]]["capital"],
            "Total Sales ($)": COUNTRY_META[name_to_key[n]]["total"],
        }
        for n in selected_names
    ]
    comparison_df = pd.DataFrame(comparison_rows)

    st.dataframe(
        comparison_df,
        width='stretch',
        hide_index=True,
        column_config={"Total Sales ($)": st.column_config.NumberColumn(format="$%d")},
    )

    # Bar chart of total sales
    chart_df = comparison_df.set_index("Country")[["Total Sales ($)"]]
    st.bar_chart(chart_df)
else:
    st.info("Select at least one country above to see the comparison.")
