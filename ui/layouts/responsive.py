import streamlit as st

class ResponsiveLayout:
    """Handles responsive design elements for the application"""
    
    @staticmethod
    def apply_responsive_design():
        """Apply responsive design elements and layout configurations"""
        # Set wide mode
        st.markdown("""
            <style>
                .main-container {
                    padding: 1rem;
                    max-width: 1200px;
                    margin: 0 auto;
                }
                
                /* Responsive grid adjustments */
                @media (max-width: 768px) {
                    .main-container {
                        padding: 0.5rem;
                    }
                }
                
                /* Improved spacing and readability */
                .block-container {
                    padding-top: 1rem;
                    padding-bottom: 1rem;
                }
                
                /* Better mobile layout */
                @media (max-width: 640px) {
                    .stMarkdown {
                        font-size: 14px;
                    }
                }
            </style>
        """, unsafe_allow_html=True)