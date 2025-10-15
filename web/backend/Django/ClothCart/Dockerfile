#dev
FROM python:3.10-slim

WORKDIR /app

RUN apt-get update && apt-get install -y \
    libpq-dev \
    gcc \
    gettext \
    && rm -rf /var/lib/apt/lists/*

RUN python -m venv /app/.venv
ENV PATH="/app/.venv/bin:$PATH"

COPY pyproject.toml ./

RUN pip install --no-cache-dir -e ".[dev]"

COPY . .

CMD ["python", "enf/manage.py", "runserver", "0.0.0.0:8000"]


#prod
# FROM python:3.10-slim

# WORKDIR /app

# RUN apt-get update && apt-get install -y\
#     libpq-dev \
#     gcc \
#     gettext \
#     vim \
#     && rm -rf /var/lib/apt/lists/*

# RUN python -m venv /app/.venv
# ENV PATH="/app/.venv/bin:$PATH"

# COPY pyproject.toml ./

# RUN pip install --no-cache-dir -e ".[prod]"

# COPY . .

# CMD ["sh", "-c", "python enf/manage.py migrate && gunicorn enf.wsgi:application --bind 0.0.0.0:8000"]


# 1. Собрать и запустить в фоне
# docker-compose up --build -d

# 2. Проверить статус
# docker-compose ps

# 3. Проверить работу
# curl http://localhost:8000

# 4. Посмотреть логи если нужно
# docker-compose logs web

# 5. Остановить и полностью удалить
# docker-compose down -v --rmi all
# docker system prune -a --volumes --force

# 6. Проверить что всё удалено
# docker ps -a
# docker images
# docker volume ls