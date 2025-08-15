# 📓 Diary

CRUD-приложение на **FastAPI** с PostgreSQL, полностью конфигурируемое через переменные окружения, упакованное в Docker и дополненное линтерами/форматтерами для чистого кода.

---

## Возможности

* **CRUD** для заметок (создать, прочитать, обновить, удалить)
* **Отметка записи как выполненной**
* **Список всех записей**
* Асинхронный доступ к базе данных через **SQLAlchemy + asyncpg**
* Деплой в 1 команду через **Docker Compose**
* Конфигурация через `.env`
* Линтеры и форматтеры (**flake8**, **black**, **isort**)
* Автоматическая проверка кода через **pre-commit**

---

## Стек технологий

* Python 3.12
* FastAPI
* SQLAlchemy (async)
* PostgreSQL
* Docker + Docker Compose
* Black, Isort, Flake8, Pre-commit

---

## Установка и запуск

### 1. Клонирование репозитория

```bash
git clone https://github.com/username/diary-api.git
cd diary-api
```

### 2. Создание `.env`

```env
POSTGRES_USER=user
POSTGRES_PASSWORD=password
POSTGRES_DB=diary
DATABASE_URL=postgresql+asyncpg://user:password@db:5432/diary
```

### 3. Запуск приложения

```bash
docker compose up --build
```

API будет доступно по адресу: **[http://localhost:8000](http://localhost:8000)**
Документация Swagger: **[http://localhost:8000/docs](http://localhost:8000/docs)**

---

## Эндпоинты

| Метод  | URL              | Описание                    |
| ------ | ---------------- | --------------------------- |
| POST   | /notes/          | Создать запись              |
| GET    | /notes/          | Получить список записей     |
| GET    | /notes/{id}      | Получить запись по ID       |
| PUT    | /notes/{id}      | Обновить запись             |
| PATCH  | /notes/{id}/done | Отметить запись выполненной |
| DELETE | /notes/{id}      | Удалить запись              |

---

## Линтеры и форматтеры

В проекте настроены:

* **black** — форматирование кода
* **isort** — сортировка импортов
* **flake8** — проверка качества кода


### Запуск проверок вручную

```bash
black .
isort .
flake8
```

---

## ⚙️ Переменные окружения

Все настройки берутся из `.env`:

| Переменная         | Описание                      |
| ------------------ | ----------------------------- |
| POSTGRES\_USER     | Пользователь БД               |
| POSTGRES\_PASSWORD | Пароль БД                     |
| POSTGRES\_DB       | Имя БД                        |
| DATABASE\_URL      | Строка подключения SQLAlchemy |

---

## 📂 Структура проекта

```
app/
├── db/               # Подключение и модели БД
├── routers/          # Эндпоинты API
├── schemas/          # Pydantic-схемы
├── services/         # Логика работы с БД
├── main.py           # Точка входа
├── logger.py         # Логгер
├── Dockerfile        # Докерфайл для сборки
├── requirements.txt  
docker-compose.yml

requirements.txt
.env.example
```

---

## 🐳 Деплой

Приложение полностью разворачивается в Docker:

```bash
docker compose up --build
```

База и приложение запускаются автоматически, конфигурация берётся из `.env`.

