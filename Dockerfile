FROM python:3.11-alpine

# Define build-time arguments
ARG PORT

# Set environment variables based on build-time arguments
ENV PORT=${PORT}

# Set working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the app code
COPY . .

# Run the app using Gunicorn
CMD gunicorn -w 4 -b 0.0.0.0:$PORT main:app