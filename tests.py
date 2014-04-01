from __future__ import absolute_import, division, print_function, unicode_literals

import pytest
from environment import Environment, is_yesish


def test_Environment_basically_works():
    env = Environment(FOO_BAR=None, environ={'FOO_BAR': 'baz'})
    assert env.foo.bar == 'baz'
    assert env.missing == []
    assert env.malformed == {}

def test_Environment_unprefixed_works():
    env = Environment(FOO=None, environ={'FOO': 'baz'})
    assert env.foo == 'baz'

def test_Environment_missing_is_missing():
    env = Environment(FOO=None, environ={})
    assert env.missing == ['FOO']

def test_Environment_malformed_is_malformed():
    env = Environment(FOO=int, environ={'FOO': 'baz'})
    assert env.malformed == {'FOO': "ValueError: invalid literal for int() with base 10: 'baz'"}


def test_is_yesish_1_is_True():
    assert is_yesish('1')

def test_is_yesish_true_is_True():
    assert is_yesish('TrUe')

def test_is_yesish_yes_is_True():
    assert is_yesish('YeS')

def test_is_yesish_0_is_False():
    assert not is_yesish('0')

def test_is_yesish_false_is_False():
    assert not is_yesish('FaLsE')

def test_is_yesish_no_is_False():
    assert not is_yesish('No')

def test_is_yesish_junk_is_False():
    assert not is_yesish('Oh yeah junk')

def test_is_yesish_chokes_on_int():
    pytest.raises(AttributeError, is_yesish, 1)

def test_is_yesish_chokes_on_bool():
    pytest.raises(AttributeError, is_yesish, True)
