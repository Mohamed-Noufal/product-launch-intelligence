# ui/components/results_display.py
import streamlit as st
import plotly.graph_objects as go
from datetime import datetime

class ResultsDisplay:
    @staticmethod
    def render_analysis_result(result_type: str, result_data: dict, company_name: str):
        """Render analysis results with interactive elements"""
        
        if result_type == "competitor":
            ResultsDisplay._render_competitor_result(result_data, company_name)
        elif result_type == "sentiment":
            ResultsDisplay._render_sentiment_result(result_data, company_name)
        elif result_type == "metrics":
            ResultsDisplay._render_metrics_result(result_data, company_name)
    
    @staticmethod
    def _render_competitor_result(data: dict, company_name: str):
        """Render competitor analysis with interactive elements"""
        
        # SWOT Analysis Visualization
        st.subheader("🔍 SWOT Analysis")
        
        swot_cols = st.columns(4)
        swot_data = [
            ("💪 Strengths", ["Innovative features", "Strong brand", "Market timing"], "#4ECDC4"),
            ("⚠️ Weaknesses", ["Support scalability", "Intl. penetration"], "#FF6B6B"),
            ("🚀 Opportunities", ["Market expansion", "New features"], "#45B7D1"),
            ("🌪️ Threats", ["Competition", "Market changes"], "#FFEAA7")
        ]
        
        for idx, (title, items, color) in enumerate(swot_data):
            with swot_cols[idx]:
                st.markdown(f"""
                <div style='
                    background: {color}20;
                    padding: 1rem;
                    border-radius: 10px;
                    border-left: 4px solid {color};
                    margin: 0.5rem 0;
                    height: 200px;
                '>
                    <h4 style='margin: 0 0 1rem 0;'>{title}</h4>
                    <ul style='margin: 0; padding-left: 1rem;'>
                """, unsafe_allow_html=True)
                
                for item in items:
                    st.markdown(f"<li>{item}</li>", unsafe_allow_html=True)
                
                st.markdown("</ul></div>", unsafe_allow_html=True)
        
        # Competitive positioning chart
        fig = go.Figure()
        
        fig.add_trace(go.Scatterpolar(
            r=[4, 3, 5, 4, 3],
            theta=['Innovation', 'Market Share', 'Customer Sat', 'Growth', 'Brand Strength'],
            fill='toself',
            name=company_name,
            line_color='#667eea'
        ))
        
        fig.add_trace(go.Scatterpolar(
            r=[3, 4, 3, 2, 4],
            theta=['Innovation', 'Market Share', 'Customer Sat', 'Growth', 'Brand Strength'],
            fill='toself',
            name='Main Competitor',
            line_color='#FF6B6B'
        ))
        
        fig.update_layout(
            polar=dict(
                radialaxis=dict(visible=True, range=[0, 5])
            ),
            showlegend=True,
            title="Competitive Positioning Radar"
        )
        
        st.plotly_chart(fig, use_container_width=True)
    
    @staticmethod
    def _render_sentiment_result(data: dict, company_name: str):
        """Render sentiment analysis with interactive charts"""
        
        # Sentiment over time chart
        dates = ['Week 1', 'Week 2', 'Week 3', 'Week 4']
        positive = [65, 70, 75, 85]
        negative = [20, 15, 12, 8]
        neutral = [15, 15, 13, 7]
        
        fig = go.Figure()
        
        fig.add_trace(go.Scatter(
            x=dates, y=positive,
            mode='lines+markers',
            name='Positive',
            line=dict(color='#4ECDC4', width=4),
            marker=dict(size=8)
        ))
        
        fig.add_trace(go.Scatter(
            x=dates, y=negative,
            mode='lines+markers',
            name='Negative',
            line=dict(color='#FF6B6B', width=4),
            marker=dict(size=8)
        ))
        
        fig.add_trace(go.Scatter(
            x=dates, y=neutral,
            mode='lines+markers',
            name='Neutral',
            line=dict(color='#45B7D1', width=4),
            marker=dict(size=8)
        ))
        
        fig.update_layout(
            title="Sentiment Trend Over Time",
            xaxis_title="Time Period",
            yaxis_title="Sentiment Percentage",
            height=400
        )
        
        st.plotly_chart(fig, use_container_width=True)
        
        # Platform-specific sentiment
        platforms = ['Twitter', 'Reddit', 'Reviews', 'Forums']
        platform_sentiment = [75, 80, 85, 70]
        
        fig2 = px.bar(
            x=platforms, 
            y=platform_sentiment,
            color=platform_sentiment,
            color_continuous_scale=['#FF6B6B', '#FFEAA7', '#4ECDC4'],
            title="Sentiment by Platform"
        )
        
        st.plotly_chart(fig2, use_container_width=True)
    
    @staticmethod
    def _render_metrics_result(data: dict, company_name: str):
        """Render metrics analysis with interactive dashboard"""
        
        # Key metrics trend chart
        months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
        users = [1000, 2500, 5000, 12000, 25000, 40000]
        revenue = [50, 125, 300, 750, 1500, 2300]  # in thousands
        
        fig = go.Figure()
        
        fig.add_trace(go.Scatter(
            x=months, y=users,
            name='User Growth',
            yaxis='y',
            line=dict(color='#667eea', width=3)
        ))
        
        fig.add_trace(go.Bar(
            x=months, y=revenue,
            name='Revenue (K)',
            yaxis='y2',
            marker_color='#4ECDC4',
            opacity=0.7
        ))
        
        fig.update_layout(
            title="User Growth vs Revenue Over Time",
            xaxis=dict(title='Month'),
            yaxis=dict(title='Users', side='left'),
            yaxis2=dict(title='Revenue ($K)', side='right', overlaying='y'),
            showlegend=True,
            height=400
        )
        
        st.plotly_chart(fig, use_container_width=True)
        
        # Performance scorecard
        st.subheader("🎯 Performance Scorecard")
        
        score_cols = st.columns(4)
        scores = [
            ("Adoption Rate", "85%", "Excellent"),
            ("Market Impact", "High", "Strong"),
            ("Revenue Growth", "45%", "Outstanding"),
            ("Customer Satisfaction", "4.5/5", "Very Good")
        ]
        
        for idx, (metric, value, rating) in enumerate(scores):
            with score_cols[idx]:
                color = "#4ECDC4" if rating in ["Excellent", "Outstanding"] else "#FFEAA7"
                st.markdown(f"""
                <div style='
                    background: {color}20;
                    padding: 1rem;
                    border-radius: 10px;
                    text-align: center;
                    border: 2px solid {color};
                '>
                    <h4 style='margin: 0;'>{metric}</h4>
                    <h2 style='margin: 0.5rem 0; color: {color};'>{value}</h2>
                    <small style='color: #666;'>{rating}</small>
                </div>
                """, unsafe_allow_html=True)