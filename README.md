# COVID-19 Data Analysis and Visualization

A Python data analysis project using the supplied country-wise COVID-19 dataset. It includes a Jupyter Notebook for exploratory data analysis and a Streamlit dashboard for interactive visualization.

## Project files

```text
COVID-19-Data-Analysis-and-Visualization/
├── COVID_19_Data_Analysis_and_Visualization.ipynb
├── country_wise_latest.csv
├── app.py
├── requirements.txt
└── README.md
```

## Technologies
- Python
- Pandas and NumPy
- Matplotlib and Seaborn
- Plotly and Streamlit
- Jupyter Notebook

## Run the notebook
Install the packages and open the notebook in Jupyter:

```bash
pip install -r requirements.txt
jupyter notebook
```

Open `COVID_19_Data_Analysis_and_Visualization.ipynb` and run the cells.

## Run the dashboard
From this project folder, run:

```bash
streamlit run app.py
```

The dashboard includes region and country filters, summary metrics, country and region charts, a confirmed-cases-versus-deaths chart, and a filtered-data download.

## Dataset note
The included CSV is a country-wise snapshot supplied for this project. The dashboard does not display live COVID-19 statistics.
