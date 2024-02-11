score = int(input("score:"))
if score >= 90 and score <= 100:
    print ("grado: A")
elif score >= 80 and score < 90:
    print("grado: B")
elif score >= 70 and score < 80:
    print("grado: C")
elif score >= 60 and score < 70:
    print("grado: D")
else:
    print("grado: E")