# test pgm to produce readin/subset/transform/aggregate steps 
# w/small test file

import csv
filepath = 'testdata.csv' 
#selection_logic = 
variables_keep = ['firstid', 'thirdthing']
outputfile_prefix = 'labor_and_delivery'

# Open the input file, one row at a time,
# count all records,
# keep and subset the header row for variables of interest,
# keep variables of interest,
# keep selected records
with open(filepath, buffering=1, mode='rt') as infile:
    print('Reading input file:  ',filepath)
    for count, line in enumerate(infile):
        if count==0:
            headerrow_all = line.replace('\n','').split(sep=',') #(minus single quotes and return char)
            print('\nEntire dataset header row:')
            print(headerrow_all)
            print('\nVariables of intereste are:')
            print(variables_keep)
            headerrow_subset = [x for x in headerrow_all if x in variables_keep]
            print('\nSubset header row (it should match above):  ')
            print(headerrow_subset)                    
            with open(f'{outputfile_prefix}_all.csv', mode='w') as outfile:
                writer = csv.writer(outfile)
                writer.writerow(headerrow_subset)
        else:

            keep_row = line[header
            quit()

