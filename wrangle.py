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
        p.calculatedfinishedsquarefeet, p.taxvaluedollarcnt, 
        p.yearbuilt, p.taxamount, p.fips
        FROM properties_2017 AS p
        WHERE p.propertylandusetypeid IN (261)
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
    filename = 'zillow.csv'
    
    if os.path.isfile(filename): 
        df = pd.read_csv(filename)
        return df
    else:
        df = new_zillow_data()

        df.to_csv(filename)
    return df
    