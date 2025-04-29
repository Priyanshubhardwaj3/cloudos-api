# Use Python base image
FROM python:3.10-slim

# Set workdir
WORKDIR /app

# Copy files
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port (Cloud Run detects automatically)
EXPOSE 8080

# Run app using gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:8080", "app.main:app"]
