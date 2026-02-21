import random
import json
from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

# ===================================
# MASTER INPUT LISTS
# ===================================

subjects_list = [
    "Mathematics","Physics","Chemistry","Biology","Computer Science",
    "Statistics","Economics","Psychology","Political Science",
    "History","Geography","Accounting","Business Studies",
    "Law","Design","AI","Data Science","Robotics",
    "Electronics","Medicine"
]

skills_list = [
    "Problem Solving","Critical Thinking","Leadership",
    "Communication","Teamwork","Creativity","Python",
    "Java","Machine Learning","Cloud Computing",
    "Cybersecurity","Data Analysis","Marketing",
    "Negotiation","Public Speaking","Research",
    "Strategic Planning","Financial Modeling",
    "CAD","Project Management"
]

interests_list = [
    "Technology","Innovation","Healthcare","Finance",
    "Startups","Public Service","Art","Media",
    "Law","Defense","Science","Research",
    "Gaming","Automation","Robotics",
    "Helping People","Psychology","Travel",
    "Environment","Space"
]

# ===================================
# CAREER PROFILES WITH DETAILS
# ===================================

careers = [
    {
        "name": "Software Engineer",
        "subjects": ["Computer Science", "Mathematics"],
        "skills": ["Python", "Problem Solving", "Critical Thinking"],
        "interests": ["Technology", "Automation"],
        "description": "Designs, builds, and maintains software applications and systems used across industries."
    },
    {
        "name": "Data Scientist",
        "subjects": ["Statistics", "Mathematics", "Computer Science"],
        "skills": ["Python", "Data Analysis", "Machine Learning"],
        "interests": ["Technology", "Research"],
        "description": "Analyzes complex data to uncover patterns, insights, and trends that guide decision-making."
    },
    {
        "name": "AI Engineer",
        "subjects": ["AI", "Computer Science", "Mathematics"],
        "skills": ["Python", "Machine Learning", "Problem Solving"],
        "interests": ["Technology", "Innovation"],
        "description": "Develops intelligent systems that can learn, reason, and automate tasks."
    },
    {
        "name": "Psychologist",
        "subjects": ["Psychology", "Biology"],
        "skills": ["Research", "Communication", "Critical Thinking"],
        "interests": ["Helping People", "Healthcare"],
        "description": "Studies human behavior and mental processes to help individuals improve mental well-being."
    },
    {
        "name": "Business Analyst",
        "subjects": ["Economics", "Statistics", "Business Studies"],
        "skills": ["Data Analysis", "Communication", "Strategic Planning"],
        "interests": ["Finance", "Startups"],
        "description": "Bridges business needs and data insights to improve processes and strategy."
    },
    {
        "name": "Mechanical Engineer",
        "subjects": ["Physics", "Mathematics"],
        "skills": ["Problem Solving", "CAD", "Project Management"],
        "interests": ["Engineering", "Robotics"],
        "description": "Designs and builds mechanical systems, machines, and tools."
    },
    {
        "name": "Doctor",
        "subjects": ["Biology", "Chemistry", "Medicine"],
        "skills": ["Critical Thinking", "Research", "Communication"],
        "interests": ["Healthcare", "Helping People"],
        "description": "Diagnoses, treats, and prevents illnesses to improve patient health."
    },
    {
        "name": "Lawyer",
        "subjects": ["Law", "Political Science"],
        "skills": ["Communication", "Negotiation", "Critical Thinking"],
        "interests": ["Law", "Public Service"],
        "description": "Advises and represents individuals or organizations in legal matters."
    }
]

# ===================================
# ROUTES
# ===================================

@app.route("/")
def home():
    return render_template(
        "index.html",
        subjects=subjects_list,
        skills=skills_list,
        interests=interests_list
    )

@app.route("/match", methods=["POST"])
def match():
    data = request.get_json()

    selected_subjects = data.get("subjects", [])
    selected_skills = data.get("skills", [])
    selected_interests = data.get("interests", [])

    results = []

    for career in careers:
        score = 0
        score += len(set(selected_subjects) & set(career["subjects"]))
        score += len(set(selected_skills) & set(career["skills"]))
        score += len(set(selected_interests) & set(career["interests"]))

        if score > 0:
            results.append({
                "name": career["name"],
                "match": f"{score * 5}% Match",
                "description": career["description"]
            })

    results.sort(
        key=lambda x: int(x["match"].replace("% Match", "")),
        reverse=True
    )

    return jsonify(results[:10])


if __name__ == "__main__":
    app.run(debug=True)