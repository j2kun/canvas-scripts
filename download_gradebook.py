from canvasapi import Canvas
from datetime import datetime
from dotenv import load_dotenv
import csv
import os

load_dotenv()

API_URL = os.getenv("CANVAS_URL")
API_KEY = os.getenv("CANVAS_TOKEN")

if not API_KEY:
    raise Exception("CANVAS_TOKEN not found, did you set your environment variable?")

canvas = Canvas(API_URL, API_KEY)

# TODO: Run the code below for every active course, and add the course name to the filename
course_id = 16916

course = canvas.get_course(course_id)

print("Downloading gradebook for {}".format(course.name))

submission_by_id = dict()  # (assignment.id, student.id) -> submission
student_set = set()

assignments = list(course.get_assignments())
assignment_by_id = {a.id: a for a in assignments}

for assignment in assignments:
    students = list(assignment.get_gradeable_students())
    student_set |= set(students)

    for submission in assignment.get_submissions():
        submission_by_id[(assignment.id, submission.user_id)] = submission


def student_sort_key(student):
    name = student.display_name
    tokens = name.split()
    last, first = tokens[1], tokens[0]
    return (last, first)


sorted_students = sorted(students, key=student_sort_key)

date = datetime.today().strftime('%Y-%m-%d')
filename = 'gradebook_{}.csv'.format(date)
with open(filename, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Student Name'] + [a.name for a in assignments])
    writer.writerow([''] + [a.points_possible for a in assignments])

    for student in sorted_students:
        scores = []
        for assignment in assignments:
            score = submission_by_id[(assignment.id, student.id)].score
            score = "" if score is None else str(score)
            scores.append(score)

        writer.writerow([student.display_name] + scores)


# TODO: upload to Google drive
