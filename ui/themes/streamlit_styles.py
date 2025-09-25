# ui/themes/streamlit_styles.py
def get_css_styles():
    return '''
        <style>
            /* Global Styles */
            div.appview-container {
                background: #0A0A0F;
                color: #E5E7EB;
                font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
            }
            
            div.block-container {
                padding: 0;
                max-width: 100%;
            }

            /* Sidebar Styling */
            section[data-testid="stSidebar"] {
                background: rgba(15, 15, 20, 0.8);
                backdrop-filter: blur(10px);
            }
            
            /* Hero Section */
            .hero-section {
                position: relative;
                background: linear-gradient(110deg, rgba(79, 70, 229, 0.15) 0%, rgba(124, 58, 237, 0.15) 50%, rgba(219, 39, 119, 0.15) 100%);
                padding: 6rem 2rem;
                text-align: center;
                overflow: hidden;
                border-bottom: 1px solid rgba(255, 255, 255, 0.05);
                animation: fadeIn 1s ease-out;
            }

            .hero-section::before {
                content: '';
                position: absolute;
                top: 0;
                left: 0;
                right: 0;
                bottom: 0;
                background: radial-gradient(circle at 50% 50%, rgba(79, 70, 229, 0.1), transparent 70%);
                z-index: 0;
            }

            .hero-content {
                position: relative;
                z-index: 1;
                max-width: 800px;
                margin: 0 auto;
                animation: fadeIn 1.2s ease-out 0.3s backwards;
            }
            
            .hero-badge {
                display: inline-flex;
                align-items: center;
                gap: 0.75rem;
                background: rgba(255, 255, 255, 0.03);
                padding: 0.625rem 1.25rem;
                border-radius: 100px;
                margin-bottom: 2.5rem;
                border: 1px solid rgba(255, 255, 255, 0.05);
                box-shadow: 0 4px 20px rgba(0, 0, 0, 0.1);
                backdrop-filter: blur(10px);
                animation: float 4s ease-in-out infinite;
            }
            
            .badge-dot {
                width: 8px;
                height: 8px;
                background: linear-gradient(135deg, #F87171, #DB2777);
                border-radius: 50%;
                box-shadow: 0 0 10px rgba(219, 39, 119, 0.5);
                animation: pulse 2s infinite;
            }
            
            .badge-text {
                color: rgba(255, 255, 255, 0.9);
                font-size: 0.875rem;
                font-weight: 500;
                letter-spacing: 0.025em;
            }
            
            .hero-title {
                font-size: 4.5rem;
                font-weight: 800;
                letter-spacing: -0.02em;
                margin-bottom: 2rem;
                line-height: 1.1;
                background: linear-gradient(135deg, #fff 0%, rgba(255, 255, 255, 0.9) 100%);
                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
                animation: fadeIn 1s ease-out;
            }

            @keyframes pulse {
                0% { transform: scale(1); opacity: 1; }
                50% { transform: scale(1.2); opacity: 0.8; }
                100% { transform: scale(1); opacity: 1; }
            }
            
            .hero-subtitle {
                font-size: 1.25rem;
                color: rgba(255, 255, 255, 0.7);
                max-width: 600px;
                margin: 0 auto;
            }
            
            /* Cards */
            div.element-container div.stButton > button {
                width: 100%;
                background: linear-gradient(135deg, #4F46E5 0%, #7C3AED 100%);
                color: white;
                border: none;
                padding: 0.75rem 1.5rem;
                border-radius: 12px;
                transition: all 0.3s ease;
                animation: glow 3s ease-in-out infinite;
            }
            
            div.element-container div.stButton > button:hover {
                transform: translateY(-2px);
                box-shadow: 0 8px 24px rgba(79, 70, 229, 0.3);
            }
            
            /* Tabs */
            .stTabs [data-baseweb="tab-list"] {
                gap: 2rem;
                background-color: transparent;
            }
            
            .stTabs [data-baseweb="tab"] {
                height: 50px;
                padding: 0 24px;
                color: rgba(255, 255, 255, 0.7);
                border-radius: 12px;
            }
            
            .stTabs [data-baseweb="tab"]:hover {
                color: white;
                background: rgba(79, 70, 229, 0.1);
            }
            
            .stTabs [aria-selected="true"] {
                color: white !important;
                background: rgba(79, 70, 229, 0.2) !important;
            }
            
            /* Form Inputs */
            /* Input Fields */
            div.stTextInput > div > div > input {
                background: rgba(255, 255, 255, 0.03);
                border: 1px solid rgba(255, 255, 255, 0.05);
                border-radius: 16px;
                color: white;
                padding: 1.25rem;
                font-size: 1rem;
                backdrop-filter: blur(10px);
                transition: all 0.3s ease;
            }
            
            div.stTextInput > div > div > input:focus {
                border-color: rgba(79, 70, 229, 0.5);
                box-shadow: 0 0 0 4px rgba(79, 70, 229, 0.15);
                background: rgba(255, 255, 255, 0.05);
            }

            div.stTextInput > div > div > input::placeholder {
                color: rgba(255, 255, 255, 0.4);
            }

            /* Status Cards */
            div[data-testid="stExpander"] {
                background: rgba(255, 255, 255, 0.02);
                border: 1px solid rgba(255, 255, 255, 0.05);
                border-radius: 20px;
                overflow: hidden;
                backdrop-filter: blur(10px);
                animation: fadeIn 0.8s ease-out;
            }

            .agent-status {
                display: flex;
                align-items: center;
                gap: 1rem;
                padding: 1rem;
                border-radius: 16px;
                background: rgba(255, 255, 255, 0.02);
                border: 1px solid rgba(255, 255, 255, 0.05);
                margin: 0.5rem 0;
            }

            .status-online {
                color: #34D399;
                text-shadow: 0 0 10px rgba(52, 211, 153, 0.5);
            }

            .status-offline {
                color: #F87171;
                text-shadow: 0 0 10px rgba(248, 113, 113, 0.5);
            }
            
            /* Animations */
            @keyframes fadeUp {
                from {
                    opacity: 0;
                    transform: translateY(20px);
                }
                to {
                    opacity: 1;
                    transform: translateY(0);
                }
            }
            
            .fade-up {
                animation: fadeUp 0.6s ease-out forwards;
            }
            
            /* Animations */
            @keyframes fadeIn {
                from { opacity: 0; transform: translateY(20px); }
                to { opacity: 1; transform: translateY(0); }
            }

            @keyframes float {
                0% { transform: translateY(0px); }
                50% { transform: translateY(-10px); }
                100% { transform: translateY(0px); }
            }

            @keyframes glow {
                0% { box-shadow: 0 0 20px rgba(79, 70, 229, 0.3); }
                50% { box-shadow: 0 0 30px rgba(79, 70, 229, 0.5); }
                100% { box-shadow: 0 0 20px rgba(79, 70, 229, 0.3); }
            }

            /* Responsive Design */
            @media (max-width: 768px) {
                .hero-section {
                    padding: 4rem 1rem;
                }

                .hero-title {
                    font-size: 2.75rem;
                }
                
                .hero-description {
                    font-size: 1rem;
                    padding: 0 1rem;
                }

                .hero-badge {
                    padding: 0.5rem 1rem;
                    margin-bottom: 2rem;
                }
            }

            /* Custom Scrollbar */
            ::-webkit-scrollbar {
                width: 8px;
                height: 8px;
            }

            ::-webkit-scrollbar-track {
                background: rgba(255, 255, 255, 0.05);
            }

            ::-webkit-scrollbar-thumb {
                background: rgba(255, 255, 255, 0.1);
                border-radius: 4px;
            }

            ::-webkit-scrollbar-thumb:hover {
                background: rgba(255, 255, 255, 0.2);
            }
        </style>
    '''
