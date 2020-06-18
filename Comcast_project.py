import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

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
plt.title(" Complaints by month")
plt.show()


# By Date
fig, ax=subplots()
ax=sns.countplot(x= 'Date', data= df)
plt.xlabel("Date")
plt.ylabel("Volume")
plt.title("Complaints Volume by Date")
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
   
Which state has the maximum complaints
Which state has the highest percentage of unresolved complaints
- Provide the percentage of complaints resolved till date, which were received through the Internet and customer care calls.


"""
# Task 2a:

top_complaints= complaints_tbl['Customer Complaint'].sort_values(ascending= False)
top_complaints[0:10]

#######################################################

# Task 2b: Create a new categorical variable with 'Open' & 'Closed' as the statuses

df['new_status'] = np.nan

for i in range(len(df)):
   if ((df['Status'][i] == 'Open') or (df['Status'][i] == "Pending")):
      df['new_status'][i] = "Open"
   else:
      df['new_status'][i] = "Closed"


# Task 2c:

df_sub= df[['State', 'new_status']]; df_sub.head()
state_wise= pd.DataFrame(df_sub.groupby(['State', 'new_status']).agg(np.size))
state_wise.unstack().plot(kind= 'bar', stacked= True, label= ['Open', 'Closed'])
plt.title("State-wise Status of Cases")
plt.legend()
plt.show()

sw_un= state_wise.head().unstack()
closed_cases= np.array(sw_un[0, 'Closed'])
open_cases= np.array(sw_un[0, 'Open'])
sw_un["Total"] = closed_cases + open_cases

sw_un['perc_unresolved'] = open_cases/sw_un["Total"]
sw_un['perc_resolved'] = closed_cases/sw_un["Total"]

top_unresolved= sw_un.sort_values('perc_unresolved', ascending= False)
top_resolved= sw_un.sort_values('perc_resolved', ascending= False)

# Subsetting cases from Alabama which were received via Customer Care or Internet
df_via= df[(df['Received Via'].isin(['Customer Care Call', 'Internet'])) & (df['State'] == "Alabama")]

df_via['new_status'].value_counts(normalize= True)


