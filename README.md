# 🛒 E-Commerce Sales Analytics

An end-to-end E-Commerce Sales Analytics project focused on analyzing sales performance, customer behavior, product performance, and regional business insights using Python, SQL, SQLite, and Microsoft Power BI.

The project transforms raw e-commerce data into meaningful business insights through data cleaning, exploratory data analysis, SQL-based data management, and an interactive Power BI dashboard.

## 📌 Project Overview

The E-Commerce Sales Analytics project helps understand business performance by analyzing important sales metrics such as revenue, profit, order volume, average order value, product categories, customer segments, and regional performance.

The project includes data preprocessing, database creation, SQL queries, analytical notebooks, and an interactive executive dashboard built using Power BI.

## 🎯 Project Objectives

- Analyze overall e-commerce sales performance.
- Identify profitable products and product categories.
- Understand customer purchasing behavior.
- Compare sales performance across different regions.
- Analyze order status and payment methods.
- Calculate important business KPIs.
- Present insights through an interactive Power BI dashboard.

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Data processing and analysis |
| Pandas | Data cleaning and manipulation |
| Jupyter Notebook | Exploratory Data Analysis |
| SQL | Database schema and queries |
| SQLite | Database management |
| Microsoft Power BI | Interactive dashboard and visualization |
| Git & GitHub | Version control and project management |

## 📊 Power BI Executive Dashboard

The project includes an interactive Executive Overview dashboard created using Microsoft Power BI.

### Dashboard Features

**1. Key Performance Indicators (KPIs)**

- Total Revenue
- Total Profit
- Total Orders
- Average Order Value (AOV)

**2. Sales Analysis**

- Monthly Revenue Trend
- Revenue by Product Category
- Regional Revenue vs Profit Comparison

**3. Business Performance Analysis**

- Orders by Order Status
- Revenue by Payment Method

**4. Interactive Filters (Slicers)**

- Order Date
- Region
- Product Category
- Payment Method

The dashboard allows users to filter data dynamically and explore business performance from different perspectives.

## 📈 Key Business Metrics

The following metrics were verified in the Power BI semantic model:

| KPI | Description |
|---|---|
| Total Revenue | Total sales revenue generated |
| Total Profit | Total profit generated |
| Total Orders | Number of distinct orders |
| Average Order Value | Total Revenue divided by Total Orders |

### DAX Measures

```dax
Total Revenue =
SUM(cleaned_order_items[LineTotal])

Total Profit =
SUM(cleaned_order_items[LineProfit])

Total Orders =
DISTINCTCOUNT(cleaned_orders[OrderID])

Average Order Value =
DIVIDE([Total Revenue], [Total Orders], 0)
```

Currency formatting is configured in Indian Rupees (₹).

## 📁 Project Structure

```text
E-Commerce-Sales-Analytics/
│
├── E-Commerce-Sales-Analytics-Executive.pbip
│
├── E-Commerce-Sales-Analytics-Executive.Report/
│
├── E-Commerce-Sales-Analytics-Executive.SemanticModel/
│
├── notebooks/
│   └── Exploratory Data Analysis notebooks
│
├── sql/
│   └── SQL schema and query files
│
├── generate_pbir_dashboard.py
│
├── verify_pbir.py
│
├── load_database.p
│
├── E-Commerce_Sales_Analytics_Implementation_Plan.docx
│
├── .gitignore
│
└── README.md
```

## ⚙️ Project Setup

### 1. Clone the Repository

```bash
git clone https://github.com/Sridharpeddamanishi9710/E-Commerce-Sales-Analytics.git
```

### 2. Navigate to the Project Folder

```bash
cd E-Commerce-Sales-Analytics
```

### 3. Create a Python Virtual Environment

```bash
python -m venv .venv
```

Activate the environment on Windows:

```bash
.venv\Scripts\activate
```

### 4. Install Required Libraries

```bash
pip install pandas numpy matplotlib seaborn jupyter
```

### 5. Prepare the Dataset

Place the required cleaned CSV files inside the local `data/` directory:

- cleaned_regions.csv
- cleaned_customers.csv
- cleaned_products.csv
- cleaned_orders.csv
- cleaned_order_items.csv

**Note:** Dataset files and the SQLite database are excluded from this public repository. You must provide the required CSV files locally before running the database loading script.

### 6. Create and Load the SQLite Database

Run:

```bash
python load_database.p
```

This script reads the SQL schema and loads the cleaned CSV datasets into SQLite tables.

### 7. Run Jupyter Notebook

```bash
jupyter notebook
```

Open the notebooks directory and execute the analysis notebooks.

### 8. Open the Power BI Dashboard

1. Install Microsoft Power BI Desktop.
2. Open `E-Commerce-Sales-Analytics-Executive.pbip`.
3. Wait for the report and semantic model to load.
4. Explore the Executive Overview dashboard using the available slicers and charts.

## 🔍 Expected Business Insights

The dashboard and analysis support investigation of:

- Overall revenue and profitability.
- Best-performing product categories.
- Regional sales performance.
- Customer purchasing patterns.
- Order status distribution.
- Preferred payment methods.
- Monthly sales trends.

## 🚀 Future Enhancements

- Advanced customer segmentation and RFM analysis.
- Sales forecasting using machine learning.
- Customer lifetime value analysis.
- Product recommendation system.
- Automated business performance reports.
- Real-time sales analytics.

## 👨‍💻 Author

**Sridhar Pedhamanishi**

GitHub: [@Sridharpeddamanishi9710](https://github.com/Sridharpeddamanishi9710)

## 📄 License

This project is available for educational and portfolio purposes. A formal open-source license has not yet been added.

---

⭐ If you find this project useful, consider giving the repository a star!