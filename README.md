# OpenCart Database Testing Framework

Фреймворк для тестирования CRUD операций с базой данных OpenCart.

## Установка зависимостей

```bash
pip install -r requirements.txt
```

## Запуск тестов

```bash
pytest tests/test_customer.py -v \
  --host=localhost \
  --port=3306 \
  --database=opencart_db \
  --user=root \
  --password=your_password
```

## Структура проекта

```
opencart_db_framework/
├── lib/
│   ├── __init__.py          # Инициализация модуля
│   └── db.py                # Функции для работы с БД
├── tests/
│   └── test_customer.py     # Тесты для CRUD операций
├── conftest.py              # Конфигурация pytest и фикстуры
├── requirements.txt         # Зависимости проекта
└── README.md               # Документация
```

## Особенности реализации

- **Динамические тестовые данные**: используются фикстуры с UUID для генерации уникальных данных
- **Автоматическая очистка**: созданные в тестах данные автоматически удаляются
- **Изоляция тестов**: каждый тест работает с уникальными данными
- **Правильный setup**: создание тестовых объектов вынесено в фикстуры

## Пример запуска с Docker MariaDB

```bash
# Запуск контейнера MariaDB
docker run -d -p 3306:3306 --name mariadb-opencart \
  -e MYSQL_ROOT_PASSWORD=root \
  -e MYSQL_DATABASE=opencart_db \
  -e MYSQL_USER=opencart_user \
  -e MYSQL_PASSWORD=secure_password123 \
  mariadb:10.6

# Запуск тестов
pytest tests/test_customer.py -v \
  --host=localhost \
  --port=3306 \
  --database=opencart_db \
  --user=root \
  --password=root
```