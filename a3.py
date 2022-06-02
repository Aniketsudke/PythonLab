Name = input("Name of studnet :")
ENG = int(input("Enter your ENG Marks:"))
EGR = int(input("Enter your EGR Marks:"))
AP = int(input("Enter your AP Marks:"))
LDC = int(input("Enter your LDC Marks:"))
SON = int(input("Enter your SON Marks:"))
print("<----------Annual Result---------->\n")
print("Student Name : ", Name)
print("\n  Course Marks")

print("\tENG\t", ENG)
print("\tEGR\t", EGR)
print("\tAP \t", AP)
print("\tLDC\t", LDC)
print("\tSON\t", SON)
per = (ENG + EGR + AP + LDC + SON)/5
print("Percentage :", per)
if ENG > 39:
    if EGR > 39:
        if AP > 39:
            if LDC > 39:
                if SON > 39:
                    if per >= 75:
                        print("Grade : Distinction")
                    elif per >= 60 and per < 75:
                        print("Grade : First Class")
                    elif per >=50 and per < 60:
                        print("Grade : Second Class")
                    elif per >=40 and per <50:
                        print("Grade : Pass Class")
                else:
                    print("Garde : Fail")
            else:
                print("Garde : Fail")
        else:
            print("Garde : Fail")
else:
    print("Garde : Fail")
