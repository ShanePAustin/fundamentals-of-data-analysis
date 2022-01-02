#!/usr/bin/env python
# coding: utf-8

# ![image](http://www.cao.ie/images/cao.png)
# 
# # CAO Points Analysis

# * A clear and concise overview of how to load CAO points information from the CAO website into a pandas data frame
# 
# * A detailed comparison of CAO points in 2019, 2020, and 2021 using the functionality in pandas.

# The purpose of this notebook is to describe how to import data from various different formats, clean the data and make it ready to plot and analysis the data.
# 
# The data will be taken from the Irish Central Applications Office (CAO) that processes college applications. It will look at the points requirements of each level 8 course available for the years 2019-2021. http://www.cao.ie/

# ### Libraries

# In[1]:


# Regular expressions
import re

# Package for making HTTP requests
import requests as rq

# Dates and times
import datetime as dt

# Data Frames
import pandas as pd

# For downloading
import urllib.request as urlrq

#Plotting
import matplotlib.pyplot as plt
import seaborn as sns


# ---
# Initially the 2021 data was stored as in and html format and contained only 4 columns, Course code, Course Name the EOS and Mid. The process to import this data is detailed below, however it was not analysed as the data was updated on the website to a csv with more data available.

# ### 2021 html

# Create a file path of where to pull the data from.

# In[2]:


# #Fetch the CAO points URL
# resp = rq.get('http://www2.cao.ie/points/l8.php')
# # Have a look
# resp


# In[3]:


# #Get the current date and time.
# now = dt.datetime.now()

# # Format as a string
# nowstr = now.strftime('%Y%m%d_%H%M%S')


# In[4]:


# #Create a file path for the original data
# pathhtml = 'data/cao2021_' + nowstr + '.html'


# The charset encoding had to be changed to read some of the data as:

# ##### Charset error on server
# 
# Technically, server states decoding as:
#     ```Content-Type: text/html; charset=iso-8859-1
#     ```
# However, one line uses \x96 which isn't defined in iso-8859-1.
# Therefore, we use the similar decoding standard cp1252, which 
# is very similar but includes \x96.

# In[5]:


# #The server uses the wrong encoding, fix it.
# original_encoding = resp.encoding
# #Change to cp1252
# resp.encoding = 'cp1252'


# Save the file to disk

# In[6]:


# #Save the original html file.
# with open(pathhtml, 'w') as f:
#     f.write(resp.text)


# In[7]:


# #Compile the regular expression for matching lines.
# re_course = re.compile(r'([A-Z]{2}[0-9]{3})(.*)')
# #   ([0-9]{3})(\*?) *


# #### Loop through the lines of the response
# 
# To read the data from the html format a csv was created and the code below shows the process of reading the data from the original format to a csv format
# 
# ---

# In[8]:


# # The file path for the csv file.
# path2021 = 'data/cao2021_csv_' + nowstr + '.csv'
    
# #Loop throught the lines of the response content.
# no_lines = 0

# #Open the csv file for writing.
# with open(path2021, 'w') as f:
#     # Write a header row
#     f.write(','.join(['code', 'title','pointsR1','pointsR2']) + '\n')
#     # Loop through lines of the response
#     for line in resp.iter_lines():
#         # Decode the line, using the wrong encoding!
#         dline = line.decode('cp1252')
#         # Match only the lines we want - the ones representing courses.
#         if re_course.fullmatch(dline):
#             #Add one to the lines counter
#             no_lines = no_lines +1          
#             # The course code
#             course_code = dline[:5]
#             # The course title
#             course_title = dline[7:57].strip()
#             # Round one points.
#             course_points = re.split(' +', dline[60:])
#             if len(course_points) != 2:
#                 course_points = course_points[:2]
#              # Join the fields using a comma.
#             linesplit = [course_code, course_title, course_points[0], course_points[1]]
#             # Rejoin the substrings with commas in between
#             f.write(','.join(linesplit)+ '\n')           


# # Print the total number of processed lines.            
# print(f"Total number of lines is {no_lines}.")


# The csv was then read in ad a dataframe for processing

# In[9]:


# df2021 = pd.read_csv(path2021, encoding='cp1252')


# <br>
# 
# ## Save original data set
# 
# Set a time stamp to save a new instance of the data

# In[10]:


#Get the current date and time.
now = dt.datetime.now()

# Format as a string
nowstr = now.strftime('%Y%m%d_%H%M%S')


# ## 2021 Points
# https://www.cao.ie/index.php?page=points&p=2021

# The new form of the data is much simpler as it can be downloaded straight from a csv and imported to a dataframe.

# In[11]:


#2021 csv location
url2021 = 'http://www2.cao.ie/points/CAOPointsCharts2021.xlsx'


# In[12]:


# Create a file path for the original data
pathxlsx = 'data/cao2021_' + nowstr + '.xlsx'


# In[13]:


#Save original file to disk
urlrq.urlretrieve(url2021, pathxlsx)


# Import the csv and take only the Level 8 data to store in a dataframe

# In[14]:


# Download and parse the excel spredsheet
df2021 = pd.read_excel(url2021, skiprows = 11)
# Only include level 8 data 
df2021 = df2021[df2021['Course Level'] == 8]


# In[15]:


# Create a file path for the pandas data
path2021 = 'data/cao2021_' + nowstr + '.csv'


# In[16]:


# Save pandas data frame to disk
df2021.to_csv(path2021, encoding='utf-8')


# Check the data of the first row

# In[17]:


df2021.iloc[0]


# Display the dataframe 

# In[18]:


df2021


# It looks like everything has been imprted successfully and the row count has been confirmed.

# ## 2020 Points
# http://www.cao.ie/index.php?page=points&p=2020

# The 2020 data is also stored in a csv so the process is repeated from the 2020 data link.

# <br>
# 
# #### Save original file

# In[19]:


url2020 = 'http://www2.cao.ie/points/CAOPointsCharts2020.xlsx'


# In[20]:


# Create a file path for the original data
pathxlsx = 'data/cao2020_' + nowstr + '.xlsx'


# In[21]:


#Save original file to disk
urlrq.urlretrieve(url2020, pathxlsx)


# <br>
# 
# #### Load spreadsheet using pandas

# In[22]:


# Download and parse the excel spredsheet
df2020 = pd.read_excel(url2020, skiprows = 10)
# Only include level 8 data
df2020 = df2020[df2020.LEVEL == 8]


# Only level 8 values of 1027rows verified in original csv file

# In[23]:


# Create a file path for the pandas data
path2020 = 'data/cao2020_' + nowstr + '.csv'


# In[24]:


# Save pandas data frame to disk
df2020.to_csv(path2020)


# In[25]:


df2020


# In[26]:


df2021.iloc[241]


# A random row was selected and spot checked for sanity check to see if produced what was expected from the csv.

# <br>
# 
# ## 2019 Points
# http://www.cao.ie/index.php?page=points&p=2019
# 
# The 2019 data was stored as a pdf, so a different import methord was required here with more substantial data cleaning process.

# ##### Steps to reproduce
# 
# 1. Download original pdf file
# 2. Open original pdf file in Microsoft Word.
# 3. Save Microsoft Word's converted PDF in docx format.
# 4. Re-save Word document for editing.
# 5. Delete headers and footers.
# 6. Delete preamble on page 1.
# 7. Select all and copy.
# 8. Paste into Notepad ++.
# 9. Remeove HEI name headings and paste onto each cousre line.
# 10. Delete blank lines.
# 11. Delete tab characters at end of college groups.
# 12. Change all backticks to apostrophes

# After the original data was converted and cleaned with the above steps it could be imported from the new csv file

# In[27]:


#Import and assign to df2019 dataframe
df2019 = pd.read_csv('data/cao2019_20211204_155130_edited.csv', sep = '\t')


# In[28]:


df2019


# <br>
# 
# ## Concat and Join
# ------------

# Now that the data has been imported we can take the columns the we required and join them into one dataframe.

# Here a new dataframe for courses 2019 was created and the columns for Course code, Course title and College were stored.

# In[29]:


#create a new df courses2019
courses2019 = df2019[['Course Code', 'INSTITUTION and COURSE', 'HEI']]
courses2019.columns = ['code', 'title', 'college']
courses2019


# The same was done for 2020, with the same column headers

# In[30]:


courses2020 = df2020[['COURSE CODE2', 'COURSE TITLE', 'HEI']]
courses2020.columns = ['code', 'title','college']
courses2020


# The same was done for 2021, with the same column headers

# In[31]:


courses2021 = df2021[['Course Code', 'Course Title', 'HEI']]
courses2021.columns = ['code', 'title','college']
courses2021


# We can now concatenate the 3 new dataframes into one, the rows counts were checked and can confirm all rows were transfered into the new dataframe.

# In[32]:


#Concat to new allcourses df
allcourses = pd.concat([courses2021, courses2020, courses2019], ignore_index=True)
allcourses


# Sort by course code

# In[33]:


#sort by course code
allcourses.sort_values('code')


# Check for duplicate entries

# In[34]:


#Finds all extra copies of duplicated rows.
allcourses[allcourses.duplicated()]


# Remove all rows with duplicate entries from multiple years

# In[35]:


#Returns a copy of the data frame with all duplicates removed.
allcourses.drop_duplicates()


# Finds all extra copies of duplicated rows.

# In[36]:


#Finds all extra copies of duplicated rows.
allcourses[allcourses.duplicated(subset=['code'])]


# Returns a copy of the data frame with all duplicates removed - based only on code

# In[37]:


#Returns a copy of the data frame with all duplicates removed - based only on code
allcourses.drop_duplicates(subset=['code'], inplace=True, ignore_index=True)


# In[38]:


allcourses


# We are now left with 1232 rows of all course offered over the 3 years 2019-2021 in the dataframe allcourses.

# <br>
# 
# ## Join to the points
# --------

# Now that we have the base of the dataframe we can add the data columns from the original dataframes to the allcourses df. Here we create a new df for 2021 data with the columns for round 1, round 2, EOS and EOS Midpoints.

# In[39]:


df2021_r1 = df2021[['Course Code', 'Course Title', 'R1 Points','R2 Points ', 'EOS Points', 'EOS Midpoints']]
df2021_r1.columns = ['code', 'title','points_r1_2021','points_r2_2021', 'points_EOS_2021', 'points_Mid_2021']
df2021_r1


#  Set the index to the code column for the new df

# In[40]:


# Set the index to the code column
df2021_r1.set_index('code', inplace=True)
df2021_r1


# Do the same for the 2020 data, with the same columns.

# In[41]:


df2020_r1 = df2020[['COURSE CODE2', 'R1 POINTS','R2 POINTS', 'EOS','EOS Mid-point']]
df2020_r1.columns = ['code', 'points_r1_2020','points_r2_2020', 'points_EOS_2020', 'points_Mid_2020']
df2020_r1


# In[42]:


# Set the index to the code column
df2020_r1.set_index('code', inplace=True)
df2020_r1


# And for the 2019 we can do the same with the two available data columns.

# In[43]:


df2019_r1 = df2019[['Course Code', 'EOS', 'Mid']]
df2019_r1.columns = ['code', 'points_EOS_2019', 'points_Mid_2019']
df2019_r1


# In[44]:


# Set the index to the code column
df2019_r1.set_index('code', inplace=True)
df2019_r1


# Now we set the index to code for the allcourses df and can start joining the data.

# In[45]:


# Set the index to the code column
allcourses.set_index('code', inplace=True)


# In[46]:


#join round 1 2021 data
allcourses = allcourses.join(df2021_r1[['points_r1_2021']])
allcourses


# In[47]:


# Join round 1 2020 data to allcourses
allcourses = allcourses.join(df2020_r1[['points_r1_2020']])


# In[48]:


# Join round 2 2021 data to allcourses
allcourses = allcourses.join(df2021_r1[['points_r2_2021']])


# In[49]:


# Join round 2 2020 data to allcourses
allcourses = allcourses.join(df2020_r1[['points_r2_2020']])


# In[50]:


# Join EOS 2021 data to allcourses
allcourses = allcourses.join(df2021_r1[['points_EOS_2021']])


# In[51]:


# Join EOS 2020 data to allcourses
allcourses = allcourses.join(df2020_r1[['points_EOS_2020']])


# In[52]:


# Join EOS 2019 data to allcourses
allcourses = allcourses.join(df2019_r1[['points_EOS_2019']])


# In[53]:


# Join Mid 2021 data to allcourses
allcourses = allcourses.join(df2021_r1[['points_Mid_2021']])


# In[54]:


# Join Mid 2020 data to allcourses
allcourses = allcourses.join(df2020_r1[['points_Mid_2020']])


# In[55]:


# Join Mid 2019 data to allcourses
allcourses = allcourses.join(df2019_r1[['points_Mid_2019']])
allcourses


# And this is the final dataframe with all the data for the 3 years

# Checking the datatypes, all the values are objects so will need to be converted to a numeric type for plotting.

# In[56]:


allcourses.dtypes


# Create a new df to convert the datatypes and drop all instances of non numeric data. 
# 
# Within the data the are # and * values referring to modules that require extra entry requirements like an interview or a portfolio. As we are only concerned with the points for analysis we will keep that data in the allcourses df and create a new df with the * and # figures removed.

# In[57]:


#create a new df with just the points values
caoPoints = allcourses[['points_r1_2021','points_r1_2020','points_r2_2021', 'points_r2_2020',
                        'points_EOS_2021', 'points_EOS_2020','points_EOS_2019',
                        'points_Mid_2021','points_Mid_2020','points_Mid_2019']].replace('[A-Z.#*+a-z]', '', regex = True)


# In[58]:


#check data types
caoPoints.dtypes


# In[59]:


#View the new caoPoints df, 
#we can set the display rows column to 1232 for scan all the df
pd.set_option('display.max_rows',12)
caoPoints


# Now to convert all the data to numeric, coerce forces the conversion and ignores errors.

# In[60]:


#convert object to float
caoPoints['points_r1_2021'] = pd.to_numeric(caoPoints['points_r1_2021'],errors = 'coerce')
caoPoints['points_r1_2020'] = pd.to_numeric(caoPoints['points_r1_2020'],errors = 'coerce')
caoPoints['points_r2_2021'] = pd.to_numeric(caoPoints['points_r2_2021'],errors = 'coerce')
caoPoints['points_r2_2020'] = pd.to_numeric(caoPoints['points_r2_2020'],errors = 'coerce')
caoPoints['points_EOS_2021'] = pd.to_numeric(caoPoints['points_EOS_2021'],errors = 'coerce')
caoPoints['points_EOS_2020'] = pd.to_numeric(caoPoints['points_EOS_2020'],errors = 'coerce')
caoPoints['points_EOS_2019'] = pd.to_numeric(caoPoints['points_EOS_2019'],errors = 'coerce')
caoPoints['points_Mid_2021'] = pd.to_numeric(caoPoints['points_Mid_2021'],errors = 'coerce')
caoPoints['points_Mid_2020'] = pd.to_numeric(caoPoints['points_Mid_2020'],errors = 'coerce')
caoPoints['points_Mid_2019'] = pd.to_numeric(caoPoints['points_Mid_2019'],errors = 'coerce')


# In[61]:


#check the new data types
caoPoints.dtypes


# Now to rejoin the non numeric columns to the caoPoints df.

# In[62]:


caoPoints = caoPoints.join(allcourses['title'])


# In[63]:


caoPoints = caoPoints.join(allcourses['college'])


# In[64]:


caoPoints.dtypes


# In[65]:


caoPoints


# We are now ready for the analysis
# 
# ---

# ## Analysis

# In[66]:


# Change default style of matplot lib pyplot charts.
plt.style.use('seaborn')

# Change default matplotlib pyplot figure size and bins.
plt.rcParams['figure.figsize'] = (10,10)


# In[67]:


caoPoints.describe()


# In[68]:


#count of data per column
caoPoints.count()


# We can see the ammount of courses offered by each instituton over the 3 year period, with Trinity College Dublin and Technological University Dublin offering by far the most courses.

# In[69]:


pd.set_option('display.max_rows',38)
countColleges = caoPoints["college"].value_counts()
countColleges


# #### Round 1 2020-2021

# In[70]:


sns.kdeplot(caoPoints['points_r1_2021'], label='R1 2021',shade=True)
sns.kdeplot(caoPoints['points_r1_2020'], label='R1 2020',shade=True)

plt.title("KDE of 2020 and 2021 Round 1 points")
plt.legend()
plt.show()


# Comparing the distributions of Round 1 points from 2021 - 2020 we can see the overall values have risen in 2021 and the peak has flattened from around the 300 points value.

# #### Round 2 2020-2021

# In[71]:


sns.kdeplot(caoPoints['points_r2_2021'], label='R2 2021',shade=True)
sns.kdeplot(caoPoints['points_r2_2020'], label='R2 2020',shade=True)

plt.title("KDE of 2020 and 2021 Round 2 points")
plt.legend()
plt.show()


# With the round 2 data there does appear to be a rise in points in 2021 and lower peaks, there is also a rise in values over 800 points suggesting more emphasis on portfolios that consider more points then the 625 max from Leaving Cert results.

# #### EOS 2020-2021

# In[72]:


sns.kdeplot(caoPoints['points_EOS_2021'], label='EOS 2021',shade=True)
sns.kdeplot(caoPoints['points_EOS_2020'], label='EOS 2020',shade=True)
sns.kdeplot(caoPoints['points_EOS_2019'], label='EOS 2019',shade=True)
plt.legend()
plt.show()


# #### Mid 2020-2021

# There is a clear trend of points increasing over the 3 years.

# In[73]:


sns.kdeplot(caoPoints['points_Mid_2021'], label='Mid 2021',shade=True)
sns.kdeplot(caoPoints['points_Mid_2020'], label='Mid 2020',shade=True)
sns.kdeplot(caoPoints['points_Mid_2019'], label='Mid 2019',shade=True)
plt.legend()
plt.show()


# #### Differences

# Now that we can see a clear trend in increasing points over the years it will be interesting to break this down further. Here we can create 8 new columns in the dataframe subtracting points of earlier years and look at the point differential.

# In[74]:


#Create new colums of point differences
caoPoints['R1_21-20'] = caoPoints['points_r1_2021'] - caoPoints['points_r1_2020']
caoPoints['R2_21-20'] = caoPoints['points_r2_2021'] - caoPoints['points_r2_2020']
caoPoints['EOS_21-20'] = caoPoints['points_EOS_2021'] - caoPoints['points_EOS_2020']
caoPoints['EOS_21-19'] = caoPoints['points_EOS_2021'] - caoPoints['points_EOS_2019']
caoPoints['EOS_20-19'] = caoPoints['points_EOS_2020'] - caoPoints['points_EOS_2019']
caoPoints['Mid_21-20'] = caoPoints['points_Mid_2021'] - caoPoints['points_Mid_2020']
caoPoints['Mid_21-19'] = caoPoints['points_Mid_2021'] - caoPoints['points_Mid_2019']
caoPoints['Mid_20-19'] = caoPoints['points_Mid_2020'] - caoPoints['points_Mid_2019']

caoPoints


# To visualize these differences we can plot the points differences and group by college to see which colleges had the greatest change in points.

# #### Round 1 and 2 differences per year by college

# In[80]:


# Change default figure size.
plt.rcParams['figure.figsize'] = (15,20)
fig, axes = plt.subplots(1,2)

ax1 = sns.barplot(x = caoPoints["R1_21-20"], y = caoPoints["college"], ax=axes[0])
ax2 = sns.barplot(x = caoPoints["R2_21-20"], y = caoPoints["college"], ax=axes[1])
ax2.get_yaxis().set_ticks([])


# #### EOS points differences per year by college

# In[76]:


fig, axes = plt.subplots(1,3)

#EOS points differences per year by college
ax1 = sns.barplot(x = caoPoints["EOS_21-20"], y = caoPoints["college"], ax=axes[0])
ax2 = sns.barplot(x = caoPoints["EOS_20-19"], y = caoPoints["college"], ax=axes[1])
ax2.get_yaxis().set_ticks([])
ax3 = sns.barplot(x = caoPoints["EOS_21-19"], y = caoPoints["college"], ax=axes[2])
ax3.get_yaxis().set_ticks([])


# #### Mid point differences per year by college

# In[77]:


fig, axes = plt.subplots(1,3)

#Mid point differences per year by college
ax1 = sns.barplot(x = caoPoints["Mid_21-20"], y = caoPoints["college"], ax=axes[0])
ax2 = sns.barplot(x = caoPoints["Mid_20-19"], y = caoPoints["college"], ax=axes[1])
ax2.get_yaxis().set_ticks([])
ax3 = sns.barplot(x = caoPoints["Mid_21-19"], y = caoPoints["college"], ax=axes[2])
ax3.get_yaxis().set_ticks([])
plt.show()


# The midpoints values all trended upwards except for ICD Business School, which dropped significanlty. This may be due to an outlier like a 0 instead of a NaN value. 

# ## References

# ##### Data sources:
# 
# 1. CAO webpage: http://www.cao.ie/
# 2. 2021 original data http://www2.cao.ie/points/l8.ph
# 3. 2021 csv https://www.cao.ie/index.php?page=points&p=2021
# 4. 2020 csv http://www.cao.ie/index.php?page=points&p=2020
# 5. 2019 pdf http://www.cao.ie/index.php?page=points&p=2019
# 
# ---
# https://github.com/ianmcloughlin/cao-points
# 
# 
# 
# 
# 
# https://stackoverflow.com/questions/48094854/pandas-convert-data-type-from-object-to-float
# 

# ---------
# # End
