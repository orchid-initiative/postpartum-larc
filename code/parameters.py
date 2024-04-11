########################################################################
#  parameters.py - User parameter file that contains all of the values 
#                  to be passed to the called programs
#
#  by Rhonda Tullis, 2/28/2024
########################################################################

# Root of your working directory
mainpath = '/home/rtullis/orchid_initiative/postpartum_larc' 

# Path and file name for input file
inpath = f'{mainpath}/raw'

# A dict w/list of the names of the input files 
# and a naming suffix to differentiate output files.
infile_names = ['csv_HCAIPDD_04-09-2024_1143_2018.csv',
                'csv_HCAIPDD_04-09-2024_1143_2019.csv',
                'csv_HCAIPDD_04-09-2024_1143_2020.csv',
                'csv_HCAIPDD_04-09-2024_1143_2021.csv',
                'csv_HCAIPDD_04-09-2024_1143_2022.csv',
                'csv_HCAIPDD_04-09-2024_1143_2023.csv',
                'csv_HCAIPDD_04-09-2024_1143_2024.csv'
                ]

# Used in the naming of output files, to differentiate when there are
# muliple files.  For example, if the input files have year in the name,
# use a slice to select the characters containing year.
# Example file name:  input_file_2024.csv
# Corresponding slice that is put in a tuple:  (-8,-4)
file_suffix_slice = (-8,-4)

# Document containing DX and PX codes for identifying procedure of 
# interest and conditions to flag
code_sets = f'{mainpath}/documentation/LARC codes.xlsx' 

# Output path for interim files
outpath = f'{mainpath}/created'

# Used in the name of the output files
outputfile_prefix = 'labor_and_delivery'

# Name of variable used to select denominator rows
filter_variable_name = 'MSDRG'

# Values for filter_variable_name for selecting denominator rows
filter_values = [768, 788, 807] #Labor and delivery DRGs

# Date formats for date variables that are read in and kept
date_formats = {'admtdate':'%m%d%Y','dschdate':'%m%d%Y'}

# Variable list for frequency report
value_count_variables = ['MSDRG','oshpd_id','dsch_yr',
                         'ethncty','race1','pls_abbr',
                         'pay_cat','pay_type','pay_plan']

# List of variables to keep in record-level output}
variables_keep = ['oshpd_id', 'data_id', 'pat_id', 'agyradm', 'sex', 
                  'ethncty', 'race1', 'race_grp', 'pls_abbr', 'patcnty',
                  'patzip', 'admtdate', 'dschdate', 'dsch_yr', 'los', 
                  'srcpo_ns', 'srcroute_ns', 'admtype_ns', 'disp', 
                  'pay_cat', 'pay_type', 'pay_plan', 'charge', 'MSDRG', 
                  'diag_p', 'poa_p', 'proc_p', 'odiag1',  
                  'odiag2', 'odiag3', 'odiag4', 'odiag5', 'odiag6', 
                  'odiag7', 'odiag8', 'odiag9', 'odiag10', 'odiag11',
                  'odiag12', 'odiag13', 'odiag14', 'odiag15', 'odiag16',
                  'odiag17', 'odiag18', 'odiag19', 'odiag20', 'odiag21',
                  'odiag22', 'odiag23', 'odiag24', 'oproc1',
                  'oproc2', 'oproc3', 'oproc4', 'oproc5', 'oproc6',
                  'oproc7', 'oproc8', 'oproc9', 'oproc10', 'oproc11',
                  'oproc12', 'oproc13', 'oproc14', 'oproc15', 'oproc16',
                  'oproc17', 'oproc18', 'oproc19', 'oproc20', 'oproc21',
                  'oproc22', 'oproc23', 'oproc24']

# List of DX variables to parse through
dx_vars = [x for x in variables_keep if 'diag' in x]

# List of PX variables to parse through
px_vars = [x for x in variables_keep if 'proc' in x]

# Data types for kept variables that need a string type indicated
datatypes = ({'oshpd_id':str, 
              'srcroute_ns':str,
              'admtype_ns':str,
              'disp':str, 
              'pay_cat':str, 
              'patcnty':str, 
              'patzip':str,
              'data_id':str,
              'pat_id':str,
              'diag_p':str,
              'odiag1':str,
              'odiag2':str,
              'odiag3':str,
              'odiag4':str,
              'odiag5':str,
              'odiag6':str,
              'odiag7':str,
              'odiag8':str,
              'odiag9':str,
              'odiag10':str,
              'odiag11':str,
              'odiag12':str,
              'odiag13':str,
              'odiag14':str,
              'odiag15':str,
              'odiag16':str,
              'odiag17':str,
              'odiag18':str,
              'odiag19':str,
              'odiag20':str,
              'odiag21':str,
              'odiag22':str,
              'odiag23':str,
              'odiag24':str,
              'odiag25':str,
              'proc_p':str,
              'oproc1':str,
              'oproc2':str,
              'oproc3':str,
              'oproc4':str,
              'oproc5':str,
              'oproc6':str,
              'oproc7':str,
              'oproc8':str,
              'oproc9':str,
              'oproc10':str,
              'oproc11':str,
              'oproc12':str,
              'oproc13':str,
              'oproc14':str,
              'oproc15':str,
              'oproc16':str,
              'oproc17':str,
              'oproc18':str,
              'oproc19':str,
              'oproc20':str,
              'oproc21':str,
              'oproc22':str,
              'oproc23':str,
              'oproc24':str})

