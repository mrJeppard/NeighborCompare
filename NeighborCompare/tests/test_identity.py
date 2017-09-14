"""A starting point for unit tests."""

from unittest import TestCase
import neighborplot.tests.utils4testing as utils
from neighborplot import CompareNeighbors


class Testings(TestCase):
    """Place holder running test class."""

    def test_identity(self):
        """Same coords should come up with a comparison score of > 1."""
        coords = utils.rand_coords()
        comparison = CompareNeighbors(coords, coords, 1, 10)
        comparison.run()
        self.assertTrue(comparison.score() >= 1)

    def test_flip_identity1(self):
        """Same coords flipped should come up with a comparison score > 1."""
        coords = utils.rand_coords()
        coords1 = utils.flip_coords(coords)
        comparison = CompareNeighbors(coords, coords1, 1, 10)
        comparison.run()
        self.assertTrue(comparison.score() >= 1)

    def test_flip_identity2(self):
        """Same coords flipped should come up with a comparison score of > 1."""
        coords = utils.rand_coords()
        coords1 = utils.flip_coords(coords)
        comparison = CompareNeighbors(coords, coords1, 1, 10)
        comparison.run()
        self.assertTrue(comparison.score() >= 1)

    def test_flip_identity3(self):
        """Same coords flipped should come up with a comparison score of > 1."""
        coords = utils.rand_coords()
        coords1 = utils.flip_coords(coords)
        comparison = CompareNeighbors(coords, coords1, 1, 10)
        comparison.run()
        self.assertTrue(comparison.score() >= 1)

    def test_non_identity(self):
        """Different coords should have a number less than 1."""
        coords = utils.rand_coords()
        coords1 = utils.rand_coords()
        comparison = CompareNeighbors(coords, coords1, 1, 10)
        comparison.run()
        self.assertTrue(comparison.score() < 1)

    def test_high_dim_identity(self):
        """Higher dimensions than two should be allowed."""
        coords = utils.rand_coords(dim=10, nnodes=32)
        comparison = CompareNeighbors(coords, coords, 1, 10)
        comparison.run()
        self.assertTrue(comparison.score() >= 1)
