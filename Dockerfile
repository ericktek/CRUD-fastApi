# 
FROM python:latest


# 
WORKDIR /app

# 
COPY ./requirements.txt /code/requirements.txt

# 
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# 
COPY . .

# Define the port number the container should expose
EXPOSE 8000
# 
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
