#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Project: The Python project to analyse recent COVID-19 nationally
and internationally

@author: Prithwiraj Sarkar
Updated on: 24/6/2020

sources: World Health Organization
John Hopkins international survey
National COVID-19 data

"""
#Importing Modules
import matplotlib
import numpy as np
from matplotlib import dates as mdate
import pandas as pd
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation

Writer=matplotlib.animation.writers['ffmpeg']
writer = Writer(fps=1,metadata=dict(artist='Me'),bitrate=1800)

choice=0
world_data=pd.read_csv("owid-covid-data.csv")
regional=pd.read_csv("district_wise.csv")
world_sum=pd.read_csv("sum_up_data.csv")

# Giving option to the user:
print("Which Data to be exposed? ")
print("================================")
print("1.Know Your Country Condition !!")
print("2.Regional")
print("3.World Comparison of COVID-19")
print("4.Geographical Analysis")

choice=int(input("Choose one option !! ( 0 to exit):  ")) #user input
while choice!=0:
    if choice ==1:
        ctr=input("Enter the Name of your country: ")
        country=world_data[world_data.location == ctr.title()]
        
        m = country.groupby(['date'])['total_cases','total_deaths'].max()
        n = country.groupby(['date'])['stringency_index'].max()
        k = country.groupby(['date'])['total_cases','total_tests','new_tests_smoothed'].max()
        
        
        m.plot(kind='line')
        plt.xlabel('Dates')
        plt.ylabel('Population')
        plt.locator_params(axis='x',nbins=12)
        plt.locator_params(axis='y',nbins=10)
        plt.title("Cases and Deaths  vs  Times")
        plt.show()
        
        n.plot(kind="line")
        plt.xlabel('Dates')
        plt.ylabel('stringency_index')
        plt.locator_params(nbins=10)
        plt.title("Efficiency and Strictness of Lock Down")
        plt.show()
        
        k.plot(kind='line')
        plt.locator_params(nbins=12)
        plt.xlabel("Dates")
        plt.ylabel("Population")
        plt.title("Comparison between cases, deaths & recovery")
        plt.show()
        
        
        print()
        print("Other information:")
        print("__________________________________")
        pop =np.array(country.population)
        hand=np.array(country.handwashing_facilities)
        hos=np.array(country.hospital_beds_per_thousand)
        male=np.array(country.male_smokers)
        female=np.array(country.female_smokers)
        dia=np.array(country.diabetes_prevalence)
        gdp=np.array(country.gdp_per_capita)
        old=np.array(country.aged_70_older)
        med_age=np.array(country.median_age)
        
        print("Population: ",int(np.mean(pop)))
        print("Median age: ",int(np.mean(med_age)))
        print("percentage of above 70+ Older people: ",int(np.mean(old)))
        print("GDP per capita: ",int(np.mean(gdp)))
        print("Diabetes prevalence: ", np.mean(dia))
        print("Hospital beds per thousand: ",int(np.mean(hos)))
        print("Male smokers percentages: ",int(np.mean(male)))
        print("Female smokers percentages: ",int(np.mean(female)))
        
        break
     
    elif choice == 2:
        regional=pd.read_csv("district_wise.csv")
        st=input("Enter your state name: ")
        state=regional[regional.State == st.title()]
        
        x = state.groupby(['District'])['Active','Recovered','Confirmed'].max()
        x.plot(kind='bar')
        plt.xlabel('Districts')
        plt.ylabel('Population')
        plt.title("States District wise Active cases")
        plt.show()
        break
    elif choice == 3:
        
        
        cases=pd.read_csv("total_cases.csv")
        most_affected = world_sum.nlargest(15, ['Sum_of_total_cases'])
        low_affected = world_sum.nsmallest(10,['Sum_of_total_cases'])
        
        
        a = low_affected.groupby(['countries'])['Sum_of_total_cases'].max()
        print("Safe countries in the world right now: ")
        print("----------------------------------------")
        print(a)
        
        
        
        cases['Dates']=pd.to_datetime(cases['Dates'], format = '%m-%d-%Y')

        
        cdate=cases['Dates']
        india=cases['India']
        china=cases['China']
        US=cases['US']
        italy=cases['Italy']
        spain=cases['Spain']
        uk=cases['United Kingdom']
        rus=cases['Russia']
        ger=cases['Germany']
        jap=cases['Japan']



        fig1 = plt.figure()
        ax1 = fig1.add_subplot(111)

        def animate1(i):
            ax1.clear()
    
    
            ax1.plot(cdate[:i],india[:i],label='India Total cases')
            ax1.plot(cdate[:i],china[:i],label='China Total cases')
            ax1.plot(cdate[:i],US[:i],label='USA Total cases')
            ax1.plot(cdate[:i],italy[:i],label='Italy Total cases')
            ax1.plot(cdate[:i],spain[:i],label='Spain Total cases')
            ax1.plot(cdate[:i],uk[:i],label='UK Total cases')
            ax1.plot(cdate[:i],ger[:i],label='germany Total cases')
            ax1.plot(cdate[:i],rus[:i],label='Russia Total cases')
            ax1.plot(cdate[:i],jap[:i],label='Japan Total cases')

            plt.xlabel("Dates")
            plt.ylabel("Population")
            plt.title("Total Cases")
            ax1.legend(loc='upper left')
            ax1.set_xlim([cdate.iloc[0],
    			  cdate.iloc[-1]])
            ax1.set_ylim([min(india.iloc[0],china.iloc[0],US.iloc[0],italy.iloc[0],spain.iloc[0],uk.iloc[0],ger.iloc[0],rus.iloc[0],jap.iloc[0]),
                  max(india.iloc[-1],china.iloc[-1],italy.iloc[-1],spain.iloc[-1],uk.iloc[-1],ger.iloc[-1],rus.iloc[-1],jap.iloc[-1])])
            ax1.xaxis.set_major_locator(mdate.DayLocator(interval=10))
            ax1.xaxis.set_major_formatter(mdate.DateFormatter('%d-%m-%Y'))
            
        ani = FuncAnimation(fig1, animate1, interval=1)
        
        #ani.save('cases.mp4', writer=writer)
  
        plt.show()
        
        
        
        recovery=pd.read_csv("recovery_rate.csv")
        recovery['Date']=pd.to_datetime(recovery['Date'], format = '%m-%d-%Y')
        
        cdate1=recovery['Date']
        india1=recovery['India']
        china1=recovery['China']
        US1=recovery['US']
        italy1=recovery['Italy']
        spain1=recovery['Spain']
        uk1=recovery['United Kingdom']
        rus1=recovery['Russia']
        ger1=recovery['Germany']
        jap1=recovery['Japan']

        
        fig2 = plt.figure()
        ax2 = fig2.add_subplot(111)

        def animate2(i):
            ax2.clear()
    
    
            ax2.plot(cdate1[:i],india1[:i],label='Indian Recovery')
            ax2.plot(cdate1[:i],china1[:i],label='China Recovery')
            ax2.plot(cdate1[:i],US1[:i],label='USA Recovery')
            ax2.plot(cdate1[:i],italy1[:i],label='Italy Recovery')
            ax2.plot(cdate1[:i],spain1[:i],label='Spain Recovery')
            ax2.plot(cdate1[:i],uk1[:i],label='UK Recovery')
            ax2.plot(cdate1[:i],ger1[:i],label='germany Recovery')
            ax2.plot(cdate1[:i],rus1[:i],label='Russia Recovery')
            ax2.plot(cdate1[:i],jap1[:i],label='Japan Recovery')

            plt.xlabel("Dates")
            plt.ylabel("Population")
            plt.title("Total Recovery")
            
    
            ax2.legend(loc='upper left')
            ax2.set_xlim([cdate1.iloc[0],
    			  cdate1.iloc[-1]])
            ax2.set_ylim([min(india1.iloc[0],china1.iloc[0],US1.iloc[0],italy1.iloc[0],spain1.iloc[0],uk1.iloc[0],ger1.iloc[0],rus1.iloc[0],jap1.iloc[0]),
                  max(india1.iloc[-1],china1.iloc[-1],italy1.iloc[-1],spain1.iloc[-1],uk1.iloc[-1],ger1.iloc[-1],rus1.iloc[-1],jap1.iloc[-1])])
            ax2.xaxis.set_major_locator(mdate.DayLocator(interval=15))
            ax2.xaxis.set_major_formatter(mdate.DateFormatter('%d-%m-%Y'))
    
        ani1 = FuncAnimation(fig2, animate2, interval=1)
        #ani1.save('recovery.mp4', writer=writer)
         
        plt.show()
        
        
        
        fig3=plt.figure(figsize=(10,7))
        plt.title("Most affected countries in the world")
        plt.pie(most_affected.Sum_of_total_cases, labels=most_affected.countries)
        plt.show()
        break
        








