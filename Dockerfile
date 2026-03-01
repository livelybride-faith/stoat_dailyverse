FROM python:3.11-slim
WORKDIR /app
# This line MUST include both requests and schedule
RUN pip install requests schedule
COPY dailyVerse.py .
CMD ["python", "dailyVerse.py"]