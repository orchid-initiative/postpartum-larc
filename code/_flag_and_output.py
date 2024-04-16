#######################################################################
# _flag_and_output.py  Adds inclusion and exclusion flags, and 
#                      category flags.  Then subsets, aggregates, 
#                      and outputs data for downstream reporting.
#
#                      NOTE:  This program is intended to be edited
#                             for and by the user to configure to
#                             their specs.  Clarity (showing each 
#                             condition) and user accessibility is 
#                             prioritized over concise coding.
#                             
# by Rhonda Tullis, 1/24/2024
# for Orchid Initiative
#######################################################################

import pandas as pd
import numpy as np
import time
import parameters as parm
import _get_mappings as mappings

# FLAG PROCEDURES, DEMOGRAPHICS, AND CONDITIONS
def flags(df, file_suffix, outpath):
   
    # **** F L A G   D E M O G R A P H I C - B A S E D   F L A G S ****
    
    # ******** MEDICAID ******** (if pay_cat=Medi-Cal)
    # else zero.  Missing pay_cat values will return missing values.
    df['medicaid'] = np.where(df['pay_cat']=='03', 1, 0) 


    # ******** PREFERRED_LANGUAGE_NOT_ENGLISH ********
    df['preferred_language_not_english'] = np.where(df['pls_abbr']\
            =='ENG', 0, 1)


    # **** R E A D   C O D E S E T S   F O R   E A C H   F L A G
    # **** T H E N   S E T   C O N D I T I O N   F L A G 

    # ******** LARCs *********
    larc_map = mappings.get_code_maps(source=parm.code_sets,
                                      sheet_name='LARC',
                                      subset_col='LARC_TYPE',
                                      subset_value='U'
                                      ) 
    df['larc_uterine'] = df[parm.px_vars].isin(larc_map).any(axis=1).astype(int)

    larc_map = mappings.get_code_maps(source=parm.code_sets,
                                      sheet_name='LARC',
                                      subset_col='LARC_TYPE',
                                      subset_value='S'
                                      ) 
    df['larc_subcutaneous'] = df[parm.px_vars].isin(larc_map).any(axis=1).astype(int)

    df['larc'] = ((df['larc_uterine'] + df['larc_subcutaneous']) > 0).astype(int)


    # ******** PRIOR PREGNANCIES ********
    prior_pregnancy_dxs = mappings.get_code_lists(source=parm.code_sets,
                                     sheet_name='prior pregnancy')
    df['known_prior_pregnancy'] = df[parm.dx_vars].isin\
            (prior_pregnancy_dxs).any(axis=1).astype(int)


    # ******** MENTAL ILLNESS AND INTELLECTUAL DISABILITY ********
    mental_illness_dx3s = mappings.get_code_lists(source=parm.code_sets,
                                            sheet_name='mental illness')

    intellectual_disability_dx3s = mappings.get_code_lists(
            source=parm.code_sets,
            sheet_name='intellectual disability')
    
    # Function to check 1st 3 chars in all DX vars against codeset lists
    def check_codes(cell, search_list):
        if type(cell)=='str':
            return any(substring in cell[:3] for substring in search_list) 

    # Flag mental illness
    df['mental_illness'] = df[parm.dx_vars].\
            applymap(lambda x: check_codes(x, \
                 search_list=mental_illness_dx3s)).any(axis=1).astype(int)

    # Flag intellectual disability
    df['intellectual_disability'] = df[parm.dx_vars].\
            applymap(lambda x: check_codes(x, \
                 search_list=intellectual_disability_dx3s)).any(axis=1).astype(int)


    # ******** HEMORRAHAGE ********
    hemorrhage_dxs = mappings.get_code_lists(source=parm.code_sets,
                                            sheet_name='hemorrhage')
    df['hemorrhage'] = df[parm.dx_vars].isin(hemorrhage_dxs).any(axis=1).astype(int)


    # ******** INTRAAMNIOTIC INFECTION ********
    intraamniotic_infection_dxs = mappings.get_code_lists(\
            source=parm.code_sets,
            sheet_name='intraamniotic infection')
    df['intraamniotic_infection'] = df[parm.dx_vars].isin\
            (intraamniotic_infection_dxs).any(axis=1).astype(int)


    # ******** CHORIOAMNIONITIS ********
    chorioamnionitis_dxs = mappings.get_code_lists(source=parm.code_sets,
                                     sheet_name='chorioamnionitis')
    df['chorioamnionitis'] = df[parm.dx_vars].isin\
            (chorioamnionitis_dxs).any(axis=1).astype(int)


    # ******** ENDOMETRITIS ********
    endometritis_dxs = mappings.get_code_lists(source=parm.code_sets,
                                     sheet_name='endometritis')
    df['endometritis'] = df[parm.dx_vars].isin\
            (endometritis_dxs).any(axis=1).astype(int)


    # **** R E P O R T   O N   F L A G S **** 

    groupby_these = ['oshpd_id','agyradm','ethncty','race1',
                     'dsch_yr','medicaid', 
                     'preferred_language_not_english',
                     'known_prior_pregnancy','mental_illness',
                     'intellectual_disability','hemorrhage',
                     'intraamniotic_infection','chorioamnionitis',
                     'endometritis']
    aggregate_these =['larc_uterine', 'larc_subcutaneous', 'larc']
    
    for var in groupby_these:
        print(f'\nResults for -- {var}')
        print(df[var].value_counts(dropna=False))


    # **** A G G R E G A T E ****
    df_summary = df.groupby(by=groupby_these, 
                            as_index=True, 
                            dropna=False,
                            group_keys=False)[aggregate_these]\
                                    .sum().reset_index()
    
    # *** O U T P U T   T O   .C S V
    df_summary.to_csv(f'{outpath}/sample_{file_suffix}.csv',index=False,)

    return df
   
