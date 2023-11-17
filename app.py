# app.py
import streamlit as st
import openai
import snowflake.connector
from snowflake.connector import ProgrammingError
import os
from pathlib import Path
from dotenv import load_dotenv

# Construct the path to the .env file in the parent directory
path = Path("/Users/melissamullen/twitter-sentiment-analysis")
env_path = os.path.join(path, ".env")

# Load environment variables from .env file
load_dotenv(dotenv_path=env_path)

def main():
    st.title("My Knowledge Base")

    # User input field
    user_input = st.text_input("Enter your query or note:")

    # Submit button
    submit_button = st.button("Submit")

    if submit_button and user_input:
        # Store and display user input
        display_chat_message("user", user_input)
        
        # Get GPT response and display it
        response = get_gpt_response(user_input)
        display_chat_message("gpt", response)

        # Store data in Snowflake
        store_data(user_input, response)

def get_gpt_response(input_text):
    openai.api_key = os.getenv('OPEN_AI_KEY')  # Replace with your API key

    response = openai.Completion.create(
      engine="davinci", 
      prompt=input_text, 
      max_tokens=150
    )
    return response.choices[0].text.strip()

def store_data(user_id, input_text, response_text):
    # Connect to Snowflake
    conn = snowflake.connector.connect(
        user=os.getenv('SNOWFLAKE_USER'),
        password=os.getenv('SNOWFLAKE_PASSWORD'),
        account=os.getenv('SNOWFLAKE_ACCOUNT'),
        warehouse=os.getenv('SNOWFLAKE_WAREHOUSE'),
        database=os.getenv('SNOWFLAKE_DATABASE'),
        schema=os.getenv('SNOWFLAKE_SCHEMA')
    )
    try:
        # SQL query to insert data
        insert_query = """
        INSERT INTO user_data (user_id, user_input, gpt_response)
        VALUES (%s, %s, %s)
        """
        cur = conn.cursor()
        cur.execute(insert_query, (user_id, input_text, response_text))
        conn.commit()
    except ProgrammingError as e:
        st.error(f"Error occurred: {e}")
    finally:
        conn.close()

def display_chat_message(user_type, message):
    if user_type == "user":
        st.markdown(f"<div style='text-align: right; color: blue;'>{message}</div>", unsafe_allow_html=True)
    else:
        st.markdown(f"<div style='text-align: left; color: green;'>{message}</div>", unsafe_allow_html=True)

if __name__ == "__main__":
    main()
