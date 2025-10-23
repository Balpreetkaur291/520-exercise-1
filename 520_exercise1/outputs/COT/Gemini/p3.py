def numerical_letter_grade(grades):


   letter_grades = []
  
   # Iterate through each GPA in the input list
   for gpa in grades:
      
       # Check from the highest GPA down
       if gpa >= 4.0:
           letter = "A+"
       elif gpa > 3.7:
           letter = "A"
       elif gpa > 3.3:
           letter = "A-"
       elif gpa > 3.0:
           letter = "B+"
       elif gpa > 2.7:
           letter = "B"
       elif gpa > 2.3:
           letter = "B-"
       elif gpa > 2.0:
           letter = "C+"
       elif gpa > 1.7:
           letter = "C"
       elif gpa > 1.3:
           letter = "C-"
       elif gpa > 1.0:
           letter = "D+"
       elif gpa > 0.7:
           letter = "D"
       elif gpa > 0.0:
           letter = "D-"
       else: # gpa <= 0.0
           letter = "E"
          
       letter_grades.append(letter)
      
   return letter_grades
