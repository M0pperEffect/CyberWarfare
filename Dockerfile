
# Use official Python base image
FROM python:3.13-slim

#set working directory
WORKDIR /app

COPY requirements.txt .
   # copy just the requirements first
RUN pip install -r requirements.txt

COPY . .                 
 # now copy the rest of the project

EXPOSE 5000
CMD ["python", "app.py"]

