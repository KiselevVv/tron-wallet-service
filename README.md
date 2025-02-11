# tron-wallet-service


## Клонирование репозитория
Склонируйте проект к себе на локальную машину:
```bash
git clone git@github.com:KiselevVv/tron-wallet-service.git
```

---

## Настройка переменных окружения
Создайте файл **`.env.dev`** в корневой директории и добавьте в него настройки базы данных:

```
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
POSTGRES_DB=mydatabase
DATABASE_URL=postgresql://postgres:postgres@db/mydatabase
```

Создайте файл **`.env.test`** в корневой директории и добавьте в него настройки базы данных:

```
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
POSTGRES_DB=test_database
DATABASE_URL=postgresql://postgres:postgres@test-db/test_database
```

---

## Сборка и запуск контейнеров
Соберите и запустите контейнеры для проверки функционала:
```bash
docker-compose --profile dev up -d --build
```
Проверить функциальность - http://localhost:8000/docs

---

## Запуск тестов
### Если контейнер запущен, его можно остановить
```bash
docker-compose --profile dev down

```

### Для запуска тестов
```bash
docker-compose --profile test up --build --abort-on-container-exit

```
