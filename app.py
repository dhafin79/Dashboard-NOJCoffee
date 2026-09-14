import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# KONFIGURASI HALAMAN

st.set_page_config(
    page_title="Dashboard Segmentasi Produk NOJ Coffee",
    page_icon="☕",
    layout="wide"
)


# MEMBACA DATA

df = pd.read_excel("data/processed/hasil_cluster.xlsx")

# JUDUL

st.title("☕ Dashboard Segmentasi Produk NOJ Coffee")

st.markdown("""
Dashboard ini menampilkan hasil segmentasi produk menggunakan
metode **RFM** dan **K-Means Clustering**.
""")

st.divider()

# SIDEBAR FILTER

st.sidebar.header("Filter")

# Opsi Filter

st.sidebar.header("Filter")

segments = ["Semua"] + sorted(df["Segment"].dropna().astype(str).unique())
clusters = ["Semua"] + sorted(df["Cluster"].dropna().astype(int).astype(str).unique())

segment = st.sidebar.selectbox("Segment", segments)
cluster = st.sidebar.selectbox("Cluster", clusters)
query = st.sidebar.text_input("Cari Nama Produk", placeholder="Masukkan nama produk...").strip()
top_n = st.sidebar.number_input("Top N Produk", 3, 50, 10)

# FILTER DATA

view = df.copy()

if segment != "Semua":
    view = view[view["Segment"].astype(str) == segment]

if cluster != "Semua":
    view = view[view["Cluster"].astype(int).astype(str) == cluster]

if query:
    view = view[view["item_name"].str.contains(query, case=False, na=False)]

# KPI

metrics = [
    ("Jumlah Produk", len(view)),
    ("Avg Recency", f"{view['Recency'].mean():.0f} Hari"),
    ("Avg Frequency", f"{view['Frequency'].mean():.0f}"),
    ("Avg Monetary", f"Rp {view['Monetary'].mean():,.0f}"),
    ("Total Monetary", f"Rp {view['Monetary'].sum():,.0f}")
]

cols = st.columns(5)

for col, (title, value) in zip(cols, metrics):
    col.metric(title, value)

# VISUALISASI

st.markdown("---")
st.subheader("Visualisasi Segmentasi Produk")

col1, col2 = st.columns(2)

with col1:

    st.markdown("### Heatmap Korelasi RFM")

    fig, ax = plt.subplots(figsize=(6,5))

    sns.heatmap(
        view[["Recency","Frequency","Monetary"]].corr(),
        annot=True,
        cmap="Blues",
        square=True,
        ax=ax
    )

    st.pyplot(fig)

with col2:

    st.markdown("### Jumlah Produk per Segmen")

    segment_count = (
        view["Segment"]
        .value_counts()
        .reset_index()
    )

    segment_count.columns = ["Segment","Jumlah"]

    fig, ax = plt.subplots(figsize=(6,5))

    sns.barplot(
        data=segment_count,
        x="Segment",
        y="Jumlah",
        ax=ax
    )

    ax.set_xlabel("")
    ax.set_ylabel("Jumlah Produk")

    plt.xticks(rotation=15)

    st.pyplot(fig)

col3, col4 = st.columns(2)

with col3:

    st.markdown(f"### Top {top_n} Produk Berdasarkan Monetary")

    top_money = (
        view
        .sort_values(
            "Monetary",
            ascending=False
        )
        .head(top_n)
    )

    fig, ax = plt.subplots(figsize=(7,5))

    sns.barplot(
        data=top_money,
        x="Monetary",
        y="item_name",
        ax=ax
    )

    st.pyplot(fig)

with col4:

    st.markdown(f"### Top {top_n} Produk Berdasarkan Frequency")

    top_freq = (
        view
        .sort_values(
            "Frequency",
            ascending=False
        )
        .head(top_n)
    )

    fig, ax = plt.subplots(figsize=(7,5))

    sns.barplot(
        data=top_freq,
        x="Frequency",
        y="item_name",
        ax=ax
    )

    st.pyplot(fig)


# TABEL HASIL SEGMENTASI

st.markdown("---")
st.subheader("Hasil Segmentasi Produk")

# Urutkan berdasarkan Monetary terbesar
table = view.sort_values(
    by="Monetary",
    ascending=False
)

st.dataframe(
    view.sort_values("Monetary", ascending=False)[
        ["item_name","Recency","Frequency","Monetary","Cluster","Segment"]
    ],
    use_container_width=True,
    hide_index=True
)


