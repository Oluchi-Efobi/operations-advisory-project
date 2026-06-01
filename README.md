#  Water Filter Business Toolkit

**Automate, Optimize, and Scale Your Water Filter Business**

*From **5,000 to 10,000+ orders** | **10% to 40% market share** | **₦20M+ revenue in 6 months***

---

##  **About**
- ** Marketing Success**: Scaled orders from **5,000 to 10,000+** and grew market share from **10% to 40%** across Nigeria’s 36 states.
- ** Production Efficiency**: Improved **F.O.B water filter factory efficiency by 25%** through **Lean Manufacturing** and process mapping.
- ** Portfolio Growth**: Managed a **₦200M portfolio** of home and commercial products, driving **₦20M+ revenue in 6 months** via inventory management and supplier negotiations.
- ** Strategic Advisory**: Transitioned to an **advisory role** (July 2024) to guide long-term growth.

This repository provides **ready-to-use Python scripts** to **replicate, automate, and scale** these strategies.

---

##  **Why This Toolkit?**

### **For Business Owners**

✅ Replicate **proven strategies** to scale your business.  
✅ Automate **marketing, production, and portfolio management**.  
✅ Make **data-driven decisions** to maximize profitability.

### **For Operations Teams**

✅ Optimize **campaigns** with real-time insights.  
✅ Identify **waste in production** and improve efficiency.  
✅ Track **inventory and suppliers** to avoid stockouts.

### **For Advisors & Investors**

✅ Assess **business health** with profitability metrics.  
✅ Identify **growth opportunities** for expansion or innovation.  
✅ Generate **reports** with actionable insights.

---

##  **Features**


| **Module**                 | **Description**                                                                         | **Key Functions**                                               |
| -------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------- |
| **Marketing Optimizer**    | Analyzes and optimizes digital/physical marketing campaigns across Nigeria’s 36 states. | `analyze_campaign_performance()`, `recommend_strategies()`      |
| **Production Efficiency**  | Identifies waste and suggests Lean Manufacturing improvements for factory processes.    | `map_processes()`, `identify_waste()`                           |
| **Portfolio Manager**      | Tracks inventory, manages suppliers, and calculates portfolio value.                    | `track_inventory()`, `negotiate_supplier_contracts()`           |
| **Profitability Analyzer** | Calculates profitability and forecasts revenue growth.                                  | `calculate_profitability()`, `forecast_revenue()`               |
| **Advisory Insights**      | Generates strategic reports and identifies growth opportunities.                        | `generate_advisory_report()`, `identify_growth_opportunities()` |


---

##  **Repository Structure**

```
water-filter-business-toolkit/
│   ├── water_filter_toolkit.py     # Main script (all modules combined)
│   ├── marketing_optimizer.py       # Marketing analysis
│   ├── production_efficiency.py    # Production optimization
│   ├── portfolio_manager.py         # Portfolio management
│   ├── profitability_analyzer.py    # Profitability analysis
│   └── advisory_insights.py         # Advisory reports
├── README.md                        # This file
├── requirements.txt                 # Python dependencies
└── LICENSE                          # MIT License
```

---

##  **Installation**

### **Prerequisites**

- Python 3.8+
- Libraries: `pandas`, `numpy`, `scikit-learn`

### **Setup**

1. Clone the repository:
  ```bash
   git clone https://github.com/Oluchi-Efobi/operations-advisory-project.git
   cd operations-advisory-project
  ```
2. Install dependencies:
  ```bash
   pip install -r requirements.txt
  ```
3. Run the toolkit:
  ```bash
   python water_filter_toolkit.py
  ```

---

##  **Quick Start**

### **Run the Full Toolkit (Demo Mode)**

The main script (`water_filter_toolkit.py`) includes a **demo mode** that creates sample data and lets you test all modules:

```bash
python water_filter_toolkit.py
```

**Example Output:**

```
🚀 Water Filter Business Toolkit

Select a module to run:
1. 📈 Marketing Optimizer
2. 🏭 Production Efficiency
3. 💰 Portfolio Manager
4. 📊 Profitability Analyzer
5. 🧠 Advisory Insights
6. 🏃 Run All Modules (Demo)

Enter your choice (1-6): 6
```

### **Use Individual Modules**

Each module can be imported and used independently. Here are examples:

#### **1. Marketing Optimizer**

```python
from scripts.marketing_optimizer import MarketingOptimizer

optimizer = MarketingOptimizer("data/marketing_data.csv")
performance = optimizer.analyze_campaign_performance(
    campaign_type="Digital",
    state="Lagos"
)
print(performance)
# Output: {"total_orders": 5000, "avg_market_share": 10, ...}
```

#### **2. Production Efficiency**

```python
from scripts.production_efficiency import ProductionEfficiency

efficiency = ProductionEfficiency("data/production_data.csv")
waste_areas = efficiency.identify_waste(threshold=5)
print(waste_areas)
# Output: [{"process_name": "Assembly", "waste_percentage": 8}, ...]
```

#### **3. Portfolio Manager**

```python
from scripts.portfolio_manager import PortfolioManager

manager = PortfolioManager("data/portfolio_data.csv")
inventory = manager.track_inventory("Home Water Filter", threshold=1000)
print(inventory)
# Output: {"current_inventory": 5000, "below_threshold": False, ...}
```

#### **4. Profitability Analyzer**

```python
from scripts.profitability_analyzer import ProfitabilityAnalyzer

analyzer = ProfitabilityAnalyzer("data/revenue_data.csv")
profitability = analyzer.calculate_profitability(revenue=20000000, costs=15000000)
print(profitability)
# Output: {"profitability_percentage": "33.33%"}
```

#### **5. Advisory Insights**

```python
from scripts.advisory_insights import AdvisoryInsights

advisory = AdvisoryInsights()
report = advisory.generate_advisory_report(
    current_revenue=20000000,
    target_revenue=50000000,
    growth_areas=["Marketing Expansion", "Production Optimization"]
)
print(report)
# Output: Markdown report with recommendations
```

---

##  **Example Data**

The toolkit **automatically generates sample data** if input files don’t exist. Here’s what the sample data looks like:

### `**data/marketing_data.csv**`


| campaign_id | campaign_type | state | orders | market_share | start_date | end_date   |
| ----------- | ------------- | ----- | ------ | ------------ | ---------- | ---------- |
| 001         | Digital       | Lagos | 5000   | 10           | 2024-01-01 | 2024-01-31 |
| 002         | Physical      | Kano  | 3000   | 15           | 2024-02-01 | 2024-02-28 |


### `**data/production_data.csv**`


| process_id | process_name  | duration_minutes | waste_percentage |
| ---------- | ------------- | ---------------- | ---------------- |
| 001        | Assembly      | 30               | 8                |
| 002        | Quality Check | 15               | 2                |


### `**data/portfolio_data.csv**`


| product_id | product_name            | category    | inventory | unit_cost | supplier     |
| ---------- | ----------------------- | ----------- | --------- | --------- | ------------ |
| 001        | Home Water Filter       | Residential | 5000      | 5000      | ABC Supplies |
| 002        | Commercial Water Filter | Commercial  | 2000      | 20000     | XYZ Supplies |


---

##  **Customization**

### **1. Replace Sample Data**

Replace the **sample CSV files** in the `data/` directory with your **real business data** for accurate insights.

### **2. Extend Functionality**

- **Integrate APIs**: Connect to CRM/ERP systems (e.g., Salesforce, SAP) for live data.
- **Add Machine Learning**: Use `scikit-learn` to predict demand or optimize marketing spend.
- **Automate Reports**: Use `smtplib` to email reports to stakeholders.

### **3. Add a Dashboard (Optional)**

Use **Streamlit** to create a live dashboard for visualizing:

- Marketing performance by state.
- Production efficiency trends.
- Revenue vs. costs over time.

**Example Dashboard Code (`dashboard.py`):**

```python
# Install Streamlit: pip install streamlit
import streamlit as st
import pandas as pd

st.title("💧 Water Filter Business Dashboard")
marketing_df = pd.read_csv("data/marketing_data.csv")
st.bar_chart(marketing_df, x="state", y="orders", color="campaign_type")
```

Run the dashboard:

```bash
streamlit run dashboard.py
```

### **4. Scale for Your Business**

- Add more states to `marketing_data.csv`.
- Track new KPIs (e.g., customer acquisition cost, lifetime value).
- Extend the `PortfolioManager` for additional product lines.

---

## **License**

This project is licensed under the **MIT License** – see the [LICENSE](LICENSE) file for details.
