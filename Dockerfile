# Use python:3.9-slim as the base image
FROM python:3.9-slim

# Set the working directory to /app
WORKDIR /app

# Copy pyproject.toml and poetry.lock and install dependencies
COPY pyproject.toml poetry.lock ./
RUN pip install poetry && poetry install --no-root --no-dev

# Copy the rest of the application code
COPY . .

# Set the command to run the FastAPI app with uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]
