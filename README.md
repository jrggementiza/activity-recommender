# Overview
AI Powered Activity Recommender based on a given Country and it's Season. Built w/ FastAPI + OpenAI.

# Setup
1. Clone the repo
```
git clone https://github.com/jrggementiza/activity-recommender.git
```
2. Create an `.env` file and add your OpenAI API Key
```
OPENAI_API_KEY=yOur_OpenAi_ApI_kEy
```

3. Venv Way (Mac)
```
- python3 -m venv venv
- source venv/bin/activate
- pip install -r requirements.txt
- uvicorn main:app --host 0.0.0.0 --port 3000
```

# Usage
1. Make a `GET` request to the following endpoint:
```
localhost:3000/?country=country&season=season
```
2. Include the `country` and `season` you want as query params


**Somewhat Happy Path**
![Somewhat Happy Path](./demo/somewhat_happy_path.gif)

**Unhappy Path**
![Unhappy Path](./demo/unhappy_paths.gif)

# Improvements
- Determine Seasons of a Country Programmatically instead of via AI
- Prompt Improvement and Token Minimization
- Throttle
- Persist Data of repeat requests to minimize OpenAI API Calls