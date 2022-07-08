#
# one.py
#
from ntpath import basename

# A global function definition at indentation level 0
def func():
    
    # This isn't part of the lesson. Adding calling the actual filename
    # via the special variable __file__ and th above imported basename 
    # function.
    print(f"func() in {basename(__file__)}")

# A global print statement at indentation level 0
print(f"Top level in {basename(__file__)}")

if __name__ == "__main__":
    print(f"{basename(__file__)} is being executed directly")

else:
    print(f"{basename(__file__)} has been imported")