import unittest
from question_model import Question


class TestQuestionModel(unittest.TestCase):
    def test_init(self):
        q = Question("A slug's blood is green.", "True")
        self.assertEqual(q.text, "A slug's blood is green.")
        self.assertEqual(q.answer, "True")


if __name__ == '__main__':
    unittest.main()
