from pathlib import Path
import pandas as pd
import plotly.express as px
import streamlit as st

st.set_page_config(page_title="COVID-19 Data Analysis", page_icon="🦠", layout="wide")
DATA_FILE = Path(__file__).parent / "country_wise_latest.csv"

@st.cache_data
def load_data():
    df = pd.read_csv(DATA_FILE)
    df.columns = df.columns.str.strip()
    return df

st.title("COVID-19 Data Analysis and Visualization")
st.caption("Explore the supplied country-wise COVID-19 dataset. This is a historical dataset, not live data.")
try:
    df = load_data()
except Exception as exc:
    st.error(f"Could not load dataset: {exc}")
    st.stop()

with st.sidebar:
    st.header("Filters")
    regions = sorted(df["WHO Region"].dropna().unique())
    selected_regions = st.multiselect("WHO Region", regions, default=regions)
    countries = sorted(df.loc[df["WHO Region"].isin(selected_regions), "Country/Region"].dropna().unique())
    selected_countries = st.multiselect("Country", countries, default=countries)

filtered = df[df["WHO Region"].isin(selected_regions) & df["Country/Region"].isin(selected_countries)]
if filtered.empty:
    st.warning("No records match the selected filters.")
    st.stop()

metrics = [
    ("Confirmed Cases", "Confirmed"),
    ("Deaths", "Deaths"),
    ("Recovered", "Recovered"),
    ("Active Cases", "Active"),
]
cols = st.columns(4)
for col, (label, field) in zip(cols, metrics):
    col.metric(label, f"{int(filtered[field].sum()):,}")

left, right = st.columns(2)
with left:
    st.subheader("Top 10 Countries by Confirmed Cases")
    top = filtered.nlargest(10, "Confirmed").sort_values("Confirmed")
    st.plotly_chart(px.bar(top, x="Confirmed", y="Country/Region", orientation="h", color="Confirmed", title="Confirmed cases"), use_container_width=True)
with right:
    st.subheader("Confirmed Cases by WHO Region")
    region_data = filtered.groupby("WHO Region", as_index=False)["Confirmed"].sum().sort_values("Confirmed", ascending=False)
    st.plotly_chart(px.bar(region_data, x="WHO Region", y="Confirmed", color="WHO Region"), use_container_width=True)

left, right = st.columns(2)
with left:
    st.subheader("Confirmed Cases vs Deaths")
    st.plotly_chart(px.scatter(filtered, x="Confirmed", y="Deaths", color="WHO Region", hover_name="Country/Region", size="Recovered", size_max=28), use_container_width=True)
with right:
    st.subheader("Recovery Rate vs Death Rate")
    st.plotly_chart(px.scatter(filtered, x="Recovered / 100 Cases", y="Deaths / 100 Cases", color="WHO Region", hover_name="Country/Region"), use_container_width=True)

st.subheader("Filtered Dataset")
st.dataframe(filtered, use_container_width=True)
st.download_button("Download filtered data (CSV)", filtered.to_csv(index=False).encode("utf-8"), "covid19_filtered_data.csv", "text/csv")
