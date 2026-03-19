How to Run the Project
1. Clone the Repository
git clone https://github.com/your-username/trader-behavior-analysis.git
cd trader-behavior-analysis
2. Install Required Libraries

Make sure Python (>= 3.8) is installed. Then install dependencies:

pip install pandas numpy matplotlib seaborn scikit-learn streamlit
3. Add Dataset Files

Download the datasets and place them in the project folder:

historical_data.csv (trades data)

fear_greed_index.csv (sentiment data)

Update file paths in code if needed.

4. Run Analysis Notebook (Optional)

If using Jupyter Notebook:

jupyter notebook

Open and run analysis.ipynb.

5. Run Streamlit Dashboard
streamlit run app.py
6. Open in Browser

If it doesn’t open automatically, go to:

http://localhost:8501
Requirements

Python 3.8+

pandas

numpy

matplotlib

seaborn

scikit-learn

streamlit

Output

Data analysis and insights in notebook

Interactive dashboard in Streamlit

Visualizations for trader performance vs sentiment
