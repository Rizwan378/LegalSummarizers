# LegalSummarizer

LegalSummarizer is a production-ready application for summarizing legal questions using OpenAI's GPT-3.5-turbo model.

## Features
- Upload CSV files with legal questions
- Generate concise summaries with state codes
- Responsive React frontend
- Scalable FastAPI backend
- Dockerized services with CI/CD

## Installation
1. Clone the repo: `git clone https://github.com/your-username/LegalSummarizer.git`
2. Configure `.env`: Update `backend/.env` with OpenAI API key
3. Build and run: `docker-compose up --build`
4. Access frontend: http://localhost:3000
5. Access API: http://localhost:8000/docs
6. Verify Redis: Ensure port 6379 is accessible

## Usage
- Upload CSV at http://localhost:3000
- API endpoint: POST `/api/v1/summarize`
- Health check: GET `/api/v1/health`
- Batch endpoint: POST `/api/v1/summarize/batch`
- View logs: `docker logs <container_id>`
- Stats: GET `/api/v1/stats`

## Data Format
- Input CSV requires `QuestionText` column
- Output CSV includes `QuestionText`, `Summary`
- Example input: "Can I evict my tenant? (NV)"
- Example output: "Eviction of tenant (NV)"
- Invalid questions return: "Not a valid legal question"
- Ensure UTF-8 encoding for CSV files

## Development
- Backend: `cd backend && uvicorn app.main:app --reload`
- Frontend: `cd frontend && npm start`
- Linting: `flake8 backend` or `npx eslint src`
- Testing: `pytest backend` or `npm test`
- Debug logs: Check `logs/app.log` or console
- Redis: `redis-cli -p 6379 ping`

