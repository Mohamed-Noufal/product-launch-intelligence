# ui/themes/colors.py
class ColorScheme:
    # Modern 2025 Color Palette
    PRIMARY = "#667eea"        # Soft Blue
    SECONDARY = "#764ba2"      # Muted Purple  
    BACKGROUND = "#f8f9fa"     # Warm Off-White
    CARD_BG = "#ffffff"        # Pure White
    TEXT = "#2d3748"           # Dark Charcoal
    ACCENT = "#4ECDC4"         # Soft Teal
    
    # Gradients
    HEADER_GRADIENT = "linear-gradient(135deg, #667eea 0%, #764ba2 100%)"
    CARD_GRADIENT = "linear-gradient(135deg, #f093fb 0%, #f5576c 100%)"
    
    # Agent specific colors
    AGENT_COLORS = {
        "launch": "#667eea",
        "sentiment": "#764ba2", 
        "metrics": "#4ECDC4"
    }

class Theme:
    DARK = {
        "bg_primary": "#0f1419",
        "bg_secondary": "#1e2328", 
        "text_primary": "#ffffff"
    }
    
    LIGHT = {
        "bg_primary": "#f8f9fa",
        "bg_secondary": "#ffffff",
        "text_primary": "#2d3748"
    }