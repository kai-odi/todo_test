# `todo-app`

This project uses Python 3.12 for the backend and TypeScript + Aurelia for the frontend.

## First-time Setup

1. Rename `env_backend_example` to `.env` and move it into the `backend` directory.
2. Rename `env_frontend_example` to `.env` and move it into the `frontend` directory.
3. Open each `.env` file and configure the required environment variables.

## Running the Project

1. Make sure Docker Desktop (or Docker Engine) is installed on your system.
2. In the project root directory, run the following command:

   ```bash
   docker compose up --build
   ```