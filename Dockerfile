# Use a base Python image
FROM python:latest

# Set the working directory in the container to the parent directory of app
WORKDIR /app

# Copy requirements file and install dependencies
COPY requirements.txt /app/

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

# Copy the entire application directory
COPY . .

# Expose the port
EXPOSE 8000

# Run the application
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
