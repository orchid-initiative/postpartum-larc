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

for filename in parm.file_names:
    my_inpath = f'{parm.inpath}'
    my_infile = filename
    my_outfile_suffix = my_infile[-8:-4]
    print(f'Heres my file location:  {my_inpath}/{my_infile}')
    print('Heres my outfile name suffix:  ', my_outfile_suffix)
   
    subset_and_output(filepath=f'{my_inpath}/{my_infile}',
                      selection_variable_name=parm.selection_variable_name,
                      selection_values=parm.selection_values,
                      variables_keep=parm.variables_keep,
                      outputfile_prefix=parm.outputfile_prefix,
                      outputfile_suffix=my_outfile_suffix)


