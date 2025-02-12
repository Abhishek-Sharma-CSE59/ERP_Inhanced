import sqlite3

DB_NAME = "database.db"

def create_user_table():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL,
            full_name TEXT NOT NULL,
            email TEXT NOT NULL,
            phone TEXT NOT NULL,
            role TEXT NOT NULL
        )
    ''')

    cursor.execute("SELECT COUNT(*) FROM users")
    if cursor.fetchone()[0] == 0:
        users_data = [
            ("user1", "password123", "Rahul Sharma", "rahul.sharma@example.com", "+91 9876543210", "Student"),
            ("user2", "securePass", "Ananya Iyer", "ananya.iyer@example.com", "+91 9123456789", "Faculty"),
            ("admin", "admin123", "Vikram Mehta", "admin@example.com", "+91 9000000000", "Admin")
        ]
        cursor.executemany("INSERT INTO users (username, password, full_name, email, phone, role) VALUES (?, ?, ?, ?, ?, ?)", users_data)

    conn.commit()
    conn.close()
    print("User database initialized!")

if __name__ == "__main__":
    create_user_table()
