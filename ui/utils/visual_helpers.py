# ui/utils/visual_helpers.py
import requests
from PIL import Image, ImageDraw, ImageFont
import io
import streamlit as st
import random

class VisualHelpers:
    @staticmethod
    def get_company_logo(company_name: str, size: int = 100):
        """Fetch or generate company logo"""
        try:
            # Try Clearbit API
            logo_url = f"https://logo.clearbit.com/{company_name.lower().replace(' ', '')}.com"
            response = requests.get(logo_url, timeout=5)
            
            if response.status_code == 200:
                image = Image.open(io.BytesIO(response.content))
                return image.resize((size, size))
        except:
            pass
        
        # Fallback to generated avatar
        return VisualHelpers._generate_avatar(company_name, size)
    
    @staticmethod
    def _generate_avatar(company_name: str, size: int = 100):
        """Generate a colorful avatar with company initial"""
        colors = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#96CEB4', '#FFEAA7', '#DDA0DD']
        color = colors[hash(company_name) % len(colors)]
        
        img = Image.new('RGB', (size, size), color)
        draw = ImageDraw.Draw(img)
        
        try:
            font = ImageFont.truetype("arial.ttf", size//2)
        except:
            font = ImageFont.load_default()
        
        text = company_name[0].upper()
        bbox = draw.textbbox((0, 0), text, font=font)
        text_width = bbox[2] - bbox[0]
        text_height = bbox[3] - bbox[1]
        
        position = ((size - text_width) // 2, (size - text_height) // 2)
        draw.text(position, text, fill="white", font=font)
        
        return img
    
    @staticmethod
    def create_metric_card(title: str, value: str, delta: str, color: str):
        """Create a beautiful metric card"""
        return f"""
        <div style='
            background: {color}15;
            padding: 1.5rem;
            border-radius: 12px;
            border-left: 4px solid {color};
            text-align: center;
            margin: 0.5rem;
            transition: transform 0.2s;
        ' onmouseover="this.style.transform='scale(1.05)'" onmouseout="this.style.transform='scale(1)'">
            <h4 style='margin: 0 0 0.5rem 0; color: #666;'>{title}</h4>
            <h2 style='margin: 0; color: {color};'>{value}</h2>
            <small style='color: #888;'>{delta}</small>
        </div>
        """
    
    @staticmethod
    def create_progress_bar(percentage: int, color: str, height: int = 20):
        """Create custom progress bar"""
        return f"""
        <div style='
            width: 100%;
            background: #f0f0f0;
            border-radius: 10px;
            overflow: hidden;
            height: {height}px;
            margin: 0.5rem 0;
        '>
            <div style='
                width: {percentage}%;
                background: {color};
                height: 100%;
                border-radius: 10px;
                transition: width 0.5s ease-in-out;
                display: flex;
                align-items: center;
                justify-content: center;
                color: white;
                font-weight: bold;
                font-size: 0.8em;
            '>{percentage}%</div>
        </div>
        """
    
    @staticmethod
    def create_info_box(message: str, message_type: str = "info"):
        """Create styled info/alert boxes"""
        colors = {
            "info": ("#45B7D1", "ℹ️"),
            "success": ("#4ECDC4", "✅"), 
            "warning": ("#FFEAA7", "⚠️"),
            "error": ("#FF6B6B", "❌")
        }
        
        color, icon = colors.get(message_type, colors["info"])
        
        return f"""
        <div style='
            background: {color}20;
            border-left: 4px solid {color};
            padding: 1rem;
            border-radius: 8px;
            margin: 1rem 0;
        '>
            <div style='display: flex; align-items: center;'>
                <span style='font-size: 1.2em; margin-right: 0.5rem;'>{icon}</span>
                <span>{message}</span>
            </div>
        </div>
        """