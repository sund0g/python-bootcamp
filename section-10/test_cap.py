
# Import the unittest module
import unittest

# Import the file we want to unit test, e.g. cap.py
import cap

# create a class containing the unit tests, (as methods)
#
# TestCap must inherit the TestCase class that is part of unittest
#
class TestCap(unittest.TestCase):
    
    # Create unit test method from simple to complex

    def test_one_word(self):
        text = 'python'

        # test cap_text() by calling it from cap.py
        result = cap.cap_text(text)

        # provide the expected results
        self.assertEqual(result, 'Python')

    def test_multiple_words(self):
        text = "monty python"

        # test cap_text() by calling it from cap.py
        result = cap.cap_text(text)

        # provide the expected results
        self.assertEqual(result, "Monty Python")

if __name__ == "__main__":
    unittest.main()