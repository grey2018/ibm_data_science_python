# -*- coding: utf-8 -*-
"""
Created on Fri Sep  4 13:45:28 2020

@author: Sergiy
"""

import pandas as pd # using dataframes (cols = variables of different types, rows = observations)

# absolute paths
path_311 = 'C:\\Users\\Sergiy\\Documents\\210 Education\\EDX - IBM - PDS5 Capstone Project\\2020-09\\data'
path_PLUTO = "C:\\Users\\Sergiy\\Documents\\210 Education\\EDX - IBM - PDS5 Capstone Project\\2020-09\\data\\PLUTO_for_WEB"

# TODO: use the RELATIVE paths
#path_311 = "\\data"
#path_PLUTO = "..\\data\\PLUTO_for_WEB"

#############################################################
# PLUTO dataset
# => NYC housing characterstics
############################################################

# reaad the files
df_pluto_bk = pd.read_csv(path_PLUTO + "\\BK_18v1.csv")
df_pluto_bx = pd.read_csv(path_PLUTO + "\\BX_18v1.csv")
df_pluto_mn = pd.read_csv(path_PLUTO + "\\MN_18v1.csv")
df_pluto_qn = pd.read_csv(path_PLUTO + "\\QN_18v1.csv")
df_pluto_si = pd.read_csv(path_PLUTO + "\\SI_18v1.csv")

df_pluto_bx.info()
# unique and valid zip codes
df_pluto_bx["ZipCode"].dropna().unique().shape # quiz 1, question 4
df_pluto_qn["ZipCode"].dropna().unique().shape # quiz 1, question 5

##############################################################
# 311 data set
# => NYC complaints
##############################################################

# read the file
df_311 = pd.read_csv(path_311 + "\\311_Service_Requests_from_2010_to_Present_min.csv")
#df_311 = pd.read_csv(path_311 + "\\311_Service_Requests_from_2010_to_Present_min.csv", 
#                     parse_dates=True, keep_date_col = True) # => memory error

######################################################
# STEP 1. EXPLORE THE DATA
######################################################

# first look at the data
df_first_last = df_311.head(10).append(df_311.tail(10))

# meta information
# df_311.dtypes # data types
df_311.info() # more info: dataframe, column types, memory use

# statisitcal summary 
df_311.describe() # only numerical columns
df_311.describe(include="all") # all columns

################################################
# STEP 2. REPAIR SOME ISSUES
################################################
# remove index column (introduced at csv creation)
del df_311['Unnamed: 0']

# convert data columns from objet to datetime
# TAKES VERY LONG! SKIP IF NOT NECESSARY
df_311['Created Date'] = pd.to_datetime(df_311['Created Date'], infer_datetime_format=True)
df_311['Closed Date'] = pd.to_datetime(df_311['Closed Date'])
# ,infer_datetime_format=True => should work faster (problems with NaN?)
# ,format="%m/%d/%Y, %H:%M:%S %p" => explicit format should work even faster
#df_first_last['Created Date'] = pd.to_datetime(df_first_last['Created Date'], format="%m/%d/%Y, %H:%M:%S %p")

# repeat summaries
df_first_last = df_311.head(10).append(df_311.tail(10))
df_311.info() # more info: dataframe, column types, memory use
summary_311 = df_311.describe(include="all") # all columns
################################################################

# QUIZ 1
df_311['Created Date'].dropna().min() # quiz 1, question 1
df_311['Created Date'].dropna().max() # quiz 1, question 2
df_311['Incident Address'].isna().sum() # quiz 1, question 3
###################################################

# QUIZ 2
df_311['Complaint Type'].dropna().count() # quiz 2, question 1 (s. also summary)
df_311['Complaint Type'].dropna().unique().shape # quiz 2, question 2
df_311['Complaint Type'].value_counts() # quiz 2, questions 3, 4, 5
complaints = df_311['Complaint Type'].value_counts() 
complaints_most = complaints.loc[complaints >= 800000] # quiz 2, question 5
# backup
summary_311.to_csv(path_311 + "\\summary_311.csv")
complaints.to_csv(path_311 + "\\complaints.csv")

##############################################################

# QUIZ 3
complaints = df_311['Borough'].value_counts() # all complaints over boroughs

#list({'HEATING','HEAT/HOT WATER'})
list(complaints_most.index.values)
#df_311.where('Complaint Type' in list(complaints_most.index.values))
#df_311_most = df_311[df_311['Complaint Type'].str.contains("|".join(list({"HEATING","HEAT/HOT WATER"})))]
df_311_most = df_311[df_311['Complaint Type'].str.contains("|".join(list(complaints_most.index.values)))]

df_311_most['Complaint Type'].value_counts() 
df_311_most['Borough'].value_counts()
df_311_most['Incident Zip'].value_counts()
df_311_most['Incident Address'].value_counts()
df_311_most['Status'].value_counts()

df_311_most.to_csv(path_311 + "\\df_311_most.csv")
#################################################################

# QUIZ 4
cols_rel = list({'Address', 'BldgArea', 'BldgDepth', 'BuiltFAR', 'CommFAR', 'FacilFAR', 
        'Lot', 'LotArea', 'LotDepth', 'NumBldgs', 'NumFloors', 'OfficeArea', 'ResArea',
        'ResidFAR', 'RetailArea', 'YearBuilt', 'YearAlter1', 'ZipCode', 'YCoord', 'XCoord'
        } )

