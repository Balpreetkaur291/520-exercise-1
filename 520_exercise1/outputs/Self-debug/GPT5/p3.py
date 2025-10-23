from typing import List


def numerical_letter_grade(grades: List[float]) -> List[str]:
   bands = [
       (3.7, "A"),
       (3.3, "A-"),
       (3.0, "B+"),
       (2.7, "B"),
       (2.3, "B-"),
       (2.0, "C+"),
       (1.7, "C"),
       (1.3, "C-"),
       (1.0, "D+"),
       (0.7, "D"),
       (0.0, "D-"),
   ]


   out: List[str] = []
   for g in grades:
       if g == 4.0:
           out.append("A+")
           continue
       if g == 0.0:
           out.append("E")
           continue


       # Apply strict '>' comparisons in descending order
       for cutoff, label in bands:
           if g > cutoff:
               out.append(label)
               break
       else:
           # No band matched: includes negative GPAs
           out.append("E")
   return out
