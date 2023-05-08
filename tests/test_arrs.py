from utils import arrs
import pytest


@pytest.fixture
def arrs_fixture():
    return [1, 2, 3, 4]

def test_arrs_add(arrs_fixture):
    assert arrs.arrs_add(arrs_fixture, 5, 6) == [1, 2, 3, 4, 5, 6]

def test_arrs_add_2(arrs_fixture):
    assert arrs.arrs_add(arrs_fixture, 5) == [1, 2, 3, 4, 5]

def test_arrs_add_3(arrs_fixture):
    assert arrs.arrs_add(arrs_fixture) == [1, 2, 3, 4]

def test_get(arrs_fixture):
    assert arrs.get(arrs_fixture, 1, "test") == 2
    assert arrs.get(arrs_fixture, -1, "test") == "test"
    assert arrs.get([], -1, "test") == "test"


def test_slice():
    assert arrs.my_slice([1, 2, 3, 4], 1, 3) == [2, 3]
    assert arrs.my_slice([1, 2, 3], 1) == [2, 3]
    assert arrs.my_slice([1, 2, 3], -5) == [1, 2, 3]
    assert arrs.my_slice([], -2) == []
    assert arrs.my_slice([1, 2, 3], -1) == [3]
