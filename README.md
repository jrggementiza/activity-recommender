# Overview
AI Powered Activity Recommender based on a given Country and it's Season. Built w/ FastAPI + OpenAI.

# Setup
1. Clone the repo
```
git clone https://github.com/jrggementiza/activity-recommender.git
```
2. Create an `.env` file
```
OPENAI_API_KEY=yOur_OpenAi_ApI_kEy
```

3. Venv Way
```
- python3 -m venv venv
- source venv/bin/activate
- uvicorn main:app --host 0.0.0.0 --port 3000
```

# Usage
localhost:3000/?country=country&season=season

# Improvements
- Persist Data of repeat requests to minimize OpenAI API Calls
- Determine Seasons of a Country Programmatically instead of via AI
- Prompt Improvement and Token Minimization