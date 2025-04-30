import streamlit as st
import json
import pandas as pd

# Load the results from the JSON file
with open('data/results.json', 'r', encoding='utf-8') as f:
    results = json.load(f)

# Streamlit page configuration
st.set_page_config(
    page_title="Virgin Media Competitor Analysis",
    page_icon="🔍",
    layout="wide"
)

# Title and description
st.title("Virgin Media Competitor Analysis")
st.markdown("""
    **Welcome to the Competitor Analysis Tool!**  
    This tool helps you identify which competitors of Infosys have collaborated with Virgin Media. 
    Below are the results from the analysis.
""")

# Displaying the results in a table
if results:
    # Convert to a DataFrame for better formatting
    df = pd.DataFrame(results)

    # Display the DataFrame in a nice table
    st.write("### Collaboration Results")
    st.dataframe(df.style.set_table_styles(
        [{'selector': 'thead th', 'props': [('background-color', '#F4D03F'), ('color', 'black')]},
         {'selector': 'tbody td', 'props': [('background-color', '#FCF3CF'), ('color', 'black')]}]
    ))

    # Add some additional info on the side
    st.sidebar.header("Filters")
    selected_competitor = st.sidebar.selectbox("Select a Competitor", df['competitor'].unique())

    # Filter the results based on the selected competitor
    filtered_results = df[df['competitor'] == selected_competitor]
    st.write(f"### Showing results for: **{selected_competitor}**")
    st.write(filtered_results)

else:
    st.write("No results found. Please check the analysis or run it again.")

# Footer
st.markdown("""
    ---
    Developed by: **Divyanshi Jain**  
    Contact: divjain093@gmail.com 
    [GitHub Link](https://github.com/DivyanshiJ93)
""")
