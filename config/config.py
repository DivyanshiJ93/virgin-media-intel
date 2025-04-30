# config/config.py

# Your SerpAPI Key
SERPAPI_KEY = "d1dd3bc741f2fa0635113f9306e5d74e40bc562dd15ac6e688eb60bbb39f8ae6"

# Optional: OpenAI Key if you want to use GPT for analysis (not required if running rule-based)
OPENAI_KEY = ""  # Leave empty if not using GPT-4

# Search query template
QUERY_TEMPLATE = "{competitor} Virgin Media partnership OR client OR case study OR project OR contract"

# Number of results to fetch from search engine per competitor
NUM_RESULTS = 5
