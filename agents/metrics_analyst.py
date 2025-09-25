# agents/metrics_analyst.py
from .base_agent import BaseAgent

class MetricsAnalyst(BaseAgent):
    """Specialized agent for launch metrics analysis"""
    
    def get_agent_name(self) -> str:
        return "Launch Metrics Specialist"
    
    def get_agent_description(self) -> str:
        return """
            You are a product launch performance analyst who specializes in tracking and analyzing launch KPIs.
            Your focus areas include:
            • User adoption and engagement metrics
            • Revenue and business performance indicators
            • Market penetration and growth rates
            • Press coverage and media attention analysis
            • Social media traction and viral coefficient tracking
            • Competitive market share analysis
            Always provide quantitative insights with context and benchmark against industry standards when possible.
            IMPORTANT: Conclude your report with a 'Sources:' section, listing all URLs of websites you crawled or searched for this analysis.
        """
    
    def analyze_metrics(self, company_name: str):
        """Analyze launch metrics for a company"""
        prompt = (
            f"List (max 10 bullets) the most important publicly available KPIs & qualitative signals for {company_name}'s recent product launches. "
            f"Include engagement stats, press coverage, adoption metrics, and market traction data if available."
        )
        return self.analyze(prompt)