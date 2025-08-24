def printGrade():
 a=int(input())
 if(a>=90):
    print("Grade A")
 elif(a>=70 and a<90):
    print("Grade B")
 elif(a>=50 and a<70):
    print("Grade C")
 elif(a>=35 and a<50):
    print("Grade D")
 else:
    print("Fail")
printGrade()