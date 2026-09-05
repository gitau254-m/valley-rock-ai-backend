# Valley Rock Tours — AI Safari Consultant (Phase 1)

FastAPI backend powering the AI chat widget on the Valley Rock Tours website.
A visitor types what kind of safari they want — the AI recommends the right package.

## Tech Stack
- Python 3.12
- FastAPI + Uvicorn
- Anthropic Claude (claude-haiku-4-5)
- python-dotenv

## Setup

**1. Clone and install dependencies:**
```bash
pip install -r requirements.txt
```

**2. Set up your API key:**
```bash
cp .env.example .env
# Open .env and paste your Anthropic API key
```

**3. Run the server:**
```bash
uvicorn main:app --reload
```

The server starts at `http://localhost:8000`.
Visit `http://localhost:8000/docs` to see the interactive API documentation.

## Testing the chat endpoint

**First message (no history):**
```bash
curl -X POST http://localhost:8000/chat \
  -H "Content-Type: application/json" \
  -d '{"message": "I have 6 days in Kenya and love wildlife", "conversation_history": []}'
```

**Second message (with conversation history):**
```bash
curl -X POST http://localhost:8000/chat \
  -H "Content-Type: application/json" \
  -d '{
    "message": "What is included in the price?",
    "conversation_history": [
      {"role": "user", "content": "I have 6 days in Kenya and love wildlife"},
      {"role": "assistant", "content": "That sounds like a great trip! Based on 6 days and wildlife focus, our 6 Days Maasai Mara, Lake Nakuru & Amboseli safari would be ideal..."}
    ]
  }'
```

**Health check:**
```bash
curl http://localhost:8000/health
```

## Phase 1 Scope

This is a working prototype with 3 hardcoded safari packages.
It is intentionally simple — no database, no vector search, no authentication.

**What Phase 2 will add:**
- WordPress integration (pull live tour data automatically)
- Vector search / RAG for handling large tour catalogues
- Enquiry creation (visitor details saved and sent to the team)
- Authentication on the endpoint before public deployment

## Security Notes

- The Anthropic API key is server-side only — never exposed to the browser
- CORS is currently set to `allow_origins=["*"]` for local development
- **Before any public deployment:** lock CORS to the real Valley Rock Tours domain only
- **Before any public deployment:** add rate limiting to prevent API abuse