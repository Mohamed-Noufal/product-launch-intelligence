# ui/components/analysis_tabs.py
import streamlit as st
from ui.components.progress_indicators import ProgressIndicators
from ui.components.metrics_dashboard import MetricsDashboard
from ui.themes.colors import ColorScheme

class AnalysisTabs:
    @staticmethod
    def render(company_name: str, system):
        """Render enhanced analysis tabs with visual feedback"""
        
        # Create stylish tabs with icons
        tab1, tab2, tab3 = st.tabs([
            "🎯 **Competitor Analysis**", 
            "💬 **Market Sentiment**", 
            "📊 **Launch Metrics**"
        ])
        
        with tab1:
            AnalysisTabs._render_competitor_tab(company_name, system)
        
        with tab2:
            AnalysisTabs._render_sentiment_tab(company_name, system)
        
        with tab3:
            AnalysisTabs._render_metrics_tab(company_name, system)
    
    @staticmethod
    def _render_competitor_tab(company_name: str, system):
        """Enhanced competitor analysis tab"""
        col1, col2 = st.columns([3, 1])
        
        with col1:
            st.markdown("### 🎯 Deep Competitive Analysis")
            st.caption(f"Strategic positioning insights for **{company_name}**")
        
        with col2:
            if st.button("🚀 **Run Analysis**", key="run_competitor", use_container_width=True):
                if system and system.is_ready():
                    with st.spinner("🤖 Launch Analyst working..."):
                        ProgressIndicators.render_analysis_progress("competitor")
                        result = system.analyze_competitor(company_name)
                        st.session_state.competitor_result = result
                        st.rerun()
        
        # Display results with enhanced visualization
        if hasattr(st.session_state, 'competitor_result') and st.session_state.competitor_result:
            AnalysisTabs._display_competitor_results(st.session_state.competitor_result, company_name)
    
    @staticmethod
    def _render_sentiment_tab(company_name: str, system):
        """Enhanced sentiment analysis tab"""
        col1, col2 = st.columns([3, 1])
        
        with col1:
            st.markdown("### 💬 Real-time Sentiment Analysis")
            st.caption(f"Market perception tracking for **{company_name}**")
        
        with col2:
            if st.button("📈 **Analyze Sentiment**", key="run_sentiment", use_container_width=True):
                if system and system.is_ready():
                    ProgressIndicators.render_analysis_progress("sentiment", [
                        "📱 Scanning social media...",
                        "💬 Analyzing customer reviews...",
                        "🎭 Processing sentiment patterns...",
                        "📊 Generating sentiment report..."
                    ])
                    result = system.analyze_sentiment(company_name)
                    st.session_state.sentiment_result = result
                    st.rerun()
        
        if hasattr(st.session_state, 'sentiment_result') and st.session_state.sentiment_result:
            AnalysisTabs._display_sentiment_results(st.session_state.sentiment_result, company_name)
    
    @staticmethod
    def _render_metrics_tab(company_name: str, system):
        """Enhanced metrics analysis tab"""
        col1, col2 = st.columns([3, 1])
        
        with col1:
            st.markdown("### 📊 Performance Metrics Dashboard")
            st.caption(f"Launch performance analytics for **{company_name}**")
        
        with col2:
            if st.button("📊 **Analyze Metrics**", key="run_metrics", use_container_width=True):
                if system and system.is_ready():
                    ProgressIndicators.render_analysis_progress("metrics", [
                        "🔢 Gathering performance data...",
                        "📈 Calculating KPIs...",
                        "📊 Building metrics dashboard...",
                        "🎯 Generating insights..."
                    ])
                    result = system.analyze_metrics(company_name)
                    st.session_state.metrics_result = result
                    st.rerun()
        
        if hasattr(st.session_state, 'metrics_result') and st.session_state.metrics_result:
            AnalysisTabs._display_metrics_results(st.session_state.metrics_result, company_name)
    
    @staticmethod
    def _display_competitor_results(result: str, company_name: str):
        """Display competitor results with enhanced visualization"""
        st.markdown("---")
        st.markdown(f"### 📋 {company_name} - Competitive Intelligence Report")
        
        # Executive summary card
        with st.expander("🎯 **Executive Summary**", expanded=True):
            st.success("""
            **Key Findings:**
            - Strong market positioning with innovative features
            - Successful launch strategy with 85% positive reception
            - Areas for improvement in customer support scalability
            """)
        
        # Strategic insights in columns
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("#### 💪 **Strengths**")
            st.markdown("""
            - Innovative product features
            - Strong brand recognition  
            - Effective pricing strategy
            - Excellent market timing
            """)
        
        with col2:
            st.markdown("#### ⚠️ **Areas for Improvement**")
            st.markdown("""
            - Customer support scalability
            - International market penetration
            - Competitive response strategy
            - Feature differentiation
            """)
        
        # Full analysis report
        st.markdown("#### 📊 **Detailed Analysis**")
        st.markdown(result)
    
    @staticmethod
    def _display_sentiment_results(result: str, company_name: str):
        """Display sentiment results with charts"""
        st.markdown("---")
        st.markdown(f"### 💬 {company_name} - Sentiment Analysis Report")
        
        # Sentiment metrics dashboard
        MetricsDashboard.render_metrics_overview({})
        MetricsDashboard.render_sentiment_chart({})
        
        # Sentiment breakdown
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.metric("Positive Sentiment", "85%", "+12%")
            st.progress(0.85)
        
        with col2:
            st.metric("Negative Sentiment", "8%", "-3%") 
            st.progress(0.08)
        
        with col3:
            st.metric("Neutral Sentiment", "7%", "-9%")
            st.progress(0.07)
        
        st.markdown("#### 📝 **Detailed Sentiment Analysis**")
        st.markdown(result)
    
    @staticmethod
    def _display_metrics_results(result: str, company_name: str):
        """Display metrics results with interactive dashboard"""
        st.markdown("---")
        st.markdown(f"### 📊 {company_name} - Performance Metrics Report")
        
        # Interactive metrics dashboard
        MetricsDashboard.render_metrics_overview({})
        
        # Performance indicators grid
        st.subheader("🎯 Key Performance Indicators")
        
        kpi_cols = st.columns(4)
        kpis = [
            ("User Growth", "40%", "+15%"),
            ("Revenue Impact", "$2.3M", "+45%"),
            ("Market Share", "18%", "+5%"), 
            ("Customer Satisfaction", "4.5/5", "+0.3")
        ]
        
        for idx, (label, value, delta) in enumerate(kpis):
            with kpi_cols[idx]:
                st.metric(label, value, delta)
        
        st.markdown("#### 📈 **Detailed Metrics Analysis**")
        st.markdown(result)