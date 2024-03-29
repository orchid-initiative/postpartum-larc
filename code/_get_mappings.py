########################################################################
# _get_mappings.py  Makes relational data available for 
#                   _flag_and_output.py
#
# by Rhonda Tullis
# for Orchid Initiative
########################################################################

import pandas as pd
import parameters as parm

# LARC procedure codes into list
def get_codelists(source, sheet_name):
    
    df = pd.read_excel(source, sheet_name=sheet_name, dtype=str)

    # Use list of codes in the first column
    # Remove decimals from all codes (they are present in DXs)
    # Output column as a list
    codelist = df.iloc[:,0].str.replace('.','', regex=True).tolist()

    return codelist

