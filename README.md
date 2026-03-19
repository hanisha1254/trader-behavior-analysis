# trader-behavior-analysis
Methodology
We analyzed trader behavior on Hyperliquid by combining historical trading data with Bitcoin market sentiment (Fear/Greed index). The data was cleaned, timestamps were aligned at a daily level, and key metrics such as daily PnL, win rate, trade size, and trading frequency were computed. The datasets were merged on date to study how sentiment impacts trader performance and behavior.

Key Insights
•	Traders perform better during Greed periods, with higher average PnL and win rates.
•	During Fear periods, trading becomes more volatile with inconsistent outcomes and higher risk.
•	Traders increase position sizes and trade frequency during Greed, indicating risk-on behavior.

Segmentation Findings
•	Frequent traders tend to overtrade and show inconsistent performance.
•	Consistent traders maintain stable PnL with controlled risk.
•	High-risk traders (large trade sizes) show higher variance in outcomes.

Strategy Recommendations
•	During Fear and Extreme Fear periods, traders should reduce leverage and position sizes to manage downside risk.
•	During Greed periods, consistent traders can increase position sizes to capitalize on market momentum, while others should maintain disciplined risk management.

Bonus Work
A Random Forest model was built to predict trader profitability using sentiment and behavioral features. Additionally, traders were clustered into behavioral archetypes using K-Means clustering.

