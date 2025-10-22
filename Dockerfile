# Use Python 3.9 slim image
FROM python:3.9-slim

# Create a non-root user
RUN useradd --create-home --shell /bin/bash app

# Set working directory
WORKDIR /app

# Copy requirements and install dependencies (as root to ensure global install)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Change ownership of the working directory to the app user
RUN chown -R app:app /app

# Switch to the non-root user
USER app

# Copy application code
COPY . .

# Expose port for Streamlit
EXPOSE 8501

# Run the Streamlit application
CMD ["/usr/local/bin/streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0", "--server.headless=true"]
