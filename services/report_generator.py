# services/report_generator.py
from datetime import datetime
import streamlit as st

class ReportGenerator:
    @staticmethod
    def generate_comprehensive_report(company_name: str, competitor_analysis: str, 
                                    sentiment_analysis: str, metrics_analysis: str, report_type: str = 'html'):
        """Generate a comprehensive report in HTML or PDF format
        
        Args:
            company_name (str): Name of the company being analyzed
            competitor_analysis (str): Competitor analysis results
            sentiment_analysis (str): Sentiment analysis results
            metrics_analysis (str): Metrics analysis results
            report_type (str): Type of report to generate ('html' or 'pdf')
        """
        if report_type.lower() == 'pdf':
            # Prefer HTML->PDF via WeasyPrint for better styling if available
            try:
                return ReportGenerator._generate_pdf_with_weasy(
                    company_name, competitor_analysis, sentiment_analysis, metrics_analysis
                )
            except Exception:
                # If WeasyPrint isn't available or fails, fall back to ReportLab PDF or HTML
                try:
                    return ReportGenerator._generate_pdf_report(
                        company_name, competitor_analysis, sentiment_analysis, metrics_analysis
                    )
                except Exception:
                    return ReportGenerator._generate_html_report(
                        company_name, competitor_analysis, sentiment_analysis, metrics_analysis
                    )
        return ReportGenerator._generate_html_report(
            company_name, competitor_analysis, sentiment_analysis, metrics_analysis
        )
        
        report_html = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <meta charset="UTF-8">
            <title>Product Intelligence Report - {company_name}</title>
            <style>
                body {{
                    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                    line-height: 1.6;
                    color: #333;
                    max-width: 1000px;
                    margin: 0 auto;
                    padding: 20px;
                }}
                .header {{
                    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                    color: white;
                    padding: 30px;
                    border-radius: 10px;
                    text-align: center;
                    margin-bottom: 30px;
                }}
                .section {{
                    background: #f8f9fa;
                    padding: 20px;
                    border-radius: 8px;
                    margin: 20px 0;
                    border-left: 4px solid #667eea;
                }}
                .executive-summary {{
                    background: #e3f2fd;
                    padding: 25px;
                    border-radius: 8px;
                    margin: 20px 0;
                }}
                .metric-card {{
                    background: white;
                    padding: 15px;
                    border-radius: 6px;
                    margin: 10px 0;
                    box-shadow: 0 2px 4px rgba(0,0,0,0.1);
                }}
                table {{
                    width: 100%;
                    border-collapse: collapse;
                    margin: 15px 0;
                }}
                th, td {{
                    padding: 12px;
                    text-align: left;
                    border-bottom: 1px solid #ddd;
                }}
                th {{
                    background-color: #667eea;
                    color: white;
                }}
            </style>
        </head>
        <body>
            <div class="header">
                <h1>Product Intelligence Report</h1>
                <h2>{company_name}</h2>
                <p>Generated on {datetime.now().strftime('%B %d, %Y at %H:%M')}</p>
            </div>
            
            <div class="executive-summary">
                <h3>📋 Executive Summary</h3>
                <p>Comprehensive analysis of {company_name}'s market position, customer sentiment, 
                and performance metrics. This report combines AI-driven insights from multiple 
                specialized analysts.</p>
            </div>
            
            <div class="section">
                <h3>🎯 Competitor Analysis</h3>
                {competitor_analysis}
            </div>
            
            <div class="section">
                <h3>💬 Market Sentiment Analysis</h3>
                {sentiment_analysis}
            </div>
            
            <div class="section">
                <h3>📊 Launch Performance Metrics</h3>
                {metrics_analysis}
            </div>
            
            <div class="section">
                <h3>🚀 Strategic Recommendations</h3>
                <ul>
                    <li><strong>Short-term (0-3 months):</strong> Focus on immediate opportunities</li>
                    <li><strong>Medium-term (3-12 months):</strong> Develop strategic initiatives</li>
                    <li><strong>Long-term (1+ years):</strong> Plan for sustainable growth</li>
                </ul>
            </div>
            
            <div style="text-align: center; margin-top: 40px; color: #666;">
                <p>Generated by AI Product Intelligence Platform</p>
                <p>Confidential - For internal use only</p>
            </div>
        </body>
        </html>
        """
        
        return report_html
    
    @staticmethod
    def _generate_pdf_report(company_name: str, competitor_analysis: str, 
                           sentiment_analysis: str, metrics_analysis: str) -> bytes:
        """Generate a richer PDF report using ReportLab with tables and an optional chart.

        The function is defensive: if matplotlib is not available, it will still produce
        a nicely formatted PDF without the chart.
        """
        from reportlab.lib.pagesizes import letter
        from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
        from reportlab.lib.units import inch
        from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, Image
        from reportlab.lib import colors
        from reportlab.lib.utils import ImageReader
        import io
        import textwrap
        import re

        # Helper to create a short preview of text
        def preview(text: str, width: int = 300):
            if not text:
                return "(No content)"
            # Trim and wrap to reasonable length
            one_line = re.sub(r"\s+", " ", text).strip()
            return textwrap.shorten(one_line, width=width, placeholder="...")

        # Convert a simple markdown-like string into ReportLab flowables
        def flowables_from_markdown(md_text: str):
            items = []
            if not md_text:
                return items

            lines = md_text.splitlines()
            bullet_block = []

            def flush_bullets():
                nonlocal bullet_block
                if bullet_block:
                    from reportlab.platypus import ListFlowable, ListItem
                    lf = ListFlowable([
                        Paragraph(b.strip().lstrip('* ').strip(), normal) for b in bullet_block
                    ], bulletType='bullet', leftIndent=12)
                    items.append(lf)
                    items.append(Spacer(1, 0.08*inch))
                    bullet_block = []

            for raw in lines:
                line = raw.strip()
                if not line:
                    flush_bullets()
                    items.append(Spacer(1, 0.08*inch))
                    continue

                if line.startswith('### '):
                    flush_bullets()
                    items.append(Paragraph(line[4:].strip(), header_style))
                    items.append(Spacer(1, 0.06*inch))
                elif line.startswith('## '):
                    flush_bullets()
                    items.append(Paragraph(line[3:].strip(), header_style))
                    items.append(Spacer(1, 0.06*inch))
                elif line.startswith('* '):
                    bullet_block.append(line)
                else:
                    flush_bullets()
                    # normal paragraph, keep some wrapping
                    cleaned = re.sub(r"\s+", " ", line)
                    items.append(Paragraph(cleaned, normal))
                    items.append(Spacer(1, 0.06*inch))

            flush_bullets()
            return items

        buffer = io.BytesIO()

        doc = SimpleDocTemplate(
            buffer,
            pagesize=letter,
            rightMargin=48,
            leftMargin=48,
            topMargin=48,
            bottomMargin=48
        )

        styles = getSampleStyleSheet()
        title_style = ParagraphStyle('TitleStyle', parent=styles['Heading1'], fontSize=20, spaceAfter=12)
        header_style = ParagraphStyle('Header', parent=styles['Heading2'], fontSize=14, textColor=colors.HexColor('#0d6efd'))
        normal = styles['Normal']

        content = []
        content.append(Paragraph(f"Product Intelligence Report", title_style))
        content.append(Paragraph(company_name, header_style))
        content.append(Spacer(1, 0.15*inch))
        content.append(Paragraph(f"Generated on {datetime.now().strftime('%B %d, %Y at %H:%M')}", normal))
        content.append(Spacer(1, 0.25*inch))

        # Executive summary block (short)
        content.append(Paragraph("Executive Summary", header_style))
        exec_summary = preview(competitor_analysis + ' ' + sentiment_analysis + ' ' + metrics_analysis, width=600)
        content.append(Paragraph(exec_summary, normal))
        content.append(Spacer(1, 0.2*inch))

        # Add a compact table summarizing sections
        table_data = [
            [Paragraph('<b>Section</b>', normal), Paragraph('<b>Summary</b>', normal)],
            [Paragraph('Competitor Analysis', normal), Paragraph(preview(competitor_analysis, width=400), normal)],
            [Paragraph('Market Sentiment', normal), Paragraph(preview(sentiment_analysis, width=400), normal)],
            [Paragraph('Performance Metrics', normal), Paragraph(preview(metrics_analysis, width=400), normal)],
        ]

        tbl = Table(table_data, colWidths=[1.6*inch, 4.6*inch])
        tbl.setStyle(TableStyle([
            ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#667eea')),
            ('TEXTCOLOR', (0,0), (-1,0), colors.white),
            ('VALIGN', (0,0), (-1,-1), 'TOP'),
            ('INNERGRID', (0,0), (-1,-1), 0.25, colors.grey),
            ('BOX', (0,0), (-1,-1), 0.25, colors.grey),
            ('LEFTPADDING', (0,0), (-1,-1), 8),
            ('RIGHTPADDING', (0,0), (-1,-1), 8),
        ]))

        content.append(tbl)
        content.append(Spacer(1, 0.25*inch))

        # Attempt to generate a small bar chart of top terms from competitor_analysis
        try:
            import matplotlib
            matplotlib.use('Agg')
            import matplotlib.pyplot as plt
            from collections import Counter

            words = re.findall(r"\w{4,}", competitor_analysis.lower())
            counter = Counter(words)
            top = counter.most_common(6)

            if top:
                labels, values = zip(*top)
                fig, ax = plt.subplots(figsize=(6, 3))
                ax.bar(labels, values, color='#4c72b0')
                ax.set_title('Top terms in Competitor Analysis')
                ax.set_ylabel('Occurrences')
                plt.xticks(rotation=30, ha='right')
                plt.tight_layout()

                img_buffer = io.BytesIO()
                fig.savefig(img_buffer, format='png', dpi=150)
                plt.close(fig)
                img_buffer.seek(0)

                content.append(Paragraph('Keyword distribution from Competitor Analysis', header_style))
                img = Image(ImageReader(img_buffer), width=5.6*inch, height=2.4*inch)
                content.append(img)
                content.append(Spacer(1, 0.25*inch))
        except Exception:
            # Matplotlib not available or chart failed - skip chart gracefully
            pass

        # Add full sections with headings and render markdown-like content into flowables
        content.append(Paragraph('Competitor Analysis', header_style))
        comp_flow = flowables_from_markdown(competitor_analysis)
        if comp_flow:
            content.extend(comp_flow)
        else:
            content.append(Paragraph(competitor_analysis or '(No competitor analysis available)', normal))
        content.append(Spacer(1, 0.15*inch))

        content.append(Paragraph('Market Sentiment', header_style))
        sent_flow = flowables_from_markdown(sentiment_analysis)
        if sent_flow:
            content.extend(sent_flow)
        else:
            content.append(Paragraph(sentiment_analysis or '(No sentiment analysis available)', normal))
        content.append(Spacer(1, 0.15*inch))

        content.append(Paragraph('Performance Metrics', header_style))
        metrics_flow = flowables_from_markdown(metrics_analysis)
        if metrics_flow:
            content.extend(metrics_flow)
        else:
            content.append(Paragraph(metrics_analysis or '(No performance metrics available)', normal))

        # Footer
        content.append(Spacer(1, 0.35*inch))
        content.append(Paragraph('Generated by AI Product Intelligence Platform — Confidential', styles['Italic']))

        doc.build(content)
        return buffer.getvalue()

    @staticmethod
    def _generate_html_report(company_name: str, competitor_analysis: str, 
                            sentiment_analysis: str, metrics_analysis: str) -> str:
        """Generate an HTML report"""
        report_html = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <meta charset="UTF-8">
            <title>Product Intelligence Report - {company_name}</title>
            <style>
                body {{
                    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                    line-height: 1.6;
                    color: #333;
                    max-width: 1000px;
                    margin: 0 auto;
                    padding: 20px;
                }}
                .header {{
                    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                    color: white;
                    padding: 30px;
                    border-radius: 10px;
                    text-align: center;
                    margin-bottom: 30px;
                }}
                .section {{
                    background: #f8f9fa;
                    padding: 20px;
                    border-radius: 8px;
                    margin: 20px 0;
                    border-left: 4px solid #667eea;
                }}
            </style>
        </head>
        <body>
            <div class="header">
                <h1>Product Intelligence Report</h1>
                <h2>{company_name}</h2>
                <p>Generated on {datetime.now().strftime('%B %d, %Y at %H:%M')}</p>
            </div>
            
            <div class="section">
                <h3>🎯 Competitor Analysis</h3>
                {competitor_analysis}
            </div>
            
            <div class="section">
                <h3>💬 Market Sentiment Analysis</h3>
                {sentiment_analysis}
            </div>
            
            <div class="section">
                <h3>📊 Launch Performance Metrics</h3>
                {metrics_analysis}
            </div>
        </body>
        </html>
        """
        return report_html

    @staticmethod
    def _generate_pdf_with_weasy(company_name: str, competitor_analysis: str,
                                sentiment_analysis: str, metrics_analysis: str) -> bytes:
        """Render the HTML template with Jinja2 and convert to PDF via WeasyPrint.

        Charts are optional — this function expects an environment with Jinja2 and WeasyPrint installed.
        """
        try:
            from jinja2 import Environment, FileSystemLoader
            from weasyprint import HTML
            import base64
            import io
            import os
        except Exception as e:
            raise

        # Prepare data dict
        data = {
            'company': company_name,
            # Exec summary: return a short list of lines
            'exec_summary': [line.strip() for line in ReportGenerator.generate_executive_summary(company_name, {
                'competitor': competitor_analysis,
                'sentiment': sentiment_analysis,
                'metrics': metrics_analysis
            }).split('\n') if line.strip()][:6],
            'kpis': [
                {'label': 'Summary metric', 'value': 'N/A', 'delta': ''}
            ],
            'sections': [
                {'title': 'Competitor Analysis', 'text': competitor_analysis},
                {'title': 'Market Sentiment', 'text': sentiment_analysis},
                {'title': 'Performance Metrics', 'text': metrics_analysis},
            ],
            'sources': []
        }

        # No charts by default; caller can extend this API later
        data['charts_b64'] = []

        # Convert markdown-style section text to safe HTML using markdown2 if available
        try:
            import markdown2
            for sec in data['sections']:
                raw = sec.get('text') or ''
                # Convert to HTML and store as 'html'
                sec['html'] = markdown2.markdown(raw, extras=["fenced-code-blocks", "tables"]) if raw else ''
        except Exception:
            # Fallback: escape simple text into paragraphs
            for sec in data['sections']:
                sec['html'] = '<p>' + (sec.get('text') or '').replace('\n', '<br/>') + '</p>'

        # Render template
        env = Environment(loader=FileSystemLoader(os.path.join(os.getcwd(), 'templates')))
        template = env.get_template('report.html')
        html_content = template.render(**data, generated_on=datetime.now().strftime('%B %d, %Y %H:%M'))

        # Convert to PDF bytes
        pdf_bytes = HTML(string=html_content).write_pdf()
        return pdf_bytes

    @staticmethod
    def generate_executive_summary(company_name: str, analyses: dict):
        """Generate a concise executive summary"""
        summary = f"""
        # Executive Summary: {company_name}
        
        ## Key Findings
        
        ### 🎯 Competitive Positioning
        - Market position: [Summary from competitor analysis]
        - Key strengths: [Top 3 strengths]
        - Areas for improvement: [Top 3 weaknesses]
        
        ### 💬 Market Sentiment
        - Overall sentiment score: [Positive/Negative/Neutral]
        - Key sentiment drivers: [Main factors influencing perception]
        - Customer satisfaction: [High/Medium/Low]
        
        ### 📊 Performance Metrics
        - Market traction: [Adoption rate, growth metrics]
        - Financial performance: [Revenue impact if available]
        - Media coverage: [Press mentions, social engagement]
        
        ## Strategic Recommendations
        
        1. **Immediate Actions** (0-3 months)
           - [Priority action 1]
           - [Priority action 2]
        
        2. **Strategic Initiatives** (3-12 months)  
           - [Medium-term initiative 1]
           - [Medium-term initiative 2]
        
        3. **Long-term Planning** (1+ years)
           - [Long-term strategy 1]
           - [Long-term strategy 2]
        
        ## Risk Assessment
        - **High Risk:** [Key risks identified]
        - **Medium Risk:** [Moderate concerns] 
        - **Low Risk:** [Minor considerations]
        
        *Report generated on {datetime.now().strftime('%Y-%m-%d')}*
        """
        
        return summary