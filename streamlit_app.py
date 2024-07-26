import os

import streamlit as st
import yaml
from openai import OpenAI

def load_schemas():
    with open("data/session/session.yml", "r") as file:
        session_schema = yaml.safe_load(file)
    with open("data/search/search.yml", "r") as file:
        search_schema = yaml.safe_load(file)
    with open("data/open_activity/open_activity.yml", "r") as file:
        open_activity_schema = yaml.safe_load(file)
    with open("data/purchase/purchase.yml", "r") as file:
        purchase_schema = yaml.safe_load(file)
    return session_schema, search_schema, open_activity_schema, purchase_schema

st.title("💬 AI Analyst")
st.write(
    "This is a simple chatbot that uses OpenAI's GPT-3.5 model to generate SQL queries based on user's task"
)
SYSTEM_CONTENT = "You are an assisnant for analyst. Analyst gives you a task, and you need to give a solution"

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

schemas = load_schemas()
schema_info = "\n".join(
    [yaml.dump(schema, default_flow_style=False) for schema in schemas]
)
with st.expander("See database schema"):
    st.code(schema_info, language="yaml")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("What is up?"):

    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    full_prompt = f"Given the following database schemas:\n{schema_info}\n\nGenerate a SQL query for the following request: {prompt}. You are allowed to use only tables from given database schema only and you can't rename the original table names and columns"

    # Generate a response using the OpenAI API.
    stream = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": SYSTEM_CONTENT},
            {"role": "user", "content": full_prompt},
        ],
        stream=True,
    )

    with st.chat_message("assistant"):
        response = st.write_stream(stream)
    st.session_state.messages.append({"role": "assistant", "content": response})
