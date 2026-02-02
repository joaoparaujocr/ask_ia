FROM python:3.12-slim

ARG UID=1000
ARG GID=1000

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV XDG_CACHE_HOME=/app/.cache

WORKDIR /app

RUN pip install --no-cache-dir uv

RUN groupadd -g $GID appgroup \
 && useradd -m -u $UID -g appgroup appuser \
 && mkdir -p /app/.cache \
 && chown -R appuser:appgroup /app

COPY pyproject.toml uv.lock ./

RUN uv venv \
    && . .venv/bin/activate \
    && uv sync

ENV PATH="/app/.venv/bin:$PATH"

COPY . .

USER appuser

EXPOSE 8000

CMD ["uv", "run", "python", "app/main.py"]
