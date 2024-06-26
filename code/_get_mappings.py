########################################################################
# _get_mappings.py  Makes relational data available for 
#                   _flag_and_output.py
#
# by Rhonda Tullis, 2/01/2024
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
    print(f'\n{sheet_name}=')
    print('Code list')
    print(code_list)
    return code_list


# Select codes using subset values and the output filter values to list
def get_code_maps(source, 
                  sheet_name, 
                  subset_col, 
                  subset_value, 
                  filter_var):

    df = pd.read_excel(source, sheet_name=sheet_name, dtype=str)
    map_list = df.loc[df[subset_col]==subset_value, filter_var]
    return map_list

