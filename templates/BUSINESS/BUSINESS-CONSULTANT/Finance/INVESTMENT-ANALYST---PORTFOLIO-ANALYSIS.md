# Investment Analyst - AI Agent Template

## Portfolio Analysis

### 1. Critical Knowledge Areas

1. Financial Statement Analysis (Balance Sheet, Income Statement, Cash Flow Statement)
2. Ratio Analysis (Liquidity, Profitability, Efficiency, Market Valuation Ratios)
3. Fundamental Analysis of Stocks/ETFs/Bonds
4. Technical Analysis (Chart Patterns, Indicators, Trends)
5. Portfolio Diversification and Risk Management
6. Asset Allocation Strategies
7. Behavioral Finance Principles
8. ESG (Environmental, Social, Governance) Investing
9. Market Microstructure Concepts
10. Regulatory Environment (SEC, FINRA, etc.)
11. Valuation Techniques (Discounted Cash Flow, Comparable Analysis)
12. Portfolio Rebalancing Procedures
13. Scenario and Stress Testing Approaches
14. Performance Attribution Analysis
15. Risk Measurement Tools (VaR, CVaR, Monte Carlo Simulations)

### 2. Execution Steps

1. **Data Collection**
   - Gather historical price data for all securities in the portfolio using Yahoo Finance API.
   - Obtain financial statements, sector benchmarks, and macroeconomic indicators from databases like S&P Capital IQ or Bloomberg Terminal (optional).

2. **Data Preprocessing**
   - Clean missing values, outliers, and inconsistencies in the dataset.
   - Normalize prices and calculate returns.

3. **Financial Statement Analysis**
   - Analyze balance sheet and income statement ratios for each company in the portfolio.
   - Compare sector averages to identify anomalies or value opportunities.

4. **Ratio Analysis**
   - Calculate key financial ratios such as P/E, P/B, ROE, Debt/Equity, Current Ratio, etc.
   - Segment securities based on these ratios into groups (e.g., Value vs Growth).

5. **Fundamental Analysis**
   - Assess each security's intrinsic value using DCF models and sector comparables.
   - Identify undervalued or overvalued stocks.

6. **Technical Analysis**
   - Implement various indicators like RSI, MACD, Bollinger Bands, etc.
   - Generate buy/sell signals based on indicator crossovers and patterns.

7. **Portfolio Optimization**
   - Use mean-variance optimization to find the optimal asset allocation maximizing expected returns for a given risk level.
   - Incorporate ESG filters if available.

8. **Risk Management**
   - Calculate VaR, CVaR, and other stress scenarios for the entire portfolio.
   - Identify single stock or sector risks that could impact overall portfolio resilience.

9. **Performance Analysis**
   - Decompose total returns into components like active return, benchmark exposure, and style alpha/beta.
   - Use regression analysis to attribute returns to specific factors (e.g., size, value).

10. **Rebalancing Strategy**
    - Develop a systematic approach for periodic rebalancing of the portfolio to maintain target allocations.
    - Automate execution using order routing APIs.

### 3. Tools and Software

- **Data Collection**: Yahoo Finance API, Alpha Vantage API (free), Quandl API (free)
- **Data Storage/Analysis**: Python Pandas, Jupyter Notebook
- **Financial Modeling**: Excel or Google Sheets (for manual calculations), YFinance library for Python integration
- **Charting and Visualization**: TradingView's free platform, Plotly in Python
- **Portfolio Optimization**: Portfolio Visualizer (free tier), Morningstar Advisor Tools (premium)
- **Risk Management**: VaR/CVaR calculators built into risk management software like RiskMetrics or using Excel models
- **Performance Attribution**: Factor Investing platforms like Bloomberg Terminal (optional) or DIY calculations in Python

### 4. Success Criteria

1. Portfolio volatility reduced by X% compared to benchmark.
2. Annualized alpha of Y% after fees.
3. ESG score meets investor's sustainability criteria with Z% allocation.
4. Portfolio rebalanced within T days of deviation from target allocations.
5. Risk metrics (VaR, CVaR) meet regulatory or internal risk appetite thresholds.

### 5. Troubleshooting

- **Data Quality Issues**
  - Verify data sources and update frequency.
  - Check for missing values or inconsistencies in the dataset.

- **Model Calibration Errors**
  - Ensure historical parameters are correctly estimated using sufficient data points.
  - Regularly backtest models against out-of-sample periods.

- **Execution Challenges**
  - Confirm order routing is working properly to all relevant exchanges.
  - Monitor market impact on trade execution prices during high volatility periods.

- **Regulatory Compliance**
  - Maintain accurate records of transactions and portfolio changes for audit purposes.
  - Ensure all investments comply with applicable laws and regulations.

### 6. Recommended Tool Stack

- Primary: Python (free), Jupyter Notebook
- Data APIs:
  - Yahoo Finance API (free)
  - Alpha Vantage API (free tier, paid beyond that)
  - Quandl API (free for many datasets, premium options available)
- Charting and Visualization:
  - TradingView Free Platform
  - Plotly (Python library) or Matplotlib
- Portfolio Optimization:
  - Portfolio Visualizer (free tier includes most features)
  - Morningstar Advisor Tools (requires subscription)
- Risk Management:
  - VaR/CVaR calculators via Excel or Python libraries like riskmetrics
- Performance Attribution:
  - Bloomberg Terminal (premium alternative for factor analysis)
  - DIY calculations in Python using libraries like Pyfolio

### 7. Timeline to Achieve Portfolio Analysis

**Month 1-2: Foundation Building**
- Familiarize with financial statement analysis and ratio metrics.
- Set up data collection pipelines using APIs.

**Month 3-4: Modeling and Optimization**
- Implement fundamental and technical analysis models in Python.
- Conduct initial portfolio optimization exercises.

**Month 5-6: Risk Management Integration**
- Incorporate risk metrics like VaR into the portfolio framework.
- Develop a comprehensive rebalancing strategy.

**Month 7-8: Refinement and Testing**
- Backtest all models against historical periods (2000-2023).
- Optimize models for performance efficiency.
- Validate results with an independent dataset or through simulation.

**Month 9-10: Documentation and Training**
- Document the entire workflow from data collection to execution.
- Conduct training sessions for junior analysts on the system.

**Month 11-12: Deployment and Review**
- Go live with the portfolio analysis model in production.
- Schedule quarterly reviews to update models, risk metrics, and allocations.

