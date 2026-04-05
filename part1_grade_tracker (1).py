# part1_grade_tracker.py
# Part 1 Assignment — Student Grade Tracker
# Building a grade tracker using core Python: loops, conditionals, strings, lists


# ─────────────────────────────────────────────
# TASK 1 — Data Parsing & Profile Cleaning
# ─────────────────────────────────────────────

# this is the raw data we were given — names have extra spaces and random casing,
# roll numbers are strings instead of ints, and marks are one big comma-separated string
raw_students = [
    {"name": " ayesha SHARMA ",  "roll": "101", "marks_str": "88, 72, 95, 60, 78"},
    {"name": "ROHIT verma",      "roll": "102", "marks_str": "55, 68, 49, 72, 61"},
    {"name": "  Priya Nair  ",   "roll": "103", "marks_str": "91, 85, 88, 94, 79"},
    {"name": "karan MEHTA",      "roll": "104", "marks_str": "40, 55, 38, 62, 50"},
    {"name": " Sneha pillai ",   "roll": "105", "marks_str": "75, 80, 70, 68, 85"},
]

cleaned_students = []  # I'll build a clean version of the list here

for student in raw_students:
    # strip() removes the extra spaces around the name, title() fixes the casing
    clean_name = student["name"].strip().title()

    # roll was stored as a string like "101", converting it to int so we can use it properly
    clean_roll = int(student["roll"])

    # splitting "88, 72, 95, 60, 78" on ", " gives us ["88", "72", ...] and then
    # I convert each one to int using a list comprehension
    marks_list = [int(m) for m in student["marks_str"].split(", ")]

    # store the cleaned version so I can use it later in other tasks
    cleaned_students.append({
        "name":  clean_name,
        "roll":  clean_roll,
        "marks": marks_list
    })

    # checking if every word in the name is purely alphabetic — no numbers or symbols
    words = clean_name.split()
    is_valid = all(word.isalpha() for word in words)

    if is_valid:
        validity_label = "✓ Valid name"
    else:
        validity_label = "✗ Invalid name"

    # printing the profile card in the format the assignment asked for
    print("================================")
    print(f"Student : {clean_name}   {validity_label}")
    print(f"Roll No : {clean_roll}")
    print(f"Marks   : {marks_list}")
    print("================================")
    print()


# ─────────────────────────────────────────────
# TASK 2 — Marks Analysis Using Loops & Conditionals
# ─────────────────────────────────────────────

# using Ayesha's data as the base student for this task
student_name = "Ayesha Sharma"
subjects     = ["Math", "Physics", "CS", "English", "Chemistry"]
marks        = [88, 72, 95, 60, 78]

print("=" * 40)
print(f"Marks Report — {student_name}")
print("=" * 40)

# zip() lets me loop through both lists together so each subject lines up with its mark
for subject, mark in zip(subjects, marks):
    # checking which grade range the mark falls into using if-elif chain
    if mark >= 90:
        grade = "A+"
    elif mark >= 80:
        grade = "A"
    elif mark >= 70:
        grade = "B"
    elif mark >= 60:
        grade = "C"
    else:
        grade = "F"

    print(f"{subject}: {mark} — {grade}")

print()

# sum() and len() make it easy to get total and average
total_marks   = sum(marks)
average_marks = round(total_marks / len(marks), 2)

# .index(max(...)) gives me the position of the highest mark,
# then I use that position to look up the subject name
highest_index = marks.index(max(marks))
lowest_index  = marks.index(min(marks))

highest_subject = subjects[highest_index]
lowest_subject  = subjects[lowest_index]

print(f"Total Marks           : {total_marks}")
print(f"Average Marks         : {average_marks}")
print(f"Highest Scoring Subject: {highest_subject} ({marks[highest_index]})")
print(f"Lowest Scoring Subject : {lowest_subject} ({marks[lowest_index]})")
print()

# while loop to let the user add new subjects interactively
print("--- Add New Subjects (type 'done' to stop) ---")

new_subjects = []
new_marks    = []

while True:
    subject_input = input("Enter subject name (or 'done' to finish): ").strip()

    # "done" is the exit signal
    if subject_input.lower() == "done":
        break

    mark_input = input(f"Enter marks for {subject_input} (0–100): ").strip()

    # isdigit() checks if the input is actually a number before converting
    # this prevents a crash if someone types letters instead of a number
    if not mark_input.isdigit():
        print("⚠ Warning: Invalid input — marks must be a number. Entry skipped.\n")
        continue

    mark_value = int(mark_input)

    # even if it's a number, it still needs to be in the valid 0–100 range
    if mark_value < 0 or mark_value > 100:
        print("⚠ Warning: Marks must be between 0 and 100. Entry skipped.\n")
        continue

    new_subjects.append(subject_input)
    new_marks.append(mark_value)
    print(f"  Added: {subject_input} — {mark_value}\n")

# combining original marks with newly added ones to get the updated average
all_marks   = marks + new_marks
updated_avg = round(sum(all_marks) / len(all_marks), 2)

print(f"\nNew subjects added : {len(new_subjects)}")
print(f"Updated average    : {updated_avg}")
print()


# ─────────────────────────────────────────────
# TASK 3 — Class Performance Summary
# ─────────────────────────────────────────────

# each entry is a tuple of (student name, list of marks)
class_data = [
    ("Ayesha Sharma", [88, 72, 95, 60, 78]),
    ("Rohit Verma",   [55, 68, 49, 72, 61]),
    ("Priya Nair",    [91, 85, 88, 94, 79]),
    ("Karan Mehta",   [40, 55, 38, 62, 50]),
    ("Sneha Pillai",  [75, 80, 70, 68, 85]),
]

# using f-string formatting to align the columns neatly
# <20 means left-align in 20 chars, >7 means right-align in 7 chars
print(f"{'Name':<20} | {'Average':>7} | {'Status'}")
print("-" * 42)

student_averages = []  # collecting (name, avg) pairs here for use after the loop
pass_count  = 0
fail_count  = 0

for name, student_marks in class_data:
    avg    = round(sum(student_marks) / len(student_marks), 2)
    # pass if average is 60 or above, otherwise fail
    status = "Pass" if avg >= 60 else "Fail"

    student_averages.append((name, avg))

    # keeping a running count of pass/fail as I go through each student
    if status == "Pass":
        pass_count += 1
    else:
        fail_count += 1

    print(f"{name:<20} | {avg:>7.2f} | {status}")

print()

# max() with a lambda lets me find the student with the highest average
topper_name, topper_avg = max(student_averages, key=lambda x: x[1])

# class average = average of all five students' averages
class_avg = round(sum(a for _, a in student_averages) / len(student_averages), 2)

print(f"Students Passed : {pass_count}")
print(f"Students Failed : {fail_count}")
print(f"Class Topper    : {topper_name} ({topper_avg})")
print(f"Class Average   : {class_avg}")
print()


# ─────────────────────────────────────────────
# TASK 4 — String Manipulation Utility
# ─────────────────────────────────────────────

essay = "  python is a versatile language. it supports object oriented, functional, and procedural programming. python is widely used in data science, web development, and automation. many developers prefer python for its simplicity and readability.  "

# step 1: remove the extra spaces at the start and end
# storing this as clean_essay and using it for all the steps below
clean_essay = essay.strip()
print(f"Step 1 — Stripped Essay:\n{clean_essay}\n")

# step 2: title() capitalises the first letter of every word
title_essay = clean_essay.title()
print(f"Step 2 — Title Case:\n{title_essay}\n")

# step 3: count how many times "python" appears
# since clean_essay is already all lowercase after step 1, I don't need .lower() again
python_count = clean_essay.count("python")
print(f"Step 3 — 'python' appears {python_count} time(s)\n")

# step 4: replace every "python" with "Python 🐍"
# again using clean_essay (lowercase) so the replace catches every occurrence
replaced_essay = clean_essay.replace("python", "Python \U0001f40d")
print(f"Step 4 — Replaced Essay:\n{replaced_essay}\n")

# step 5: split on ". " (period + space) to get individual sentences as a list
sentences = clean_essay.split(". ")
print(f"Step 5 — Sentences list:\n{sentences}\n")

# step 6: print each sentence numbered from 1
# if a sentence doesn't already end with ".", add one
print("Step 6 — Numbered Sentences:")
for i, sentence in enumerate(sentences, start=1):
    if not sentence.endswith("."):
        sentence = sentence + "."
    print(f"{i}. {sentence}")
