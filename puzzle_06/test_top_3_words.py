from .top_3_words import top_3_words


def test_00():
    assert top_3_words("a a a  b  c c  d d d d  e e e e e") == ["e", "d", "a"]


def test_01():
    assert top_3_words("e e e e DDD ddd DdD: ddd ddd aa aA Aa, bb cc cC e e e") == ["e", "ddd", "aa"]


def test_02():
    assert top_3_words("  //wont won't won't ") == ["won't", "wont"]


def test_03():
    assert top_3_words("  , e   .. ") == ["e"]


def test_04():
    assert top_3_words("  ...  ") == []


def test_05():
    assert top_3_words("  '  ") == []


def test_06():
    assert top_3_words("  '''  ") == []


def test_07():
    assert top_3_words("""In a village of La Mancha, the name of which I have
    no desire to call to mind, there lived not long since one of those gentlemen
    that keep a lance in the lance-rack, an old buckler, a lean hack, and a
    greyhound for coursing. An olla of rather more beef than mutton, a salad on
    most nights, scraps on Saturdays, lentils on Fridays, and a pigeon or so
    extra on Sundays, made away with three-quarters of his
    income.""") == ["a", "of", "on"]


def test_08():
    test = " ".join([',kpayuyz;', 'kih:?kih;?;kpayuyz/-kpayuyz',
                     'kpayuyz;,.;/kih?-kih::--kpayuyz.:_:'
                     '_kpayuyz;.://kpayuyz;/;'])
    assert top_3_words(test) == ['kpayuyz', 'kih']


def test_09():
    test = " ".join(["'uhql", "'uhql-'uhql"])
    assert top_3_words(test) == ["'uhql"]


def test_10():
    test = " ".join(['oobjiexux', 'fsnje', 'oobjiexux--fsnje'])
    assert top_3_words(test) == ['oobjiexux', 'fsnje']


def test_11():
    test = " ".join(['pwlz', 'sbygn', 'pvkfgzem'])
    assert top_3_words(test) == ['pwlz', 'sbygn', 'pvkfgzem']
