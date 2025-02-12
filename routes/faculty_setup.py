import sqlite3

FDB_NAME = "faculty_database.db"

def create_faculty_table():
    conn = sqlite3.connect(FDB_NAME)
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS faculty (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            department TEXT NOT NULL,
            photo TEXT NOT NULL,
            email TEXT NOT NULL,
            phone TEXT NOT NULL,
            qualification TEXT NOT NULL
        )
    ''')

    cursor.execute("SELECT COUNT(*) FROM faculty")
    if cursor.fetchone()[0] == 0:
        faculty_data = [
            ("Dr. Ravi Kapoor", "Computer Science", "faculty1.jpg", "ravi.kapoor@university.edu", "+91 9898989898", "PhD in Artificial Intelligence"),
            ("Prof. Meera Nair", "Mathematics", "faculty2.jpg", "meera.nair@university.edu", "+91 9876543211", "MSc in Pure Mathematics"),
            ("Dr. Suresh Reddy", "Physics", "faculty3.jpg", "suresh.reddy@university.edu", "+91 9123456789", "PhD in Quantum Mechanics"),
            ("Prof. Anjali Sharma", "Mechanical Engineering", "faculty4.jpg", "anjali.sharma@university.edu", "+91 9812345678", "MTech in Thermal Engineering"),("Dr. Anjali Sharma", "Computer Science", "faculty2.jpg", "anjali.sharma@university.edu", "+91 9876543210", "PhD in Machine Learning"), ("Dr. Neeraj Kumar", "Physics", "faculty3.jpg", "neeraj.kumar@university.edu", "+91 9977453321", "PhD in Quantum Mechanics"), ("Prof. Sunita Reddy", "Mathematics", "faculty4.jpg", "sunita.reddy@university.edu", "+91 9888776655", "MSc in Pure Mathematics"), ("Dr. Mohan Raj", "Electrical Engineering", "faculty5.jpg", "mohan.raj@university.edu", "+91 9999888777", "PhD in Power Systems"), ("Dr. Priya Patel", "Biology", "faculty6.jpg", "priya.patel@university.edu", "+91 9899887766", "PhD in Biotechnology"), ("Prof. Sandeep Mehta", "Civil Engineering", "faculty7.jpg", "sandeep.mehta@university.edu", "+91 9944556677", "MTech in Structural Engineering"), ("Dr. Aarti Verma", "Psychology", "faculty8.jpg", "aarti.verma@university.edu", "+91 9888778899", "PhD in Cognitive Psychology"), ("Dr. Arvind Jain", "Mechanical Engineering", "faculty9.jpg", "arvind.jain@university.edu", "+91 9556677889", "PhD in Thermal Engineering"), ("Dr. Meera Gupta", "Chemistry", "faculty10.jpg", "meera.gupta@university.edu", "+91 9333445566", "PhD in Organic Chemistry"), ("Prof. Vijay Singh", "Economics", "faculty11.jpg", "vijay.singh@university.edu", "+91 9444667788", "MA in Economics")
        ]
        cursor.executemany("INSERT INTO faculty (name, department, photo, email, phone, qualification) VALUES (?, ?, ?, ?, ?, ?)", faculty_data)

    conn.commit()
    conn.close()
    print("Faculty database initialized!")

if __name__ == "__main__":
    create_faculty_table()
