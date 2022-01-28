#Write the necessary code to display the total population count for the next 3 years (without a leap year).

#Here are the specifications:

#In the country we want to investigate:

#The current population is 380,123,456
# One person is born every 6 seconds
# One person dies every 12 seconds
# One person immigrates every 40 seconds

#The initial population
p0=380123456
#lenght of time to calculate in years
tf=3
#define modifications of people, deaths, births
de=12 #meaning every 12 seconds there is 1 death
bo=6  #meaning every 6 seconds there is 1 birth
inmi=40 #meaning every 40 seconds there is 1 inmigration

sec=365*24*60*60 #in 1 year..
tfs=tf*sec    #seconds in the amount of years in study
Q1=tfs/bo # Amount of people increased by births in 3 years
Q2=tfs/inmi # Amount of people increased by inmigration in 3 years
Q3=tfs/de # Amount of people taken away by deaths in 3 years

pf=p0+Q1+Q2-Q3 #we can say there is 3 quotas, the people given by
#births, the people given by inmigration and the ones taken away by deaths. 
print(pf)
print("In",tf,"years, the growth of population will be",int(pf))