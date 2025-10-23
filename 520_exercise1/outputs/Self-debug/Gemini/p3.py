def numerical_letter_grade(grades):
   """
   Converts a list of numerical GPAs (floats) into a list of corresponding
   letter grades based on the teacher's grading table.


   The logic iterates through grades from highest to lowest threshold.
   Using 'elif' blocks handles the inclusive upper boundaries implicitly.


   Args:
       grades (list[float]): A list of GPAs to be converted.


   Returns:
       list[str]: A list of letter grades.
   """
  
   def _get_single_grade(gpa):
       """Helper function to convert a single GPA."""
      
       # Exact Match: 4.0 -> A+
       if gpa == 4.0:
           return 'A+'
      
       # Use descending order of thresholds (> X)
       elif gpa > 3.7:
           return 'A'
       elif gpa > 3.3:
           return 'A-'
       elif gpa > 3.0:
           return 'B+'
       elif gpa > 2.7:
           return 'B'
       elif gpa > 2.3:
           return 'B-'
       elif gpa > 2.0:
           return 'C+'
       elif gpa > 1.7:
           return 'C'
       elif gpa > 1.3:
           return 'C-'
       elif gpa > 1.0:
           return 'D+'
       elif gpa > 0.7:
           return 'D'
       elif gpa > 0.0:
           return 'D-'
      
       # Exact Match: 0.0 -> E
       elif gpa == 0.0:
           return 'E'
      
       # Fallback for unexpected inputs (e.g., negative GPA)
       else:
           return 'N/A'


   # Apply the conversion helper function to all items in the input list using a list comprehension
   return [_get_single_grade(gpa) for gpa in grades]