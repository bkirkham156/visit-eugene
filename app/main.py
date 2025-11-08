import streamlit as st
import pandas as pd
import sqlite3
import plotly.express as px
from pathlib import Path

# Path to your database
DB = Path(__file__).resolve().parents[1] / "data" / "eugene.db"

st.set_page_config(page_title="Visit Eugene Recommender", layout="wide")
st.title("Visit Eugene: Personalized Guide")

# --- DATABASE SETUP ---
@st.cache_resource
def get_conn():
    return sqlite3.connect(DB.as_posix(), check_same_thread=False)

@st.cache_data
def load_places():
    return pd.read_sql_query("SELECT * FROM places", get_conn())

# --- FILTER LOGIC ---
def filter_places(df, interests, budget, vibes):
    if budget:
        df = df[df["price_level"].isin(budget)]
    if vibes:
        df = df[df["vibe"].isin(vibes)]
    if interests:
        interests_lower = [i.lower() for i in interests]
        mask = df.apply(
            lambda r: any(
                i in (r["tags"] or "").lower() or i in (r["category"] or "").lower()
                for i in interests_lower
            ),
            axis=1,
        )
        df = df[mask]
    return df

# --- SIDEBAR ---
st.sidebar.header("Choose your preferences:")
interests = st.sidebar.multiselect(
    "Interests",
    ["Food", "Coffee", "Nature", "Bars", "Live Music", "Shopping", "Museums", "Market", "Hike"],
)
budget = st.sidebar.multiselect("Budget", ["$", "$$", "$$$"])
vibes = st.sidebar.multiselect("Vibe", ["chill", "lively", "scenic", "artsy", "social", "date-night"])

# --- MAIN PAGE ---
places = load_places()
filtered = filter_places(places.copy(), interests, budget, vibes)

st.sidebar.metric("Matches", len(filtered))

if not filtered.empty:
    cat_counts = filtered["category"].value_counts().reset_index()
    cat_counts.columns = ["category", "count"]
    st.plotly_chart(
        px.bar(cat_counts, x="category", y="count", title="Results by Category"),
        use_container_width=True,
    )

st.subheader("Recommendations")
if filtered.empty:
    st.info("No matches — try broadening your interests or budget.")
else:
    for _, r in filtered.sort_values(["rating"], ascending=False).iterrows():
        with st.container(border=True):
            st.markdown(f"### {r['name']}")
            st.caption(f"{r['category'].title()} · {r['price_level']} · ⭐ {r['rating']} · {r['vibe']}")
            st.write(r["description"])
            st.link_button(
                "Open in Maps",
                f"https://www.google.com/maps/search/{r['name'].replace(' ', '+')}+Eugene",
            )
