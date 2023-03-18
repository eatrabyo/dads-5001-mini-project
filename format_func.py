import pandas as pd

from list_dict import rename_th_expend,rename_country_dict,rename_th_stay_expend

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

def format_th_stay_expend(df):
    stay = df.copy()
    stay.rename(columns=rename_th_stay_expend,inplace=True)
    stay['Country'] = stay['Country'].str.strip()
    stay.drop(index=[61,62],inplace=True)
    return stay

def format_th_stay_expend_2020(df):
    stay = df.copy()
    stay['Country'] = stay['Country'].str.strip()
    stay['Country'] = stay['Country'].str.split().str.join(' ')
    stay = stay.iloc[:370]
    stay['Country'] = stay['Country'].ffill()
    stay.dropna(subset=['Item'],axis=0,inplace=True)
    stay.rename(columns={'Country':'Nationality',2020:'Values'},inplace=True)
    stay= stay.loc[~stay['Nationality'].isin(['Others','Total'])]
    return stay