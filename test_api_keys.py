from agno.models.google import Gemini
from agno.tools.firecrawl import FirecrawlTools

def test_gemini_and_firecrawl():
    try:
        # Replace with your actual API keys
        google_api_key = "YOUR_GOOGLE_API_KEY"
        firecrawl_api_key = "YOUR_FIRECRAWL_API_KEY"

        # Test Gemini initialization
        gemini = Gemini(id="gemini-1.5-flash")
        print("Gemini initialized successfully.")

        # Test FirecrawlTools initialization
        firecrawl_tools = FirecrawlTools(api_key=firecrawl_api_key)
        print("FirecrawlTools initialized successfully.")

    except Exception as e:
        print(f"Error during initialization: {e}")

if __name__ == "__main__":
    test_gemini_and_firecrawl()
