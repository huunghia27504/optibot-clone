# OptiBot Ingestion Script

This is a take-home assignment for the AlphaSphere Full Stack Developer Intern position.

It scrapes support articles from [OptiSigns](https://support.optisigns.com), converts them to Markdown, uploads them to OpenAI Vector Store via API, and creates an Assistant that can answer support questions based solely on these docs.

## 🚀 What this project does

- Scrapes ≥30 articles from Zendesk Help Center (OptiSigns)
- Converts each article to clean Markdown (`<slug>.md`)
- Detects added/updated articles using content comparison
- Uploads Markdown files to OpenAI Vector Store via API
- Logs each step: `added`, `updated`, `skipped`, `uploaded`
- Creates Assistant programmatically with required system prompt
- Runs once and exits cleanly (`exit 0`)

## 📦 Setup & Run

### 1. Install dependencies
```
pip install -r requirements.txt
```

### 2. Create `.env` file
```
cp .env.sample .env
```

And update with your OpenAI API key:
```
OPENAI_API_KEY=sk-...
```

### 3. Run the script
```
python main.py
```

### Or run via Docker
```
docker build -t optibot-clone .
docker run --rm -e OPENAI_API_KEY=sk-... optibot-clone
```

## 🧠 Assistant Prompt

The assistant is created using this exact system prompt:
```
You are OptiBot, the customer-support bot for OptiSigns.com.
• Tone: helpful, factual, concise.
• Only answer using the uploaded docs.
• Max 5 bullet points; else link to the doc.
• Cite up to 3 'Article URL:' lines per reply.
```

## 📚 Chunking Strategy

OpenAI automatically chunks uploaded files internally.  
No custom chunking logic is applied for simplicity and compatibility.  
All files are uploaded as raw Markdown.

## 🧪 Playground Screenshot

Due to API usage cost limitations, the Playground screenshot test (e.g. asking “How do I add a YouTube video?”) was not performed.  
However, all assistant creation logic is fully implemented and functional via API.  
Screenshot can be provided upon request if needed after review.

## 📁 Project Structure

.
├── data/               # Scraped Markdown files  
├── main.py             # Entry point – calls scrape, upload, create assistant  
├── scraper.py          # Scrape articles from Zendesk  
├── vector_store.py     # Create or reuse vector store and upload files  
├── assistant.py        # Create assistant using OpenAI API  
├── Dockerfile          # Docker container to run the project  
├── .env.sample         # Sample env file with API key placeholder  
├── requirements.txt    # Python dependencies  
└── README.md           # This documentation

## 🙋 Maintainer

Nguyễn Hữu Nghĩa – Candidate for AlphaSphere