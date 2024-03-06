# 1_subset_inputdata.py 


import csv
from operator import itemgetter

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
def subset_and_output(filepath, 
                      selection_variable_name,
                      selection_values,
                      variables_keep,
                      outputfile_prefix,
                      outputfile_suffix):

    with open(filepath, buffering=1, mode='rt') as infile:
        print('Reading input file:  ',filepath)
        for count, line in enumerate(infile):
            #print('\nROW NUMBER:  ',count)
            if count==0:
                # Get header row for all the data
                headerrow_all = line.replace('\n','').split(sep=',')
                print('\nEntire dataset header row:')
                print(headerrow_all)
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
                #if headerrow_subset==variables_keep:
                    print("""--> Good.  The headerrow_subset contains the 
                             expected variables""")
                else:
                    print("""--> !! ERROR:  Header row subset and selected 
                            variables dont match!!!""")
                del hdr_subset, var_keep

                # Use headerrow subset as index list to use on data in next 
                # section
                datarow_idx = [i for i, val in enumerate(headerrow_all) \
                        if val in variables_keep] 
                print("""\nHere are the indices for selected variables:  """\
                        , datarow_idx)
                print('\nAnd here are the corresponding variables selected:  ')
                print(headerrow_subset)                    
                with open(f'{outputfile_prefix}_{outputfile_suffix}.csv', mode='w') \
                          as outfile:
                    writer = csv.writer(outfile)
                    writer.writerow(headerrow_subset)
                # Set subset_count (used in log)
                subset_count = 0

            else:
                # Convert line in input file to list
                datarow = line.replace('\n','').split(sep=',') 
                # Get the selection variable
                selection_var_idx = headerrow_all.index\
                        (f'{selection_variable_name}')

                # Look at whole line in file
                if count==1:
                    print('\nWhole line for first row of data:  ')
                    print(line)
                    # Print out selection criteria
                    print('\nSelection criteria for variable of interest:') 
                    print(f'{selection_variable_name=}')
                    print('is in:')
                    print(f'{selection_values=}')

                # Set 'keep' flag
                keep = (datarow[selection_var_idx] in(f'{selection_values}'))
                #print('Keeping row? :  ', keep)

                # Output record where keep=True
                # keep only variables of interest
                if keep==True:
                    # Count output records
                    subset_count = subset_count + 1
                    # Subset row for variables of interest
                    output_row = itemgetter(*datarow_idx)(datarow)
                    # Output data with select variables to file
                    with open(f'{outputfile_prefix}_{outputfile_suffix}.csv', mode='a') \
                            as outfile:
                        writer = csv.writer(outfile)
                        writer.writerow(output_row)

    print(f'\n{filepath}')
    print('TOTAL RECORDS:  ', count)
    print(f'\n{outputfile_prefix}_{outputfile_suffix}.csv')
    print('RECORDS IN SUBSET:  ', subset_count)
    # ending time
    # time elapsed

