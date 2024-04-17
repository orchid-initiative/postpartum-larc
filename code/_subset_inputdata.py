########################################################################
# READ, SUBSET, AND OUTPUT TO FILE
# Open the input file, one row at a time,
# count all records,
# keep and subset the header row for variables of interest,
# output selected records with the selected variables 
#
# USER DEFINED INPUTS:
#   infilepath = {Path and file name for input file} 
#   filter_variable_name = {Name of variable used to select data}
#   filter_values = {Desired value for filter_variable_name}
#   variables_keep = {list of variables to keep in output}
#   outfile_path = {Is derived. Used to name the subset output file}
#
# NOTE:  CHOICE TO USE with open(file) INSTEAD OF PANDAS
#        READ_CSV was made due to performance considerations.
#        This program is intended for use on files as large
#        as a million rows or larger.
#
# by Rhonda Tullis, 2/01/2024
# for Orchid Initiative
########################################################################

import csv
from operator import itemgetter

def subset_and_output(infilepath, 
                      filter_variable_name,
                      filter_values,
                      variables_keep,
                      outfilepath):

    with open(infilepath, buffering=1, mode='rt') as infile:
        print('\nReading input file:  ', infilepath)
        for count, line in enumerate(infile):
            if count==0:
                # Get header row for all the data
                headerrow_all = line.replace('\n','').split(sep=',')
                print('\nVariables of interest are:')
                print(variables_keep)

                # Using the variables_keep parameter, get new header row 
                # with variables of interest. This is used in output file
                headerrow_subset = [x for x in headerrow_all if x in \
                        variables_keep]
                print("""\nCheck to see if headerrow_subset and 
                         variables_keep match.""")
                # Keep versions of the original order, but also make
                # sorted lists to compare
                hdr_subset = sorted(headerrow_subset)
                var_keep = sorted(variables_keep)
                if hdr_subset==var_keep:
                    print("""--> Good.  The headerrow_subset contains 
                             the expected variables""")
                else:
                    print("""--> !! ERROR:  Header row subset and 
                             selected variables dont match!!!""")
                del hdr_subset, var_keep

                # Use headerrow subset as index list to use on data in next 
                # section
                datarow_idx = [i for i, val in enumerate(headerrow_all) \
                        if val in variables_keep] 
                print("""\nHere are the indices for selected variables:  """\
                        , datarow_idx)
                print('\nAnd here are the corresponding variables selected:  ')
                print(headerrow_subset)                    
                with open(f'{outfilepath}.csv', mode='w') \
                          as outfile:
                    writer = csv.writer(outfile)
                    writer.writerow(headerrow_subset)
                # Set subset_count (used in log)
                subset_count = 0

            else:
                # Convert line in input file to list
                datarow = line.replace('\n','').split(sep=',') 
                # Get the selection variable
                filter_var_idx = headerrow_all.index\
                        (f'{filter_variable_name}')

                # Look at whole line in file
                if count==1:
                    print('\nWhole line for first row of data:  ')
                    print(line)
                    # Print out selection criteria
                    print('\nSelection criteria for variable of interest:') 
                    print(f'{filter_variable_name=}')
                    print('is in:')
                    print(f'{filter_values=}')

                # Set 'keep' flag. Dont look where values are missing
                if len(datarow[filter_var_idx])>0:
                    keep = (datarow[filter_var_idx] in(f'{filter_values}'))

                # Output record where keep=True
                # keep only variables of interest
                if keep==True:
                    # Count output records
                    subset_count = subset_count + 1
                    # Subset row for variables of interest
                    output_row = itemgetter(*datarow_idx)(datarow)
                    # Output data with select variables to file
                    with open(f'{outfilepath}.csv', mode='a') \
                            as outfile:
                        writer = csv.writer(outfile)
                        writer.writerow(output_row)
                        # Set keep value to False for next row
                        keep = False

    print(f'\n{infilepath}')
    print('TOTAL RECORDS INPUT:  ', count)
    print(f'\n{outfilepath}.csv')
    print('RECORDS OUTPUT IN SUBSET:  ', subset_count)

