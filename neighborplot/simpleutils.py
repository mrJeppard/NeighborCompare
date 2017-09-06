"""

"""

import pandas as pd

def common_rows(p1, p2):
    '''
    Reduces two pandas dataframes to rows they have in common.
    @param p1: A pandas dataframe.
    @param p2: A pandas dataframe.
    @return: Tuple of pandas dataframes having the same rows in the same order.
    '''

    p1rows = set(p1.index)
    p2rows = set(p2.index)
    rowsInCommon = p1rows.intersection(p2rows)
    p1 = p1.loc[rowsInCommon]
    p2 = p2.loc[rowsInCommon]
    return p1, p2


def read_coords(filepath,typeOfFormat="tab"):
    """
    Reads coordinates from a file with specified format.
    :param filepath:
    :param typeOfFormat:
    :return:
    """
    if typeOfFormat == "tab":
        coords = pd.read_csv(filepath, sep='\t', index_col=0)
    return coords



