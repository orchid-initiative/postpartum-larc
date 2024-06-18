### USER_GUIDE.md

### PROGRAM DESCRIPTIONS

- call.py -- Calls the other programs, processing one input file at a time
- parameters.py -- Contains *user-defined* values for paths, filenames, subset constraints, reporting and output variables
- _get_mappings.py -- Makes *study-specific* relational data available to other programs 
- _subset_inputdata.py -- Subsets raw file for records and variables of interest
and writes subset data to text file.  Does not yet read into dataframe. 
- _readin_and_report.py -- Reads subsetted data into dataframe, reports on select variables
- _flag_and_output.py -- Makes *study-specific* inclusion/exclusion flags and categories.  Then subsets, aggregates, and outputs data for downstream reporting.

### RELATIONAL FILES DESCRIPTIONS
- LARC codes.xlsx -- Study-specific codesets prepared to identify LARCs, exclusion conditions, and categories
- Appendix H - Plan Codes.xlsx -- Provides health plan names
- Proc Format_PDD Hospital Name.xlsx -- Provides California hospital names

Both of the above files are from:  https://hcai.ca.gov/data/request-data/data-documentation/#2022-data-documentation 

### INSTRUCTIONS FOR RUNNING PROGRAMS

1. Clone the repository to your machine (computer or linux environment) by submitting the following at the command line in the directory where you want the programs and data:
  
`git clone git@github.com:orchid-initiative/postpartum-larc.git {user-defined subdirectory name}`

2. Make a new Git branch by submitting the following:
  
`git checkout -b {user-defined branch name}`

3. In parameters.py, edit paths and file names for your operating environment and input files
4. Run call.py by submitting the following at the command line:
  
`python -u call.py | tee call.log`

[Back to main README](../README.md)
