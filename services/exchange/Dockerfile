
# Stage 1: Install dependencies
FROM python:3.12-slim AS builder

WORKDIR /build

COPY requirements.txt .
RUN pip install --no-cache-dir --prefix=/install -r requirements.txt

# Stage 2: Production image
FROM python:3.12-slim AS production

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN useradd --create-home --uid 10001 --user-group appuser

WORKDIR /app

COPY --from=builder /install /usr/local
COPY services/exchange/app ./services/exchange/app

USER 10001:10001

EXPOSE 8000

CMD ["uvicorn", "services.exchange.app.main:app", "--host", "0.0.0.0", "--port", "8000"]
