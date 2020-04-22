import one_hot_encoder
import unittest


class Test_one_hot_encoder(unittest.TestCase):
    def test_eq(self):
        res = one_hot_encoder.fit_transform(['one', 'hot', 'encoder'])
        exp = [('one', [0, 0, 1]), ('hot', [0, 1, 0]), ('encoder', [1, 0, 0])]

        self.assertEqual(res, exp)

    def test_eq2(self):
        res = one_hot_encoder.fit_transform(list('HELL'))
        exp = [('H', [0, 0, 1]), ('E', [0, 1, 0]), ('L', [1, 0, 0]), ('L', [1, 0, 0])]

        self.assertEqual(res, exp)

    def test_notin(self):
        res = one_hot_encoder.fit_transform(list('No'))
        exp = [('N', [1, 0]), ('o', [0, 1])]

        self.assertNotIn(res, exp)

    def test_except(self):
        self.assertRaises(TypeError, one_hot_encoder.fit_transform)

    def test_except2(self):
        self.assertRaises(TypeError, one_hot_encoder.fit_transform([1, 2, 3]))


if __name__ == "__main__":
    unittest.main()
