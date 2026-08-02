# Money Management App

A full-stack money management application with a Next.js dashboard and an AI-powered analytics service.

## Project Overview

This repository contains two main folders:

- `web-app` — a Next.js 16 application for user authentication, transaction tracking, and dashboard visualization.
- `ai-service` — a FastAPI service providing spending predictions, anomaly detection, and budget insights using machine learning.

The app is designed to help users manage expenses, view spending trends, and get AI-powered recommendations.

## Key Features

- User sign up and login with credentials-based authentication
- Transaction logging and history
- Spending prediction for expense categories
- Anomaly detection for unusual transactions
- Budget health analysis with recommendations
- Responsive dashboard and charts
- Local development support with Docker Compose

## Architecture

### `web-app`

- Framework: Next.js 16
- Authentication: NextAuth with credentials provider
- Database: Prisma ORM with libSQL adapter
- Frontend: React, Recharts, and custom UI components
- AI integration: `web-app/src/lib/ai-client.ts` calls the AI service endpoints

### `ai-service`

- Framework: FastAPI
- ML libraries: scikit-learn, pandas, numpy
- Prediction engine: Linear regression-based spending forecast
- Anomaly detection: Isolation Forest
- Budget insights: category-based needs/wants/savings analysis

## Repository Structure

- `docker-compose.yml` — orchestrates `web` and `ai-service` containers
- `web-app/` — frontend and backend integration code for the Next.js app
- `ai-service/` — backend AI service code and model logic

## Getting Started

### Prerequisites

- Node.js 20+
- npm
- Python 3.11+ with `venv`
- Docker and Docker Compose (optional but recommended)

### Option 1: Run locally without Docker

1. Start the AI service:

```bash
cd ai-service
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

2. Start the web app:

```bash
cd ../web-app
npm install
npm run dev
```

3. Open the app in your browser:

- Frontend: `http://localhost:3000`
- AI service health: `http://localhost:8000/health`

### Option 2: Run with Docker Compose

```bash
docker compose up --build
```

The Compose setup launches:

- `web` on port `3000`
- `ai-service` on port `8000`

## Environment Variables

The web app expects an AI service URL with:

- `AI_SERVICE_URL` — for example `http://localhost:8000`

The Next.js app may also require standard environment variables for Prisma and NextAuth such as:

- `DATABASE_URL`
- `NEXTAUTH_URL`
- `NEXTAUTH_SECRET`

## AI Service Endpoints

The AI service exposes three main endpoints:

- `POST /api/v1/predict-spending`
  - Request: list of transactions
  - Response: projected spending per category
- `POST /api/v1/detect-anomalies`
  - Request: list of transactions
  - Response: anomaly detection results
- `POST /api/v1/budget-insights`
  - Request: list of transactions and monthly income
  - Response: budget percentages, balance evaluation, recommendation

## Important Notes

- CORS is configured to allow all origins in `ai-service/app/main.py`; tighten this for production.
- The AI service uses simple ML heuristics suitable for demo and prototype use.
- Ensure the `web-app` and `ai-service` containers can communicate via `AI_SERVICE_URL` when using Docker.

## How to Contribute

1. Fork the repository.
2. Create a feature branch.
3. Add tests or verify locally.
4. Submit a pull request with a clear description.

## License

This repository does not include a specific license file. Add a license if you intend to share or distribute it publicly.
