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

start_time = time.time()

for filename in parm.infile_names:
    my_inpath = parm.inpath
    my_infile = filename
    my_outfile_prefix = parm.outputfile_prefix
    my_outfile_suffix = \
          my_infile[parm.file_suffix_slice[0]:parm.file_suffix_slice[1]]
    my_outfile_filepath = \
          f'{parm.outpath}/{parm.outputfile_prefix}_{my_outfile_suffix}'
    my_dateformats = parm.date_formats

    print('\n\n\n','#'*10,f'RUNNING subset_and_output for {my_outfile_suffix}','#'*10)

    subset_and_output(infilepath=f'{my_inpath}/{my_infile}',
                      filter_variable_name=parm.filter_variable_name,
                      filter_values=parm.filter_values,
                      variables_keep=parm.variables_keep,
                      outfilepath=my_outfile_filepath)
    #printElapsedTime(start_time=start_time)


    print('\n\n','#'*10,f'RUNNING readin_and_report for {my_outfile_suffix}','#'*10)
    dataframe=readin_and_report(filepath=f'{my_outfile_filepath}.csv',
                                datatypes=parm.datatypes,
                                variables_keep=parm.variables_keep,
                                # date_formats itself is not used, but 
                                # it provides the list of date vars.
                                date_formats=parm.date_formats,
                                value_count_variables= \
                                        parm.value_count_variables)

    print('\n\n','#'*10,f'RUNNING flags for {my_outfile_suffix}','#'*10)
    flags(df=dataframe, file_suffix=my_outfile_suffix, outpath= \
            parm.outpath, outfile_prefix=my_outfile_prefix)

elapsed_time = time.time() - start_time
print('\n\nElapsed time (seconds):  ', elapsed_time)

