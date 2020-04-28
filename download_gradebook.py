from canvasapi import Canvas
from datetime import datetime
from dotenv import load_dotenv
import csv
import os
from upload_to_drive import upload_csv

load_dotenv()

API_URL = os.getenv("CANVAS_URL")
API_KEY = os.getenv("CANVAS_TOKEN")

if not API_KEY:
    raise Exception("CANVAS_TOKEN not found, did you set your environment variable?")

canvas = Canvas(API_URL, API_KEY)

# TODO: Run the code below for every active course, and add the course name to the filename
#course_id = 16916  # Erin's course_id
course_id = 9558   # Testing on Daniel's course

course = canvas.get_course(course_id)

print("Downloading gradebook for {}".format(course.name))

submission_by_id = dict()  # (assignment.id, student.id) -> submission
student_set = set()

assignments = list(course.get_assignments())
assignment_by_id = {a.id: a for a in assignments}

for assignment in assignments:
    students = list(assignment.get_gradeable_students())
    student_set |= set(students)    # Issue: this seems to include students that dropped midway in the class

    for submission in assignment.get_submissions():
        submission_by_id[(assignment.id, submission.user_id)] = submission


def student_sort_key(student):
    name = student.display_name
    tokens = name.split()
    last, first = tokens[1], tokens[0]
    return (last, first)


sorted_students = sorted(students, key=student_sort_key)

date = datetime.today().strftime('%Y-%m-%d')
# TODO: Add course number, and semester/quarter to filename
filename = 'gradebook_{}.csv'.format(date)

with open(filename, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Student Name'] + [a.name for a in assignments])
    writer.writerow([''] + [a.points_possible for a in assignments])

    for student in sorted_students:
        scores = []
        for assignment in assignments:
            try:
                # It's possible not every student made a submission here
                score = submission_by_id[(assignment.id, student.id)].score
                score = "" if score is None else str(score)
            except KeyError:
                score = ""
            
            scores.append(score)

        writer.writerow([student.display_name] + scores)

# Upload to Google Drive
upload_csv(filename)