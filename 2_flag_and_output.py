# 2_flag_and_output.py  Adds inclusion and exclusion flags,
#                       and category flags.  Then subsets 
#                       and outputs data for downstream 
#                       reporting.
#
# by Rhonda Tullis, 1/24/2024
# for Orchid Initiative

import pandas as pd
import lxml
import datetime as dt
from ydata_profiling import ProfileReport, compare

# MSDRGs for Labor & Delivery to select denominator records
ld_drgs = [768, 788, 807]

# LARC procedures (both snomed and ICD10)  >>> Testing PX that is present to make sure code works:  80146002
larcs = ['80146002','65200003','0UH97HZ','0UH98HZ','0UHC7HZ','0UHC8HZ','169553002','0JHD0HZ','0JHD3HZ','0JHF0HZ','0JHF3HZ']

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
