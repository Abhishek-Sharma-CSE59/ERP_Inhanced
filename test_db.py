import sqlite3

CDB_NAME = "category_base.db"

def check_clubs():
    conn = sqlite3.connect(CDB_NAME)
    cursor = conn.cursor()
    
    cursor.execute("SELECT * FROM clubs")
    clubs = cursor.fetchall()
    
    conn.close()

    if clubs:
        print("✅ Clubs Found in category_base.db:")
        for club in clubs:
            print(club)
    else:
        print("❌ No clubs found in category_base.db!")

if __name__ == "__main__":
    check_clubs()
