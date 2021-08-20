#Python_GPA Calculator Program
"Computer Programming Tutor - Aug,2021"

def calculateGPA(grades):
    points = 0
    i = 0
    gradepoint ={"A":4,"A-":3.5,"B+":3.25,"B":3,"B-":2.75,
                 "C+":2.5,"C-":2.25,"D":2,"D-1":1.5,
                 "E":1,"F":0}
        
    if grades != []:
        for grade in grades:
            points += gradepoint[grade]
        gpa = points / len(grades)
        return gpa
    else:
        return None

grades = ["A","B","E","A","A"]
print(calculateGPA(grades))

grades = ["A","B","C+","F","A","B+"]
print(calculateGPA(grades))
grades =  ["B","B","C+","B","A-","B+"]
print(calculateGPA(grades))
