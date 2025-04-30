#  Virgin Media Competitor Intelligence Tool

This tool was developed as part of an internship assignment for **Anapan AI**. Its goal is to automate the process of identifying which **competitors of Infosys** have previously worked with the target account **Virgin Media**, using only publicly available sources.

---

##  What It Does

This tool simulates a real-world enterprise research assistant. It:

1. Takes a list of Infosys's top competitors.
2. Searches Google via **SerpAPI** for "<Competitor> and Virgin Media".
3. Parses news articles using **newspaper3k**.
4. Analyzes the article text to check for actual collaborations.
5. Outputs results into a readable JSON file.
6. Optionally displays results via a **Streamlit frontend**.

---
The project is deployed at [ https://virgin-media-intel.streamlit.app/ ] 
