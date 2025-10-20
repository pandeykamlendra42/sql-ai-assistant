import streamlit as st
import psycopg2
import pandas as pd
from openai import OpenAI
import os

# -----------------------------
# ⚙️ CONFIGURATION
# -----------------------------
st.set_page_config(page_title="AI SQL Assistant", page_icon="🧠", layout="wide")

# OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# PostgreSQL connection config
DB_CONFIG = {
    "host": "localhost",
    "port": 5432,
    "dbname": "hotel",
    "user": "postgresW",
    "password": "postgresW"
}

# -----------------------------
# 🧩 DATABASE FUNCTIONS
# -----------------------------
def run_query(query):
    try:
        conn = psycopg2.connect(**DB_CONFIG)
        df = pd.read_sql(query, conn)
        conn.close()
        return df
    except Exception as e:
        st.error(f"Error executing query: {e}")
        return None


def get_db_schema():
    """
    Reads all table & column names from the public schema.
    """
    query = """
    SELECT table_name, column_name
    FROM information_schema.columns
    WHERE table_schema = 'public'
    ORDER BY table_name, ordinal_position;
    """
    conn = psycopg2.connect(**DB_CONFIG)
    cur = conn.cursor()
    cur.execute(query)
    rows = cur.fetchall()
    cur.close()
    conn.close()

    schema = {}
    for table, column in rows:
        schema.setdefault(table, []).append(column)
    return schema


# -----------------------------
# 🧠 OPENAI QUERY GENERATOR
# -----------------------------
def generate_sql(prompt, schema):
    """
    Uses OpenAI to generate SQL based on the user's natural language question.
    """
    schema_text = "\n".join(
        [f"Table {t}: columns {', '.join(cols)}" for t, cols in schema.items()]
    )

    system_prompt = (
        "You are an expert data analyst. "
        "Generate ONLY valid SQL queries for PostgreSQL based on the given schema. "
        "Never invent columns or tables that are not present."
    )

    messages = [
        {"role": "system", "content": system_prompt},
        {
            "role": "user",
            "content": f"Schema:\n{schema_text}\n\nUser question:\n{prompt}",
        },
    ]

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages,
        temperature=0
    )

    sql_query = response.choices[0].message.content.strip()
    return sql_query


# -----------------------------
# 🖥️ STREAMLIT UI
# -----------------------------
st.title("🧠 AI SQL Assistant for PostgreSQL")
st.caption("Ask natural-language questions and get answers directly from your database.")

# Load schema
with st.spinner("Reading database schema..."):
    schema = get_db_schema()

st.subheader("📋 Database Schema")
st.json(schema)

# Input question
user_question = st.text_area("💬 Ask a question about your data:", "Show total order amount per user")

# -----------------------------
# Generate SQL Button
# -----------------------------
if st.button("🚀 Generate SQL & See Results"):
    sql_query = generate_sql(user_question, schema)
    print(sql_query)  # For debugging
    st.session_state["sql_query"] = sql_query  # Save to session_state
    # Clean the SQL query
    query_to_run = sql_query.strip()
    sql_query = query_to_run.strip().replace("```sql", "").replace("```", "").strip()
    print(f"Running SQL: {sql_query}")  # For debugging

    # Execute
    df = run_query(sql_query)
    if df is not None and not df.empty:
        st.success("✅ Query executed successfully!")
        st.dataframe(df)
    else:
        st.warning("⚠️ No data returned or query failed.")
    
    st.code(sql_query, language="sql")


