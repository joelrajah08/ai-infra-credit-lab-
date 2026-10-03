# AI Infrastructure Credit Lab

**Which companies funding the AI and data-center buildout could handle higher borrowing costs or slower returns on their spending?**

An interactive tool that pulls public financial data from SEC EDGAR, runs credit scenarios, and shows the effect on cash flow and debt metrics. Every displayed figure links back to its source filing and reporting period.

## Team
- **Joel Rajah**: Engineering (data pipeline, calculations, interface)
- **Zack Aziz**: Analysis (company selection, metric definitions, scenarios, memo)

## Scope
- **Companies:** 3 to start (TBD)
- **Scenarios:** Base, Higher Rates, Slower Payoff
- **Metrics:** Free cash flow, capex coverage, leverage, interest coverage (definitions in progress)

## Stack
Python, pandas, SEC EDGAR XBRL API, Streamlit

## Roadmap
- [ ] Weeks 1–2: Select companies, define metrics, manually verify filing figures
- [ ] Weeks 3–4: Data pipeline and comparison screen
- [ ] Weeks 5–6: Scenario engine, validated against a separate spreadsheet
- [ ] Weeks 7–8: Analyst memo, demo polish, walkthrough video

## Disclaimer
A student portfolio project for educational purposes. Not investment advice and not affiliated with any financial institution.

