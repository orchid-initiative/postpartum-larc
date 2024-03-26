#######################################################################
# _flag_and_output.py  Adds inclusion and exclusion flags, and 
#                      category flags.  Then subsets, aggregates, 
#                      and outputs data for downstream reporting.
#
# by Rhonda Tullis, 1/24/2024
# for Orchid Initiative
#######################################################################

import pandas as pd
import numpy as np
import parameters as parm
import _get_mappings as mappings

# FLAG PROCEDURES, DEMOGRAPHICS, AND CONDITIONS
def flags(df):

    # LARC procedures
    df['larc'] = 0
    for var in parm.px_vars:
        df.loc[df[var].isin(mappings.larc_procedures), 'larc'] = 1

    # Medicaid payer (if pay_cat=Medi-Cal)
    # else zero.  Missing pay_cat values will return missing values.
    df['medicaid'] = np.where(df['pay_cat']==3, 1, 0) 

    # Latinx
    df.loc[df['ethncty']=='E1', 'latinx'] = 1

    # Non-white
    df.loc[df['race1'].isin('R1','R2','R3','R4','R9'), 'nonwhite'] = 1

    # Preferred language not English
    df.loc[df['pls_abbr']=='ENG', 'non_english_speaking'] = 1

    # Prior pregnancies
    df['known_prior_pregnancy'] = 0
    for var in parm.dx_vars:
        df.loc[df[var].isin(mappings.prior_pregnancy_dxs), 'known_prior_pregnancy'] = 1

    # Mental illness DX3 (first 3 characters of DX)
    df['mental_illness'] = 0
    for var in parm.dx_vars:
        df.loc[df[var][0:3].isin(mappings.mental_illness_dx3s), 'mental_illness'] = 1

    # Intellectual disability DX3
    df['intellectual_disability'] = 0
    for var in parm.dx_vars:
        df.loc[df[var][0:3].isin(mappings.intellectual_disability_dx3s),\
                'intellectual_disability'] = 1

    check_these = ['larc','medicaid','latinx','nonwhite',\
                   'non_english_speaking','known_prior_pregnancy',\
                   'mental_illness','intellectual_disability']
    for vars in check_these:
        print(f'\nCheck -- {var}')
        print(df[var].value_counts(dropna=False))

    return df

