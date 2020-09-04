FROM python:3.7-alpine
WORKDIR /app
COPY version.txt .
RUN pip install -r version.txt
COPY . .
EXPOSE 5001
CMD ["python", "rng.py"]