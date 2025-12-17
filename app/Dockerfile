# -------- Builder --------
FROM python:3.11-slim AS builder

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt


# -------- Runtime --------
FROM python:3.11-slim

WORKDIR /app

# Copy system-installed packages
COPY --from=builder /usr/local /usr/local

# Create non-root user
RUN useradd -m -u 1000 appuser

COPY --chown=appuser:appuser . .

USER appuser

EXPOSE 5000

CMD ["gunicorn", "--bind", "0.0.0.0:5000", "--workers", "2", "app:app"]
