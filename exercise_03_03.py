score = input("Enter Score: ")
fscore = float(score)
if fscore > 1.0 :
    print("Please enter a value between 0.0 and 1.0")
    quit()
elif fscore < 0.0 :
    print("Please enter a value between 0.0 and 1.0")
    quit()
elif fscore >= 0.9 :
    grade = "A"
elif fscore >= 0.8 :
    grade = "B"
elif fscore >= 0.7 :
    grade = "C"
elif fscore >= 0.6 :
    grade = "D"
elif fscore < 0.6 :
    grade = "F"
print(grade)
