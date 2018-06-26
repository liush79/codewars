from common import Test


def two_sum(ns, t):
    return next([i, ns.index(t - n)] for i, n in enumerate(ns) if t - n in ns and i != ns.index(t - n))


Test.assert_equals(sorted(two_sum([1, 2, 3], 4)), [0, 2])
Test.assert_equals(sorted(two_sum([1234, 5678, 9012], 14690)), [1, 2])
Test.assert_equals(sorted(two_sum([2, 2, 3], 4)), [0, 1])
