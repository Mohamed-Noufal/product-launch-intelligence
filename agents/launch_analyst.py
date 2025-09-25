# agents/launch_analyst.py
from .base_agent import BaseAgent

class LaunchAnalyst(BaseAgent):
    """Specialized agent for competitor launch analysis"""
    
    def get_agent_name(self) -> str:
        return "Product Launch Analyst"
    
    def get_agent_description(self) -> str:
        return """
            You are a senior Go-To-Market strategist who evaluates competitor product launches with a critical, evidence-driven lens.
            Your objective is to uncover:
            • How the product is positioned in the market
            • Which launch tactics drove success (strengths)
            • Where execution fell short (weaknesses)
            • Actionable learnings competitors can leverage
            Always cite observable signals (messaging, pricing actions, channel mix, timing, engagement metrics). Maintain a crisp, executive tone and focus on strategic value.
            IMPORTANT: Conclude your report with a 'Sources:' section, listing all URLs of websites you crawled or searched for this analysis.
        """
    
    def generate_competitor_insights(self, company_name: str):
        """Generate competitor insights with proper formatting"""
        prompt = (
            f"Generate up to 16 evidence-based insight bullets about {company_name}'s most recent product launches.\n"
            f"Format requirements:\n"
            f"• Start every bullet with exactly one tag: Positioning | Strength | Weakness | Learning\n"
            f"• Follow the tag with a concise statement (max 30 words) referencing concrete observations: messaging, differentiation, pricing, channel selection, timing, engagement metrics, or customer feedback."
        )
        return self.analyze(prompt)