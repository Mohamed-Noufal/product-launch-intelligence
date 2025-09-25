# ui/components/sidebar.py
import streamlit as st
import os
from ui.themes.colors import ColorScheme

class Sidebar:
    @staticmethod
    def render():
        """Render enhanced sidebar with system status and controls"""
        with st.sidebar:
            # Header with logo
            st.markdown(f"""
            <div style='
                background: {ColorScheme.HEADER_GRADIENT};
                padding: 1.5rem;
                border-radius: 10px;
                color: white;
                text-align: center;
                margin-bottom: 1rem;
            '>
                <h2 style='margin: 0;'>🤖 AI Agents</h2>
                <p style='margin: 0; opacity: 0.9;'>System Status</p>
            </div>
            """, unsafe_allow_html=True)
            
            # API Configuration - CAPTURE THE RETURN VALUES
            google_key, firecrawl_key = Sidebar._render_api_config()
            
            # System Status
            Sidebar._render_system_status()
            
            # Quick Actions
            Sidebar._render_quick_actions()
            
            # Analysis History
            Sidebar._render_analysis_history()
            
            # RETURN THE API KEYS TO app.py
            return google_key, firecrawl_key  # ← ADD THIS LINE
    
    @staticmethod
    def _render_api_config():
        """Render API configuration section"""
        with st.expander("🔑 **API Configuration**", expanded=True):
            google_key = st.text_input(
                "Google AI Key",
                type="password",
                value=os.getenv("GOOGLE_API_KEY", ""),
                help="Required for AI analysis"
            )
            
            firecrawl_key = st.text_input(
                "Firecrawl Key", 
                type="password",
                value=os.getenv("FIRECRAWL_API_KEY", ""),
                help="Required for web data"
            )
            
            if google_key and firecrawl_key:
                st.success("✅ APIs Configured")
            else:
                st.warning("⚠️ Configure APIs")
            
            return google_key, firecrawl_key


    @staticmethod
    def _render_report_download(company_name: str):
        """Render report download options"""
        if not company_name:
            return
        
        st.markdown("### 📥 Export Reports")
        
        col1, col2 = st.columns(2)
        
        with col1:
            if st.button("📄 HTML Report", use_container_width=True):
                # This will be connected to your report generator
                st.session_state.generate_report = True
        
        with col2:
            if st.button("📊 Executive Summary", use_container_width=True):
                st.session_state.generate_summary = True
        
        
    # ... rest of your methods remain the same ...
    @staticmethod
    def _render_system_status():
        """Render system and agent status"""
        st.markdown("### 📊 System Status")
        
        # Agent status indicators
        agents = [
            ("🎯", "Launch Analyst", "Online", "#4ECDC4"),
            ("💬", "Sentiment Specialist", "Online", "#45B7D1"),
            ("📊", "Metrics Analyst", "Online", "#FF6B6B")
        ]
        
        for icon, name, status, color in agents:
            st.markdown(f"""
            <div style='
                display: flex;
                align-items: center;
                justify-content: space-between;
                padding: 0.5rem;
                background: {color}15;
                border-radius: 8px;
                margin: 0.3rem 0;
                border-left: 3px solid {color};
            '>
                <div style='display: flex; align-items: center;'>
                    <span style='font-size: 1.2em; margin-right: 0.5rem;'>{icon}</span>
                    <span><strong>{name}</strong></span>
                </div>
                <span style='
                    background: {color};
                    color: white;
                    padding: 0.2rem 0.5rem;
                    border-radius: 12px;
                    font-size: 0.8em;
                '>{status}</span>
            </div>
            """, unsafe_allow_html=True)
    

    @staticmethod
    def _render_report_download(company_name: str):
        """Render report download options"""
        if not company_name:
            return
        
        st.markdown("### 📥 Export Reports")
        
        col1, col2 = st.columns(2)
        
        with col1:
            if st.button("📄 HTML Report", use_container_width=True):
                # This will be connected to your report generator
                st.session_state.generate_report = True
        
        with col2:
            if st.button("📊 Executive Summary", use_container_width=True):
                st.session_state.generate_summary = True
    
    @staticmethod
    def _render_quick_actions():
        """Render quick action buttons"""
        st.markdown("### ⚡ Quick Actions")
        
        if st.button("🔄 **Refresh All Data**", use_container_width=True):
            st.rerun()
            
        if st.button("📥 **Export Report**", use_container_width=True):
            st.success("Report exported successfully!")
            
        if st.button("🛠️ **Debug Mode**", use_container_width=True):
            st.session_state.debug_mode = not st.session_state.get('debug_mode', False)
    
    @staticmethod
    def _render_analysis_history():
        """Render recent analysis history"""
        if hasattr(st.session_state, 'analysis_history') and st.session_state.analysis_history:
            st.markdown("### 📚 Recent Analysis")
            
            for company, timestamp in st.session_state.analysis_history[-3:]:
                st.markdown(f"""
                <div style='
                    padding: 0.5rem;
                    background: #f8f9fa;
                    border-radius: 6px;
                    margin: 0.2rem 0;
                    font-size: 0.9em;
                '>
                    <strong>{company}</strong><br>
                    <small>{timestamp}</small>
                </div>
                """, unsafe_allow_html=True)