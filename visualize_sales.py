"""
visualize_sales.py

CodeAlpha Internship - Data Analytics Track
Task 3: Data Visualization

Reads sales_data.csv and produces 5 individual charts plus a combined
dashboard image, saved in the same folder.

Run with:
    python visualize_sales.py
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_style("whitegrid")
plt.rcParams["figure.dpi"] = 120

# ---------------------------------------------------------
# 1. Load and prep the data
# ---------------------------------------------------------
df = pd.read_csv("sales_data.csv", parse_dates=["Date"])
df["Month"] = df["Date"].dt.to_period("M").astype(str)

print("Loaded", len(df), "rows")
print(df.head())
print(df.describe())

# ---------------------------------------------------------
# Chart 1: Monthly sales trend
# ---------------------------------------------------------
monthly_sales = df.groupby("Month")["Sales"].sum().reset_index()

plt.figure(figsize=(10, 5))
plt.plot(monthly_sales["Month"], monthly_sales["Sales"], marker="o", color="#2E86AB", linewidth=2)
plt.title("Monthly Sales Trend (2024)")
plt.xlabel("Month")
plt.ylabel("Total Sales ($)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("chart1_monthly_sales_trend.png")
plt.close()

# ---------------------------------------------------------
# Chart 2: Sales by category
# ---------------------------------------------------------
category_sales = df.groupby("Category")["Sales"].sum().sort_values(ascending=False)

plt.figure(figsize=(8, 5))
sns.barplot(x=category_sales.values, y=category_sales.index, palette="viridis")
plt.title("Total Sales by Category")
plt.xlabel("Total Sales ($)")
plt.ylabel("Category")
plt.tight_layout()
plt.savefig("chart2_sales_by_category.png")
plt.close()

# ---------------------------------------------------------
# Chart 3: Sales share by region (pie chart)
# ---------------------------------------------------------
region_sales = df.groupby("Region")["Sales"].sum()

plt.figure(figsize=(7, 7))
plt.pie(
    region_sales.values,
    labels=region_sales.index,
    autopct="%1.1f%%",
    startangle=90,
    colors=sns.color_palette("pastel"),
)
plt.title("Sales Share by Region")
plt.tight_layout()
plt.savefig("chart3_sales_share_by_region.png")
plt.close()

# ---------------------------------------------------------
# Chart 4: Profit vs Sales (scatter)
# ---------------------------------------------------------
plt.figure(figsize=(8, 6))
sns.scatterplot(data=df, x="Sales", y="Profit", hue="Category", alpha=0.6, s=40)
plt.title("Profit vs Sales")
plt.xlabel("Sales ($)")
plt.ylabel("Profit ($)")
plt.legend(bbox_to_anchor=(1.02, 1), loc="upper left")
plt.tight_layout()
plt.savefig("chart4_profit_vs_sales.png")
plt.close()

# ---------------------------------------------------------
# Chart 5: Category x Region heatmap
# ---------------------------------------------------------
pivot = df.pivot_table(index="Category", columns="Region", values="Sales", aggfunc="sum")

plt.figure(figsize=(8, 6))
sns.heatmap(pivot, annot=True, fmt=".0f", cmap="YlOrRd", cbar_kws={"label": "Sales ($)"})
plt.title("Sales by Category and Region")
plt.tight_layout()
plt.savefig("chart5_category_region_heatmap.png")
plt.close()

# ---------------------------------------------------------
# Dashboard: combine everything into one overview image
# ---------------------------------------------------------
fig, axes = plt.subplots(2, 3, figsize=(18, 10))
fig.suptitle("Sales Overview Dashboard - 2024", fontsize=16, fontweight="bold")

# monthly trend
axes[0, 0].plot(monthly_sales["Month"], monthly_sales["Sales"], marker="o", color="#2E86AB")
axes[0, 0].set_title("Monthly Sales Trend")
axes[0, 0].tick_params(axis="x", rotation=45)

# category bar
sns.barplot(x=category_sales.values, y=category_sales.index, palette="viridis", ax=axes[0, 1])
axes[0, 1].set_title("Sales by Category")

# region pie
axes[0, 2].pie(region_sales.values, labels=region_sales.index, autopct="%1.1f%%", startangle=90,
               colors=sns.color_palette("pastel"))
axes[0, 2].set_title("Sales Share by Region")

# profit vs sales
sns.scatterplot(data=df, x="Sales", y="Profit", hue="Category", alpha=0.6, s=30, ax=axes[1, 0], legend=False)
axes[1, 0].set_title("Profit vs Sales")

# heatmap
sns.heatmap(pivot, annot=True, fmt=".0f", cmap="YlOrRd", ax=axes[1, 1], cbar=False)
axes[1, 1].set_title("Category x Region Sales")

# quick summary stats panel
axes[1, 2].axis("off")
total_sales = df["Sales"].sum()
total_profit = df["Profit"].sum()
top_category = category_sales.index[0]
top_region = region_sales.idxmax()
summary_text = (
    f"Total Sales: ${total_sales:,.0f}\n\n"
    f"Total Profit: ${total_profit:,.0f}\n\n"
    f"Top Category: {top_category}\n\n"
    f"Top Region: {top_region}\n\n"
    f"Avg Order Value: ${df['Sales'].mean():.2f}"
)
axes[1, 2].text(0.1, 0.5, summary_text, fontsize=13, va="center")
axes[1, 2].set_title("Key Numbers")

plt.tight_layout(rect=[0, 0, 1, 0.96])
plt.savefig("dashboard_sales_overview.png")
plt.close()

print("\nAll charts saved successfully.")
