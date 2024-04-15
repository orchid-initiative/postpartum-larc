########################################################################
# _get_mappings.py  Makes relational data available for 
#                   _flag_and_output.py
#
# by Rhonda Tullis
# for Orchid Initiative
########################################################################

import pandas as pd
import parameters as parm

# Codes for conditions into list
def get_code_lists(source, sheet_name):
    
    df = pd.read_excel(source, sheet_name=sheet_name, dtype=str)

    # Use list of codes in the first column
    # Remove decimals from all codes (they are present in DXs)
    # Output column as a list
    code_list = df.iloc[:,0].str.replace('.','', regex=True).tolist()

    return code_list


# Procedure codes into dictionary, setting categories
def get_code_dicts(source, sheet_name, keep_columns):

    df = pd.read_excel(source, sheet_name=sheet_name, 
                       usecols=keep_columns,
                       dtype=str)

    # Output as a dictionary 
    code_dict = df.to_dict() 

    return code_dict
