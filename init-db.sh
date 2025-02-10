# init-db.sh
set -e

# Создание основной базы данных
if ! psql -U "$POSTGRES_USER" -lqt | cut -d \| -f 1 | grep -qw "$POSTGRES_DB"; then
  echo "Creating main database..."
  psql -U "$POSTGRES_USER" -c "CREATE DATABASE $POSTGRES_DB;"
else
  echo "Main database already exists."
fi

# Создание тестовой базы данных
if ! psql -U "$POSTGRES_USER" -lqt | cut -d \| -f 1 | grep -qw "$TEST_POSTGRES_DB"; then
  echo "Creating test database..."
  psql -U "$POSTGRES_USER" -c "CREATE DATABASE $TEST_POSTGRES_DB;"
else
  echo "Test database already exists."
fi
