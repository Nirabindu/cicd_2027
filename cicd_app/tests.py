from django.test import TestCase

# Create your tests here.
def mul(a, b):
    return a * b


def test_add():
    assert mul(2, 3) == 8