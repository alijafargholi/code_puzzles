from .the_observed_pin import get_pins

expectations = {'8': ['5', '7', '8', '9', '0'],
                '11':["11", "22", "44", "12", "21", "14", "41", "24", "42"],
                '369': ["339","366","399","658","636","258","268","669","668","266","369","398","256","296","259","368","638","396","238","356","659","639","666","359","336","299","338","696","269","358","656","698","699","298","236","239"]}


def test_01():
    assert sorted(get_pins('8')) == sorted(expectations.get('8'))


def test_02():
    assert sorted(get_pins('11')) == sorted(expectations.get('11'))


def test_03():
    assert sorted(get_pins('369')) == sorted(expectations.get('369'))
