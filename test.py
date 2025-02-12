import unittest
from Polynomial import *

class TestPolynomial(unittest.TestCase):

    def test_init(self):
        p1 = Polynomial({0: 0, 1: 3, 2: 0, 3: 1})
        self.assertEqual(p1.coefficients, {1: 3, 3: 1})
        with self.assertRaises(ValueError):
            Polynomial("not a dictionary")

    def test_degree(self):
        p1 = Polynomial({0: 1, 1: 0, 2: 2})     # 1 + 2x^2
        p2 = Polynomial({0:0})
        p3 = Polynomial({0: 1, 3: 2, 5: 9})  # 1 + 2x^3 + 9x^5
        self.assertEqual(p1.degree(),2)
        self.assertEqual(p2.degree(), 0)
        self.assertEqual(p3.degree(), 5)

    def test_is_zero(self):
        p = Polynomial({0: 0, 0: 0, 0: 0})
        self.assertTrue(p.is_zero())

    def test_eq(self):
        p1 = Polynomial({0: 1, 1: 2, 2: 0})
        p2 = Polynomial({0: 1, 1: 2})
        self.assertEqual(p1, p2)

    def test_ne(self):
        p1 = Polynomial({0: 1, 1: 2, 2: 3})
        p2 = Polynomial({0: 1, 1: 3, 2: 2})
        self.assertNotEqual(p1, p2)

    def test_str(self):
        p1 = Polynomial({0: 1, 1: 2, 2: 3})
        p2 = Polynomial({0: -1, 1: -3, 2: 4})
        p3 = Polynomial({0: 0, 1: 0, 2: 3})
        self.assertEqual(str(p1), "3x^2 + 2x + 1")
        self.assertEqual(str(p2), "4x^2 - 3x - 1")
        self.assertEqual(str(p3), "3x^2")

    def test_getitem(self):
        p = Polynomial({0: 5, 1: 3, 2: 7})       # 5 + 3x + 7x^2
        self.assertEqual(p[2], 7)
        self.assertEqual(p[100], 0)

    def test_add(self):
        p1 = Polynomial({0: 1, 1: 2, 2: 3})     # 1 + 2x + 3x^2
        p2 = Polynomial({0: 3, 1: 4, 2: 0})     # 3 + 4x
        self.assertEqual(p1 + p2, Polynomial({0: 4, 1: 6, 2: 3}))
        self.assertEqual(p1 + 5, Polynomial({0: 6, 1: 2, 2: 3}))

    def test_radd(self):
        p = Polynomial({0: 1, 1: 2, 2: 3})  # 1 + 2x + 3x^2
        self.assertEqual(5 + p, Polynomial({0: 6, 1: 2, 2: 3}))

    def test_sub(self):
        p1 = Polynomial({0: 1, 1: 2, 2: 3})
        p2 = Polynomial({0: 3, 1: 4, 2: 0})
        self.assertEqual(p1 - p2, Polynomial({0: -2, 1: -2, 2: 3}))
        self.assertEqual(p1 - 10, Polynomial({0: -9, 1: 2, 2: 3}))

    def test_rsub(self):
        p = Polynomial({0: 1, 1: 2, 2: 3})  # 1 + 2x + 3x^2
        self.assertEqual(5 - p, Polynomial({0: 4, 1: -2, 2: -3}))

    def test_mul(self):
        p1 = Polynomial({0: 1, 1: 1})      # 1 + x
        p2 = Polynomial({0: 1, 1: -1})     # 1 - x
        self.assertEqual(p1 * p2, Polynomial({0: 1, 2: -1}))
        self.assertEqual(p1 * 3, Polynomial({0: 3, 1: 3}))
        self.assertEqual(p1 * 3, Polynomial({0: 3, 1: 3}))
        p3 = Polynomial({0: 1, 1: 2})  # 1 + 2x
        p4 = Polynomial({0: 1, 1: -1, 2: 2})  # 1 - x + 2x^2
        self.assertEqual(p3 * p4, Polynomial({0: 1, 1: 1, 2: 0, 3: 4}))

    def test_rmul(self):
        p = Polynomial({0: 1, 1: 2, 2: 3})  # 1 + 2x + 3x^2
        self.assertEqual(2 * p, Polynomial({0: 2, 1: 4, 2: 6}))

    def test_call(self):
        p1 = Polynomial({0: 1, 1: 2, 2: 3})   # 1 + 2x + 3x^2
        p2 = Polynomial({0: -1, 1: -2, 2: 3})    # -1 -2x + 3x^2
        self.assertEqual(p1(0), 1)
        self.assertEqual(p1(2), 17)
        self.assertEqual(p2(0), -1)
        self.assertEqual(p2(2), 7)
        p3 = Polynomial({1:2, 2:-3, 3:4})
        self.assertEqual(p3(-3), -141)

    def test_integrate(self):
        p1 = Polynomial({0: 1, 1: 2, 2: 3})   # 1 + 2x + 3x^2, całka: (1/3)x^3 + x^2 + 3x + C
        self.assertEqual(p1.integrate(), Polynomial({1: 1, 2: 1, 3: 1}))
        self.assertEqual(p1.integrate(5), Polynomial({0: 5, 1: 1, 2: 1, 3: 1}))

    def test_differentiate(self):
        p1 = Polynomial({0: 1, 1: 2, 2: 3})   # 1 + 2x + 3x^2
        self.assertEqual(p1.differentiate(), Polynomial({0: 2, 1: 6}))
        p3 = Polynomial({0: 5, 1: 3})     # 5 + 3x
        self.assertEqual(p3.differentiate(), Polynomial({0: 3}))
        p4 = Polynomial({0: 5})       # 5
        self.assertEqual(p4.differentiate(), Polynomial({0: 0}))


if __name__ == '__main__':
    unittest.main()