# ui/components/header.py
import streamlit as st
from ui.themes.colors import ColorScheme

class Header:
    @staticmethod
    def render_main_header():
        st.markdown(f"""
        <div class="main-header">
            <h1 style="margin:0; font-size: 2.8em; font-weight: 300;">🚀 Product Intelligence Platform</h1>
            <p style="margin:0; opacity: 0.9; font-size: 1.2em;">AI-Powered Market Analysis</p>
        </div>
        """, unsafe_allow_html=True)
    
    @staticmethod
    def render_company_header(company_name: str):
        if company_name:
            st.markdown(f"""
            <div style='
                background: {ColorScheme.CARD_BG};
                padding: 1.5rem;
                border-radius: 12px;
                border-left: 4px solid {ColorScheme.SECONDARY};
                margin: 1rem 0;
                box-shadow: 0 2px 8px rgba(0,0,0,0.05);
            '>
                <h2 style="margin: 0; color: {ColorScheme.TEXT};">
                    🔍 Analyzing: <span style="color: {ColorScheme.PRIMARY};">{company_name}</span>
                </h2>
            </div>
            """, unsafe_allow_html=True)