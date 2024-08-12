FROM python:3.9-slim
WORKDIR /app
RUN apt-get update && apt-get install -y \
    libmagic-dev \
    build-essential \
    curl \
    software-properties-common \
    git \
    && rm -rf /var/lib/apt/lists/*
COPY . .
EXPOSE 8080
ENTRYPOINT ["main.py", "--server.port=8080", "--server.address=0.0.0.0"]
