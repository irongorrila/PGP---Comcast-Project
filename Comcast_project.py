import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Setting style for uniform formatting across project
sns.set_style("whitegrid")
sns.set_context("paper")
sns.set_palette("PuBuGn_d")

##########################################################################

"""
Data Dictionary

Ticket #: Ticket number assigned to each complaint
Customer Complaint: Description of complaint
Date: Date of complaint
Time: Time of complaint
Received Via: Mode of communication of the complaint
City: Customer city
State: Customer state
Zipcode: Customer zip
Status: Status of complaint
Filing on behalf of someone
Analysis Task

Task 3:
Which state has the maximum complaints
Which state has the highest percentage of unresolved complaints
- Provide the percentage of complaints resolved till date, which were received through the Internet and customer care calls.

The analysis results to be provided with insights wherever applicable.

"""
#############################################################################
""" Task 1a: Import Data ito python environment """

df= pd.read_csv('Comcast_telecom_complaints_data.csv', parse_dates= True)
df= df.sort_values('Date')
df['Date']= pd.to_datetime(df['Date'])

df['month']= df['Date'].dt.month
############################################################################
"""
Task 1b. Provide the trend chart for the number of complaints at monthly 
         and daily granularity levels.
"""
# Complaints Trend by Month

sns.countplot(x= 'month', data= df)
plt.xlabel('Months')
plt.ylabel('Volume')
sns.set_title(" Complaints by month")
plt.show()
plt.clf()

# By Date
fig, ax=subplots()
ax=sns.countplot(x= 'Date', data= df)
plt.xlabel("Date")
plt.ylabel("Volume")
plt.title()
plt.xticks(rotation=90) # too many tick labels cannot fit in graph
plt.show()
#########################################################################
"""Task 1c. Provide a table with the frequency of complaint types
"""

complaints_tbl = pd.DataFrame(df['Customer Complaint'].value_counts()); complaints_tbl

########################################################################
"""
Task 2:
a. Which complaint types are maximum i.e., around internet, network issues, or across any 
   other domains.

b. Create a new categorical variable with value as Open and Closed. 
   Open & Pending is to be categorized as Open and Closed & Solved is to be categorized 
   as Closed.

c. Provide state wise status of complaints in a stacked bar chart. Use the categorized 
   variable from Q3. Provide insights on:

"""
# Task 2a:

top_complaints= complaints_tbl['Customer Complaint'].sort_values(ascending= False)
top_complaints[0:10]

#######################################################

# Task 2b:
a= ['Open', 'Pending']
df['Status_revised'] = []

x= df['Status'].isin(a)

for i in range(len(x)):
    if x[i] == True:
        df['Status_revised'][i] = 'Open'
    else:
        df['Status_revised'][i] = 'Closed'


   

