def check_winners(scores, student_score):
    top_scores = sorted(scores, reverse=True)[:3]
    if student_score in top_scores:
        print("Вы в тройке победителей!")
    else:
        print("Вы не попали в тройку победителей.")

scores = [20, 48, 52, 38, 36, 13, 7, 41, 34, 24, 5, 51, 9, 14, 28]
student_score = 52
check_winners(scores, student_score)