# ui/layouts/main_layout.py
import streamlit as st
from ui.components.header import Header
from ui.themes.streamlit_styles import get_css_styles
from ui.layouts.responsive import ResponsiveLayout
from ui.components.animated_shapes import AnimatedShapes
from ui.utils.animations import Animations

class MainLayout:
    def __init__(self):
        self._apply_styles()
        self._apply_responsive_design()
        self._setup_page_config()
    
    def _setup_page_config(self):
        """Configure the page settings"""
        st.set_page_config(
            layout="wide",
            initial_sidebar_state="collapsed",
            page_title="Product Intelligence Hub",
            page_icon="🚀"
        )
    
    def _apply_styles(self):
        """Apply custom CSS styles"""
        st.markdown(get_css_styles(), unsafe_allow_html=True)
    
    def _apply_responsive_design(self):
        """Apply responsive design elements"""
        ResponsiveLayout.apply_responsive_design()
    
    def render_hero_section(self):
        """Render the modern hero section with animations"""
        st.markdown("""
        <div class="hero-section">
            <div class="hero-content">
                <div class="hero-badge">
                    <span class="badge-dot"></span>
                    <span class="badge-text">Product Intelligence Hub</span>
                </div>
                <div class="hero-title-container">
                    <h1 class="hero-title gradient-text">Elevate Your Launch Strategy</h1>
                </div>
                <p class="hero-description">
                    Transform scattered market data into actionable intelligence with our AI-powered analysis suite.
                </p>
            </div>
            <div class="hero-shape"></div>
        </div>
        """, unsafe_allow_html=True)
        
        # Add the animated floating shapes
        AnimatedShapes.render()
    
    def render(self, company_name: str = ""):
        """Render the main application layout"""
        # Add main container with modern styling
        st.markdown('<div class="app-container">', unsafe_allow_html=True)
        
        # Render the hero section
        self.render_hero_section()
        
        # Main content container
        st.markdown('<div class="content-container">', unsafe_allow_html=True)
        
        # Company-specific content if provided
        if company_name:
            Header.render_company_header(company_name)
        
        st.markdown('</div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
        
        return self