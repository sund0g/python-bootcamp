#
# two.py
#
from ntpath import basename
import one

print(f"Top level in {basename(__file__)}")

one.func()

if __name__ == "__main__":
    print(f"{basename(__file__)} is being executed directly")

else:
    print(f"{basename(__file__)} has been imported")