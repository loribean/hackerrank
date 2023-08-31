import rick_improved
import unittest
import random
import string

def generate_random_string(length):
    alphabet = string.ascii_lowercase
    result = []

    for _ in range(length):
         #Generate a random string that contains only lowercase letters and question marks
        #and each adjacent letter is different
        if random.random() < 0.5:
            result.append("?")
        else:
            letter = random.choice(alphabet)
            previous = result[_-1] if _ > 0 else None
            if letter == previous:
                result.append("?")
            else:
                result.append(letter)
    return ''.join(result)


class TestSolution(unittest.TestCase):
    def test_case_one(self):
        testcase = "ab???"
        result = rick_improved.solution(testcase)
        #assert that string does not contain any question marks
        self.assertEqual(result.count("?"), 0)
        #assert that the string does not contain any adjacent letters that are the same
        for i in range(len(result) - 1):
            self.assertNotEqual(result[i], result[i+1])

    def test_case_five(self):
        # Test with random input
        testcase = generate_random_string(100)
        result = rick_improved.solution(testcase)
        self.assertEqual(result.count("?"), 0)
        for i in range(len(result) - 1):
            self.assertNotEqual(result[i], result[i+1])

    

if __name__ == '__main__':
    unittest.main()