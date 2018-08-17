"""
Duplicate Encoder
=================

Source: http://www.codewars.com/kata/54b42f9314d9229fd6000d9c/train/python

The goal of this exercise is to convert a string to a new string where each
character in the new string is '(' if that character appears only once in the
original string, or ')' if that character appears more than once in the
original string. Ignore capitalization when determining if a character is a
duplicate.

Examples:

::

   "din" => "((("
   "recede" => "()()()"
   "Success" => ")())())"
   "(( @" => "))(("
"""


def duplicate_encode(word):
    """convert a string to a new string where each character in the new string
    is '(' if that character appears only once in the original string, or ')'
    if that character appears more than once in the original string. Ignore
    capitalization when determining if a character is a duplicate.

    :type word: str
    :param word: Word to decode
    :rtype: str
    :return: Decoded string
    """
    word = word.lower()
    return ''.join(["(" if word.count(_) == 1 else ")" for _ in word])
