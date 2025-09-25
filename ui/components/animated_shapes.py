import streamlit as st

class AnimatedShapes:
    @staticmethod
    def render():
        # Add the floating shapes animation CSS
        st.markdown("""
        <style>
        @keyframes float {
            0% { transform: translateY(0px) rotate(0deg); }
            50% { transform: translateY(-20px) rotate(5deg); }
            100% { transform: translateY(0px) rotate(0deg); }
        }
        
        .shape {
            position: absolute;
            border-radius: 50%;
            backdrop-filter: blur(8px);
            -webkit-backdrop-filter: blur(8px);
            animation: float 12s infinite ease-in-out;
            box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.2);
            border: 1px solid rgba(255, 255, 255, 0.18);
            background: linear-gradient(45deg, rgba(255,255,255,0.1), rgba(255,255,255,0.05));
        }
        
        .shape-1 {
            width: 600px;
            height: 140px;
            left: -5%;
            top: 20%;
            transform: rotate(12deg);
            animation-delay: 0.3s;
            background: linear-gradient(45deg, rgba(79, 70, 229, 0.15), transparent);
        }
        
        .shape-2 {
            width: 500px;
            height: 120px;
            right: 0%;
            top: 75%;
            transform: rotate(-15deg);
            animation-delay: 0.5s;
            background: linear-gradient(45deg, rgba(219, 39, 119, 0.15), transparent);
        }
        
        .shape-3 {
            width: 300px;
            height: 80px;
            left: 10%;
            bottom: 10%;
            transform: rotate(-8deg);
            animation-delay: 0.4s;
            background: linear-gradient(45deg, rgba(139, 92, 246, 0.15), transparent);
        }
        
        .shape-4 {
            width: 200px;
            height: 60px;
            right: 20%;
            top: 15%;
            transform: rotate(20deg);
            animation-delay: 0.6s;
            background: linear-gradient(45deg, rgba(245, 158, 11, 0.15), transparent);
        }
        
        .shape-5 {
            width: 150px;
            height: 40px;
            left: 25%;
            top: 10%;
            transform: rotate(-25deg);
            animation-delay: 0.7s;
            background: linear-gradient(45deg, rgba(6, 182, 212, 0.15), transparent);
        }

        .shape::after {
            content: '';
            position: absolute;
            inset: 0;
            border-radius: 50%;
            background: radial-gradient(circle at 50% 50%, rgba(255,255,255,0.2), transparent 70%);
        }
        </style>
        
        <div class="shape shape-1"></div>
        <div class="shape shape-2"></div>
        <div class="shape shape-3"></div>
        <div class="shape shape-4"></div>
        <div class="shape shape-5"></div>
        """, unsafe_allow_html=True)
