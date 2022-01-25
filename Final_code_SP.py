#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
# importing code from environment.
# setting column names from problem description
col_names=['stationID','bikeID','ArrTime','DepTime']
bikedata = pd.read_csv('data.csv', names=col_names, header=None)


# In[2]:


bikedata


# In[3]:


# Class that takes data frame from CSV loaded 
# methods 
class Reporting_Period():
    def __init__(self,df):
        self.df=df #  data passed to class as Dataframe loaded through CSV file
        self.sort_df=[] 
        self.time_count=[]
        
        # this function dont take any input but apply date time format to Arrivala and departure Time.
        # just saves values to class parameter self.df
        
    def format_converter_to_date(self):
        cols = self.df.columns[2:4]
        self.df[cols] = bikedata[cols].apply(pd.to_datetime, errors='coerce')
        return self.df
        
        # this function takes bike id and calculates average journey of bike between stations using arrival and departure time.
        # function returns average time delta to calling function
        
    def calculate_individual_bike_journey(self,bikeid):
                single=bikedata[bikedata["bikeID"]==bikeid]
                self.sort_df=[]
                self.sort_df=single.sort_values(by=['DepTime'])
                self.time_count=[]
                count=0
                for i in range(len(self.sort_df)-1) :
                        if(count<=len(self.sort_df)-1):
                            self.time_count.append(self.sort_df.iloc[i+1,2]-self.sort_df.iloc[i,3])
                            count=count+1
                return pd.to_timedelta(pd.Series(self.time_count)).mean()
            
    # this function prints the format of the output requested 'HH:MM:SS'
    
    def calculate_Journy_Time(self,time_data):
        hours, remainder = divmod(time_data.seconds, 3600)
        minutes, seconds = divmod(remainder, 60)
        print('{:02}:{:02}:{:02}'.format(int(hours), int(minutes), int(seconds)))
        return ('{:02}:{:02}:{:02}'.format(int(hours), int(minutes), int(seconds)))
    
    # this function loads class paramater df and class format_converter_to_date to assign data types to columns 
    # Also calls all bikes avrage mean time function called calculate_individual_bike_journey
    # returns all bikes avrage journy time across satitions
        
    def individual_bike_sort(self):
        self.format_converter_to_date()
        bike_list=self.df['bikeID'].unique()
        avrg_data=[]
        for i in bike_list:
            time=self.calculate_individual_bike_journey(i)
            avrg_data.append(time)
        return pd.to_timedelta(pd.Series(avrg_data)).mean()
            
        


# In[4]:


new_df=Reporting_Period(bikedata)


# In[5]:


time_data=new_df.individual_bike_sort()


# In[6]:


time_data # printing all bikes avrage across all stations


# In[7]:


new_df.calculate_Journy_Time(time_data) #calling to print data in 'hh:mm:ss' format


# In[ ]:





# In[ ]:




