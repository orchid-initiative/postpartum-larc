########################################################################
#  call.py - references parameters.py and program files to do the 
#            following:
#
#  READ, SUBSET, AND OUTPUT TO FILE
#  Open the input file, one row at a time,
#  count all records,
#  keep and subset the header row for variables of interest,
#  output selected records with the selected variables 
#
#  by Rhonda Tullis, 2/28/2024
#
########################################################################
import csv
from operator import itemgetter
from _subset_inputdata import subset_and_output
import parameters as parm

for filename in parm.infile_names:
    my_inpath = f'{parm.inpath}'
    my_infile = filename
    my_outfile_suffix = my_infile[-8:-4] # Slicing needs parameterized?
    my_outfile_filepath = f'{parm.outpath}/{parm.outputfile_prefix}_{my_outfile_suffix}'

    print('\n')
    print('#'*72)
    print('RUNNING SUBSET_AND_OUTPUT')
    subset_and_output(infilepath=f'{my_inpath}/{my_infile}',
                      filter_variable_name=parm.filter_variable_name,
                      filter_values=parm.filter_values,
                      variables_keep=parm.variables_keep,
                      outfilepath=f'{my_outfile_filepath}')

