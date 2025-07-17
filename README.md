# AI Compliance Agent

This ADK agent automates regulatory compliance checks for open-source AI in medical devices.

## Features
- License validation
- Dataset traceability
- Risk analysis (ISO 14971)
- Drift monitoring
- Explainability (SHAP, LIME)

## Structure
```
ai-compliance-adk/
├── agents/
│   └── compliance_agent/
│       ├── agent.py
│       ├── tools/
│       └── prompts/
├── protos/
├── tests/
├── scripts/
├── config/
```

## Getting Started
```bash
pip install -r requirements.txt
python scripts/run_agent.py
```