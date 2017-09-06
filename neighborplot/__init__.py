"""
Contains code for the CompareNeighbors Class.
"""

import scipy.spatial.distance as dist
import numpy as np
import scipy.stats
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

class CompareNeighbors(object):
    """

    """
    def __init__(self, coords1, coords2, minNeighbors, maxNeighbors):
        """

        :return:
        """
        self.coords1 = coords1
        self.coords2 = coords2
        self.minNeighbors = minNeighbors
        self.maxNeighbors = maxNeighbors

    def run(self):
        self._compute_neighbor_overlap_matrix()

    def plot(self):
        """

        :return:
        """

        plt.imshow(self.neighbor_overlap_matrix,
                   cmap='hot',
                   interpolation='nearest',
                   origin='lower'
                   )
        plt.colorbar()

    def plot_to_pdf(self, fout):
        pp = PdfPages(fout)
        self.plot()
        pp.savefig()
        pp.close()

    def _compute_euc_dist_ranks(self):
        '''
        Computes the distance matrices for the given coordinates.
        :param xys:
        :return: numpy 2d array
        '''
        euc_dist1 = dist.squareform(dist.pdist(self.coords1,'euclidean'))
        euc_dist2 = dist.squareform(dist.pdist(self.coords2,'euclidean'))

        self.rank1 = np.apply_along_axis(
                        lambda x: scipy.stats.rankdata(x,method='min'),
                        1,
                        euc_dist1
                     )

        self.rank2 = np.apply_along_axis(
                        lambda x: scipy.stats.rankdata(x,method='min'),
                        1,
                        euc_dist2
                     )

    def _neighbor_similarity(self, ks):
        """

        :param ks:
        :return:
        """
        k1 = ks[0]
        k2 = ks[1]
        return ((self.rank1 <=k1) * (self.rank2 <=k2)).sum()  \
            / (self.rank1.shape[0] * float(min(k1,k2)))


    def _compute_neighbor_overlap_matrix(self):

        self._compute_euc_dist_ranks()
        # Make a grid of all parameters between the max and the min neighbors.
        grid = np.mgrid[self.minNeighbors:self.maxNeighbors+1,
                        self.minNeighbors:self.maxNeighbors+1]

        self.neighbor_overlap_matrix= np.apply_along_axis(
                                         lambda x: self._neighbor_similarity(x),
                                         0,
                                         grid
                                      )

