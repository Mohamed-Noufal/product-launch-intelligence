# ui/components/progress_indicators.py
import streamlit as st
import time

class ProgressIndicators:
    @staticmethod
    def render_analysis_progress(agent_type: str, steps: list = None):
        """Show beautiful progress indicator"""
        if steps is None:
            steps = [
                "🔍 Gathering market data...",
                "🤖 Analyzing with AI agents...",
                "📊 Generating insights...", 
                "🎯 Finalizing report..."
            ]
        
        progress_bar = st.progress(0)
        status_container = st.empty()
        
        for i, step in enumerate(steps):
            progress = (i + 1) * 25
            progress_bar.progress(progress)
            status_container.info(f"**{step}** ({progress}%)")
            time.sleep(0.5)  # Simulate processing
        
        progress_bar.progress(100)
        status_container.success("✅ Analysis complete!")
    
    @staticmethod
    def render_loading_animation():
        """Simple loading spinner"""
        return st.spinner("🤖 AI agents are working their magic...")