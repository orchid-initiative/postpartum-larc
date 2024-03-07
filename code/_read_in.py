# 1_read_in.py   Reads in administrative hospital data,
#                produces data quality reports.
#
# by Rhonda Tullis, 1/05/2024
# for Orchid Initiative

import pandas as pd
import datetime as dt
from ydata_profiling import ProfileReport, compare

# Location of data (currently CA synthetic data)
data_url = 'https://github.com/orchid-initiative/synthetic-database-project/files/13679383/csv_HCAIPDD_12-14-2023_1416.csv'

# READ IN DATA
# Data types
datatypes = ({'typcare':str, 
              'oshpd_id':str, 
              'hplzip':str, 
              'hplcnty':str,
              'srcroute_ns':str,
              'admtype_ns':str,
              'disp':str, 
              'pay_cat':str, 
              'patcnty':str, 
              'patzip':str,
              'data_id':str,
              'pat_id':str,
              'rln':str,
              'proc_p':str,
              'oproc2':str,
              'oproc3':str,
              'oproc4':str,
              'oproc5':str,
              'oproc6':str,
              'oproc7':str,
              'oproc8':str,
              'oproc9':str,
              'oproc10':str,
              'oproc11':str,
              'oproc12':str,
              'oproc13':str,
              'oproc14':str,
              'oproc15':str,
              'oproc16':str,
              'oproc17':str,
              'oproc18':str,
              'oproc19':str,
              'oproc20':str,
              'oproc21':str,
              'oproc22':str,
              'oproc23':str,
              'oproc24':str})

# Date formats
date_formats = {'admtdate':'%m%d%Y','dschdate':'%m%d%Y','proc_pdt':'%Y%m%d'}

# Date variables
dates = list(date_formats.keys())

# Read in
df = pd.read_csv(data_url, 
                 dtype=datatypes, 
                 usecols=('typcare','oshpd_id','data_id','pat_id','rln',
                          'agyradm','sex','ethncty','race1','race_grp','pls_abbr',
                          'patcnty','patzip',
                          'admtdate','dschdate','dsch_yr','los','srcpo_ns',
                          'srcroute_ns','admtype_ns','disp',
                          'pay_cat','pay_type','pay_plan','charge','MSDRG',
                          'diag_p','poa_p','proc_p','proc_pdt',
                          'odiag2','odiag3','odiag4','odiag5','odiag6',
                          'odiag7','odiag8','odiag9','odiag10','odiag11',
                          'odiag12','odiag13','odiag14','odiag15','odiag16',
                          'odiag17','odiag18','odiag19','odiag20','odiag21',
                          'odiag22','odiag23','odiag24',
                          'oproc2','oproc3','oproc4','oproc5','oproc6',
                          'oproc7','oproc8','oproc9','oproc10','oproc11',
                          'oproc12','oproc13','oproc14','oproc15','oproc16',
                          'oproc17','oproc18','oproc19','oproc20','oproc21',
                          'oproc22','oproc23','oproc24'),
                 parse_dates = dates,
                 date_format=date_formats
                 )

report = ProfileReport(df=df, minimal=True)
report.to_file('readin_report.html')

