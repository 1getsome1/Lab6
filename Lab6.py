import data
from typing import Optional

# Write your functions for each part in the space below.

# Part 0

# Finds the index of the smallest value in the list, if there are values,
#     starting from the provided index (if in bounds).
# input: a list of integers
# input: a starting index
# returns: index of smallest value as an int or None if no value is found
def index_smallest_from(values:list[int], start:int) -> Optional[int]:
    if start >= len(values) or start < 0:
        return None

    mindex = start
    for idx in range(start + 1, len(values)):
        if values[idx] < values[mindex]:
            mindex = idx

    return mindex


# Sorts, in place, the elements of a list using the selection sort algorithm.
# input: a list of integers
# returns: nothing is returned; the list is sorted in place
#    <This function modifies/mutates the input list. Though a traditional
#     approach, cloning the list sorting the clone is potentially less
#     surprising. Or even using a different sorting algorithm.>
def selection_sort(values:list[int]) -> None:
    for idx in range(len(values) - 1):
        mindex = index_smallest_from(values, idx)
        tmp = values[mindex]
        values[mindex] = values[idx]
        values[idx] = tmp


# Part 1
# design Recipe:
# 1) take a list of books and return that list with its books in alphabetical order by title
# 2) def selection_sort_books(bList: list[book]):
# 3) template of function
#     - if the length of the list is 0 return none
#     - get the length of the list
#     - make a for loop for the range of the length of the list
#     - assign the current number of the loop to a variable
#     - go through the list one index ahead at a time
#     - if the new title is lower in the alphabet than replace both new and old
# 4) test case:     def test_selection_sort_books_1(self):
#                       B1 = data.Book(["An author", "Second author"], "A Book")
#                       B2 = data.Book(["Another author"], "B Book")
#                       B3 = data.Book(["An author again"], "C Book")
#                       Book_L = [B3, B2, B1]
#                       Lab6.selection_sort_books(Book_L)
#                       assert Book_L == [B1, B2, B3]
# 5)

def selection_sort_books(Books:list[data.Book]):
    if len(Books) == 0:
        return None
    n = len(Books)
    for x in range(n):
        min_idx = x
        for y in range(x + 1, n):
            if Books[y].title < Books[min_idx].title:
                min_idx = y
        Books[x], Books[min_idx] = Books[min_idx], Books[x]




# Part 2
# design Recipe:
# 1) This cycles through a string and makes every lower case letter upper case.
# It also makes every lower case letter upper case.
# 2) swap_case(s: str)->str:
# 3) template of function
#     - make a new list
#     - cycle through the characters in the string
#     - if the character is lower case then turn it upper-cased
#     - else is character is upper case then turn it into lower-cased
#     - return every value that isn't a letter
#     - add the character to the new list each time it goes through the loop. Whether its lower, upper case or not
# 4) test case:     def test_swap_case_1(self):
#                       switch = Lab6.swap_case(" Not Going to @")
#                       assert switch == " nOT gOING TO @"
# 5)

def swap_case(s: str)->str:
    end = ""
    for ch in s:
        if ch.isalpha():
            if ch.islower():
                end += ch.upper()
            else:
                end += ch.lower()
        else:
            end += ch
    return end


# Part 3
# design Recipe:
# 1) replaces the specified character with the inputted one in a string
# 2) str_translate(s: str, old: str, new: str):
# 3) template of function
#     - make a new list
#     - cycle through the characters in the string
#     - if the character matches the specified one the change it to the new character
#     - if the characters do not match then keep it the same
# 4) test case:       def test_str_translate_1(self):
#                         words = "Old Town Road, Take Me Home"
#                         fun = Lab6.str_translate(words, "T", "d")
#                         assert fun == "Old down Road, dake Me Home"
# 5)

def str_translate(s: str, old: str, new: str):
    end = ""
    for ch in s:
        if ch == old:
            end += new
        else:
            end += ch
    return end

# Part 4
# design Recipe:
# 1) uses a dictionary to count how many times a word shows up in a string
# 2) histogram(s: str)
# 3) template of function
#     - make a dictionary
#     - split up the inputted string
#     - each different word gets a starting value of one
#     - each time a word appears it will add one to its total
# 4) test case:       def test_histogram_1(self):
#                         words = "we are the ones"
#                         D = Lab6.histogram(words)
#                         assert D == {"we":1, "are":1, "the":1, "ones":1}
# 5)

def histogram(s: str):
    word_Lib = {}
    w = s.split()
    for x in w:
        if x in word_Lib:
            word_Lib[x] += 1
        else:
            word_Lib[x] = 1
    return word_Lib



