import unittest
import sys
from .context import trytopkg


class BasicTestSuite(unittest.TestCase):
    """Basic test cases.
    change dir to top level of the project and type follows
    > nosetests tests
    """

    def test_hello1(self):
        trytopkg.hello.hello1()
        output = sys.stdout.getvalue().strip()
        self.assertEqual(output, 'Hello Package!')


if __name__ == '__main__':
    unittest.main()
