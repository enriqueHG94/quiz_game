import unittest
from unittest.mock import patch
from io import StringIO
from quiz_brain import QuizBrain
from question_model import Question


class TestQuizBrain(unittest.TestCase):
    def setUp(self):
        self.question1 = Question("A slug's blood is green.", "True")
        self.question2 = Question("The loudest animal is the African Elephant.", "False")
        self.quiz = QuizBrain([self.question1, self.question2])

    def test_still_has_questions(self):
        self.assertTrue(self.quiz.still_has_questions())
        self.quiz.question_number = 2
        self.assertFalse(self.quiz.still_has_questions())

    def test_next_question(self):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            with patch('builtins.input', return_value="True"):
                self.quiz.next_question()
                self.assertEqual(fake_out.getvalue().strip(),
                                 "You got it right!\nThe correct answer was: True.\nYour current score is: 1/1")

                self.assertEqual(self.quiz.score, 1)
                self.assertEqual(self.quiz.question_number, 1)


if __name__ == '__main__':
    unittest.main()
