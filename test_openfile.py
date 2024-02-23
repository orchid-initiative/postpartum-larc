# test pgm to produce readin/subset/transform/aggregate steps 
# w/small test file

import csv
from operator import itemgetter
filepath = 'testdata.csv' 
selection_variable_name = 'thirdthing'
selection_values = "uio"
variables_keep = ['firstid', 'thirdthing']
outputfile_prefix = 'labor_and_delivery'

# Open the input file, one row at a time,
# count all records,
# keep and subset the header row for variables of interest,
# output selected records with the selected variables 
with open(filepath, buffering=1, mode='rt') as infile:
    print('Reading input file:  ',filepath)
    for count, line in enumerate(infile):
        print('\nROW NUMBER:  ',count)
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
            print("""\nCheck to see if headerrow_subset and variables_keep
                    match.""")
            if headerrow_subset==variables_keep:
                print("""--> Good.  The headerrow_subset contains the 
                        expected variables""")
            else:
                print("""--> !! ERROR:  Header row subset and selected 
                        variables dont match!!!""")

            # Use headerrow subset as index list to use on data in next 
            # section
            datarow_idx = [i for i, val in enumerate(headerrow_all) \
                    if val in variables_keep] 
            print("""\nHere are the indices for selected variables:  """\
                    , datarow_idx)
            print(headerrow_subset)                    
            with open(f'{outputfile_prefix}_all.csv', mode='w') as outfile:
                writer = csv.writer(outfile)
                writer.writerow(headerrow_subset)

        else:
            print('Datarow_idx is:  ', datarow_idx)
            # Convert line in input file to list
            datarow = line.replace('\n','').split(sep=',') 
            # Get the selection variable
            selection_var_idx = headerrow_all.index\
                    (f'{selection_variable_name}')
            # Look at whole line in file
            print('\nWhole line:  ')
            print(line)
            # Print out selection criteria
            print('Selection criteria for variable of interest:')  
            print(f'{selection_variable_name} == {selection_values}')
            # Set 'keep' flag
            keep = datarow[selection_var_idx]==f'{selection_values}'
            print('Keeping row? :  ', keep)
            # Output record where keep=True
            # keep only variables of interest
            if keep==True:
                # Subset row for variables of interest
                output_row = itemgetter(*datarow_idx)(datarow)
                # Output data with select variables to file
                with open(f'{outputfile_prefix}_all.csv', mode='a') \
                        as outfile:
                    writer = csv.writer(outfile)
                    writer.writerow(output_row)
            else:
                print('Record does not get printed to output file')

