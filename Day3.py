subject1=int(input("Enter subject 1 marks:"))
subject2=int(input("Enter subject 2 marks:"))
subject3=int(input("Enter subject 3 marks:"))
average=(subject1+subject2+subject3)/3
# print(average)
if (average<=100):
    if average>=90:
        print("A Grade")
    elif 80<=average<90:
        print("B Grade")
    elif 70<=average<80:
        print("C Grade")
    else:
        print("Fail")
else:
    print("Invalid result")