# app.py (Complete orchestrator with all enhancements)
import streamlit as st
from dotenv import load_dotenv
import os
import time

# Import UI components
from ui.layouts.main_layout import MainLayout
from ui.components.agent_cards import AgentCards
from ui.components.analysis_tabs import AnalysisTabs
from ui.components.sidebar import Sidebar
from ui.components.results_display import ResultsDisplay
from ui.utils.visual_helpers import VisualHelpers
from ui.components.report_generator import ReportGenerator

# Import business logic
from agents.team_coordinator import TeamCoordinator

class ProductIntelligenceApp:
    def __init__(self):
        self.system = None
        self._initialize_session_state()

    def animated_analysis_trigger(self, company_name: str):
        """Smooth animation for analysis initiation"""
        if st.button(f"🔍 Analyze {company_name}", type="primary", use_container_width=True):
            with st.spinner("🤖 AI agents are gathering intelligence..."):
                # Smooth progress animation
                progress_bar = st.progress(0)
                for percent in range(100):
                    time.sleep(0.02)
                    progress_bar.progress(percent + 1)
                
                st.success("✅ Analysis complete!")
                st.balloons()  # Celebration effect
        
    def _initialize_session_state(self):
        """Initialize all session state variables"""
        # Analysis results
        if "competitor_result" not in st.session_state:
            st.session_state.competitor_result = None
        if "sentiment_result" not in st.session_state:
            st.session_state.sentiment_result = None
        if "metrics_result" not in st.session_state:
            st.session_state.metrics_result = None
        
        # Report caching
        if "report_cache_pdf" not in st.session_state:
            st.session_state.report_cache_pdf = None
        if "report_cache_html" not in st.session_state:
            st.session_state.report_cache_html = None
        if "last_report_company" not in st.session_state:
            st.session_state.last_report_company = None
        
        # App state
        if "company_name" not in st.session_state:
            st.session_state.company_name = ""
        if "api_keys_configured" not in st.session_state:
            st.session_state.api_keys_configured = False
        if "analysis_history" not in st.session_state:
            st.session_state.analysis_history = []
        if "analysis_in_progress" not in st.session_state:
            st.session_state.analysis_in_progress = False
    
    def _initialize_system(self, google_key: str, firecrawl_key: str):
        """Initialize the multi-agent system"""
        try:
            if not self.system or not self.system.is_ready():
                self.system = TeamCoordinator(google_key, firecrawl_key)
                st.session_state.api_keys_configured = True
                return True
            return True
        except Exception as e:
            st.error(f"❌ Failed to initialize system: {e}")
            return False
    
    def _add_to_history(self, company_name: str):
        """Add analysis to history"""
        from datetime import datetime
        analysis_entry = (company_name, datetime.now().strftime("%Y-%m-%d %H:%M"))
        st.session_state.analysis_history.append(analysis_entry)
        # Keep only last 5 entries
        st.session_state.analysis_history = st.session_state.analysis_history[-5:]
    
    def render_company_input(self):
        """Render enhanced company input section with better placement"""
        st.markdown("---")

        # Center the input field
        st.markdown(
            """
            <div style='text-align: center;'>
                <h2>🏢 Enter Company Name to Analyze</h2>
            </div>
            """,
            unsafe_allow_html=True
        )

        company_name = st.text_input(
            "",
            placeholder="e.g., OpenAI, Tesla, Netflix, Apple...",
            help="Enter the company you want competitive intelligence on",
            key="company_input_main",
            label_visibility="collapsed"
        )

        if company_name:
            st.session_state.company_name = company_name

        return company_name

    def render_main_dashboard(self, company_name: str):
        """Render the main analysis dashboard with full report generation"""
        if not company_name:
            self._render_welcome_state()
            return

        st.markdown("---")

        # Display agent team visualization
        st.markdown("### 🤖 Your AI Analysis Team")
        AgentCards.render_agent_grid()

        # Add the analyze button to trigger all agents
        st.markdown("---")
        if st.button("🔍 Analyze All", type="primary", use_container_width=True):
            try:
                st.session_state.analysis_in_progress = True
                progress_text = st.empty()
                progress_bar = st.progress(0)
                
                # Reset results
                st.session_state.competitor_result = None
                st.session_state.sentiment_result = None
                st.session_state.metrics_result = None
                
                # Run competitor analysis
                progress_text.text("🎯 Analyzing competitor data...")
                competitor_result = self.system.analyze_competitor(company_name)
                st.session_state.competitor_result = competitor_result
                progress_bar.progress(33)
                
                # Run sentiment analysis
                progress_text.text("💬 Analyzing market sentiment...")
                sentiment_result = self.system.analyze_sentiment(company_name)
                st.session_state.sentiment_result = sentiment_result
                progress_bar.progress(66)
                
                # Run metrics analysis
                progress_text.text("📊 Analyzing performance metrics...")
                metrics_result = self.system.analyze_metrics(company_name)
                st.session_state.metrics_result = metrics_result
                progress_bar.progress(100)
                
                progress_text.text("✅ Analysis complete! Generating reports...")
                
                # Clear caches when new analysis is done
                st.session_state.report_cache_pdf = None
                st.session_state.report_cache_html = None
                st.session_state.last_report_company = company_name
                
                st.success("✅ Full analysis complete!")
                st.balloons()
                
            except Exception as e:
                st.error(f"❌ Analysis failed: {str(e)}")
            finally:
                st.session_state.analysis_in_progress = False

        # Display analysis tabs
        AnalysisTabs.render(company_name, self.system)
        
        # ADD REPORT GENERATION SECTION - This is the key addition
        if (st.session_state.get('competitor_result') and 
            st.session_state.get('sentiment_result') and 
            st.session_state.get('metrics_result')):
            
            st.markdown("---")
            st.markdown("### 📊 Report Generation")
        
        # Render inline report download controls using the existing generate_report
        # and the lightweight UI ReportGenerator for raw text export.
        col1, col2, col3 = st.columns([1, 1, 1])
        with col1:
            if st.button("📥 Generate & Download PDF", key="download_pdf"):
                self.generate_report(company_name, report_type='pdf')

        with col2:
            if st.button("🌐 Generate & Download HTML", key="download_html"):
                self.generate_report(company_name, report_type='html')

        with col3:
            if st.button("🗒️ Download Raw Data (TXT)", key="download_raw"):
                # Use the UI ReportGenerator to build a simple raw text export
                raw = ReportGenerator._generate_raw_data(
                    company_name,
                    str(st.session_state.get('competitor_result')),
                    str(st.session_state.get('sentiment_result')),
                    str(st.session_state.get('metrics_result')),
                )
                st.download_button(
                    label="📥 Download Raw Data (TXT)",
                    data=raw,
                    file_name=f"{company_name}_raw_report.txt",
                    mime="text/plain",
                )

        # Update analysis history if we have results
        if any([st.session_state.get('competitor_result'), st.session_state.get('sentiment_result'), st.session_state.get('metrics_result')]):
            if company_name not in [entry[0] for entry in st.session_state.analysis_history]:
                self._add_to_history(company_name)
    
    # ...existing code...

    def _render_welcome_state(self):
        """Render welcome/initial state"""
        st.markdown("""
        <div style='
            background: linear-gradient(135deg, #667eea15 0%, #764ba215 100%);
            padding: 3rem;
            border-radius: 15px;
            text-align: center;
            margin: 2rem 0;
        '>
            <h1 style='color: #667eea;'>🚀 Welcome to Product Intelligence</h1>
            <p style='font-size: 1.2em; color: #666;'>
                Enter a company name above to get started with AI-powered competitive analysis.
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        # Feature highlights
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.markdown("""
            <div style='text-align: center; padding: 1rem;'>
                <div style='font-size: 2.5em;'>🎯</div>
                <h3>Competitor Analysis</h3>
                <p>Strategic positioning and launch evaluation</p>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            st.markdown("""
            <div style='text-align: center; padding: 1rem;'>
                <div style='font-size: 2.5em;'>💬</div>
                <h3>Market Sentiment</h3>
                <p>Customer perception and social analysis</p>
            </div>
            """, unsafe_allow_html=True)
        
        with col3:
            st.markdown("""
            <div style='text-align: center; padding: 1rem;'>
                <div style='font-size: 2.5em;'>📊</div>
                <h3>Launch Metrics</h3>
                <p>Performance KPIs and growth tracking</p>
            </div>
            """, unsafe_allow_html=True)
    
    def generate_report(self, company_name: str, report_type: str = 'pdf'):
        """Generate a formatted report and provide download options
        
        Args:
            company_name (str): Name of the company being analyzed
            report_type (str): Type of report to generate ('pdf' or 'html')
        """
        from services.report_generator import ReportGenerator
        
        # Ensure we have all the required data
        competitor_result = st.session_state.get("competitor_result")
        sentiment_result = st.session_state.get("sentiment_result")
        metrics_result = st.session_state.get("metrics_result")
        
        if not all([competitor_result, sentiment_result, metrics_result]):
            st.warning("⚠️ Please complete all analyses before generating a report.")
            return
        
        try:
            # Generate the report
            report_data = ReportGenerator.generate_comprehensive_report(
                company_name=company_name,
                competitor_analysis=competitor_result,
                sentiment_analysis=sentiment_result,
                metrics_analysis=metrics_result,
                report_type=report_type
            )
            
            # Create download button based on report type
            if report_type.lower() == 'pdf':
                try:
                    st.download_button(
                        label="📥 Download Report as PDF",
                        data=report_data,
                        file_name=f"{company_name}_analysis_report.pdf",
                        mime="application/pdf"
                    )
                except ModuleNotFoundError as e:
                    # Friendly fallback if reportlab is not installed in the venv
                    st.error("❌ Failed to generate PDF: missing dependency 'reportlab'.")
                    st.info("You can still download an HTML report. To enable PDF exports, run: `pip install reportlab` in your active virtualenv.")
                    # If report_data is None because PDF generation failed, request HTML instead
                    html_report = None
                    try:
                        from services.report_generator import ReportGenerator as RG
                        html_report = RG.generate_comprehensive_report(
                            company_name=company_name,
                            competitor_analysis=competitor_result,
                            sentiment_analysis=sentiment_result,
                            metrics_analysis=metrics_result,
                            report_type='html'
                        )
                    except Exception:
                        html_report = None

                    if html_report:
                        st.download_button(
                            label="📥 Download Report as HTML",
                            data=html_report,
                            file_name=f"{company_name}_analysis_report.html",
                            mime="text/html"
                        )
            else:
                st.download_button(
                    label="� Download Report as HTML",
                    data=report_data,
                    file_name=f"{company_name}_analysis_report.html",
                    mime="text/html"
                )
            
            # Cache the report in session state
            cache_key = f"report_cache_{report_type}"
            st.session_state[cache_key] = report_data
            
        except Exception as e:
            st.error(f"❌ Failed to generate report: {str(e)}")
            return None
    
    def run(self):
        """Main application orchestrator"""
        # Apply main layout and styles
        layout = MainLayout()
        layout.render()
        
        # Get API keys from sidebar
        google_key, firecrawl_key = Sidebar.render()
        
        # Initialize system if keys are provided
        if google_key and firecrawl_key:
            system_ready = self._initialize_system(google_key, firecrawl_key)
            
            if system_ready:
                # Render main application content
                company_name = self.render_company_input()
                self.render_main_dashboard(company_name)
            else:
                st.error("⚠️ Please check your API keys and try again.")
        else:
            # Show API configuration required message
            st.info("🔑 **Please configure your API keys in the sidebar to begin analysis.**")
            
            # Still show company input but disabled state
            company_name = self.render_company_input()
            if company_name:
                st.warning("⚠️ API keys required to perform analysis.")

def main():
    """Application entry point"""
    # Page configuration
    st.set_page_config(
        page_title="AI Product Intelligence Agent",
        page_icon="🚀",
        layout="wide",
        initial_sidebar_state="expanded"
    )
    
    # Load environment variables
    load_dotenv()
    
    # Initialize and run application
    app = ProductIntelligenceApp()
    app.run()

if __name__ == "__main__":
    main()