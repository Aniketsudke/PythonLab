ENG =   int(input("Enter the marks of ENG(Out of 100) :"))
EGR =   int(input("Enter the marks of EGR(Out of 100) :"))
AP =   int(input("Enter the marks of AP(Out of 100) :"))
LDC =   int(input("Enter the marks of LDC(Out of 100) :"))
SON =   int(input("Enter the marks of SON(Out of 100) :"))

per = (ENG + EGR + AP + LDC + SON)/5
print("<----------Semister I Result---------->")
print("\tCourse \tMarks")
print("\tENG\t", ENG)
print("\tEGR\t", EGR)
print("\t AP\t", AP)
print("\tLDC\t", LDC)
print("\tSON\t", SON)

print("Percentage :", per)

if ENG>=40 :
    if EGR>=40 :
        if AP>=40 :
            if LDC>=40 :
                if SON>=40 :
                    if per>=75 :
                        print("Grade : Distinction")
                    elif per>=60 and per<75 :
                        print("Grade : First Class")
                    elif per>=50 and per<60 :
                        print("Grade : Second Class")
                    elif per>=40 and per<50 :
                        print("Grade : Pass Class")
                else :
                    print("Grade : Fail Class")
            else :
                    print("Grade : Fail Class")
        else :
                    print("Grade : Fail Class")
    else :
                    print("Grade : Fail Class")
else :
                    print("Grade : Fail Class")

    

