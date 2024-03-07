########################################################################
#  parameters.py - contains all of the values to be passed to the 
#                  called programs
#
#  by Rhonda Tullis, 2/28/2024
########################################################################

# mainpath = root of your working directory
mainpath='/home/rtullis/orchid_initiative/postpartum_larc' 

# inpath = {Path and file name for input file} 
inpath=f'{mainpath}/raw'

# input_files = {a dict w/list of the names of the input files 
#                and a naming suffix to differentiate output files}
infile_names=['csv_HCAIPDD_01-31-2024_1538_2018.csv',
              'csv_HCAIPDD_01-31-2024_1538_2019.csv',
              'csv_HCAIPDD_01-31-2024_1538_2020.csv',
              'csv_HCAIPDD_01-31-2024_1538_2021.csv',
              'csv_HCAIPDD_01-31-2024_1538_2022.csv',
              'csv_HCAIPDD_01-31-2024_1538_2023.csv',
              'csv_HCAIPDD_01-31-2024_1538_2024.csv']

# output path for interim files
outpath=f'{mainpath}/created'

# outputfile_prefix = {Used in the name of the output files}
outputfile_prefix = 'labor_and_delivery'

# selection_variable_name = {Name of variable used to select data}
filter_variable_name='admtype_ns'

# selection_values = {Desired values for selection_variable_name}
filter_values=[4, 5, 6]

# variables_keep = {list of variables to keep in output}
variables_keep=['oshpd_id', 'data_id', 'pat_id', 'agyradm', 'sex', 
                'ethncty', 'race1', 'race_grp', 'pls_abbr', 'patcnty',
                'patzip', 'admtdate', 'dschdate', 'dsch_yr', 'los', 
                'srcpo_ns', 'srcroute_ns', 'admtype_ns', 'disp', 
                'pay_cat', 'pay_type', 'pay_plan', 'charge', 'MSDRG', 
                'diag_p', 'poa_p', 'proc_p', 'proc_pdt',
                'odiag2', 'odiag3', 'odiag4', 'odiag5', 'odiag6', 
                'odiag7', 'odiag8', 'odiag9', 'odiag10', 'odiag11',
                'odiag12', 'odiag13', 'odiag14', 'odiag15', 'odiag16',
                'odiag17', 'odiag18', 'odiag19', 'odiag20', 'odiag21',
                'odiag22', 'odiag23', 'odiag24', 
                'oproc2', 'oproc3', 'oproc4', 'oproc5', 'oproc6',
                'oproc7', 'oproc8', 'oproc9', 'oproc10', 'oproc11',
                'oproc12', 'oproc13', 'oproc14', 'oproc15', 'oproc16',
                'oproc17', 'oproc18', 'oproc19', 'oproc20', 'oproc21',
                'oproc22', 'oproc23', 'oproc24']

