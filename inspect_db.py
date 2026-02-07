
import sqlite3
import json

def inspect_db():
    try:
        conn = sqlite3.connect('test.db')
        cursor = conn.cursor()

        print("--- Tables ---")
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = cursor.fetchall()
        for table in tables:
            print(f"Table: {table[0]}")
            cursor.execute(f"PRAGMA table_info({table[0]})")
            columns = cursor.fetchall()
            for col in columns:
                print(f"  Col: {col[1]} ({col[2]})")

        print("\n--- Recent Tasks ---")
        cursor.execute("SELECT id, title, position FROM task ORDER BY id DESC LIMIT 5;")
        tasks = cursor.fetchall()
        for t in tasks:
            print(f"ID: {t[0]}, Title: {t[1]}, Position: {t[2]}")

        conn.close()
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    inspect_db()
