#######################################################################
# _flag_and_output.py  Adds inclusion and exclusion flags, and 
#                      category flags.  Then subsets, aggregates, 
#                      and outputs data for downstream reporting.
#
# by Rhonda Tullis, 1/24/2024
# for Orchid Initiative
#######################################################################

import pandas as pd
import parameters as parm
import _get_mappings as mappings

# Flag LARC procedures
def flag_larcs(df):
    df['larc'] = 0
    for var in parm.px_vars:
        df.loc[df[var].isin(mappings.larc_procedures), 'larc'] = 1

    print(df['larc'].value_counts(dropna=False))
    return df

