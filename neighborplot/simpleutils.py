"""Simple utilities for neighborplot package."""

import pandas as pd


def common_rows(df1, df2):
    """
    Reduces two pandas dataframes to rows they have in common.

    @param df1: A pandas dataframe.
    @param df2: A pandas dataframe.
    @return: Tuple of pandas dataframes having the same rows in the same order.
    """
    # Get common row names so each data frame can be reduced.
    df1rows = set(df1.index)
    df2rows = set(df2.index)
    common_rowids = df1rows.intersection(df2rows)

    # Reduce each data frame.
    df1 = df1.loc[common_rowids]
    df2 = df2.loc[common_rowids]

    return df1, df2


def read_coords(filepath, format_type="tab"):
    """
    Read coordinates from a file with specified format.

    :param filepath: Path to file to be read.
    :param format_type: Specifies how the file should be read in.
    :return: Pandas dataframe of the given file.
    """
    if format_type == "tab":
        coords = pd.read_csv(filepath, sep='\t', index_col=0)
    else:
        raise ValueError("Unrecognized format_type")
    return coords
