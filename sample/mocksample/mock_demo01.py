from unittest import mock
import unittest

from .modular import Count


class TestCount(unittest.TestCase):

    def test_add(self):
        count = Count()
        count.add = mock.Mock(return_value=13, side_effect=count.add)
        result = count.add(8, 5)
        print(result)
        count.add.assert_called_with(8, 5)
        self.assertEqual(result, 13)


if __name__ == '__main__':
    unittest.main()

