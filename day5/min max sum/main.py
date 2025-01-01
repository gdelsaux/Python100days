student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 55, 91, 64, 89]

# Total score using sum()
total_score = sum(student_scores)
print(f"total student score: {total_score}")

# Find the highest using max()
highest_score = max(student_scores)
print(f"highest score: {highest_score}")

# Find the lowest score using min()
lowest_score = min(student_scores)
print(f"lowest score: {lowest_score}")

# Exercise: find the highest score without using max()
temp_highest_score = 0
for score in student_scores:
    if score > temp_highest_score:
        temp_highest_score = score
print(f"highest score: {temp_highest_score}")