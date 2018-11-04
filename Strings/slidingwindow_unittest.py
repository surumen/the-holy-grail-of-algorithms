#
# Sliding window min/max test (Python 2, 3)
#

import random, unittest
import slidingwindowminmax


class SlidingWindowMinMaxTest(unittest.TestCase):
	def test_randomly(self):
		trials = 3000
		for _ in range(trials):
			arraylen = random.randrange(300)
			array = [random.randrange(100) for _ in range(arraylen)]
			window = random.randrange(1, 31)
			maximize = random.randrange(2) != 0
			expect = _compute_naive(array, window, maximize)
			actual = slidingwindowminmax.compute(array, window, maximize)
			self.assertEqual(expect, actual)

	def test_incremental(self):
		trials = 100
		for _ in range(trials):
			array = [random.randrange(100) for _ in range(1000)]
			swm = slidingwindowminmax.SlidingWindowMinMax()
			start = 0
			end = 0
			while start < len(array):
				if start == end or (end < len(array) and random.randrange(2) != 0):
					swm.add_tail(array[end])
					end += 1
				else:
					swm.remove_head(array[start])
					start += 1
				assert start <= end
				if start < end:
					self.assertEqual(min(array[start : end]), swm.get_minimum())
					self.assertEqual(max(array[start : end]), swm.get_maximum())


def _compute_naive(array, window, maximize):
	if window <= 0:
		raise ValueError()
	func = max if maximize else min
	return [func(array[i : i + window]) for i in range(len(array) - window + 1)]


if __name__ == "__main__":
	unittest.main()
