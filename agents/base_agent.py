# agents/base_agent.py
from abc import ABC, abstractmethod
from agno.agent import Agent
from agno.models.google import Gemini
from agno.tools.firecrawl import FirecrawlTools
from textwrap import dedent

class BaseAgent(ABC):
    """Base class for all specialized agents with common configuration"""
    
    def __init__(self, google_api_key: str, firecrawl_api_key: str):
        self.google_api_key = google_api_key
        self.firecrawl_api_key = firecrawl_api_key
        self.agent = None
        self._initialize_agent()
    
    @abstractmethod
    def get_agent_description(self) -> str:
        """Return the agent's specialized description"""
        pass
    
    @abstractmethod
    def get_agent_name(self) -> str:
        """Return the agent's name"""
        pass
    
    def _initialize_agent(self):
        """Initialize the agent with common configuration"""
        try:
            self.agent = Agent(
                name=self.get_agent_name(),
                description=dedent(self.get_agent_description()),
                model=Gemini(id="gemini-2.5-flash"),
                tools=[FirecrawlTools(api_key=self.firecrawl_api_key)],
                markdown=True,
                exponential_backoff=True,
                delay_between_retries=2,
            )
        except Exception as e:
            raise Exception(f"Failed to initialize {self.get_agent_name()}: {e}")
    
    def is_ready(self) -> bool:
        """Check if agent is properly initialized"""
        return self.agent is not None
    
    def analyze(self, prompt: str):
        """Execute analysis with the agent"""
        if not self.is_ready():
            raise ValueError(f"{self.get_agent_name()} is not initialized")
        
        return self.agent.run(prompt)