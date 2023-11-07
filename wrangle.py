## IMPORTS ##

import pandas as pd
import numpy as np
from env import user, password, host
import os
directory = os.getcwd()
from sklearn.model_selection import train_test_split


## FUNCTIONS ##
##-------------------------------------------------------------------##
def get_db_url(database_name):
    """
    this function will:
    - take in a string database_name 
    - return a string connection url to be used with sqlalchemy later.
    """
    return f'mysql+pymysql://{user}:{password}@{host}/{database_name}'

def new_zillow_data():
    """
    This function will:
    - take in a SQL_query
    - create a connection_url to mySQL
    - return a df of the given query from the zillow
    """
    sql_query = """
        SELECT p.id, p.bedroomcnt, p.bathroomcnt,
        p.calculatedfinishedsquarefeet, 
        p.structuretaxvaluedollarcnt,
        p.landtaxvaluedollarcnt,
        p.taxvaluedollarcnt, p.yearbuilt,
        p.taxamount, p.fips
        FROM properties_2017 AS p
        WHERE p.propertylandusetypeid IN (261)
        AND p.yearbuilt < 2017
        AND p.assessmentyear = 2016
        ;
        """
    
    url = get_db_url('zillow')
    
    df = pd.read_sql(sql_query, url)
    
    return df


def get_zillow_data():
    """
    This function will:
    - Check local directory for csv file
        - return if exists
    - if csv doesn't exist:
        - creates df of sql query
        - writes df to csv
    - outputs zillow df
    """
    filename = 'zillow_2017.csv'
    
    if os.path.isfile(filename): 
        df = pd.read_csv(filename, index_col=0)
        return df
    else:
        df = new_zillow_data()

        df.to_csv(filename)
    return df

def prep_zillow(df):
    '''
    This function takes in a dataframe
    renames the columns and drops nulls values
    Additionally it changes datatypes for appropriate columns
    and renames fips to actual county names.
    Then returns a cleaned dataframe
    '''
    df = df.rename(columns = 
                   {'bedroomcnt':'bedrooms',
                    'bathroomcnt':'bathrooms',
                    'landtaxvaluedollarcnt':'tax_land',
                    'structuretaxvaluedollarcnt':'tax_structure',
                    'calculatedfinishedsquarefeet':'sqft',
                    'taxvaluedollarcnt':'taxvalue',
                    'fips':'county'})
    
    df = df.dropna()
    
    make_ints = ['bedrooms','sqft','taxvalue','yearbuilt']

    for col in make_ints:
        df[col] = df[col].astype(int)
        
    df.county = df.county.map({6037:'LA',6059:'Orange',6111:'Ventura'})
    
    return df


def split_data(df):
    '''
    take in a DataFrame and return train, validate, and test DataFrames.
    return train, validate, test DataFrames.
    '''
    
    # Create train_validate and test datasets
    train, validate_test = train_test_split(df, train_size=0.60, random_state=123)
    
    # Create train and validate datsets
    validate, test = train_test_split(validate_test, test_size=0.5, random_state=123)

    # Take a look at your split datasets

    print(f"""
    train -> {train.shape}
    validate -> {validate.shape}
    test -> {test.shape}""")
    
    return train, validate, test