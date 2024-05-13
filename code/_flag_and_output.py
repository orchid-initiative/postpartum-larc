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

##################################################
# FLAG PROCEDURES, DEMOGRAPHICS, AND CONDITIONS
##################################################
def flags(df, file_suffix, outpath, outfile_prefix):
   
    #   S E T   S E V E R A L   S T A N D A R D   V A R I A B L E S
    #   Set labor and delivery variables to 1.  Data has already
    #   been subset in a previous program.
    df['l_and_d_total'] = 1

    #   Set age group using age in years at admission
    df['age_group'] = pd.cut(df['agyradm'], 
                             bins=parm.age_bins, 
                             labels=parm.age_bin_labels)

    #   For hospital ID, race, ethnicity, (and age group?), set missing 
    #   values to 'unknown' so that groupby will work correctly
    source_dimension_variables = ['oshpd_id', 
                                  'ethncty', 
                                  'race1' 
                                  ]

    for var in source_dimension_variables: 
        df.loc[df[var].isna(), var] = 'unknown'


    #   F L A G   D E M O G R A P H I C - B A S E D   F L A G S 
    
    # ******** MEDICAID ******** (if pay_cat=Medi-Cal)
    # else zero.  Missing pay_cat values will return missing values.
    df['medicaid'] = np.where(df['pay_cat']=='03', 1, 0) 


    # ******** PREFERRED_LANGUAGE_NOT_ENGLISH ********
    df['preferred_language_not_english'] = np.where(df['pls_abbr']\
            =='ENG', 0, 1)


    #   R E A D   C O D E S E T S   F O R   E A C H   F L A G
    #   T H E N   S E T   C O N D I T I O N   F L A G 

    # ******** LARCs *********
    # Uterine LARCs
    larc_u_map = mappings.get_code_maps(source=parm.code_sets,
                                      sheet_name='LARC',
                                      subset_col='LARC_TYPE',
                                      subset_value='U',
                                      filter_var='PX'
                                      ) 
    df['larc_uterine'] = df[parm.px_vars].isin(larc_u_map).\
            any(axis=1).astype(int)

    # Subcutaneous LARCs
    larc_s_map = mappings.get_code_maps(source=parm.code_sets,
                                      sheet_name='LARC',
                                      subset_col='LARC_TYPE',
                                      subset_value='S',
                                      filter_var='PX'
                                      ) 
    df['larc_subcutaneous'] = df[parm.px_vars].isin(larc_s_map).\
            any(axis=1).astype(int)

    # All LARCs
    df['larc'] = ((df['larc_uterine'] + df['larc_subcutaneous']) > 0)\
            .astype(int)


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
        if type(cell)==str:
            return any(substring in cell[:3] for substring in search_list)

    # Flag mental illness
    df['mental_illness'] = df[parm.dx_vars].\
            applymap(lambda x: check_codes(x, \
            search_list=mental_illness_dx3s)).any(axis=1).astype(int)

    # Flag intellectual disability
    df['intellectual_disability'] = df[parm.dx_vars].\
            applymap(lambda x: check_codes(x, \
                 search_list=intellectual_disability_dx3s)).any(axis=1)\
                 .astype(int)


    # ******** HEMORRAHAGE ********
    hemorrhage_dxs = mappings.get_code_lists(source=parm.code_sets,
                                            sheet_name='hemorrhage')
    df['hemorrhage'] = df[parm.dx_vars].isin(hemorrhage_dxs).any(axis=1)\
            .astype(int)


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


    # ******** USE CONDITION FLAGS TO SET EXCL FLAG ********
    df['excl'] = df[['hemorrhage', 'intraamniotic_infection',
                     'chorioamnionitis', 'endometritis']].any(axis=1).\
                             astype(int)


    # ******** MAKE VARIABLE FOR INCLUDED L & D ********
    df['l_and_d_incl'] = (df['excl']==0).astype(int)
    

    #   R E P O R T   O N   F L A G S 

    report_on_these = parm.aggregate_these + parm.groupby_these 

    for var in report_on_these:
        print(f'\nResults for -- {var}')
        print(df[var].value_counts(dropna=False).sort_index())

    # Report showing crosstab of age and age group
    print(f'\nResults for age mapping to groups')
    print(pd.crosstab(df['agyradm'], df['age_group']))


    #   A G G R E G A T E   A N D   O U T P U T   T 0   C S V
    #   Count exclusion conditions by hospital
    df_excl_summary = df.groupby(by='oshpd_id',
                                 observed=True,
                                 as_index=True,
                                 group_keys=False,
                                 dropna=False)\
                                         ['l_and_d_total',
                                          'l_and_d_incl',
                                          'excl',
                                          'hemorrhage',
                                          'intraamniotic_infection',
                                          'chorioamnionitis', 
                                          'endometritis'].apply(sum)
    df_excl_summary.to_csv(\
            f'{outpath}/{outfile_prefix}_EXCL_{file_suffix}.csv', 
            index=True)


    #   Make main aggregated output file for data visualizations,
    #   keeping only where excl equal 0
    df_main_summary = df[df['excl'] == 0].groupby(by=parm.groupby_these,
                            observed=True,
                            as_index=False,
                            group_keys=False,
                            dropna=False)[parm.aggregate_these]\
                                    .apply(sum)
    
    df_main_summary.to_csv(\
            f'{outpath}/{outfile_prefix}_SUMMARY_{file_suffix}.csv', 
            index=False)

