# String Evaluation
from samwise import pb
s_var = "James Bond"
pb(s_var,"Original text")
pb(f"{s_var[2::-1]}","Start at 3rd character and go backwards to the end: var[2::-1]")
