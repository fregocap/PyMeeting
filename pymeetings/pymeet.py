import pandas as pd
import numpy as np
from pymeetings.utils import *
import pytz
from geopy import geocoders
from datetime import datetime


class GetMeetingHour():
    
    def __init__(self,cities,day):
        """
        Computes the most interesting hours for a particular day, considering 
        that you provide several cities
        
        :param vec cities: the number of cities to consider for the algorithm 
        :param str day  : the date to make the calculation in the format: 2020/02/20 
        """

        self.cities_vec = cities
        self.day = day
        self.g = geocoders.GoogleV3()


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


    def TimeZone(self, city):
        """
        Function that computes the timezone for a particular city
        """
        if citycheck(city):
            place, (lat, lng) = self.g.geocode(city)
            timezone = self.g.timezone((lat, lng))
            return timezone
        else:
            print('The city %s does not exist' %city)
            return 'The city %s does not exist' %city
            

    
    def TimeZones(self):
        """
        Function that computes the different timezones for each city 
        """
        
        timezones = []
        for city in self.cities_vec:
                timezones.append(self.TimeZone(city))
                
        return timezones


    def CityTimes(self, city):
        """
        Function that given the cities provides the times
        """
        hour_vec = self.__Hours()
        city_tz = pytz
        for 
    

    def __checkdate(self,date):
        """
        Function that checks that the date string is in the right format
        """
        
    
    def __Hours(self):
        """
        Function that calculates the vector of times for a particular day
        """
        
        hours = []

        if self.__checkdate(self.day):
            for j in range(0, 24):
                if j<10:
                    hours.append(self.day+' '+'0'+str(j)+':00')
                else:
                    hours.append(self.day+' '+str(j)+':00')

        return hours

                    
    def BestHour(self):
        """
        Function that computes the best hour for the meeting, the `feel lucky` guess
        """
        pass
    
    
    def ConstructTable(self):
        """
        Function that provides the table of interest 
        """
        dic_pd = {}
        dic_pd['Hour'] = self.__Hours()
        for city in self.cities_vec:
            dic_pd[city] = self.CityTimes(city)
            
        
        main_table = pd.DataFrame(dic_pd)


        return main_table
        

