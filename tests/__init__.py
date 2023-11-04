import unittest
import tests


def all_tests():
    loader = unittest.TestLoader()
    loader.loadTestsFromModule(tests)
    return loader
