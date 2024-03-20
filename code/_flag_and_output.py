#######################################################################
# _flag_and_output.py  Adds inclusion and exclusion flags, and 
#                      category flags.  Then subsets, aggregates, 
#                      and outputs data for downstream reporting.
#
# by Rhonda Tullis, 1/24/2024
# for Orchid Initiative
#######################################################################

import pandas as pd
import lxml
import datetime as dt


# Get lists of codes to use for exclusions and category flags
specs = "https://docs.google.com/document/d/141xp-JPispApGdvv8b8Ou8yDhxEQ6M6KO9Ats9ZrIHg/edit?usp=sharing"
obj = pd.read_html(specs)
print(obj)
"""
# Look for LARC procs
df['larc'] = 0
for var in proc_vars:
    df.loc[df[var].isin(larcs), 'larc'] = 1

report = ProfileReport(df=df, minimal=True)
report.to_file('readin_report.html')
"""
