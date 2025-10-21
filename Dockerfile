# Use official lightweight Python image
FROM python:3.10-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set working directory
WORKDIR /app

# Copy requirements and install
COPY requirements.txt .

# --- Fix build failures for numpy / setuptools ---
RUN pip install --upgrade pip setuptools wheel

# Now install project dependencies
RUN pip install --no-cache-dir -r requirements.txt


# Copy the rest of the code
COPY . .

# Expose port
EXPOSE 5000

# Run the app
CMD ["python", "app.py"]
