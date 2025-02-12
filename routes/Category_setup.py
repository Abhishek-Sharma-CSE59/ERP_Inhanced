import sqlite3

CDB_NAME = "category_base.db"

def create_club_table():
    conn = sqlite3.connect(CDB_NAME)
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS clubs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            category TEXT NOT NULL,
            description TEXT,
            timings TEXT,
            registration_open TEXT,
            venue TEXT,
            leader TEXT,
            leader_contact TEXT,
            achievements TEXT,
            image TEXT
        )
    ''')

    cursor.execute("SELECT COUNT(*) FROM clubs")
    if cursor.fetchone()[0] == 0:
        clubs_data = [
            ("Nritya Kala Dance Club", "Dance", "A cultural dance club promoting Indian classical and folk dances.", "5 PM - 7 PM", "Open", "Auditorium Hall", "Priya Verma", "+91 9823123123", "Won Inter-College Dance Fest 2023", "dance-club.jpg"),
            ("Cyber Security Warriors", "Cyber", "Learn ethical hacking & cybersecurity skills.", "6 PM - 8 PM", "Open", "Lab 101", "Aryan Gupta", "+91 9712312321", "DefCon Finalists 2022", "cyber-club.jpg"),
            ("Shastrarth Debate Club", "Debate", "Improve your public speaking and critical thinking.", "3 PM - 5 PM", "Closed", "Lecture Hall 5", "Sneha Patel", "+91 9812345678", "National Debate Championship 2022", "debate-club.jpg"),
            ("Khel Sports Club", "Sports", "A multi-sports club encouraging participation in various games.", "4 PM - 6 PM", "Open", "Sports Ground", "Rohan Desai", "+91 9809876543", "Winners of College Cricket League 2023", "sports-club.jpg"),("Khel Sports Club", "Sports", "A multi-sports club encouraging participation in various games.", "4 PM - 6 PM", "Open", "Sports Ground", "Rohan Desai", "+91 9809876543", "Winners of College Cricket League 2023", "sports-club.jpg"), ("Fitness Club", "Health & Fitness", "A club promoting physical fitness and wellness.", "6 AM - 8 AM", "Open", "Gymnasium", "Anita Rao", "+91 9898765432", "Best Fitness Club 2023", "fitness-club.jpg"), ("Music Academy", "Music", "A center for learning and practicing music.", "10 AM - 12 PM", "Open", "Music Hall", "Rajiv Kumar", "+91 9786451234", "Best Music Academy of the Year", "music-academy.jpg"), ("Art Circle", "Arts", "A space for artists to collaborate and create.", "2 PM - 5 PM", "Open", "Art Studio", "Sneha Patel", "+91 9812345678", "Exhibited at National Art Fair", "art-circle.jpg"), ("Debate Society", "Debate", "A platform for intellectual discussions and debates.", "3 PM - 5 PM", "Open", "Debate Hall", "Vikas Singh", "+91 9934567890", "Winners of National Debate Competition 2023", "debate-society.jpg"), ("Drama Club", "Drama", "A club fostering drama skills and performances.", "4 PM - 6 PM", "Open", "Theater Room", "Meera Joshi", "+91 9745234678", "Best Play of the Year 2023", "drama-club.jpg"), ("Dance Troupe", "Dance", "A group dedicated to promoting various dance forms.", "5 PM - 7 PM", "Open", "Dance Studio", "Ravi Sharma", "+91 9933445567", "Winner of National Dance Competition", "dance-troupe.jpg"), ("Coding Club", "Technology", "A club for learning and practicing coding.", "7 PM - 9 PM", "Open", "Computer Lab", "Priya Kumar", "+91 9876543210", "Best Coding Projects 2023", "coding-club.jpg"), ("Photography Club", "Photography", "A group for photography enthusiasts to explore their craft.", "8 AM - 10 AM", "Open", "Photography Room", "Karan Mehta", "+91 9922334455", "Winner of Photography Contest 2023", "photography-club.jpg"), ("Cooking Club", "Food & Culinary", "A club dedicated to exploring culinary arts.", "12 PM - 2 PM", "Open", "Kitchen Lab", "Simran Verma", "+91 9056789234", "Top Culinary School 2023", "cooking-club.jpg")
        ]
        cursor.executemany("INSERT INTO clubs (name, category, description, timings, registration_open, venue, leader, leader_contact, achievements, image) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", clubs_data)

    conn.commit()
    conn.close()
    print("Club database initialized!")

if __name__ == "__main__":
    create_club_table()
