# Investment Analyst - AI Agent Template

## Market Research

### 1. Critical Knowledge Areas

1. Fundamental Analysis (Financial Statements, Ratios)
2. Technical Analysis (Chart Patterns, Indicators)
3. Valuation Models (Discounted Cash Flow, P/E Ratio)
4. Industry & Sector Analysis
5. Risk Management (VaR, Stress Testing)
6. Macroeconomic Factors (Inflation, Interest Rates)
7. Behavioral Finance
8. Portfolio Construction and Diversification
9. Regulatory Environment
10. Emerging Markets & Trends

### 2. Execution Steps with Specific Actions

1. **Define Research Scope**: Identify the specific market(s), sector(s) or asset class(es) to research.
2. **Gather Historical Data**: Collect historical price, volume, and fundamental data using free APIs (e.g., Alpha Vantage, Yahoo Finance).
3. **Analyze Financial Statements**: Use tools like Python Pandas for cleaning and analyzing financial statements (income statement, balance sheet, cash flow).
4. **Perform Fundamental Analysis**:
   - Calculate key ratios (P/E, P/B, ROE, etc.)
   - Compare to peers and industry benchmarks
5. **Conduct Technical Analysis**:
   - Identify chart patterns and indicators
   - Backtest strategies using historical data
6. **Valuation Modeling**: Build DCF models or other valuation approaches in Excel or Google Sheets.
7. **Market Sentiment Analysis**: Use social media monitoring tools (e.g., Hugging Face Inference API with sentiment analysis models) to gauge market mood.
8. **Regulatory & News Monitoring**: Track relevant news and regulatory changes using RSS feeds from financial news sites.
9. **Stress Testing**: Assess portfolio resilience under various scenarios (e.g., 2008 crisis, inflation shock).
10. **Report Generation**: Compile findings into a structured report with visualizations.

### 3. Tools, Software, and Platforms

**Primary Tools:**

1. Python for data analysis and modeling
2. Jupyter Notebook or Google Colab for interactive coding
3. Excel/Google Sheets for financial models and static reporting
4. Notion or Evernote for knowledge management
5. Slack/Discord for team collaboration
6. Hugging Face Inference API (free) for sentiment analysis from text data

**Alternative Paid Tools:**

1. Bloomberg Terminal (premium)
2. Refinitiv Eikon (premium alternative)
3. Tableau Public (for advanced visualizations)

### 4. Success Criteria

- **Depth of Analysis**: Minimum of 5 different financial ratios calculated and benchmarked.
- **Accuracy in Valuation**: Models should be tested against at least 3 years of historical data with <10% error margin.
- **Market Sentiment Insight**: At least 2 social media sentiment analyses conducted, showing clear trends or anomalies.
- **Risk Assessment**: Portfolio stress-tested under at least 3 adverse scenarios without breaching risk limits.
- **Report Quality**: Final report should have a mix of text, tables, and charts with citations for all data sources.

### 5. Troubleshooting Common Issues

1. **Data Quality**:
   - Ensure all financial statements are audited and from the most recent year available.
   - Check for missing values in time series data; use interpolation techniques or mark as NaN.
2. **Model Limitations**:
   - DCF models assume constant growth rates, which may not hold true.
   - Be cautious with technical indicators that require large datasets to be statistically significant.
3. **Sentiment Analysis Errors**:
   - Use a diverse dataset (news sites, forums) to avoid bias in sentiment scoring.
   - Validate sentiment model predictions manually on a small sample set.
4. **Resource Limitations**:
   - If API limits are reached, switch to free alternatives or batch processing of requests.

### 6. Recommended Tool Stack

1. Python (free)
2. Jupyter Notebook / Google Colab (free)
3. Excel / Google Sheets (free with optional premium add-ons)
4. Notion / Evernote (free tier available)
5. Slack / Discord (team collaboration)
6. Hugging Face Inference API (free, with paid models for higher accuracy)

### 7. Realistic Timeline

**Phase 1: Research Planning & Data Gathering** (2 weeks):
- Define scope and collect data using APIs.

**Phase 2: Analysis Execution** (4 weeks):
- Perform fundamental and technical analysis.
- Build valuation models.

**Phase 3: Sentiment & Risk Analysis** (2 weeks):
- Analyze market sentiment using social media.
- Conduct stress tests on the portfolio.

**Phase 4: Reporting** (1 week):
- Compile findings into a comprehensive report.

### 8. Best Practices for 2024-2025

- **AI Integration**: Utilize AI-driven tools like ChatGPT or Claude for initial data summarization and hypothesis generation.
- **Automation**: Leverage APIs and web scraping libraries to automate data collection from sources like Yahoo Finance, Alpha Vantage, and IEX Cloud.
- **Real-Time Data**: Incorporate real-time price feeds for immediate sentiment analysis and portfolio monitoring.
- **Collaborative Note-Taking**: Use platforms like Notion or Confluence for shared research notes accessible by the entire team.

By following this comprehensive template and leveraging the recommended tools and practices, a new Investment Analyst can effectively conduct market research to inform investment decisions while staying ahead of industry trends in 2024-2025.

