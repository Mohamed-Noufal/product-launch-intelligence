# ui/components/metrics_dashboard.py
import streamlit as st
import plotly.graph_objects as go
import plotly.express as px

class MetricsDashboard:
    @staticmethod
    def render_metrics_overview(analysis_data: dict):
        """Render interactive metrics dashboard"""
        st.subheader("📊 Launch Performance Dashboard")
        
        # Key metrics in columns
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.metric(
                label="🎯 Market Position", 
                value="Leader", 
                delta="Strong"
            )
        
        with col2:
            st.metric(
                label="💬 Sentiment Score", 
                value="85%", 
                delta="+12%"
            )
        
        with col3:
            st.metric(
                label="📈 Adoption Rate", 
                value="40%", 
                delta="+15%"
            )
        
        with col4:
            st.metric(
                label="🌟 Media Coverage", 
                value="156", 
                delta="+45"
            )
    
    @staticmethod
    def render_sentiment_chart(sentiment_data: dict):
        """Render sentiment analysis chart"""
        fig = go.Figure(data=[
            go.Bar(name='Positive', x=['Twitter', 'Reddit', 'Reviews'], y=[65, 70, 80], marker_color='#4ECDC4'),
            go.Bar(name='Negative', x=['Twitter', 'Reddit', 'Reviews'], y=[15, 20, 10], marker_color='#FF6B6B'),
            go.Bar(name='Neutral', x=['Twitter', 'Reddit', 'Reviews'], y=[20, 10, 10], marker_color='#45B7D1')
        ])
        
        fig.update_layout(
            title="Sentiment Analysis Across Platforms",
            barmode='stack',
            height=300
        )
        
        st.plotly_chart(fig, use_container_width=True)