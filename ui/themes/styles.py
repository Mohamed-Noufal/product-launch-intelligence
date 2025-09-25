# ui/themes/styles.py
def get_css_styles():
    """Return a small, safe CSS string for Streamlit injection."""
    return """
    <style>
    .appview-container { background-color: #030303; }
    .block-container { padding-top: 0; max-width: 100%; }
    .hero-title { font-size: 2.2rem; font-weight: 700; color: #fff; }
    .hero-description { color: rgba(255,255,255,0.7); }
    .agent-card { border-radius: 12px; background: rgba(255,255,255,0.02); padding: 1rem; }
    .stButton button { background: linear-gradient(135deg,#4F46E5,#7C3AED); color:#fff; }
    </style>
    """