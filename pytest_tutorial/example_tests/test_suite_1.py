import pytest

pytestmark = pytest.mark.collection


@pytest.mark.smoke
def test_1():
    print('doing test 1')
    print('test_1 is finished')


@pytest.mark.smoke
def test_2():
    print('doing test 2')
    print('test_2 is finished')
    assert 2 == 2, '1 is not equal to 2'


@pytest.mark.regression
def test_3():
    print('doing test 3')
    print('test_3 is finished')


@pytest.mark.regression
def test_4():
    print('doing test 4')
    print('test_4 is finished')
    assert 10 == 12, '10 is not equal to 12'


@pytest.mark.regression
def test_5():
    print('doing test 5')
    print('test_5 is finished')


@pytest.mark.regression
def test_6():
    print('doing test 6')
    print('test_6 is finished')
    assert 4 == 8, '4 is not equal to 8'
