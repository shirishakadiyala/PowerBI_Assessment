university_data = {
    "S101": {
        "name": "Alice Johnson",
        "major": "Computer Science",
        "courses": {
            "Python101": {"midterm": 88, "final": 92, "project": 94},
            "Math201": {"midterm": 78, "final": 85, "project": 80}
        }
    },
    "S102": {
        "name": "Bob Smith",
        "major": "Mathematics",
        "courses": {
            "Math201": {"midterm": 90, "final": 93, "project": 88},
            "Stats101": {"midterm": 84, "final": 80, "project": 85}
        }
    },
    "S103": {
        "name": "Clara Lopez",
        "major": "Physics",
        "courses": {
            "Physics101": {"midterm": 75, "final": 82, "project": 78},
            "Math201": {"midterm": 70, "final": 72, "project": 68}
        }
    }
}

#  Q1: Print all student names and their majors
for student_id, info in university_data.items():
    print(f"{info['name']} : {info['major']}")

# Q2: Average score per course per student
for student_id, info in university_data.items():
    print(f"Student: {info['name']}")
    for course, scores in info['courses'].items():
        avg = sum(scores.values()) / len(scores)
        print(f"  {course}: Average Score = {avg:.2f}")


# Q3: Find students who scored >90 in final of Python101
for student_id, info in university_data.items():
    courses = info['courses']
    if "Python101" in courses and courses["Python101"].get("final", 0) > 90:
        print(info["name"])


# Q4: Add new course AI101 for student S101
university_data["S101"]["courses"]["AI101"] = {"midterm": 89, "final": 91, "project": 95}
print(f"S101 updated courses: {list(university_data['S101']['courses'].keys())}")

# Q5: Print average for each course across all students
print("Average score for each course ")

# # Helper to accumulate scores
from collections import defaultdict

course_scores = defaultdict(lambda: {"total": 0, "count": 0})

for details in university_data.values():
    for course, assessments in details["courses"].items():
        avg = sum(assessments.values()) / len(assessments)
        course_scores[course]["total"] += avg
        course_scores[course]["count"] += 1

for course, data in course_scores.items():
    overall_avg = data["total"] / data["count"]
    print(f"{course}: {overall_avg:.2f}")

