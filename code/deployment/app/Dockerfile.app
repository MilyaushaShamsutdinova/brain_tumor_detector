FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

RUN apt-get update \
    && apt-get install -y \
    libglib2.0-0 \
    libsm6 \
    libxext6 \
    libxrender-dev \
    libgl1-mesa-glx \
    && rm -rf /var/lib/apt/lists/*


COPY ./code/deployment/app /app/code/deployment/app
COPY ./code/models /app/code/models
COPY ./code/setup.py /app/code/setup.py
COPY ./code/__init__.py /app/code/__init__.py
COPY ./data /app/data
COPY ./models /app/models


RUN pip install --upgrade pip \
    && pip install -r /app/code/deployment/app/requirements.txt \
    && pip install -e /app/code

EXPOSE 8501

ENV PYTHONPATH=/app:/app/code

CMD ["streamlit", "run", "code/deployment/app/app.py", "--server.port=8501"]
