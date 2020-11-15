import pandas as pd



def citycheck(city):
    """
    Function that checks if the city is within the list of cities available
    
    :param str city: the city that we would like to check against
    """
    city = city.lower()
    df_cities = pd.read_csv('world_cities.csv')
    cities_list = df_cities['name'].tolist()
    cities_list = [cit.lower() for cit in cities_list]
    condition = city in cities_list
    return condition


def country(city):
    """
    Function that gets the country where the city is 

    :param str city: the city that we would like to check against
    """
    df = pd.read_csv('world_cities.csv')
    if citycheck(city):
        thecountry = df[df['name'] == city]['country'].tolist()
        return thecountry[0]
    else:
        print('The city is not in our DB')
        
