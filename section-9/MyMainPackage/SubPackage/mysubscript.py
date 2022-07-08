
from ntpath import basename

def sub_report():

    # This isn't part of the lesson. Adding calling the actual filename
    # via the special variable __file__ and th above imported basename 
    # function.
    print(f"I am a function in {basename(__file__)}")