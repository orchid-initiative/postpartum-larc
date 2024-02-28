########################################################################
# READ, SUBSET, AND OUTPUT TO FILE
# Open the input file, one row at a time,
# count all records,
# keep and subset the header row for variables of interest,
# output selected records with the selected variables 
#
# USER DEFINED INPUTS:
#   filepath = {Path and file name for input file} 
#   selection_variable_name = {Name of variable used to select data}
#   selection_values = {Desired value for selection_variable_name}
#   variables_keep = {list of variables to keep in output}
#   outputfile_prefix = {will be used to name the subset output file}
########################################################################
import csv
from operator import itemgetter
from _subset_inputdata import subset_and_output

subset_and_output(filepath='/home/rtullis/orchid_initiative/postpartum_larc/raw/csv_HCAIPDD_01-31-2024_1538_2024.csv',
                  selection_variable_name='race1',
                  selection_values='R2',
                  variables_keep=['oshpd_id','data_id','pat_id',
                          'agyradm','sex','ethncty','race1','race_grp','pls_abbr',
                          'patcnty','patzip',
                          'admtdate','dschdate','dsch_yr','los','srcpo_ns',
                          'srcroute_ns','admtype_ns','disp',
                          'pay_cat','pay_type','pay_plan','charge','MSDRG',
                          'diag_p','poa_p','proc_p','proc_pdt',
                          'odiag2','odiag3','odiag4','odiag5','odiag6',
                          'odiag7','odiag8','odiag9','odiag10','odiag11',
                          'odiag12','odiag13','odiag14','odiag15','odiag16',
                          'odiag17','odiag18','odiag19','odiag20','odiag21',
                          'odiag22','odiag23','odiag24',
                          'oproc2','oproc3','oproc4','oproc5','oproc6',
                          'oproc7','oproc8','oproc9','oproc10','oproc11',
                          'oproc12','oproc13','oproc14','oproc15','oproc16',
                          'oproc17','oproc18','oproc19','oproc20','oproc21',
                          'oproc22','oproc23','oproc24'],
                  outputfile_prefix = 'labor_and_delivery_2024')


