# agents/team_coordinator.py
from agno.team import Team
from agno.models.google import Gemini
from .launch_analyst import LaunchAnalyst
from .sentiment_analyst import SentimentAnalyst
from .metrics_analyst import MetricsAnalyst

class TeamCoordinator:
    """Coordinates the multi-agent team for product intelligence"""
    
    def __init__(self, google_api_key: str, firecrawl_api_key: str):
        self.google_api_key = google_api_key
        self.firecrawl_api_key = firecrawl_api_key
        self.team = None
        self.agents = {}
        self._initialize_team()
    
    def _initialize_team(self):
        """Initialize all agents and the coordinated team"""
        try:
            # Initialize individual agents
            self.agents['launch'] = LaunchAnalyst(self.google_api_key, self.firecrawl_api_key)
            self.agents['sentiment'] = SentimentAnalyst(self.google_api_key, self.firecrawl_api_key)
            self.agents['metrics'] = MetricsAnalyst(self.google_api_key, self.firecrawl_api_key)
            
            # Create the coordinated team
            self.team = Team(
                name="Product Intelligence Team",
                model=Gemini(id="gemini-1.5-flash"),
                members=[agent.agent for agent in self.agents.values()],
                instructions=[
                    "Coordinate the analysis based on the user's request type:",
                    "1. For competitor analysis: Use the Product Launch Analyst to evaluate positioning, strengths, weaknesses, and strategic insights",
                    "2. For market sentiment: Use the Market Sentiment Specialist to analyze social media sentiment, customer feedback, and brand perception",
                    "3. For launch metrics: Use the Launch Metrics Specialist to track KPIs, adoption rates, press coverage, and performance indicators",
                    "Always provide evidence-based insights with specific examples and data points",
                    "Structure responses with clear sections and actionable recommendations",
                    "Include sources section with all URLs crawled or searched"
                ],
                markdown=True,
                debug_mode=True,
                show_members_responses=True,
            )
        except Exception as e:
            raise Exception(f"Failed to initialize team coordinator: {e}")
    
    def is_ready(self) -> bool:
        """Check if all agents and team are ready"""
        return (self.team is not None and 
                all(agent.is_ready() for agent in self.agents.values()))
    
    def get_agent_status(self) -> dict:
        """Get status of all individual agents"""
        return {
            agent_name: agent.is_ready() 
            for agent_name, agent in self.agents.items()
        }
    
    def _extract_content(self, response):
        """Extract content from Agno response objects"""
        if response is None:
            return ""
        
        # If it's a string, return directly
        if isinstance(response, str):
            return response
        
        # If it has content attribute (RunOutput object)
        if hasattr(response, 'content') and response.content:
            return response.content
        
        # If it's a messages list
        if hasattr(response, 'messages'):
            for message in response.messages:
                if hasattr(message, 'content') and message.content:
                    return message.content
        
        # Fallback to string conversion
        return str(response)
    
    def run_analysis(self, prompt: str):
        """Run analysis using the coordinated team and return clean content"""
        if not self.is_ready():
            raise ValueError("Team coordinator is not fully initialized")
        
        response = self.team.run(prompt)
        return self._extract_content(response)
    
    def analyze_competitor(self, company_name: str):
        """Analyze competitor using the Launch Analyst"""
        if not self.is_ready():
            raise ValueError("Team coordinator is not fully initialized")

        response = self.agents['launch'].analyze(
            f"Generate insights about {company_name}'s product launches."
        )
        return self._extract_content(response)
    
    def analyze_sentiment(self, company_name: str):
        """Analyze sentiment using the Sentiment Analyst"""
        if not self.is_ready():
            raise ValueError("Team coordinator is not fully initialized")

        response = self.agents['sentiment'].analyze(
            f"Analyze the market sentiment for {company_name}."
        )
        return self._extract_content(response)
    
    def analyze_metrics(self, company_name: str):
        """Analyze metrics using the Metrics Analyst"""
        if not self.is_ready():
            raise ValueError("Team coordinator is not fully initialized")

        response = self.agents['metrics'].analyze(
            f"Analyze the performance metrics for {company_name}."
        )
        return self._extract_content(response)