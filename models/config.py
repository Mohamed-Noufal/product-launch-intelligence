# models/config.py
from dataclasses import dataclass

@dataclass
class AgentConfig:
    """Configuration for agent settings"""
    google_api_key: str
    firecrawl_api_key: str
    model_id: str = "gemini-1.5-flash"