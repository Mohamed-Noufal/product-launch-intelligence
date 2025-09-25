# ui/utils/animations.py
import streamlit as st
import time
import random

class Animations:
    @staticmethod
    def typewriter_effect(text: str, speed: float = 0.03):
        """Create modern typewriter effect with cursor animation"""
        placeholder = st.empty()
        current_text = ""
        cursor_styles = ["│", ""]  # Blinking cursor
        
        st.markdown("""
        <style>
        @keyframes blink {
            0%, 100% { opacity: 1; }
            50% { opacity: 0; }
        }
        .cursor {
            animation: blink 1s infinite;
        }
        .typewriter {
            font-family: 'Courier New', monospace;
            padding: 1rem;
            background: rgba(0,0,0,0.05);
            border-radius: 8px;
        }
        </style>
        """, unsafe_allow_html=True)
        
        for char in text:
            current_text += char
            placeholder.markdown(f'<div class="typewriter">{current_text}<span class="cursor">│</span></div>', unsafe_allow_html=True)
            time.sleep(speed)
        
        placeholder.markdown(f'<div class="typewriter">{text}</div>', unsafe_allow_html=True)
    
    @staticmethod
    def loading_animation(duration: int = 3):
        """Show modern loading animation with gradient"""
        placeholder = st.empty()
        
        css = """
        <style>
        @keyframes gradient {
            0% { background-position: 0% 50%; }
            50% { background-position: 100% 50%; }
            100% { background-position: 0% 50%; }
        }
        .loading-bar {
            height: 4px;
            background: linear-gradient(90deg, #4F46E5, #7C3AED, #DB2777, #4F46E5);
            background-size: 300% 100%;
            animation: gradient 2s ease infinite;
            border-radius: 2px;
            margin: 1rem 0;
        }
        .loading-text {
            color: #6B7280;
            font-size: 0.875rem;
            text-align: center;
            margin-top: 0.5rem;
        }
        </style>
        <div class="loading-bar"></div>
        <div class="loading-text">Processing your request...</div>
        """
        
        placeholder.markdown(css, unsafe_allow_html=True)
        time.sleep(duration)
        placeholder.empty()
    
    @staticmethod
    def pulse_animation(element_class: str = "pulse-element"):
        """Create smooth pulse animation for elements"""
        css = """
        <style>
        @keyframes pulse {
            0% { transform: scale(1); box-shadow: 0 0 0 0 rgba(79, 70, 229, 0.4); }
            70% { transform: scale(1.05); box-shadow: 0 0 0 10px rgba(79, 70, 229, 0); }
            100% { transform: scale(1); box-shadow: 0 0 0 0 rgba(79, 70, 229, 0); }
        }
        .%s {
            animation: pulse 2s cubic-bezier(0.4, 0, 0.6, 1) infinite;
        }
        </style>
        """ % element_class
        st.markdown(css, unsafe_allow_html=True)
        return element_class
    
    @staticmethod
    def success_animation():
        """Show modern success animation"""
        success_placeholder = st.empty()
        
        css = """
        <style>
        @keyframes checkmark {
            0% { transform: scale(0); opacity: 0; }
            50% { transform: scale(1.2); opacity: 0.8; }
            100% { transform: scale(1); opacity: 1; }
        }
        .success-icon {
            display: flex;
            justify-content: center;
            align-items: center;
            width: 80px;
            height: 80px;
            margin: 0 auto;
            background: linear-gradient(135deg, #4F46E5, #10B981);
            border-radius: 50%;
            animation: checkmark 0.5s cubic-bezier(0.4, 0, 0.2, 1);
        }
        .success-icon svg {
            width: 40px;
            height: 40px;
            color: white;
        }
        </style>
        <div class="success-icon">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                <path d="M20 6L9 17l-5-5" stroke="white" stroke-linecap="round" stroke-linejoin="round"/>
            </svg>
        </div>
        """
        
        success_placeholder.markdown(css, unsafe_allow_html=True)
        time.sleep(2)
        success_placeholder.empty()
    
    @staticmethod
    def countup_animation(final_value: int, duration: int = 2, prefix: str = "", label: str = "Progress"):
        """Animate counting up with smooth easing"""
        placeholder = st.empty()
        steps = 50  # More steps for smoother animation
        
        css = """
        <style>
        .metric-container {
            padding: 1rem;
            background: white;
            border-radius: 12px;
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.05);
            text-align: center;
        }
        .metric-value {
            font-size: 2.5rem;
            font-weight: 600;
            color: #4F46E5;
            margin: 0.5rem 0;
        }
        .metric-label {
            color: #6B7280;
            font-size: 0.875rem;
        }
        </style>
        """
        
        st.markdown(css, unsafe_allow_html=True)
        
        import math
        for i in range(steps + 1):
            # Use easing function for smoother animation
            progress = i / steps
            ease = -(math.cos(math.pi * progress) - 1) / 2
            current_value = int(final_value * ease)
            
            placeholder.markdown(f"""
            <div class="metric-container">
                <div class="metric-label">{label}</div>
                <div class="metric-value">{prefix}{current_value}</div>
            </div>
            """, unsafe_allow_html=True)
            
            time.sleep(duration / steps)
            
        # Final value
        placeholder.markdown(f"""
        <div class="metric-container">
            <div class="metric-label">{label}</div>
            <div class="metric-value">{prefix}{final_value}</div>
        </div>
        """, unsafe_allow_html=True)