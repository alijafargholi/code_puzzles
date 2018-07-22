"""
https://www.hackerrank.com/challenges/ctci-balanced-brackets/problem
"""


def main(expression):
    """

    :param expression:
    :return:
    """

    open_brackets = ['{', '(', '[']
    close_bracket = ['}', ')', ']']

    opened_brackets = []
    for index, bracket in enumerate(expression):
        if bracket not in open_brackets and bracket not in close_bracket:
            continue
        if bracket in close_bracket:
            if index == 0:
                return False
            if opened_brackets[-1] != open_brackets[close_bracket.index(bracket)]:
                return False
            else:
                opened_brackets.pop(-1)
        else:
            opened_brackets.append(bracket)

    return True


main("{{[[(())]]}}")
