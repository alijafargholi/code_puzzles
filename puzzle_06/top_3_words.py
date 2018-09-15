"""
Most frequently used words in a text
====================================

Write a function that, given a string of text (possibly with punctuation and
line-breaks), returns an array of the top-3 most occurring words, in descending
order of the number of occurrences.

Assumptions:
A word is a string of letters (A to Z) optionally containing one or more
apostrophes (') in ASCII. (No need to handle fancy punctuation.)
Matches should be case-insensitive, and the words in the result should be
lowercase. Ties may be broken arbitrarily.

If a text contains fewer than three unique words, then either the top-2 or
top-1 words should be returned, or an empty array if a text contains no words.

Example
^^^^^^^

::

   top_3_words("In a village of La Mancha, the name of which I have no desire
   to call to mind, there lived not long since one of those gentlemen that keep
   a lance in the lance-rack, an old buckler, a lean hack, and a greyhound for
   coursing. An olla of rather more beef than mutton, a salad on most
   nights, scraps on Saturdays, lentils on Fridays, and a pigeon or so extra
   on Sundays, made away with three-quarters of his income.")
   # => ["a", "of", "on"]

   top_3_words("e e e e DDD ddd DdD: ddd ddd aa aA Aa, bb cc cC e e e")
   # => ["e", "ddd", "aa"]

   top_3_words("  //wont won't won't")
   # => ["won't", "wont"]

Source
^^^^^^

https://www.codewars.com/kata/most-frequently-used-words-in-a-text/train/python

"""
import re
from collections import Counter


def top_3_words(text: str) -> list:
    """Get the top 3 most used world inside a given string"""
    # Remove the illegal character
    clean_text = re.sub(r'[?|$|.|!|/|;|:|_|\-|,]', r' ', text.lower())

    # Break the string by the space and remove the none words
    text_list = [_ for _ in (clean_text.split(" ")) if is_word(_)]

    # Get the most 3 used
    result = Counter(text_list).most_common(3)
    return [_[0] for _ in result]


def is_word(word: str) -> bool:
    """Whether or not the string contains any characters other than alphabet"""
    found = re.search('[a-zA-Z]', word)
    return bool(found)
