# ui/components/agent_cards.py
import streamlit as st
from ui.themes.colors import ColorScheme

class AgentCards:
    AGENTS_DATA = [
        {
            "id": "launch",
            "icon": "🎯", 
            "name": "Launch Analyst",
            "description": "Competitive positioning & strategy analysis",
            "color": ColorScheme.AGENT_COLORS["launch"]
        },
        {
            "id": "sentiment",
            "icon": "💬",
            "name": "Sentiment Specialist", 
            "description": "Market perception & customer feedback",
            "color": ColorScheme.AGENT_COLORS["sentiment"]
        },
        {
            "id": "metrics", 
            "icon": "📊",
            "name": "Metrics Analyst",
            "description": "Performance KPIs & growth tracking",
            "color": ColorScheme.AGENT_COLORS["metrics"]
        }
    ]
    
    @staticmethod
    def render_agent_grid():
        cols = st.columns(3)
        for idx, agent in enumerate(AgentCards.AGENTS_DATA):
            with cols[idx]:
                AgentCards._render_agent_card(agent)
    
    @staticmethod
    def _render_agent_card(agent: dict):
        st.markdown(f"""
        <div class="agent-card" style="border-left-color: {agent['color']};">
            <div style="font-size: 2.5em; text-align: center; margin-bottom: 0.5rem;">{agent['icon']}</div>
            <h3 style="text-align: center; color: {ColorScheme.TEXT}; margin: 0.5rem 0;">{agent['name']}</h3>
            <p style="text-align: center; color: #718096; margin: 0; line-height: 1.4;">{agent['description']}</p>
        </div>
        """, unsafe_allow_html=True)