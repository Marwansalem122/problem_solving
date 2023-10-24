num=float(input())
if 0.0<=num<=25.0:
    print("Interval [0,25]")
elif 25.0<num<=50.0:
    print("Interval (25,50]")
elif 50.0<num<=75.0:
    print("Interval (50,75]")
elif 75.0<num<=100.0:
    print("Interval (75,100]")
else:
    print("Out of Intervals")