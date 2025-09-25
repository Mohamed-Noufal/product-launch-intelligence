# agents/sentiment_analyst.py
from .base_agent import BaseAgent

class SentimentAnalyst(BaseAgent):
    """Specialized agent for market sentiment analysis"""
    
    def get_agent_name(self) -> str:
        return "Market Sentiment Specialist"
    
    def get_agent_description(self) -> str:
        return """
            You are a market research expert specializing in sentiment analysis and consumer perception tracking.
            Your expertise includes:
            • Analyzing social media sentiment and customer feedback
            • Identifying positive and negative sentiment drivers
            • Tracking brand perception trends across platforms
            • Monitoring customer satisfaction and review patterns
            • Providing actionable insights on market reception
            Focus on extracting sentiment signals from social platforms, review sites, forums, and customer feedback channels.
            IMPORTANT: Conclude your report with a 'Sources:' section, listing all URLs of websites you crawled or searched for this analysis.
        """
    
    def analyze_sentiment(self, company_name: str):
        """Analyze market sentiment for a company"""
        prompt = (
            f"Summarize market sentiment for {company_name} in <=10 bullets. "
            f"Cover top positive & negative themes with source mentions (G2, Reddit, Twitter, customer reviews)."
        )
        return self.analyze(prompt)