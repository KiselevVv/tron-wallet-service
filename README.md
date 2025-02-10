# tron-wallet-service

Вот инструкция в формате Markdown:  

```md

## Клонирование репозитория
Склонируйте проект к себе на локальную машину:
```bash
git@github.com:KiselevVv/tron-wallet-service.git
```

---

## Настройка переменных окружения
Создайте файл **`.env`** в корневой директории и добавьте в него настройки базы данных:

```
# используются для подключения и создания БД в Docker
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
POSTGRES_DB=mydatabase
DATABASE_URL=postgresql://postgres:postgres@db/mydatabase

# используется для создания БД в Docker
TEST_POSTGRES_DB=test_database
```

---

## Сборка и запуск контейнеров
Соберите и запустите контейнеры в фоновом режиме:
```bash
docker-compose up -d --build
```
Проверить функциальность - http://localhost:8000/docs

---

## Запуск тестов
### Если контейнер запущен, его необходимо остановить
```bash
docker-compose down
```

### Затем изменить параметры в .env
```
# используются для подключения и создания БД в Docker
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
POSTGRES_DB=test_database
DATABASE_URL=postgresql://postgres:postgres@db/test_database

# используется для создания БД в Docker
TEST_POSTGRES_DB=test_database
```

### Снова запустить контейнер
```bash
docker-compose up -d

```

### И запустить тесты
```bash
docker-compose exec web pytest

```
