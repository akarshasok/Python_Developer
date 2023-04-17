import unittest
import script

class testscript(unittest.TestCase):
    def test_input(self):
        guess=5
        answer=5
        val=script.run_guess(guess,answer)
        self.assertTrue(val)
    def test_input2(self):
        guess =7
        answer=5
        val = script.run_guess(guess, answer)
        self.assertFalse(val)
    def test_input3(self):
        guess =12
        answer=5
        val = script.run_guess(guess, answer)
        self.assertFalse(val)
    def test_input4(self):
        val = script.run_guess(7,"aka")
        self.assertFalse(val)
if __name__=='__main__':
    unittest.main()