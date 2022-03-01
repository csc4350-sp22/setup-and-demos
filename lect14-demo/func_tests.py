import unittest
from func import swap_words


class TestSwapWords(unittest.TestCase):
    def test_regular_sentence(self):
        sentence = "Hello world"
        expected_output = "world Hello"
        output = swap_words(sentence)
        self.assertEqual(expected_output, output)

    def test_oneword_sentence(self):
        sentence = "Hello"
        expected_output = "Hello"
        output = swap_words(sentence)
        self.assertEqual(expected_output, output)


if __name__ == "__main__":
    unittest.main()
