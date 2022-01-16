class TestMethod(object):

    def test_1(self):
        print('doing test 1')
        print('test_1 is finished')

    def test_2(self):
        print('doing test 2')
        print('test_2 is finished')
        assert 1 == 2, '1 is not equal to 2'
