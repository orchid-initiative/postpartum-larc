#########################################################
# _readin_and_report.py   Reads in administrative hospital data,
#               produces data quality reports.
#
# by Rhonda Tullis, 1/05/2024
# for Orchid Initiative
#########################################################

import pandas as pd
import parameters as parm

# READ IN DATA
def readin_and_report(filepath,
                      datatypes,
                      variables_keep,
                      date_formats,
                      value_count_variables):

    # Derive list of dates from date_formats
    dates = list(date_formats.keys())
    
    # Read in
    df = pd.read_csv(filepath, 
                     dtype=datatypes, 
                     usecols=variables_keep,
                     parse_dates = dates)
    print('\nRead in of subset')
    print(filepath)
    print(df.describe(percentiles="").T)
    for var in value_count_variables:
        print('\n',df.value_counts(var,dropna=False))

    return df

