FROM python:3.11-slim
WORKDIR /app
RUN pip install requests
COPY dailyVerse.py .
CMD ["python", "dailyVerse.py"]