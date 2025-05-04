from decouple import config
import psycopg2

try:
    conn = psycopg2.connect(
        dbname=config('DB_NAME'),
        user=config('DB_USER'),
        password=config('DB_PASSWORD'),
        host=config('DB_HOST')
    )
    print("✅ Подключение к БД прошло успешно!")
except Exception as e:
    print("❌ Ошибка подключения:", str(e))