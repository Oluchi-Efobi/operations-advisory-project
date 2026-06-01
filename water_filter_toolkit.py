import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from datetime import datetime, timedelta
import json
import os

# ======================
# 1. MARKETING OPTIMIZER
# ======================
class MarketingOptimizer:
    def __init__(self, data_path="data/marketing_data.csv"):
        self.data_path = data_path
        self.data = self._load_data()

    def _load_data(self):
        if not os.path.exists(self.data_path):
            # Create sample data if file doesn't exist
            sample_data = {
                "campaign_id": ["001", "002", "003"],
                "campaign_type": ["Digital", "Physical", "Digital"],
                "state": ["Lagos", "Kano", "Rivers"],
                "orders": [5000, 3000, 7000],
                "market_share": [10, 15, 25],
                "start_date": ["2024-01-01", "2024-02-01", "2024-03-01"],
                "end_date": ["2024-01-31", "2024-02-28", "2024-03-31"]
            }
            pd.DataFrame(sample_data).to_csv(self.data_path, index=False)
        return pd.read_csv(self.data_path)

    def analyze_campaign_performance(self, campaign_type=None, state=None):
        """Analyze performance of campaigns by type or state."""
        filtered_data = self.data
        if campaign_type:
            filtered_data = filtered_data[filtered_data["campaign_type"] == campaign_type]
        if state:
            filtered_data = filtered_data[filtered_data["state"] == state]

        if filtered_data.empty:
            return {"error": "No data found for the specified filters."}

        return {
            "total_orders": filtered_data["orders"].sum(),
            "avg_market_share": filtered_data["market_share"].mean(),
            "campaigns": len(filtered_data),
            "states": filtered_data["state"].unique().tolist()
        }

    def recommend_strategies(self, current_market_share, target_market_share):
        """Recommend strategies to grow market share."""
        gap = target_market_share - current_market_share
        strategies = []
        if gap > 20:
            strategies.extend([
                "Launch targeted digital campaigns in high-potential states (e.g., Kano, Rivers).",
                "Partner with local influencers and retailers for physical sales boosts.",
                "Allocate 60% of marketing budget to digital, 40% to physical."
            ])
        elif gap > 10:
            strategies.extend([
                "Increase ad spend in underperforming regions by 20%.",
                "Offer limited-time promotions or discounts to attract new customers.",
                "Leverage customer referrals with incentives."
            ])
        else:
            strategies.extend([
                "Focus on customer retention and loyalty programs.",
                "Optimize existing campaigns for higher conversion rates.",
                "Expand to adjacent states with similar demographics."
            ])
        return strategies

# ======================
# 2. PRODUCTION EFFICIENCY
# ======================
class ProductionEfficiency:
    def __init__(self, data_path="data/production_data.csv"):
        self.data_path = data_path
        self.data = self._load_data()

    def _load_data(self):
        if not os.path.exists(self.data_path):
            # Create sample data if file doesn't exist
            sample_data = {
                "process_id": ["001", "002", "003", "004"],
                "process_name": ["Assembly", "Quality Check", "Packaging", "Filter Installation"],
                "duration_minutes": [30, 15, 20, 25],
                "waste_percentage": [8, 2, 5, 10],
                "improvement_potential": ["High", "Low", "Medium", "High"]
            }
            pd.DataFrame(sample_data).to_csv(self.data_path, index=False)
        return pd.read_csv(self.data_path)

    def map_processes(self):
        """Map all production processes with details."""
        return self.data.to_dict('records')

    def identify_waste(self, threshold=5):
        """Identify processes with waste above a threshold."""
        waste_processes = self.data[self.data["waste_percentage"] > threshold]
        return waste_processes[["process_id", "process_name", "waste_percentage"]].to_dict('records')

    def suggest_improvements(self):
        """Suggest Lean Manufacturing improvements."""
        waste_areas = self.identify_waste()
        improvements = []
        for area in waste_areas:
            if area["waste_percentage"] > 10:
                improvements.append(
                    f"🔴 **High Priority**: Redesign {area['process_name']} to reduce waste (current: {area['waste_percentage']}%). "
                    f"Potential: {area['improvement_potential']}"
                )
            else:
                improvements.append(
                    f"🟡 **Medium Priority**: Optimize {area['process_name']} for better efficiency (current waste: {area['waste_percentage']}%)."
                )
        return improvements if improvements else ["✅ No significant waste detected."]

# ======================
# 3. PORTFOLIO MANAGER
# ======================
class PortfolioManager:
    def __init__(self, data_path="data/portfolio_data.csv"):
        self.data_path = data_path
        self.data = self._load_data()

    def _load_data(self):
        if not os.path.exists(self.data_path):
            # Create sample data if file doesn't exist
            sample_data = {
                "product_id": ["001", "002", "003"],
                "product_name": ["Home Water Filter", "Commercial Water Filter", "Portable Water Filter"],
                "category": ["Residential", "Commercial", "Residential"],
                "inventory": [5000, 2000, 3000],
                "unit_cost": [5000, 20000, 3000],
                "supplier": ["ABC Supplies", "XYZ Supplies", "DEF Supplies"],
                "reorder_level": [1000, 500, 800]
            }
            pd.DataFrame(sample_data).to_csv(self.data_path, index=False)
        return pd.read_csv(self.data_path)

    def track_inventory(self, product_name, threshold):
        """Track inventory levels for a product."""
        product_data = self.data[self.data["product_name"] == product_name]
        if product_data.empty:
            return {"error": f"Product '{product_name}' not found."}

        current_inventory = product_data.iloc[0]["inventory"]
        reorder_level = product_data.iloc[0]["reorder_level"]
        return {
            "product": product_name,
            "current_inventory": current_inventory,
            "reorder_level": reorder_level,
            "below_threshold": current_inventory < threshold,
            "needs_reorder": current_inventory < reorder_level
        }

    def negotiate_supplier_contracts(self, supplier, current_price, target_price):
        """Simulate supplier contract negotiations."""
        supplier_data = self.data[self.data["supplier"] == supplier]
        if supplier_data.empty:
            return {"error": f"Supplier '{supplier}' not found."}

        savings = current_price - target_price
        savings_percentage = (savings / current_price) * 100
        return {
            "supplier": supplier,
            "current_price": current_price,
            "target_price": target_price,
            "savings": savings,
            "savings_percentage": f"{savings_percentage:.2f}%",
            "status": "✅ Success" if savings > 0 else "❌ No savings"
        }

    def calculate_portfolio_value(self):
        """Calculate total portfolio value."""
        self.data["total_value"] = self.data["inventory"] * self.data["unit_cost"]
        return {
            "total_value": f"₦{self.data['total_value'].sum():,}",
            "breakdown": self.data[["product_name", "total_value"]].to_dict('records')
        }

# ======================
# 4. PROFITABILITY ANALYZER
# ======================
class ProfitabilityAnalyzer:
    def __init__(self, data_path="data/revenue_data.csv"):
        self.data_path = data_path
        self.data = self._load_data()

    def _load_data(self):
        if not os.path.exists(self.data_path):
            # Create sample data if file doesn't exist
            sample_data = {
                "month": ["2024-01", "2024-02", "2024-03", "2024-04"],
                "revenue": [10000000, 15000000, 20000000, 25000000],
                "costs": [8000000, 10000000, 12000000, 15000000],
                "profit": [2000000, 5000000, 8000000, 10000000],
                "market_share": [10, 15, 25, 30]
            }
            pd.DataFrame(sample_data).to_csv(self.data_path, index=False)
        return pd.read_csv(self.data_path)

    def calculate_profitability(self, revenue, costs):
        """Calculate profitability percentage."""
        profit = revenue - costs
        profitability = (profit / revenue) * 100 if revenue > 0 else 0
        return {
            "revenue": f"₦{revenue:,}",
            "costs": f"₦{costs:,}",
            "profit": f"₦{profit:,}",
            "profitability_percentage": f"{profitability:.2f}%"
        }

    def forecast_revenue(self, historical_data, periods=3):
        """Forecast future revenue using linear regression."""
        X = np.arange(len(historical_data)).reshape(-1, 1)
        y = np.array(historical_data)
        model = LinearRegression()
        model.fit(X, y)
        future_X = np.arange(len(historical_data), len(historical_data) + periods).reshape(-1, 1)
        forecast = model.predict(future_X)
        return [f"₦{int(rev):,}" for rev in forecast]

# ======================
# 5. ADVISORY INSIGHTS
# ======================
class AdvisoryInsights:
    def generate_advisory_report(self, current_revenue, target_revenue, growth_areas):
        """Generate a strategic advisory report."""
        growth_needed = target_revenue - current_revenue
        growth_percentage = (growth_needed / current_revenue) * 100 if current_revenue > 0 else 0

        report = f"""
        📊 **STRATEGIC ADVISORY REPORT**
        ==============================
        **Generated on:** {datetime.now().strftime("%Y-%m-%d")}

        📈 **CURRENT STATUS**
        - Current Revenue: ₦{current_revenue:,}
        - Target Revenue: ₦{target_revenue:,}
        - Growth Needed: ₦{growth_needed:,} ({growth_percentage:.2f}%)

        🎯 **GROWTH AREAS**
        """
        for area in growth_areas:
            report += f"  - **{area}**\n"

        report += """
        💡 **RECOMMENDATIONS**
        1. **Marketing**: Allocate 60% of the budget to digital campaigns in high-growth states.
        2. **Production**: Implement Lean Manufacturing to reduce waste by 25%.
        3. **Portfolio**: Negotiate supplier contracts to cut costs by 10-15%.
        4. **Expansion**: Target adjacent states with similar demographics to Lagos and Kano.

        📅 **NEXT STEPS**
        - Review marketing performance weekly.
        - Audit production processes monthly.
        - Renegotiate supplier contracts quarterly.
        """
        return report

    def identify_growth_opportunities(self, market_share, competitors):
        """Identify growth opportunities based on market share and competitors."""
        opportunities = []
        if market_share < 30:
            opportunities.append("🌍 **Expand Geographically**: Target states with low penetration (e.g., North East).")
        if len(competitors) > 2:
            opportunities.append("🏆 **Differentiate Products**: Introduce unique features (e.g., smart filters, subscription models).")
        if market_share < 50:
            opportunities.append("📢 **Boost Marketing**: Increase digital ad spend by 30% in high-potential regions.")
        opportunities.append("🤝 **Partnerships**: Collaborate with NGOs or government agencies for bulk contracts.")
        return opportunities

# ======================
# MAIN EXECUTION
# ======================
def main():
    print("🚀 **Water Filter Business Toolkit**\n")
    print("Select a module to run:")
    print("1. 📈 Marketing Optimizer")
    print("2. 🏭 Production Efficiency")
    print("3. 💰 Portfolio Manager")
    print("4. 📊 Profitability Analyzer")
    print("5. 🧠 Advisory Insights")
    print("6. 🏃 Run All Modules (Demo)\n")

    choice = input("Enter your choice (1-6): ")

    if choice == "1":
        # Marketing Optimizer Demo
        print("\n📈 **MARKETING OPTIMIZER**\n")
        optimizer = MarketingOptimizer()
        performance = optimizer.analyze_campaign_performance(campaign_type="Digital", state="Lagos")
        print("📊 Campaign Performance in Lagos (Digital):")
        print(json.dumps(performance, indent=2))

        strategies = optimizer.recommend_strategies(current_market_share=10, target_market_share=40)
        print("\n💡 Recommended Strategies to Grow Market Share:")
        for i, strategy in enumerate(strategies, 1):
            print(f"   {i}. {strategy}")

    elif choice == "2":
        # Production Efficiency Demo
        print("\n🏭 **PRODUCTION EFFICIENCY**\n")
        efficiency = ProductionEfficiency()
        process_map = efficiency.map_processes()
        print("📋 Factory Process Map:")
        for process in process_map:
            print(f"   - {process['process_name']}: {process['duration_minutes']} mins, {process['waste_percentage']}% waste")

        waste_areas = efficiency.identify_waste(threshold=5)
        print("\n⚠️  Areas with >5% Waste:")
        for area in waste_areas:
            print(f"   - {area['process_name']}: {area['waste_percentage']}%")

        improvements = efficiency.suggest_improvements()
        print("\n💡 Suggested Improvements:")
        for improvement in improvements:
            print(f"   {improvement}")

    elif choice == "3":
        # Portfolio Manager Demo
        print("\n💰 **PORTFOLIO MANAGER**\n")
        manager = PortfolioManager()
        inventory = manager.track_inventory("Home Water Filter", threshold=1000)
        print("📦 Inventory Status for Home Water Filter:")
        print(json.dumps(inventory, indent=2))

        contract = manager.negotiate_supplier_contracts("ABC Supplies", 5000, 4500)
        print("\n🤝 Supplier Contract Negotiation:")
        print(json.dumps(contract, indent=2))

        portfolio_value = manager.calculate_portfolio_value()
        print("\n💵 Portfolio Value:")
        print(json.dumps(portfolio_value, indent=2))

    elif choice == "4":
        # Profitability Analyzer Demo
        print("\n📊 **PROFITABILITY ANALYZER**\n")
        analyzer = ProfitabilityAnalyzer()
        profitability = analyzer.calculate_profitability(revenue=20000000, costs=15000000)
        print("💰 Profitability Analysis:")
        print(json.dumps(profitability, indent=2))

        forecast = analyzer.forecast_revenue([10000000, 15000000, 20000000], periods=3)
        print("\n🔮 Revenue Forecast (Next 3 Months):")
        for i, rev in enumerate(forecast, 1):
            print(f"   Month {i}: {rev}")

    elif choice == "5":
        # Advisory Insights Demo
        print("\n🧠 **ADVISORY INSIGHTS**\n")
        advisory = AdvisoryInsights()
        report = advisory.generate_advisory_report(
            current_revenue=20000000,
            target_revenue=50000000,
            growth_areas=["Marketing Expansion", "Production Optimization", "Supplier Negotiations"]
        )
        print(report)

        opportunities = advisory.identify_growth_opportunities(
            market_share=40,
            competitors=["Brand A", "Brand B", "Brand C"]
        )
        print("\n🌱 Growth Opportunities:")
        for opportunity in opportunities:
            print(f"   {opportunity}")

    elif choice == "6":
        # Run All Modules
        print("\n🏃 **RUNNING ALL MODULES (DEMO)**\n")
        print("=" * 50)

        # Marketing Optimizer
        print("\n📈 **MARKETING OPTIMIZER**")
        optimizer = MarketingOptimizer()
        performance = optimizer.analyze_campaign_performance(campaign_type="Digital")
        print(f"Total Orders (Digital): {performance['total_orders']}")
        print(f"Average Market Share: {performance['avg_market_share']}%")

        # Production Efficiency
        print("\n🏭 **PRODUCTION EFFICIENCY**")
        efficiency = ProductionEfficiency()
        waste_areas = efficiency.identify_waste(threshold=5)
        print(f"Processes with >5% waste: {len(waste_areas)}")

        # Portfolio Manager
        print("\n💰 **PORTFOLIO MANAGER**")
        manager = PortfolioManager()
        portfolio_value = manager.calculate_portfolio_value()
        print(f"Total Portfolio Value: {portfolio_value['total_value']}")

        # Profitability Analyzer
        print("\n📊 **PROFITABILITY ANALYZER**")
        analyzer = ProfitabilityAnalyzer()
        profitability = analyzer.calculate_profitability(revenue=20000000, costs=15000000)
        print(f"Profitability: {profitability['profitability_percentage']}")

        # Advisory Insights
        print("\n🧠 **ADVISORY INSIGHTS**")
        advisory = AdvisoryInsights()
        opportunities = advisory.identify_growth_opportunities(market_share=40, competitors=["Brand A", "Brand B"])
        print(f"Growth Opportunities Identified: {len(opportunities)}")

        print("\n" + "=" * 50)
        print("✅ All modules executed successfully!")

    else:
        print("❌ Invalid choice. Please select 1-6.")

if __name__ == "__main__":
    # Create data directory if it doesn't exist
    if not os.path.exists("data"):
        os.makedirs("data")
    main()
