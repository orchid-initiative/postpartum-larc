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
def flags(df, file_suffix, outpath):

    # ******** LARC **********
    # Get list of PXs for LARCs
    larc_procedures = mappings.get_codelists(source=parm.code_sets,
                                             sheet_name='LARC') 
    # Set flag to zero for all records
    df['larc'] = 0
    # Set records where a PX is in the LARC list
    for var in parm.px_vars:
        df.loc[df[var].isin(larc_procedures), 'larc'] = 1
        

    # ******** MEDICAID ******** (if pay_cat=Medi-Cal)
    # else zero.  Missing pay_cat values will return missing values.
    df['medicaid'] = np.where(df['pay_cat']=='03', 1, 0) 


    # ******** PREFERRED_LANGUAGE_NOT_ENGLISH ********
    df['preferred_language_not_english'] = np.where(df['pls_abbr']=='ENG', 0, 1)


    # ******** PRIOR PREGNANCIES ********
    # Get list of DXs for prior pregnancies
    prior_pregnancy_dxs = mappings.get_codelists(source=parm.code_sets,
                                     sheet_name='prior pregnancy')
    # Set flag to zero for all records
    df['known_prior_pregnancy'] = 0
    # Set records where a DX is in the prior pregnancy list
    for var in parm.dx_vars:
        df.loc[df[var].isin(prior_pregnancy_dxs), \
                'known_prior_pregnancy'] = 1


    # ******** MENTAL ILLNESS ********
    # Get list of DX3s for mental illness
    mental_illness_dx3s = mappings.get_codelists(source=parm.code_sets,
                                     sheet_name='mental illness')
    # Set flag to zero for all records
    df['mental_illness'] = 0
    # Set records where first 3 chars of a DX is in mental illness list
    for var in parm.dx_vars:
        df.loc[df[var].str[:3].isin(mental_illness_dx3s), \
                'mental_illness'] = 1


    # ******** INTELLECTUAL DISABILITY ********
    # Get list of DX3s for intellectual disability
    intellectual_disability_dx3s = mappings.get_codelists(
            source=parm.code_sets,
            sheet_name='intellectual disability')
    # Set flag to zero for all records
    df['intellectual_disability'] = 0
    # Set records where first 3 chars of a DX in intellctl disablty list
    for var in parm.dx_vars:
        df.loc[df[var].str[:3].isin(intellectual_disability_dx3s),\
                'intellectual_disability'] = 1


    # ******** HEMORRAHAGE ********
    # Get list of DXs for hemorrhage 
    hemorrhage_dxs = mappings.get_codelists(source=parm.code_sets,
                                            sheet_name='hemorrhage')
    # Set flag to zero for all records
    df['hemorrhage'] = 0
    # Set records where a DX is in the hemorrhage list
    for var in parm.dx_vars:
        df.loc[df[var].isin(hemorrhage_dxs), 'hemorrhage'] = 1


    # ******** INTRAAMNIOTIC INFECTION ********
    # Get list of DXs for intraamniotic infection
    intraamniotic_infection_dxs = mappings.get_codelists(\
            source=parm.code_sets,
            sheet_name='intraamniotic infection')
    # Set flag to zero for all records
    df['intraamniotic_infection'] = 0
    # Set records where a DX is in the intraamniotic infection list
    for var in parm.dx_vars:
        df.loc[df[var].isin(intraamniotic_infection_dxs), \
                'intraamniotic_infection'] = 1


    # ******** CHORIOAMNIONITIS ********
    # Get list of DXs for chorioamnionitis
    chorioamnionitis_dxs = mappings.get_codelists(source=parm.code_sets,
                                     sheet_name='chorioamnionitis')
    # Set flag to zero for all records
    df['chorioamnionitis'] = 0
    # Set records where a DX is in the chorioamnionitis list
    for var in parm.dx_vars:
        df.loc[df[var].isin(chorioamnionitis_dxs), \
                'chorioamnionitis'] = 1


    # ******** ENDOMETRITIS ********
    # Get list of DXs for endometritis
    endometritis_dxs = mappings.get_codelists(source=parm.code_sets,
                                     sheet_name='endometritis')
    # Set flag to zero for all records
    df['endometritis'] = 0
    # Set records where a DX is in the endometritis list
    for var in parm.dx_vars:
        df.loc[df[var].isin(endometritis_dxs), \
                'endometritis'] = 1


    # Report on flags
    check_these = ['larc','pay_cat','medicaid',
                   'pls_abbr','preferred_language_not_english',
                   'known_prior_pregnancy','mental_illness',
                   'intellectual_disability','hemorrhage',
                   'intraamniotic_infection','chorioamnionitis',
                   'endometritis']

    for var in check_these:
        print(f'\nResults for -- {var}')
        print(df[var].value_counts(dropna=False))


    # Output to csv
    record_info_vars = ['oshpd_id','agyradm','sex','ethncty','race1',
                        'dsch_yr','disp','MSDRG']
    
    vars_in_output = record_info_vars + check_these

    df.to_csv(f'{outpath}/sample_{file_suffix}.csv',index=False,
              columns=vars_in_output)

    return df

