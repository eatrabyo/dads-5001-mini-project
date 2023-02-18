import pandas as pd

from list_dict import rename_th_expend,rename_country_dict

def format_th_arrival(df):
    arrival = df.copy()

    arrival['Nationality'] =  arrival['Nationality'].str.strip()

    # slice out headers
    arrival = arrival.iloc[:61,:3]

    # slice out Others data
    arrival = arrival.loc[~arrival['Nationality'].isin(['Others'])]
    
    arrival.replace({'Nationality':rename_country_dict},inplace=True)
    return arrival

def format_th_expend(df):
    expend = df.copy()

    expend['Country'] = expend['Country'].str.strip()

    expend.drop(index=[0,62],inplace=True)

    # rename column
    expend.rename(columns=rename_th_expend,inplace=True)
    return expend
