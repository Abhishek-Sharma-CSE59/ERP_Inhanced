from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3
import os
from os.path import dirname, abspath
from routes.gemini_api import get_ai_suggestions
from routes.gemini_api import ask_gemini

BASE_DIR = dirname(abspath(__file__))

app = Flask(__name__ , template_folder='templates' )
app.secret_key = "supersecretkey"
TEMPLATES_DIR = os.path.join(BASE_DIR, "templates")

DB_NAME = "database.db"
CDB_NAME = "category_base.db"
FDB_NAME = os.path.abspath("faculty_database.db")



def validate_login(username, password):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))
    user = cursor.fetchone()
    conn.close()
    return user is not None



@app.route("/my-events")
def my_events():
    events = [
        {
            "name": "Bharat-Tech-Xperience2.0",
            "venue": "SVIET College, Chandigarh",
            "time": "Feburary 8, 2025, 9:30 AM - Feburary 9 2025 ,5:00 PM",
            "description": "A 30-hour coding marathon where developers solve real-world problems.",
            "timeline": [
                "📝 9:30 AM - Registration & Setup",
                "10:00 AM - Welcome!",
                "10:10 AM - The Reason Why We are All Here",
                "💻 10:20 AM - LET THE HACKING BEGIN!",
                "🍔 1:00 PM - Lunch Break",
                "3:00 PM - Audience Feedback Session",
                "🏆 6:00 PM - Team progress report",
                "9:00 PM - Dinner & Networking",
                "🌞 8:00 AM - Breakfast",
                "🎉 10:00 AM - Book your Demo slot",
                "🎤 11:00 AM How to make your Pitch",
                "1:00 PM - Lunch Break",
                "🎉 01:45 PM - Hacking Ends",
                "🎉 02:00 PM - PITCH SESSION",
                "🏆 04:00 PM - The judges retire to decide the winners – drinks are provided for the participants.",
                "🎉 04:30 PM - Prizegiving & quick “Thank You” speech.",
                "🎉 05:00 PM - Event Ends"


            ]
        }
    ]
    return render_template("my_events.html", events=events)

@app.route("/campus-map")
def campus_map():
    return render_template("campus_map.html")


def get_clubs(category):
    conn = sqlite3.connect(CDB_NAME)
    cursor = conn.cursor()

    category = category.strip().lower()
    print(f"🔍 Searching for category: {category}")  
    cursor.execute("SELECT * FROM clubs WHERE LOWER(category) = LOWER(?)", (category,))
    clubs = cursor.fetchall()

    if not clubs:
        print(f"No direct category match found, searching in descriptions...")
        cursor.execute("SELECT * FROM clubs WHERE LOWER(description) LIKE LOWER(?)", (f"%{category}%",))
        clubs = cursor.fetchall()

    conn.close()

    print(f"Clubs found: {clubs}") 
    return clubs


@app.route("/search", methods=["GET"])
def search_clubs():
    user_query = request.args.get("query", "").strip().lower()
    print(f"User search query: {user_query}") 

    if not user_query:
        flash("Please enter a search term!", "error")
        return render_template("category.html", clubs=[], category="Search Results")


    suggested_categories = get_ai_suggestions(user_query)
    print(f"AI suggested categories: {suggested_categories}")  

    clubs = []

    if suggested_categories:
        conn = sqlite3.connect(CDB_NAME)
        cursor = conn.cursor()

        placeholders = ', '.join(['?'] * len(suggested_categories))
        query = f"SELECT * FROM clubs WHERE LOWER(category) IN ({placeholders})"
        cursor.execute(query, tuple(suggested_categories))
        clubs = cursor.fetchall()
        conn.close()

        print(f"Clubs found (via category match): {clubs}") 

    if not clubs:
        print("No category match found, searching in descriptions...")
        conn = sqlite3.connect(CDB_NAME)
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM clubs WHERE LOWER(description) LIKE ?", (f"%{user_query}%",))
        clubs = cursor.fetchall()
        conn.close()

        print(f"Clubs found (via description match): {clubs}") 

    if not clubs:
        flash("No clubs matched your search!", "error")

    return render_template("category.html", clubs=clubs, category="Search Results")


@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        if validate_login(username, password):
            return redirect(url_for("home"))

        flash("Invalid Username or Password!", "error")

    return render_template("login.html")

@app.route("/home")
def home():
    return render_template("home_page.html")

@app.route("/academic-calendar")
def academic_calendar():
    return render_template("academic_calendar.html")

@app.route("/category/<category>")
def category_page(category):
    clubs = get_clubs(category)

    if not clubs:
        flash(f"No clubs found for '{category}'!", "error")

    return render_template("category.html", clubs=clubs, category=category)

@app.route("/club/<int:club_id>")
def club_details(club_id):
    conn = sqlite3.connect(CDB_NAME)
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM clubs WHERE id = ?", (club_id,))
    club = cursor.fetchone()
    
    conn.close()

    if not club:
        return "Club not found", 404

    return render_template("club.html", club=club)


@app.route("/faculty")
def faculty_page():
    conn = sqlite3.connect(FDB_NAME)
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM faculty")
    faculties = cursor.fetchall()
    
    conn.close()

    return render_template("faculty.html", faculties=faculties, template_folder=TEMPLATES_DIR)



@app.route("/chatbot", methods=["POST"])
def chatbot():
    data = request.json
    user_message = data.get("message", "").strip()

    if not user_message:
        return {"response": "⚠️ Please enter a question!"}, 400

    ai_response = ask_gemini(user_message)
    
    return {"response": ai_response}


@app.route("/campus-details")
def campus_details():
    return render_template("campus_details.html")

@app.route("/submit-feedback/<int:club_id>", methods=["POST"])
def submit_feedback(club_id):
    return redirect(url_for("club_details", club_id=club_id))


if __name__ == "__main__":
    app.run(debug=True)
