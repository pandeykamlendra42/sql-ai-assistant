# 🤖 AI SQL Assistant  

### Chat Directly with Your Database — No More Waiting for Data Teams!  

The **AI SQL Assistant** empowers **business, marketing, and product teams** to get instant data insights by simply chatting with their database in natural language.  
No SQL knowledge required. No dependency on Data Engineering or Analytics teams.  

---

## 🚀 Business Impact  

✅ **Faster Decision-Making:** Get answers in seconds instead of waiting days for reports.  
✅ **Empower Non-Technical Teams:** Anyone can explore data with plain English queries.  
✅ **Reduce Engineering Bottlenecks:** Free up data teams from repetitive requests.  
✅ **Universal Plug & Play:** Works with any PostgreSQL database — just update your `.env` file.  

---

## 💡 Example Use Cases  

- **Marketing:** “Show me top 10 campaigns by ROI last quarter.”  
- **Product:** “What’s the most used feature this month?”  
- **Business:** “Compare monthly revenue growth for the last 6 months.”  

---

## ⚙️ How It Works  

1. The assistant takes your natural language query.  
2. It uses OpenAI’s language model to generate the SQL query.  
3. The SQL query runs on your connected PostgreSQL database.  
4. You get structured results — instantly and accurately.  

---

## 🧩 Setup Instructions  

### 1️⃣ Clone the Repository  

```bash
git clone https://github.com/yourusername/ai-sql-assistant.git
cd ai-sql-assistant
```

### 2️⃣ Update the .env File
```bash
OPENAI_API_KEY=your_openai_api_key
DATABASE_URL=postgresql+psycopg2://readonly:readonlypass@localhost:5432/mydb
MAX_ROWS=200
```

### 3️⃣ Activate the Virtual Environment
```bash
source .venv/bin/activate
```

### 4️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 5️⃣ Run the App
```bash
streamlit run app.py
```
<img width="1325" height="652" alt="Screenshot 2025-10-20 at 12 34 04 PM" src="https://github.com/user-attachments/assets/6fd8773f-3dfc-4742-a0a2-2d6cbb129b6b" />


