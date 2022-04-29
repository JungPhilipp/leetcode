from .is_bipartite import Solution

solution = Solution()


def test_example_1():
    assert solution.isBipartite([[1, 2, 3], [0, 2], [0, 1, 3], [0, 2]]) is False


def test_example_2():
    assert solution.isBipartite([[1, 3], [0, 2], [1, 3], [0, 2]]) is True
