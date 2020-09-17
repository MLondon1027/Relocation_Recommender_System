import pandas as pd
import numpy as np
pd.set_option('mode.chained_assignment', None)
import warnings
warnings.filterwarnings("ignore")

# Import datasets
data = pd.read_csv('data/ACSST5Y2018.S0101_data_with_overlays_2020-09-09T171138.csv', low_memory=False, header=1)
real_estate = pd.read_excel('data/HPI_AT_BDL_ZIP5.xlsx')
veteran = pd.read_csv('data/ACSST5Y2018.S2101_data_with_overlays_2020-09-14T113935.csv', low_memory=False, header=1)
transportation = pd.read_csv('data/ACSST5Y2018.S0801_data_with_overlays_2020-09-05T010054.csv', low_memory=False, header=1)
financial_char = pd.read_csv('data/ACSST5Y2018.S2503_data_with_overlays_2020-09-08T115524.csv', low_memory=False, header=1)
education = pd.read_csv('data/Education.csv', low_memory=False, header=1)
employment = pd.read_csv('data/ACSST5Y2018.S2302_data_with_overlays_2020-09-08T190000.csv', low_memory=False, header=1)
marital = pd.read_csv('data/ACSST5Y2018.S1201_data_with_overlays_2020-09-14T121102.csv', low_memory=False, header=1)
language = pd.read_csv('data/ACSST5Y2018.S1601_data_with_overlays_2020-09-14T123248.csv', low_memory=False, header=1)
density = pd.read_csv('data/uszips.csv')
dem_char = pd.read_csv('data/ACSST5Y2018.S2502_data_with_overlays_2020-09-08T190727.csv', low_memory=False, header=1)
housing_char = pd.read_csv('data/Physical_Housing_Characteristics.csv', low_memory=False, header=1)

# Clean data dataframe
data = data[data.columns.drop(list(data.filter(regex='^Margin')))] # Delete margin of error cols
data = data.replace({'(X)': np.nan}) # Replace (X) with NaN values
data.drop(['Estimate!!Percent!!Total population'], axis=1, inplace=True) # Drop estimate percent total population because it doesn't make sense
data['Estimate!!Percent Male!!Total population'] = data['Estimate!!Male!!Total population']/data['Estimate!!Total!!Total population'] # Fill in percentage male total population
data['Estimate!!Percent Female!!Total population'] = data['Estimate!!Female!!Total population']/data['Estimate!!Total!!Total population'] # Fill in percentage female total population
data.drop(['Estimate!!Female!!PERCENT ALLOCATED!!Sex'], axis=1, inplace=True) # Delete percent allocated columns
data.drop(['Estimate!!Percent Female!!PERCENT ALLOCATED!!Sex'], axis=1, inplace=True) # Delete percent allocated columns
data.drop(['Estimate!!Total!!PERCENT ALLOCATED!!Age'], axis=1, inplace=True) # Delete percent allocated columns
data.drop(['Estimate!!Percent!!PERCENT ALLOCATED!!Age'], axis=1, inplace=True) # Delete percent allocated columns
data.drop(['Estimate!!Male!!PERCENT ALLOCATED!!Age'], axis=1, inplace=True) # Delete percent allocated columns
data.drop(['Estimate!!Percent Male!!PERCENT ALLOCATED!!Age'], axis=1, inplace=True) # Delete percent allocated columns
data.drop(['Estimate!!Female!!PERCENT ALLOCATED!!Age'], axis=1, inplace=True) # Delete percent allocated columns
data.drop(['Estimate!!Percent Female!!PERCENT ALLOCATED!!Age'], axis=1, inplace=True) # Delete percent allocated columns
data.drop('Estimate!!Total!!PERCENT ALLOCATED!!Sex', axis=1, inplace=True) # Delete percent allocated columns
data['zip'] = data['Geographic Area Name'].str[-5:] # Add zip code column
data.drop('id', axis=1, inplace=True) # Drop id column
data.drop('Geographic Area Name', axis=1, inplace=True) # Drop Geo Area Name column
data = data.loc[:, ~(data == '(X)').any()] # Drop columns with any (X)
data.set_index('zip', inplace=True) # Set zip as index
total_pop = data['Estimate!!Total!!Total population'] # Remove total_population from data
data_percents = data.filter(regex='Percent') # Keep percent columns
data_percents['total_pop'] = total_pop # Add back in total pop column
data_percents = data_percents.replace({'-': np.nan})
data_percents.dropna(axis=1, how='all', inplace=True)
for i in data_percents.columns:
    try:
        data_percents[i] = data_percents[i].astype(float)
    except:
        continue
data_percents = data_percents.select_dtypes(exclude=['object']) # Delete dtypes that are not floats
data_percents.rename(columns={'Estimate!!Percent!!Total population!!AGE!!Under 5 years' : 'Percent_Under_5'}, inplace=True)
data_percents.rename(columns=  {'Estimate!!Percent!!Total population!!AGE!!5 to 9 years': 'Percent_5_to_9'}, inplace=True)
data_percents.rename(columns = {'Estimate!!Percent!!Total population!!AGE!!10 to 14 years': 'Percent_10_to_14'}, inplace=True)
data_percents.rename(columns = {'Estimate!!Percent!!Total population!!AGE!!15 to 19 years': 'Percent_15_to_19'}, inplace=True)
data_percents.rename(columns = {'Estimate!!Percent!!Total population!!AGE!!20 to 24 years': 'Percent_20_to_24'}, inplace=True)
data_percents.rename(columns = {'Estimate!!Percent!!Total population!!AGE!!25 to 29 years': 'Percent_25_to_29'}, inplace=True)
data_percents.rename(columns = {'Estimate!!Percent!!Total population!!AGE!!30 to 34 years': 'Percent_30_to_34'}, inplace=True)
data_percents.rename(columns = {'Estimate!!Percent!!Total population!!AGE!!35 to 39 years': 'Percent_35_to_39'}, inplace=True)
data_percents.rename(columns = {'Estimate!!Percent!!Total population!!AGE!!40 to 44 years': 'Percent_40_to_44'}, inplace=True)
data_percents.rename(columns = {'Estimate!!Percent!!Total population!!AGE!!45 to 49 years': 'Percent_45_to_49'}, inplace=True)
data_percents.rename(columns = {'Estimate!!Percent!!Total population!!AGE!!50 to 54 years': 'Percent_50_to_54'}, inplace=True)
data_percents.rename(columns = {'Estimate!!Percent!!Total population!!AGE!!55 to 59 years': 'Percent_55_to_59'}, inplace=True)
data_percents.rename(columns = {'Estimate!!Percent!!Total population!!AGE!!60 to 64 years': 'Percent_60_to_64'}, inplace=True)
data_percents.rename(columns = {'Estimate!!Percent!!Total population!!AGE!!65 to 69 years': 'Percent_65_to_69'}, inplace=True)
data_percents.rename(columns = {'Estimate!!Percent!!Total population!!AGE!!70 to 74 years': 'Percent_70_to_74'}, inplace=True)
data_percents.rename(columns = {'Estimate!!Percent!!Total population!!AGE!!75 to 79 years': 'Percent_75_to_79'}, inplace=True)
data_percents.rename(columns = {'Estimate!!Percent!!Total population!!AGE!!80 to 84 years': 'Percent_80_to_84'}, inplace=True)
data_percents.rename(columns = {'Estimate!!Percent!!Total population!!AGE!!85 years and over': 'Percent_85_Plus'}, inplace=True)
data_percents = data_percents[['total_pop', 'Percent_Under_5', 'Percent_5_to_9', 
                               'Percent_10_to_14', 'Percent_15_to_19', 'Percent_20_to_24', 
                               'Percent_25_to_29', 'Percent_30_to_34', 'Percent_35_to_39', 
                               'Percent_40_to_44', 'Percent_45_to_49', 'Percent_50_to_54', 
                               'Percent_55_to_59', 'Percent_60_to_64', 'Percent_65_to_69', 
                               'Percent_70_to_74', 'Percent_75_to_79', 'Percent_80_to_84', 'Percent_85_Plus']]

# Clean density dataframe
density = density[['zip', 'density']]
density['zip'] = density['zip'].astype(str) # Set zip as string
density['zip']=density['zip'].str.rjust(5, "0") # Fill zip codes that begin with 0
density.set_index('zip', inplace=True) # Set zip as index

# Clean real estate dataframe
real_estate = real_estate.iloc[5:] # Drop first 5 rows of headers
real_estate.rename(columns=real_estate.iloc[0], inplace = True) # Assign first row as header
real_estate = real_estate.iloc[1:] # Delete repeating row
real_estate_2019 = real_estate[real_estate['Year']=='2019'] # Select rows that are 2019
real_estate_2019.rename(columns={'Five-Digit ZIP Code': 'zip'}, inplace=True) # Rename zip code column to zip
real_estate_2019 = real_estate_2019[['zip', 'Annual Change (%)', 'HPI']] # Select only columns needed
real_estate_2019.set_index('zip', inplace=True) # Set zip as index
real_estate_2019.rename(columns={'Annual Change (%)': 'HPI_%_Annual_Change'}, inplace=True) # Rename annual change % column

# Clean housing characteristics dataframe
housing_char['zip'] = housing_char['Geographic Area Name'].str[-5:]
housing_char = housing_char[housing_char.columns.drop(list(housing_char.filter(regex='^Margin')))]
housing_char.drop('id', axis=1, inplace=True)
housing_char.drop('Geographic Area Name', axis=1, inplace=True)
housing_char.set_index('zip', inplace=True)
housing_char_percents = housing_char.filter(regex='Percent')
housing_char_percents = housing_char_percents.replace({'-': np.nan})
for i in housing_char_percents.columns:
    try:
        housing_char_percents[i] = housing_char_percents[i].astype(float)
    except:
        continue
housing_char_percents.rename(columns={'Estimate!!Percent occupied housing units!!Occupied housing units!!UNITS IN STRUCTURE!!1, detached': 'Percent_SF_Houses_Det'}, inplace=True)
housing_char_percents.rename(columns={'Estimate!!Percent occupied housing units!!Occupied housing units!!UNITS IN STRUCTURE!!1, attached': 'Percent_SF_Houses_Att'}, inplace=True)
housing_char_percents.rename(columns={'Estimate!!Percent occupied housing units!!Occupied housing units!!UNITS IN STRUCTURE!!2 apartments': 'Percent_2F_Apts'}, inplace=True)
housing_char_percents.rename(columns={'Estimate!!Percent occupied housing units!!Occupied housing units!!UNITS IN STRUCTURE!!3 or 4 apartments': 'Percent_3_4F_Apts'}, inplace=True)
housing_char_percents.rename(columns={'Estimate!!Percent occupied housing units!!Occupied housing units!!UNITS IN STRUCTURE!!5 to 9 apartments':'Percent_5_9F_Apts'}, inplace=True)
housing_char_percents.rename(columns={'Estimate!!Percent occupied housing units!!Occupied housing units!!UNITS IN STRUCTURE!!10 or more apartments':'Percent_10_PlusF_Apts'}, inplace=True)
housing_char_percents.rename(columns={'Estimate!!Percent occupied housing units!!Occupied housing units!!UNITS IN STRUCTURE!!Mobile home or other type of housing':'Percent_Mobile_Home'}, inplace=True)
housing_char_percents.rename(columns={'Estimate!!Percent occupied housing units!!Occupied housing units!!YEAR STRUCTURE BUILT!!2014 or later':'Percent_Yr_Built_2014_Plus'}, inplace=True)
housing_char_percents.rename(columns={'Estimate!!Percent occupied housing units!!Occupied housing units!!YEAR STRUCTURE BUILT!!2010 to 2013':'Percent_Yr_Built_2010_2013'}, inplace=True)
housing_char_percents.rename(columns={'Estimate!!Percent occupied housing units!!Occupied housing units!!YEAR STRUCTURE BUILT!!2000 to 2009':'Percent_Yr_Built_2000_2009'}, inplace=True)
housing_char_percents.rename(columns={'Estimate!!Percent occupied housing units!!Occupied housing units!!YEAR STRUCTURE BUILT!!1980 to 1999':'Percent_Yr_Built_1980_1999'}, inplace=True)
housing_char_percents.rename(columns={'Estimate!!Percent occupied housing units!!Occupied housing units!!YEAR STRUCTURE BUILT!!1960 to 1979':'Percent_Yr_Built_1960_1979'}, inplace=True)
housing_char_percents.rename(columns={'Estimate!!Percent occupied housing units!!Occupied housing units!!YEAR STRUCTURE BUILT!!1940 to 1959':'Percent_Yr_Built_1940_1959'}, inplace=True)
housing_char_percents.rename(columns={'Estimate!!Percent occupied housing units!!Occupied housing units!!YEAR STRUCTURE BUILT!!1939 or earlier':'Percent_Yr_Built_1939_Prior'}, inplace=True)
housing_char_percents = housing_char_percents[['Percent_SF_Houses_Det', 'Percent_SF_Houses_Att', 'Percent_2F_Apts', 'Percent_3_4F_Apts', 'Percent_5_9F_Apts', 'Percent_10_PlusF_Apts', 'Percent_Mobile_Home', 'Percent_Yr_Built_2014_Plus', 'Percent_Yr_Built_2010_2013', 'Percent_Yr_Built_2000_2009', 'Percent_Yr_Built_1980_1999', 'Percent_Yr_Built_1960_1979', 'Percent_Yr_Built_1940_1959', 'Percent_Yr_Built_1939_Prior']]

# Clean demographic characteristics dataframe
dem_char['zip'] = dem_char['Geographic Area Name'].str[-5:]
dem_char = dem_char[dem_char.columns.drop(list(dem_char.filter(regex='^Margin')))]
dem_char.drop('id', axis=1, inplace=True)
dem_char.drop('Geographic Area Name', axis=1, inplace=True)
dem_char.set_index('zip', inplace=True)
dem_char_percents = dem_char.filter(regex='Percent')
dem_char_percents = dem_char_percents.replace({'-': np.nan})
for i in dem_char_percents.columns:
    try:
        dem_char_percents[i] = dem_char_percents[i].astype(float)
    except:
        continue
dem_char_percents.rename(columns={'Estimate!!Percent occupied housing units!!Occupied housing units!!YEAR HOUSEHOLDER MOVED INTO UNIT!!Moved in 2017 or later':'Percent_Moved_In_2017_Plus'}, inplace=True)
dem_char_percents.rename(columns={'Estimate!!Percent occupied housing units!!Occupied housing units!!YEAR HOUSEHOLDER MOVED INTO UNIT!!Moved in 2015 to 2016':'Percent_Moved_In_2015_2016'}, inplace=True)
dem_char_percents.rename(columns={'Estimate!!Percent occupied housing units!!Occupied housing units!!YEAR HOUSEHOLDER MOVED INTO UNIT!!Moved in 2010 to 2014':'Percent_Moved_In_2010_2014'}, inplace=True)
dem_char_percents.rename(columns={'Estimate!!Percent occupied housing units!!Occupied housing units!!YEAR HOUSEHOLDER MOVED INTO UNIT!!Moved in 2000 to 2009':'Percent_Moved_In_2000_2009'}, inplace=True)
dem_char_percents.rename(columns={'Estimate!!Percent occupied housing units!!Occupied housing units!!YEAR HOUSEHOLDER MOVED INTO UNIT!!Moved in 1990 to 1999':'Percent_Moved_In_1990_1999'}, inplace=True)
dem_char_percents.rename(columns={'Estimate!!Percent occupied housing units!!Occupied housing units!!YEAR HOUSEHOLDER MOVED INTO UNIT!!Moved in 1989 or earlier':'Percent_Moved_In_1989_Prior'}, inplace=True)
dem_char_percents = dem_char_percents[['Percent_Moved_In_2017_Plus', 'Percent_Moved_In_2015_2016', 'Percent_Moved_In_2010_2014', 'Percent_Moved_In_2000_2009', 'Percent_Moved_In_1990_1999', 'Percent_Moved_In_1989_Prior']]

# Clean veteran dataframe
veteran['zip'] = veteran['Geographic Area Name'].str[-5:] # Add zip code column
veteran = veteran[veteran.columns.drop(list(veteran.filter(regex='^Margin')))] # Delete margin of error column
veteran.drop('id', axis=1, inplace=True) # Drop id column
veteran.drop('Geographic Area Name', axis=1, inplace=True) # Drop Geo Area Name column
veteran = veteran.loc[:, ~(veteran == '(X)').any()] # Drop columns with any (X)
veteran.set_index('zip', inplace=True) # Set zip as index
veteran_percents = veteran.filter(regex='Percent') # Keep percentage columns
veteran_percents = veteran_percents.replace({'-': np.nan})
for i in veteran_percents.columns:
    try:
        veteran_percents[i] = veteran_percents[i].astype(float)
    except:
        continue
veteran_percents.rename(columns = {'Estimate!!Percent Veterans!!Civilian population 18 years and over' : 'Percent_Veterans'}, inplace=True)
veteran_percents = veteran_percents[['Percent_Veterans']] # Final veterans dataset

# Clean transportation dataframe
transportation['zip'] = transportation['Geographic Area Name'].str[-5:] # Add zip code column
transportation = transportation[transportation.columns.drop(list(transportation.filter(regex='MOE')))] # Delete margin of error column
transportation.drop('id', axis=1, inplace=True) # Drop id column
transportation.drop('Geographic Area Name', axis=1, inplace=True) # Drop Geographic Area Name column
transportation = transportation.loc[:, ~(transportation == '(X)').any()] # Drop columns with any (X)
transportation.set_index('zip', inplace=True) # Set zip as index
transportation.rename(columns = {'Estimate!!Total!!Workers 16 years and over!!MEANS OF TRANSPORTATION TO WORK!!Car, truck, or van' : 'Percent_Private_Vehicle'}, inplace=True)
transportation.rename(columns = {'Estimate!!Total!!Workers 16 years and over!!MEANS OF TRANSPORTATION TO WORK!!Public transportation (excluding taxicab)' : 'Percent_Public_Trans'}, inplace=True)
transportation.rename(columns = {'Estimate!!Total!!Workers 16 years and over!!MEANS OF TRANSPORTATION TO WORK!!Walked' : 'Percent_Walked'}, inplace=True)
transportation.rename(columns = {'Estimate!!Total!!Workers 16 years and over!!MEANS OF TRANSPORTATION TO WORK!!Worked at home' :'Percent_Remote_Work'}, inplace=True)
transportation.rename(columns = {'Estimate!!Total!!Workers 16 years and over who did not work at home!!TRAVEL TIME TO WORK!!Mean travel time to work (minutes)': 'Mean_Commute_Time'}, inplace=True)
transportation_percents = transportation[['Percent_Private_Vehicle', 'Percent_Public_Trans', 'Percent_Walked', 'Percent_Remote_Work', 'Mean_Commute_Time']]
transportation_percents = transportation_percents.replace({'-': np.nan})
transportation_percents = transportation_percents.replace({'N': np.nan})
for i in transportation_percents.columns:
    try:
        transportation_percents[i] = transportation_percents[i].astype(float)
    except:
        continue

# Clean financial characteristics dataframe
financial_char['zip'] = financial_char['Geographic Area Name'].str[-5:] # Add zip code column
financial_char = financial_char[financial_char.columns.drop(list(financial_char.filter(regex='^Margin')))] # Delete margin of error column
financial_char.drop('id', axis=1, inplace=True) # Drop id column
financial_char.drop('Geographic Area Name', axis=1, inplace=True) # Drop Geo Area Name column
financial_char = financial_char.loc[:, ~(financial_char == '(X)').any()] # Drop columns with any (X)
financial_char.set_index('zip', inplace=True) # Set zip as index
financial_char['Estimate!!Percent owner-occupied housing units!!Occupied housing units'] = financial_char['Estimate!!Owner-occupied housing units!!Occupied housing units'] / financial_char['Estimate!!Occupied housing units!!Occupied housing units']
financial_char['Estimate!!Percent renter-occupied housing units!!Occupied housing units'] = 1 - financial_char['Estimate!!Percent owner-occupied housing units!!Occupied housing units']
financial_char_percents = financial_char.filter(regex='Percent') # Keep percentage columns
financial_char_percents = financial_char_percents.replace({'-': np.nan})
for i in financial_char_percents.columns:
    try:
        financial_char_percents[i] = financial_char_percents[i].astype(float)
    except:
        continue
financial_char.rename(columns = {'Estimate!!Percent owner-occupied housing units!!Occupied housing units': 'Percent_Owner_Occupied'}, inplace=True)
financial_char.rename(columns = {'Estimate!!Percent occupied housing units!!Occupied housing units!!HOUSEHOLD INCOME IN THE PAST 12 MONTHS (IN 2018 INFLATION-ADJUSTED DOLLARS)!!Median household income (dollars)' : 'Median_HH_Income'}, inplace=True)
financial_char.rename(columns = {'Estimate!!Percent owner-occupied housing units!!Occupied housing units!!HOUSEHOLD INCOME IN THE PAST 12 MONTHS (IN 2018 INFLATION-ADJUSTED DOLLARS)!!Median household income (dollars)' : 'Median_Owner_HH_Income'}, inplace=True)
financial_char.rename(columns = { 'Estimate!!Percent renter-occupied housing units!!Occupied housing units!!HOUSEHOLD INCOME IN THE PAST 12 MONTHS (IN 2018 INFLATION-ADJUSTED DOLLARS)!!Median household income (dollars)' : 'Median_Renter_HH_Income'}, inplace=True)
financial_percents = financial_char[['Percent_Owner_Occupied', 'Median_HH_Income', 'Median_Owner_HH_Income', 'Median_Renter_HH_Income']]
financial_percents['Percent_Owner_Occupied'] = financial_percents['Percent_Owner_Occupied']*100


# Clean education dataframe
education['zip'] = education['Geographic Area Name'].str[-5:] # Add zip code column
education = education[education.columns.drop(list(education.filter(regex='^Margin')))] # Delete margin of error column
education.drop('id', axis=1, inplace=True) # Drop id column
education.drop('Geographic Area Name', axis=1, inplace=True) # Drop Geo Area Name column
education = education.loc[:, ~(education == '(X)').any()] # Drop columns with any (X)
education.set_index('zip', inplace=True) # Set zip as index
education_percents = education.filter(regex='Percent') # Keep percentage columns
education_percents = education_percents.replace({'-': np.nan})
for i in education_percents.columns:
    try:
        education_percents[i] = education_percents[i].astype(float)
    except:
        continue
education_percents = education_percents[["Estimate!!Percent!!Population 25 years and over!!Bachelor's degree", 
                                         "Estimate!!Percent!!Population 25 years and over!!Graduate or professional degree", 
                                         "Estimate!!Percent!!Population 25 years and over!!High school graduate or higher", 
                                         "Estimate!!Percent!!Population 25 years and over!!Some college, no degree", 
                                         "Estimate!!Percent Male!!Population 25 years and over!!Bachelor's degree", 
                                         "Estimate!!Percent Female!!Population 25 years and over!!Bachelor's degree", 
                                         "Estimate!!Percent Male!!Population 25 years and over!!Graduate or professional degree", 
                                         "Estimate!!Percent Female!!Population 25 years and over!!Graduate or professional degree", 
                                         "Estimate!!Percent Male!!Population 25 years and over!!High school graduate or higher", 
                                         "Estimate!!Percent Female!!Population 25 years and over!!High school graduate or higher"]]


# Clean employment dataframe
employment['zip'] = employment['Geographic Area Name'].str[-5:] # Add zip code column
employment = employment[employment.columns.drop(list(employment.filter(regex='^Margin')))] # Drop margin of error columns
employment.drop('id', axis=1, inplace=True)
employment.drop('Geographic Area Name', axis=1, inplace=True)
employment = employment.loc[:, ~(employment == '(X)').any()]
employment.set_index('zip', inplace=True) # Set zip as index
employment_percents = employment.filter(regex='Percent') # Keep percentage columns
employment_percents = employment_percents.replace({'-': np.nan})
for i in employment_percents.columns:
    try:
        employment_percents[i] = employment_percents[i].astype(float)
    except:
        continue
employment_percents.rename(columns={'Estimate!!Percent Families with own children under 18 years!!Families' : 'Percent_Families_With_Children'}, inplace=True)
employment_percents['Percent_Families_With_Children'] = employment_percents['Percent_Families_With_Children']/employment_percents['Estimate!!Percent!!Families']*100
employment_percents = employment_percents[['Percent_Families_With_Children','Estimate!!Percent!!Families!!EMPLOYMENT STATUS CHARACTERISTICS!!Married-couple families!!Husband in labor force, wife not in labor force', 
'Estimate!!Percent Families with own children under 18 years!!Families!!EMPLOYMENT STATUS CHARACTERISTICS!!Married-couple families!!Husband in labor force, wife not in labor force', 
'Estimate!!Percent!!Families!!EMPLOYMENT STATUS CHARACTERISTICS!!Married-couple families!!Wife in labor force, husband not in labor force', 
'Estimate!!Percent Families with own children under 18 years!!Families!!EMPLOYMENT STATUS CHARACTERISTICS!!Married-couple families!!Wife in labor force, husband not in labor force', 
'Estimate!!Percent!!Families!!EMPLOYMENT STATUS CHARACTERISTICS!!Married-couple families!!Both husband and wife not in labor force',
'Estimate!!Percent Families with own children under 18 years!!Families!!EMPLOYMENT STATUS CHARACTERISTICS!!Married-couple families!!Both husband and wife not in labor force',
'Estimate!!Percent!!Families!!EMPLOYMENT STATUS CHARACTERISTICS!!Other families', 'Estimate!!Percent Families with own children under 18 years!!Families!!EMPLOYMENT STATUS CHARACTERISTICS!!Other families',
'Estimate!!Percent!!Families!!EMPLOYMENT STATUS CHARACTERISTICS!!Other families!!Female householder, no husband present', 
'Estimate!!Percent Families with own children under 18 years!!Families!!EMPLOYMENT STATUS CHARACTERISTICS!!Other families!!Female householder, no husband present',
'Estimate!!Percent!!Families!!EMPLOYMENT STATUS CHARACTERISTICS!!Other families!!Female householder, no husband present!!In labor force', 
'Estimate!!Percent Families with own children under 18 years!!Families!!EMPLOYMENT STATUS CHARACTERISTICS!!Other families!!Female householder, no husband present!!In labor force', 
'Estimate!!Percent!!Families!!EMPLOYMENT STATUS CHARACTERISTICS!!Other families!!Male householder, no wife present',  
'Estimate!!Percent Families with own children under 18 years!!Families!!EMPLOYMENT STATUS CHARACTERISTICS!!Other families!!Male householder, no wife present', 
'Estimate!!Percent!!Families!!EMPLOYMENT STATUS CHARACTERISTICS!!Other families!!Male householder, no wife present!!In labor force', 
'Estimate!!Percent Families with own children under 18 years!!Families!!EMPLOYMENT STATUS CHARACTERISTICS!!Other families!!Male householder, no wife present!!In labor force', 
'Estimate!!Percent!!Families!!EMPLOYMENT STATUS CHARACTERISTICS!!Other families!!Male householder, no wife present!!Not in labor force', 
'Estimate!!Percent!!WORK STATUS CHARACTERISTICS!!Families!!1 worker in the past 12 months', 
'Estimate!!Percent!!WORK STATUS CHARACTERISTICS!!Families!!2 or more workers in the past 12 months',
'Estimate!!Percent Families with own children under 18 years!!WORK STATUS CHARACTERISTICS!!Families!!No workers in the past 12 months', 
'Estimate!!Percent Families with own children under 18 years!!WORK STATUS CHARACTERISTICS!!Families!!1 worker in the past 12 months', 
'Estimate!!Percent!!WORK STATUS CHARACTERISTICS!!Families!!No workers in the past 12 months']]


# Clean marital status dataframe
marital['zip'] = marital['Geographic Area Name'].str[-5:] # Add zip code column
marital = marital[marital.columns.drop(list(marital.filter(regex='^Margin')))] # Drop margin of error columns
marital.drop('id', axis=1, inplace=True) # Drop id column
marital.drop('Geographic Area Name', axis=1, inplace=True) # Drop Geo Area Name column
marital.drop('Estimate!!Now married (except separated)!!PERCENT ALLOCATED!!Marital status', axis=1, inplace=True)
marital.drop('Estimate!!Widowed!!PERCENT ALLOCATED!!Marital status', axis=1, inplace=True)
marital.drop('Estimate!!Divorced!!PERCENT ALLOCATED!!Marital status', axis=1, inplace=True)
marital.drop('Estimate!!Separated!!PERCENT ALLOCATED!!Marital status', axis=1, inplace=True)
marital.drop('Estimate!!Never married!!PERCENT ALLOCATED!!Marital status', axis=1, inplace=True)
#marital = marital.loc[:, ~(marital == '(X)').any()] # Drop columns with any (X)
marital.set_index('zip', inplace=True) # Set zip as index
marital_percents = marital.iloc[:, 1:6] # Keep percentage columns
marital_percents = marital_percents.replace({'-': np.nan})
for i in marital_percents.columns:
    try:
        marital_percents[i] = marital_percents[i].astype(float)
    except:
        continue

# Clean language dataframe
language['zip'] = language['Geographic Area Name'].str[-5:] # Add zip code column
language = language[language.columns.drop(list(language.filter(regex='^Margin')))] # Drop margin of error column
language.drop('Estimate!!Percent!!Population 5 years and over', axis=1, inplace=True) # Drop column with no data
language.drop('id', axis=1, inplace=True) # Drop id column
language.drop('Geographic Area Name', axis=1, inplace=True) # Drop Geo Area Name column
language = language.loc[:, ~(language == '(X)').any()] # Drop columns with any (X)
language.set_index('zip', inplace=True) # Set zip as index
language_percents = language.filter(regex='Percent') # Keep percentage columns
language_percents.rename(columns = {'Estimate!!Percent!!Population 5 years and over!!All citizens 18 years old and over!!Speak a language other than English!!Spanish' : "Speaks_Spanish"}, inplace=True)
language_percents.rename(columns = {'Estimate!!Percent!!Population 5 years and over!!Speak only English' : "Speak_Only_English"}, inplace=True)
language_percents.rename(columns = {'Estimate!!Percent!!Population 5 years and over!!Speak a language other than English' : "Speaks_Other_Language"}, inplace=True)
language_percents.rename(columns = {'Estimate!!Percent of specified language speakers!!Percent speak English less than very well"!!Population 5 years and over"' : "Poor_English_Speaking"}, inplace=True)
language_percents = language_percents[['Speaks_Spanish', 'Speaks_Other_Language', 'Speak_Only_English', 'Poor_English_Speaking']]
language_percents = language_percents.replace({'-': np.nan})
for i in language_percents.columns:
    try:
        language_percents[i] = language_percents[i].astype(float)
    except:
        continue

# Create final dataframe
final = pd.concat([data_percents, education_percents, employment_percents, language_percents, veteran_percents, transportation_percents, financial_percents, marital_percents, real_estate_2019, density, housing_char_percents, dem_char_percents], axis=1)

# Fix the remaining object datatypes in the final. Cut down zip codes less than 2000
final['Mean_Commute_Time'] = final['Mean_Commute_Time'].astype(float)
final['Median_HH_Income'] = final['Median_HH_Income'].replace({'-': np.nan})
final['Median_HH_Income'] = final['Median_HH_Income'].replace({'2,500-': 2500.0})
final['Median_HH_Income'] = final['Median_HH_Income'].replace({'250,000+': 250000.0})
final['Median_HH_Income'] = final['Median_HH_Income'].astype(float)
final['Median_Owner_HH_Income'] = final['Median_Owner_HH_Income'].replace({'-': np.nan})
final['Median_Owner_HH_Income'] = final['Median_Owner_HH_Income'].replace({'2,500-': 2500.0})
final['Median_Owner_HH_Income'] = final['Median_Owner_HH_Income'].replace({'250,000+': 250000.0})
final['Median_Owner_HH_Income'] = final['Median_Owner_HH_Income'].astype(float)
final['HPI_%_Annual_Change'] = final['HPI_%_Annual_Change'].replace({'.': np.nan})
final['HPI_%_Annual_Change'] = final['HPI_%_Annual_Change'].astype(float)
final['Median_Renter_HH_Income'] = final['Median_Renter_HH_Income'].replace({'-': np.nan})
final['Median_Renter_HH_Income'] = final['Median_Renter_HH_Income'].replace({'2,500-': 2500.0})
final['Median_Renter_HH_Income'] = final['Median_Renter_HH_Income'].replace({'250,000+': 250000.0})
final['Median_Renter_HH_Income'] = final['Median_Renter_HH_Income'].astype(float)
final['HPI'] = final['HPI'].replace({'.': np.nan})
final['HPI'] = final['HPI'].astype(float)

final = final[final['total_pop'] >= 2000] # Drop zip codes with fewer than 2000 people

final.dropna(axis=0, how='any', inplace=True) # Drop NaNs

# Save to csv
final.to_csv('data/final.csv', index=False)