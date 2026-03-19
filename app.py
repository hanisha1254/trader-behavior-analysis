import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# =========================
# PAGE CONFIG
# =========================
st.set_page_config(page_title="Trader Behavior Dashboard", layout="wide")
st.title("📊 Trader Performance vs Market Sentiment")

# =========================
# LOAD DATA (CACHED)
# =========================
@st.cache_data
def load_data():
    trades = pd.read_csv(r"C:\Users\Hanisha\Downloads\historical_data.csv")
    sentiment = pd.read_csv(r"C:\Users\Hanisha\Downloads\fear_greed_index.csv")
    return trades, sentiment

trades, sentiment = load_data()

# Clean columns
trades.columns = trades.columns.str.strip()
sentiment.columns = sentiment.columns.str.strip()

# =========================
# DATA PREVIEW
# =========================
st.subheader("📁 Trades Data")
st.dataframe(trades.head())

st.subheader("📁 Sentiment Data")
st.dataframe(sentiment.head())

# =========================
# DATA PREPARATION
# =========================

# Convert dates
trades['date'] = pd.to_datetime(
    trades['Timestamp IST'],
    dayfirst=True,
    errors='coerce'
).dt.date

sentiment['date'] = pd.to_datetime(
    sentiment['date'],
    dayfirst=True,
    errors='coerce'
).dt.date

# Drop invalid rows
trades = trades.dropna(subset=['date'])
sentiment = sentiment.dropna(subset=['date'])

# Rename for clarity
trades.rename(columns={
    'Account': 'account_id',
    'Closed PnL': 'pnl',
    'Size USD': 'trade_size',
    'Side': 'side'
}, inplace=True)

sentiment.rename(columns={'classification': 'sentiment'}, inplace=True)

# Merge
merged = trades.merge(
    sentiment[['date', 'sentiment']],
    on='date',
    how='left'
)

# =========================
# FEATURE ENGINEERING
# =========================

# Win rate
merged['win'] = (merged['pnl'] > 0).astype(int)

# Daily PnL per trader
daily_pnl = merged.groupby(['account_id', 'date'])['pnl'].sum().reset_index()

# =========================
# SECTION: PnL DISTRIBUTION
# =========================
st.subheader("📊 PnL Distribution")

fig, ax = plt.subplots()
ax.hist(merged['pnl'].dropna(), bins=50)
ax.set_xlabel("PnL")
ax.set_ylabel("Frequency")
st.pyplot(fig)

# =========================
# SECTION: PERFORMANCE ANALYSIS
# =========================
st.subheader("📈 Performance vs Sentiment")

pnl_sentiment = merged.groupby('sentiment')['pnl'].mean()
st.bar_chart(pnl_sentiment)

win_rate = merged.groupby('sentiment')['win'].mean()
st.bar_chart(win_rate)

# =========================
# SECTION: BEHAVIOR ANALYSIS
# =========================
st.subheader("📊 Trader Behavior vs Sentiment")

# Trade frequency
freq = merged.groupby('sentiment').size()
st.bar_chart(freq)

# Trade size
size = merged.groupby('sentiment')['trade_size'].mean()
st.bar_chart(size)

# Buy vs Sell
bias = merged.groupby(['sentiment', 'side']).size().unstack(fill_value=0)
st.bar_chart(bias)

# =========================
# SECTION: SEGMENTATION
# =========================
st.subheader("📌 Trader Segmentation")

# Frequent vs Infrequent
trade_counts = merged['account_id'].value_counts()
threshold = trade_counts.median()

merged['segment'] = merged['account_id'].map(
    lambda x: 'Frequent' if trade_counts[x] > threshold else 'Infrequent'
)

segment_perf = merged.groupby('segment')['pnl'].mean()
st.bar_chart(segment_perf)

# =========================
# FINAL INSIGHTS
# =========================
st.subheader("🧠 Key Insights")

st.write("""
✔ Traders tend to perform better during Greed periods with higher average PnL and win rates.

✔ During Fear and Extreme Fear, performance becomes volatile and risk increases.

✔ Traders increase trade size and activity during Greed, indicating risk-on behavior.

✔ Frequent traders show inconsistent performance compared to controlled traders.
""")