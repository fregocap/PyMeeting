import pandas as pd
import numpy as np
from pymeetings.utils import *
import pytz
from geopy import geocoders


class GetMeetingHour():
    
    def __init__(self,cities,day):
        """
        Computes the most interesting hours for a particular day, considering 
        that you provide several cities
        
        :param vec cities: the number of cities to consider for the algorithm 
        :param date day  : the date to make the calculation 
        """

        self.cities_vec = cities
        self.day = day
        self.g = geocoders.GoogleV3()

        
    def BestHour(self):
        pass


    def Countries(self):
        """
        Function that computes the different countries where the cities are in
        """
        countries = []
        for city in self.cities_vec:
            if citycheck(city):
                ctry = country(city)
                countries.append(ctry)
            else:
                print('The city %s does not exist' %s)
                countries.append(None)
        return countries

    
    def TimeZones(self):
        """
        Function that computes the different timezones and provides a vector
        """
        
        timezones = []
        for city in self.cities_vec:
            if citycheck(city):
                place, (lat, lng) = self.g.geocode(city)
                timezone = self.g.timezone((lat, lng))
                timezones.append(timezone)
            else:
                print('The city %s does not exist' %city)
                timezones.append(None)

        return timezones
        
        
        
