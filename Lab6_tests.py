import data
import Lab6
import unittest


# Write your test cases for each part below.

class TestCases(unittest.TestCase):
    # Part 0
    def test_index_smallest_from_1(self):
        input = [2, 1, 9, 0, 4, 5]
        expected = 3
        actual = Lab6.index_smallest_from(input, 0)
        self.assertEqual(expected, actual)


    def test_index_smallest_from_2(self):
        input = [2, 1, 9, 0, 4, 5]
        expected = 4
        actual = Lab6.index_smallest_from(input, 4)
        self.assertEqual(expected, actual)


    def test_index_smallest_from_3(self):
        input = [2, 1, 9, 0, 4, 5]
        expected = None
        actual = Lab6.index_smallest_from(input, 6)
        self.assertEqual(expected, actual)


    def test_index_smallest_from_4(self):
        input = []
        expected = None
        actual = Lab6.index_smallest_from(input, 0)
        self.assertEqual(expected, actual)


    def test_selection_sort_1(self):
        input = [1, 2, 3, 4, 5]
        expected = [1, 2, 3, 4, 5]
        Lab6.selection_sort(input)
        self.assertEqual(expected, input)


    def test_selection_sort_2(self):
        input = []
        expected = []
        Lab6.selection_sort(input)
        self.assertEqual(expected, input)


    def test_selection_sort_3(self):
        input = [9, 7, 5, 3, 1]
        expected = [1, 3, 5, 7, 9]
        Lab6.selection_sort(input)
        self.assertEqual(expected, input)


    def test_selection_sort_4(self):
        input = [5, 0, 19, 21, 4, 6]
        expected = [0, 4, 5, 6, 19, 21]
        Lab6.selection_sort(input)
        self.assertEqual(expected, input)


    # Part 1
    def test_selection_sort_books_1(self):
        B1 = data.Book(["An author", "Second author"], "A Book")
        B2 = data.Book(["Another author"], "B Book")
        B3 = data.Book(["An author again"], "C Book")
        Book_L = [B3, B2, B1]
        Lab6.selection_sort_books(Book_L)
        assert Book_L == [B1, B2, B3]

    def test_selection_sort_books_2(self):
        B1 = data.Book(["An author", "Second author"], "A Book")
        B2 = data.Book(["Another author"], "B Book")
        B3 = data.Book(["An author again"], "C Book")
        Book_L = [B1, B3, B2]
        Lab6.selection_sort_books(Book_L)
        assert Book_L == [B1, B2, B3]

    def test_selection_sort_books_3(self):
        B1 = data.Book(["An author", "Second author"], "Ab Book")
        B2 = data.Book(["Another author"], "Bc Book")
        B3 = data.Book(["An author again"], "BC Book")
        Book_L = [B1, B3, B2]
        Lab6.selection_sort_books(Book_L)
        assert Book_L == [B1, B3, B2]

    def test_selection_sort_books_4(self):
        Book_L = []
        Lab6.selection_sort_books(Book_L)
        assert Book_L == []

    # Part 2
    def test_swap_case_1(self):
        switch = Lab6.swap_case(" Not Going to @")
        assert switch == " nOT gOING TO @"

    def test_swap_case_2(self):
        switch = Lab6.swap_case("1234")
        assert switch == "1234"

    def test_swap_case_3(self):
        switch = Lab6.swap_case("Yo me llamo algo diferente")
        assert switch == "yO ME LLAMO ALGO DIFERENTE"

    # Part 3
    def test_str_translate_1(self):
        words = "Old Town Road, Take Me Home"
        fun = Lab6.str_translate(words, "T", "d")
        assert fun == "Old down Road, dake Me Home"

    def test_str_translate_2(self):
        words = "Wy ary gryat"
        fun = Lab6.str_translate(words, "y", "e")
        assert fun == "We are great"

    def test_str_translate_3(self):
        words = "@ u//uuuu90oildfu_"
        fun = Lab6.str_translate(words, "u", "f")
        assert fun == "@ f//ffff90oildff_"

    # Part 4
    def test_histogram_1(self):
        words = "we are the ones"
        D = Lab6.histogram(words)
        assert D == {"we":1, "are":1, "the":1, "ones":1}

    def test_histogram_2(self):
        words = "2 34 2 12 2 3 2 3"
        D = Lab6.histogram(words)
        assert D == {"2":4, "34":1, "12":1, "3":2}




if __name__ == '__main__':
    unittest.main()
