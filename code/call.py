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
#  for Orchid Initiative
########################################################################
import csv
import time
from _subset_inputdata import subset_and_output
from _readin_and_report import readin_and_report
from _flag_and_output import flags
import parameters as parm

for filename in parm.infile_names:
    my_inpath = f'{parm.inpath}'
    my_infile = filename
    my_outfile_suffix = my_infile[-8:-4] # Slicing needs parameterized?
    my_outfile_filepath = f'{parm.outpath}/{parm.outputfile_prefix}_{my_outfile_suffix}'
    my_dateformats = parm.date_formats

    print(f'\n\n########## RUNNING subset_and_output for {my_outfile_suffix} ##########')

    subset_and_output(infilepath=f'{my_inpath}/{my_infile}',
                      filter_variable_name=parm.filter_variable_name,
                      filter_values=parm.filter_values,
                      variables_keep=parm.variables_keep,
                      outfilepath=f'{my_outfile_filepath}')
    #printElapsedTime(start_time=start_time)


    print(f'\n########## RUNNING readin_and_report for {my_outfile_suffix} ##########')
    dataframe=readin_and_report(filepath=f'{my_outfile_filepath}.csv',
                                datatypes=parm.datatypes,
                                variables_keep=parm.variables_keep,
                                # date_formats itself is not used, but 
                                # it provides the list of date vars.
                                date_formats=parm.date_formats,
                                value_count_variables=parm.value_count_variables)

    print(f'\n########## RUNNING flags for {my_outfile_suffix} ##########')
    start_time = time.time()
    flags(df=dataframe,file_suffix=my_outfile_suffix,outpath=parm.outpath)
    elapsed_time = time.time() - start_time
    print('Elapsed time (seconds):  ', elapsed_time)

