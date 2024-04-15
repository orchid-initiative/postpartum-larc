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

    # ******** LARC **********
    larc_dict = mappings.get_code_dicts(source=parm.code_sets,
                                        keep_columns=['PX','LARC_TYPE'],
                                        sheet_name='LARC') 

    df['larc'] = df[parm.px_vars].isin(list(larc_dict.keys())).any(axis=1)
    df['larc_uterine'] = df[parm.px_vars].isin(list(larc_dict.keys(value=='U')))
    df['larc_subcutaneous'] = df[parm.px_vars].isin(list(larc_dict.keys(value=='S')))


    # ******** PRIOR PREGNANCIES ********
    prior_pregnancy_dxs = mappings.get_code_lists(source=parm.code_sets,
                                     sheet_name='prior pregnancy')
    df['known_prior_pregnancy'] = df[parm.dx_vars].isin\
            (prior_pregnancy_dxs).any(axis=1)


    # ******** MENTAL ILLNESS ********
    mental_illness_dx3s = mappings.get_code_lists(source=parm.code_sets,
                                     sheet_name='mental illness')
    df['mental_illness'] = df[parm.dx_vars][:3].isin\
            (mental_illness_dx3s).any(axis=1)


    # ******** INTELLECTUAL DISABILITY ********
    intellectual_disability_dx3s = mappings.get_code_lists(
            source=parm.code_sets,
            sheet_name='intellectual disability')
    df['intellectual_disability'] = df[parm.dx_vars][:3].isin\
            (intellectual_disability_dx3s).any(axis=1)


    # ******** HEMORRAHAGE ********
    hemorrhage_dxs = mappings.get_code_lists(source=parm.code_sets,
                                            sheet_name='hemorrhage')
    df['hemorrhage'] = df[parm.dx_vars].isin(hemorrhage_dxs).any(axis=1)


    # ******** INTRAAMNIOTIC INFECTION ********
    intraamniotic_infection_dxs = mappings.get_code_lists(\
            source=parm.code_sets,
            sheet_name='intraamniotic infection')
    df['intraamniotic_infection'] = df[parm.dx_vars].isin\
            (intraamniotic_infection_dxs).any(axis=1)


    # ******** CHORIOAMNIONITIS ********
    chorioamnionitis_dxs = mappings.get_code_lists(source=parm.code_sets,
                                     sheet_name='chorioamnionitis')
    df['chorioamnionitis'] = df[parm.dx_vars].isin\
            (chorioamnionitis_dxs).any(axis=1)


    # ******** ENDOMETRITIS ********
    endometritis_dxs = mappings.get_code_lists(source=parm.code_sets,
                                     sheet_name='endometritis')
    df['endometritis'] = df[parm.dx_vars].isin\
            (endometritis_dxs).any(axis=1)


    # **** R E P O R T   O N   F L A G S **** 
    check_these = ['larc' ,'pay_cat','medicaid',
                   'pls_abbr','preferred_language_not_english',
                   'known_prior_pregnancy','mental_illness',
                   'intellectual_disability','hemorrhage',
                   'intraamniotic_infection','chorioamnionitis',
                   'endometritis'
                   ]

    for var in check_these:
        print(f'\nResults for -- {var}')
        print(df[var].value_counts(dropna=False))


    # **** A G G R E G A T E ****

    # *** O U T P U T   T O   .C S V
    record_info_vars = ['oshpd_id','agyradm','sex','ethncty','race1',
                        'dsch_yr','disp','MSDRG']
    
    vars_in_output = record_info_vars + check_these

    df[vars_in_output].to_csv(f'{outpath}/sample_{file_suffix}.csv',index=False,)

    return df

