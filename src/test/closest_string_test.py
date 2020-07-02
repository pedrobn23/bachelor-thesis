"""
Module that implements automatic test cases for
Graph class.
"""


from unittest import TestCase, main
from SATreduce import closest_string as cs
from bitarray import bitarray


class ClosestStringTestCase(TestCase):
    """
    Test Class for closest_string module
    """

    def __init__(self, *args, **kwargs):
        super(__class__, self).__init__(*args, **kwargs)

        self.s1 = bitarray('010111')
        self.s2 = bitarray('010101')

        self.s3 = bitarray('101')
        self.s4 = bitarray('010')

    def test_closest_string(self):
        for index, elem in enumerate([False, False, False, False, True]):
            self.assertEqual(
                cs.closest_string([self.s1, self.s2, self.s3, self.s4],
                                  index),
                elem)
        self.assertEqual(
            cs.minimum_distance([self.s1, self.s2, self.s3, self.s4]), 4)


if __name__ == '__main__':
    main()
