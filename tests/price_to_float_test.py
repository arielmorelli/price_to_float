import unittest
from resources.price_to_float import price_to_float


class PriceToFloatTest(unittest.TestCase):
    def only_number(self):
        test_value = str('1111')
        expected = 1111.00
        number = price_to_float(test_value)
        self.assertEquals(expected, number)

    # test_value = str('1111.')
    # print test_value, price_to_float(test_value)
    #
    # test_value = str('1111.2')
    # print test_value, price_to_float(test_value)
    #
    # test_value = str('1111.22')
    # print test_value, price_to_float(test_value)
    #
    # test_value = str('1111')
    # print test_value, price_to_float(test_value)
    #
    # test_value = str('1111')
    # print test_value, price_to_float(test_value)
    #
    # test_value = str('1111')
    # print test_value, price_to_float(test_value)
    #
    # test_value = str('1111.')
    # print test_value, price_to_float(test_value)
    #
    # test_value = str('11111.0')
    # print test_value, price_to_float(test_value)
    #
    # test_value = str('11111.00')
    # print test_value, price_to_float(test_value)
    #
    # test_value = str('1111,')
    # print test_value, price_to_float(test_value)
    #
    # test_value = str('11111,0')
    # print test_value, price_to_float(test_value)
    #
    # test_value = str('11111,00')
    # print test_value, price_to_float(test_value)
    #
    # test_value = str('1.000')
    # print test_value, price_to_float(test_value)
    #
    # test_value = str('1.000.000')
    # print test_value, price_to_float(test_value)
    #
    # test_value = str('1.000.000.000')
    # print test_value, price_to_float(test_value)
    #
    # test_value = str('1,000,000,000')
    # print test_value, price_to_float(test_value)
    #
    # print test_value, price_to_float(test_value)
    #
    # test_value = str('1,000.22')
    # print test_value, price_to_float(test_value)
    #
    # test_value = str('1.111,33')
    # print test_value, price_to_float(test_value)
    #
    # test_value = str('1 111,33')
    # print test_value, price_to_float(test_value)
    #
    # test_value = str('1 111.33')
    # print test_value, price_to_float(test_value)
