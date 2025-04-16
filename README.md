# blume-assistant
the backend of blume voice assistant

## Deploying the API to Google Cloud Run

1. **Install Google Cloud SDK**: Follow the instructions [here](https://cloud.google.com/sdk/docs/install) to install the Google Cloud SDK.

2. **Authenticate with Google Cloud**: Run the following command to authenticate with your Google Cloud account:
   ```sh
   gcloud auth login
   ```

3. **Set your Google Cloud project**: Replace `YOUR_PROJECT_ID` with your actual project ID.
   ```sh
   gcloud config set project YOUR_PROJECT_ID
   ```

4. **Build and deploy the Docker image**:
   ```sh
   gcloud builds submit --tag gcr.io/YOUR_PROJECT_ID/blume-assistant
   gcloud run deploy blume-assistant --image gcr.io/YOUR_PROJECT_ID/blume-assistant --platform managed
   ```

## Configuring External AI in Vapi

1. **Set up Google Cloud Vertex AI**: Follow the instructions [here](https://cloud.google.com/vertex-ai/docs/start) to set up Vertex AI.

2. **Create a service account**: Create a service account with the necessary permissions to access Vertex AI. Download the service account key file and save it as `service_account.json`.

3. **Set environment variables**: Set the `PROJECT_ID` and `REGION` environment variables in your deployment environment.

## Testing the API Locally with Docker

1. **Build the Docker image**:
   ```sh
   docker build -t blume-assistant .
   ```

2. **Run the Docker container**:
   ```sh
   docker run -p 8080:8080 -e PROJECT_ID=your_project_id -e REGION=your_region -v /path/to/service_account.json:/app/service_account.json blume-assistant
   ```

## Using Poetry for Package Management

1. **Install Poetry**: Follow the instructions [here](https://python-poetry.org/docs/#installation) to install Poetry.

2. **Install dependencies**:
   ```sh
   poetry install
   ```

3. **Add new dependencies**:
   ```sh
   poetry add <package_name>
   ```

## Agenda Booking System Integration

The API includes an endpoint for booking appointments. This is a placeholder for integration with an agenda booking system like Calendly.

To use this endpoint, send a POST request to `/book-appointment`. The implementation can be extended to integrate with the desired booking system.
