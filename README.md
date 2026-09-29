# CodeAlpha_DataVisualization

## Task
This is Task 3 (Data Visualization) of my CodeAlpha Data Analytics internship. The goal was to take a sales dataset and create clear, easy-to-read visualizations that show trends, comparisons and relationships in the data.

## What I did
Since I didn't have a real company dataset handy, I generated a sample e-commerce style sales dataset (`sales_data.csv`) covering a full year (2024) with daily transactions across 5 categories and 4 regions, including units sold, sales value and profit. I then wrote a Python script (`visualize_sales.py`) that reads this data and builds a set of charts using matplotlib and seaborn.

## Files in this repo
- `sales_data.csv` – the sales dataset (Date, Category, Region, Units, Sales, Profit)
- `generate_data.py` – script I used once to create the sample dataset
- `visualize_sales.py` – main script that loads the data and builds all the charts
- `requirements.txt` – Python packages needed to run the script
- `chart1_monthly_sales_trend.png` – line chart of total sales by month
- `chart2_sales_by_category.png` – bar chart comparing total sales across categories
- `chart3_sales_share_by_region.png` – pie chart of sales share by region
- `chart4_profit_vs_sales.png` – scatter plot of profit vs sales, colored by category
- `chart5_category_region_heatmap.png` – heatmap of sales across category and region
- `dashboard_sales_overview.png` – a single dashboard image combining all the charts plus key numbers (total sales, total profit, top category, top region, avg order value)

## How to run it
```bash
pip install -r requirements.txt
python visualize_sales.py
```
This will regenerate all the chart PNGs in the same folder.

## What I noticed in the data
- Sales pick up noticeably in November and December (added a seasonal bump for the holiday period).
- Electronics brings in the most total sales but Books has the smallest average order value, which makes sense given typical price points.
- Sales are fairly evenly spread across the four regions, with no single region dominating.

## Tools used
Python, pandas, matplotlib, seaborn
