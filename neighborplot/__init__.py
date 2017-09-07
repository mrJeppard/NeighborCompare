"""Contains code for the CompareNeighbors Class."""

import scipy.spatial.distance as dist
import numpy as np
import scipy.stats
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages


class CompareNeighbors(object):
    """Compare neighbors class is used to generate a neighborplot."""

    def __init__(self, coords1, coords2, min_neighbors, max_neighbors):
        """Initialize the compare neighbors class."""
        self.coords1 = coords1
        self.coords2 = coords2
        self.min_neighbors = min_neighbors
        self.max_neighbors = max_neighbors
        self.rank1 = None
        self.rank2 = None
        self.neighbor_overlap_matrix = None

    def run(self):
        """Run the computations necessary to make a neighbor plot."""
        self._compute_overlap_matrix()

    def score(self):
        """Compute the average of all neighbor overlap averages."""
        return self.neighbor_overlap_matrix.sum().sum() \
            / (self.max_neighbors - self.min_neighbors) ** 2

    def plot(self):
        """Plot the neighborplot visualization."""
        plt.imshow(self.neighbor_overlap_matrix,
                   cmap='seismic',
                   interpolation='nearest',
                   origin='lower'
                   )
        plt.colorbar()

    def plot_to_pdf(self, fout):
        """Output a pdf to the path specified by 'fout'."""
        pdfout = PdfPages(fout)
        self.plot()
        pdfout.savefig()
        pdfout.close()

    def _compute_euc_dist_ranks(self):
        """Compute the distance matrices for the given coordinates."""
        euc_dist1 = dist.squareform(dist.pdist(self.coords1, 'euclidean'))
        euc_dist2 = dist.squareform(dist.pdist(self.coords2, 'euclidean'))

        self.rank1 = np.apply_along_axis(
                        lambda x: scipy.stats.rankdata(x, method='min'),
                        1,
                        euc_dist1
                     )

        self.rank2 = np.apply_along_axis(
                        lambda x: scipy.stats.rankdata(x, method='min'),
                        1,
                        euc_dist2
                     )

    def _neighbor_similarity(self, kneighbors):
        """
        Compute the neighbor similarity for two k's.

        :param kneighbors: Tuple containing the first and seconod k
        neighbors.
        :return: A float, bounded between 0-1 if there are no ties.
        """
        kneighbor1 = kneighbors[0]
        kneighbor2 = kneighbors[1]
        return ((self.rank1 <= kneighbor1) * (self.rank2 <= kneighbor2)).sum()\
            / (self.rank1.shape[0] * float(min(kneighbor1, kneighbor2)))

    def _compute_overlap_matrix(self):
        """Compute the average shared neighbors over given ranges of k's."""
        self._compute_euc_dist_ranks()
        # Make a grid of all parameters between the max and the min neighbors.
        grid = np.mgrid[self.min_neighbors:self.max_neighbors+1,
                        self.min_neighbors:self.max_neighbors+1]

        self.neighbor_overlap_matrix = np.apply_along_axis(
                                         lambda x: self._neighbor_similarity(x),
                                         0,
                                         grid
                                      )
