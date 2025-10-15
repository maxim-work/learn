# 🛍 ERD - Интернет-магазин одежды (Django + HTMX + Alpine.js)

> Original repository: [s6ptember/enf](https://github.com/s6ptember/enf)

## 🌟 Особенности проекта

- **Современный стек**: Django + HTMX + Alpine.js
- **Две платежные системы**: Stripe и Heleket (крипто)
- **Docker-контейнеризация** с PostgreSQL
- **Кастомизированная модель пользователя**
- **Защищенные настройки** (CSRF, HTTPS, Security Headers)

## 🚀 Запуск проекта

### 1. Локальный запуск (без Docker)

#### 1) Создайте и активируйте виртуальное окружение:

```bash
python -m venv .venv
source .venv/bin/activate  # Linux/Mac
.venv\Scripts\activate    # Windows
```

#### 2) Установите зависимости:

```bash
# Установить основные зависимости
pip install .

# Установить с dev-зависимостями (django-debug-toolbar и т.д.)
pip install -e ".[dev]"

# Установить с prod-зависимостями (gunicorn, whitenoise)
pip install ".[prod]"
```

#### 3) Настройте переменные окружения:

```bash
# Заполните .env своими значениями (пример .env env-example)
cp env-example .env
```

#### 4) Запустите миграции:

```bash
python manage.py migrate
```

#### 5) Создайте суперпользователя:

```bash
python manage.py createsuperuser
```

#### 6) Запустите локальный сервер:

```bash
python manage.py runserver
```

### 2. Запуск через Docker

#### 1) Сборка и запуск

```bash
docker-compose up --build -d
```

#### 2) Проверка статуса

```bash
docker-compose ps
```

#### 3) Остановка

```bash
docker-compose down
```

## 🔒 Настройки безопасности

Проект предварительно настроен с:

- CSRF защитой
- Secure cookies
- Security Headers
- HTTPS при работе через Docker

### ⚙️ Важные настройки из settings.py

#### Безопасность

```python
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True
SECURE_BROWSER_XSS_FILTER = True
```

#### База данных

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('POSTGRES_DB'),
        # ... другие параметры
    }
}
```

#### Платежные системы

```python
STRIPE_SECRET_KEY = os.getenv('STRIPE_SECRET_KEY')
```