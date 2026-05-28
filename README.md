# 📊 Business Sales Performance Analytics
### Future Interns — Data Science & Analytics | Task 1

![Python](https://img.shields.io/badge/Python-3.8+-blue?logo=python)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-150458?logo=pandas)
![Matplotlib](https://img.shields.io/badge/Matplotlib-Visualization-orange)
![Seaborn](https://img.shields.io/badge/Seaborn-Statistical%20Plots-4c72b0)
![ReportLab](https://img.shields.io/badge/ReportLab-PDF%20Report-red)
![Status](https://img.shields.io/badge/Status-Completed✅-2dc653)

---

## 📌 Objective

Analyze business sales data from the Sample Superstore dataset to identify:
- Revenue trends across categories and regions
- Top-selling products and sub-categories
- High-value customer segments
- Impact of discounts on profitability
- Actionable recommendations for business growth

---

## 📁 Repository Structure

```
FUTURE_DS_01/
├── FUTURE_DS_01_FullCode.py     # Complete Python analysis script
├── FUTURE_DS_01_Report.pdf      # Client-ready analysis report with charts
├── SampleSuperstore.csv         # Dataset used for analysis
└── README.md                    # Project documentation
```

---

## 📦 Dataset

| Property | Details |
|----------|---------|
| Name | Sample Superstore |
| Rows | 9,994 |
| Columns | 13 |
| Source | Kaggle / Tableau Sample Data |
| Features | Ship Mode, Segment, Region, Category, Sub-Category, Sales, Quantity, Discount, Profit |

---

## 🛠️ Tools & Libraries

| Tool | Purpose |
|------|---------|
| Python 3.8+ | Core programming language |
| Pandas | Data loading, cleaning, aggregation |
| Matplotlib | Charts and visualizations |
| Seaborn | Statistical plots and heatmaps |
| ReportLab | PDF report generation |

---

## ⚙️ How to Run

**1. Clone the repository**
```bash
git clone https://github.com/<your-username>/FUTURE_DS_01.git
cd FUTURE_DS_01
```

**2. Install dependencies**
```bash
pip install pandas matplotlib seaborn reportlab
```

**3. Run the analysis**
```bash
python FUTURE_DS_01_FullCode.py
```

**4. Outputs generated**
- 6 chart PNG files
- `FUTURE_DS_01_Report.pdf` — complete analysis report

---

## 📊 Analysis Sections

| # | Section | Description |
|---|---------|-------------|
| 1 | Data Loading & Cleaning | Load CSV, remove duplicates, feature engineering |
| 2 | KPI Dashboard | Revenue, Profit, Orders, Avg Discount, Margin |
| 3 | Category Analysis | Sales & Profit by Category and Top 10 Sub-Categories |
| 4 | Regional Performance | Sales, Profit & Margin across 4 regions |
| 5 | Discount vs Profit | Correlation analysis + Sub-category profit/loss |
| 6 | Segment Analysis | Consumer, Corporate, Home Office breakdown |
| 7 | Ship Mode & Heatmap | Ship mode performance + Region × Category heatmap |
| 8 | Key Insights | Printed summary with top findings |
| 9 | PDF Report | Auto-generated client-ready PDF report |

---

## 📈 Key Findings

| Metric | Value |
|--------|-------|
| Total Revenue | $2.29M |
| Total Profit | $286K |
| Overall Profit Margin | 12.5% |
| Top Category | Technology |
| Top Region | West |
| Discount–Profit Correlation | −0.31 |

### 🔑 Business Insights

- **Technology** is the highest revenue and profit-generating category
- **West region** leads in both sales and profit
- Heavy discounting in **Furniture** is the primary profit killer
- Sub-categories **Tables, Bookcases, and Supplies** operate at a loss
- **Consumer segment** drives the most revenue; **Corporate** delivers better margins
- Orders with discounts **above 40%** almost always result in losses

### ✅ Recommendations

1. Cap discounts at **20%** across all categories
2. Conduct a pricing audit on loss-making sub-categories (Tables, Bookcases, Supplies)
3. Invest marketing budget in **West & East** regions for highest ROI
4. Upsell **Technology** products to **Corporate** clients
5. Apply stricter discount controls in the **Central region**

---

## 📷 Visualizations Generated

| Chart | Description |
|-------|-------------|
| `kpi.png` | 5-card KPI dashboard |
| `category_chart.png` | Category & Sub-Category bar charts |
| `regional_chart.png` | Regional Sales, Profit & Margin breakdown |
| `discount_profit.png` | Discount vs Profit scatter + Sub-cat profit bars |
| `segment_states.png` | Segment pie charts + Top 10 States |
| `shipmode_heatmap.png` | Ship Mode bars + Region × Category heatmap |

---

## 🏢 About This Internship

This project was completed as part of the **Future Interns Data Science & Analytics** program.

- 🌐 Website: [futureinterns.com](https://futureinterns.com)
- 💼 LinkedIn: [Future Interns](https://www.linkedin.com/company/future-interns/)
- 📧 Contact: contact@futureinterns.com

---

## 👤 Author

**[Your Name]**
- GitHub: [@your-username](https://github.com/your-username)
- LinkedIn: [your-linkedin](https://linkedin.com/in/your-linkedin)

---

*Completed as Task 1 of the Future Interns Data Science & Analytics Internship*
*Track Code: **FUTURE_DS_01***
