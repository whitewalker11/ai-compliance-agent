from .tools import licensing, lineage, risk_assessment

class ComplianceAgent:
    def run_checks(self):
        print("Running licensing checks...")
        licensing.check_licenses()
        print("Checking dataset lineage...")
        lineage.verify_lineage()
        print("Assessing risk...")
        risk_assessment.run_risk_analysis()