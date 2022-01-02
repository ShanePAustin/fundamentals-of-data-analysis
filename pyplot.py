#!/usr/bin/env python
# coding: utf-8

# ## Fundamentals of Data Analysis, Winter 21/22
# 
# ### Overview of the matplotlib.pyplot Python package
# 

# #### Pyplot Notebook
# 
# 
# * A clear and concise overview of the matplotlib.pyplot Python package.
# * An in-depth explanation of three interesting plots from the matplotlib.pyplot Python package.

# # Introduction

# -----------------------------
# #### What is Matplotlib
# 
# Matplotlib is a comprehensive library for creating static, animated, and interactive visualizations in Python [1](https://matplotlib.org/). Matplotlib is an open source library, created by John D. Hunter mostly written in python, with a few segments written in C, Objective-C and Javascript for Platform compatibility. It was built to work in a similar fashion to the MATLAB programming language and provides a similar MATLAB like interface for graphics. 
# 
# Matplotlib is a powerful tool for executing a variety of tasks. It is able to create different types of visualization reports like line plots, scatter plots, histograms, bar charts, pie charts, box plots, and many more different plots including 3-dimensional plotting [2](https://www.analyticsvidhya.com/blog/2021/10/introduction-to-matplotlib-using-python-for-beginners/). It integrates with the pandas packaage, which handles data in an organised manner and together make up the fundamentals of data wrangling and visualisation within Python.  <br /><br />

# Matplotlib uses an object oriented approach to plotting. This means that plots can be built step-by-step by adding new elements to the plot. Matplotlib is conceptually split into three layers shown below.
# 
# ![image](https://delftswa.gitbooks.io/desosa-2017/content/matplotlib/images-matplotlib/functional_view.png)
# 
# ##### Backend Layer
# 
# This layer interacts directly with the environment it is run on, and it consists of 3 main components:
# 
# * ```FigureCanvas``` - Acts as the surface that is drawn into to make the plots
# * ```Renderer``` - This does the drawing of the plots
# * ```Event``` - This component handles user inputs such as mouse or keyboard events
# 
# ##### Artist Layer
# 
# This layer handles the communication with the backend layer and is responsible of most of the code requirements. Every image component inside a plot made by Matplotlib (axes, legends, etc) is an instance of the ```Artist``` class. The most important Artist object in Matplotlib is Axes which is responsible for composing the 2D data plots by combining multiple other Artist objects.
# 
# ##### Scripting Layer
# 
# The scripting layer is accessed through the ```pyplot``` module and contains methods to create commonly used plotting graphics such as the histogram or the scatterplot. This layer also handles additional plot arguments such as setting the color of the plot or the plot labels.
# 

# --------------------------------
# ### Plotting
# 
# There are two primary objects associated with a matplotlib plot:
# 
# * figure object: the overall figure space that can contain one or more plots.
# * axis objects: the individual plots that are rendered within the figure.
# 
# Different elements of a standard graph are shown in the image below

# ![image](https://3.bp.blogspot.com/-AtPG_12l4e8/XRSuQEECZGI/AAAAAAAAHxY/ZsgtA4rMphMZujcWUur9BB-xYKoWDkKPQCLcBGAs/s1600/basics_matplotlib.PNG)
# 
# [3]

# Matplotlib comes pre installed on many Python distrubutions like Anaconda, if it is not it can be easily installed by using the command.
# 
# ```pip install matplotlib```

# Matplotlib contains many modules that provide different plotting functionality, the most commonly used module is pyplot.
# 
# The pyplot module is typically imported using "plt" key.

# In[1]:


# Import pyplot
import matplotlib.pyplot as plt


# In[2]:


get_ipython().run_line_magic('matplotlib', 'inline')


# The below series of plots will show the use of figures and axes within pyplot as examples of how these objects build the plots.
# 
# Using pyplot to set the figure object

# In[3]:


#setting the figure
fig, ax = plt.subplots()


# Applying 2 axes onto the figure object

# In[4]:


#Plotting 2 axes on one figure
fig, (ax1, ax2) = plt.subplots(1,2)


# A simple line plot using pyplot. A simple dataset is created and pyplot is call using plt.plot() to plot the data contained in x.

# In[5]:


#Simple dataset
x = (1,2,3,4,5,6,7)

#Using pyplot to the line 
plt.plot(x)
#Use to display the plot
plt.show()


# Plotting a formula of x squared

# In[6]:


x = (1,2,3,4,5,6,7)
#Iterate through x and calculate the square of each
x2 = [x ** 2 for x in x]

#plotting the new list
plt.plot(x2)
plt.show()


# Using pyplot to plot two lines on one axis

# In[7]:


plt.plot(x)
plt.plot(x2)

plt.show()


# Using pyplot to plot one a different axis

# In[8]:


#Set the 2 axes
fig, (ax1, ax2) = plt.subplots(1,2)

#Set which axis to plot to
ax1.plot(x)
ax2.plot(x2)

plt.show()


# #### Labels
# 
# Matplotlib has built in functions that allow the labelling of plots command include:
# 
# * ```label()```  - can assign a label to each plot
# * ```xlabel()``` - for labelling the x axis
# * ```ylabel()``` - for labelling the x axis
# * ```title()```  - for the plot title
# * ```legend()``` - creates a key of the labels

# The plot below shows the use of these label functions within pyplot.

# In[9]:


#establish the dataset
x = (1,2,3,4)
x2 = [x ** 2 for x in x]
x3 = [x ** 3 for x in x]

#plot as before with added labels
plt.plot(x, label = "x")
plt.plot(x2, label = "x2")
#can call on the variable itself to display the contents
plt.plot(x3, label = x3)

#Add a title
plt.title ("Example of labels")
#x and y labels
plt.xlabel("x")
plt.ylabel("y")
#legend that takes values from "label"
plt.legend()
plt.show()


# #### Styling
# 
# They are many different style function built into matplotlib some commands include
# 
# * ```color```     - can change the line colour  
# * ```linestyle``` - assign a style to the line
# * ```linewidth``` - set the thickness of the line
# * ```marker```    - add an interval marker on the line
# * ```grid```      - apply a background grid, can also set to apply to just one axis
# * ```facecolor``` - set the background colour
# 
# The plot below shows the use of these style functions within pyplot. 

# In[10]:


fig, ax = plt.subplots()

#establish the dataset
x = (1,2,3,4)
x2 = [x ** 2 for x in x]
x3 = [x ** 3 for x in x]

#plot just "*" instead of a line, coloured red
plt.plot(x, "*", color = "red")
#apply marker
plt.plot(x2, marker = "o")
#set the linestyle and thickness
plt.plot(x3, linestyle ="dashed", linewidth = "5")
#apply a grid (set to only y axis and dashed line)
plt.grid(axis = "y", linestyle ="dashed")
#change the axis colour
ax.set_facecolor("lightblue")
plt.show()


# #### Putting it together
# 
# With this plot numpy is imported to use the linspace function to plot evenly spaced samples over an interval range, this will result in a curved plot. Then the markers have to be set to the desired interval rather than at every plot point.
# 
# Latex math notation can also be used to style the labels.

# In[11]:


#For arrays, contains linspace function
import numpy as np

#define dataset
lowRange = 0
highRange = 4
#I decided to make the step 10 * the high range, this means it will plot 10 points for each whole number on the x axis
#this makes the "markevery" consistent and easy to configure
step = (highRange*10)+1

#set axes area, i extended the y limit to 70 otherwise in cuts off at 60 and the highest value is 64
ax = plt.axes()
#ylim and xlim can hardcode the plot area
plt.ylim(-2,70)

#create dataset, I used linspace as it plots evenly spaced samples over the interval range
xpoints = np.linspace(lowRange,highRange,step)

#calculations for x, xsquared and xcubed
x = xpoints
x2 = xpoints**2
x3 = xpoints**3

#plots x and y, using $""$ denote LaTeX math notation for labels, colours chosen from CSS color
#markevery plots a point at every whole number on the x axis
plt.plot(xpoints, x,label = "$f(x)= x$", color="firebrick", linewidth = 2, marker = "o", markevery = 10)
plt.plot(xpoints, x2,label = "$g(x)= x^{2}$", color="royalblue", linewidth = 2, marker = "o", markevery = 10)
plt.plot(xpoints, x3, label = "$h(x)= x^{3}$", color="forestgreen", linewidth = 2, marker = "o", markevery = 10)

#labels, using LaTeX math notation
plt.title ("Values of $x$, $x^{}$, and $x^{}$ in the range {}-{}".format(2,3,lowRange,highRange))
plt.xlabel("$x$")
plt.ylabel("$x^{n}$")
plt.legend()

#style, sets background colour and a dashed grid
plt.grid(linestyle ="dashed")
ax.set_facecolor("lightgrey")
plt.show()


# These have all been plotted using the default line plot type within the library, other simple plots can be defined with the following functions:
# 
# | Type of Plot  | Function  |
# |---|---|
# | line plot (Default)  | plt.plot(  )  |  
# | vertical bar plots  | plt.bar(  )  | 
# | horizontal bar plots  | plt.barh(  )  |
# | histogram  | plt.hist(  )  |  
# | boxplot  | plt.box(  )  |  
# | area plots  | plt.area(  )  |  
# | scatter plots  | plt.scatter(  )  |  
# | pie plots  | plt.pie(  )  |  
# | hexagonal bin plots  | plt.hexbin(  )  |  
# 
# Three of these plot types will be analysed further below.

# ----------
# ## Three Interesting Plots
# 
# For the interesting plots the Iris dataset will be used to give examples of the various plots and help describe the functionality.

# In[12]:


#For data frames
import pandas as pd


# Pyplot style sheets to set a style for all future plots [4](https://matplotlib.org/stable/gallery/style_sheets/style_sheets_reference.html)

# In[13]:


#Set the style for future plots 
plt.style.use('ggplot')


# For the following examples the Iris dataset will be used to represent the plots. The dataset can be imported from .csv and assigned to a Pandas dataframe, the columns are also labelled.

# In[14]:


filename = ".\Pyplot Data\iris.csv"

df = pd.read_csv(filename, header = None, names = ["SepalLength", "SepalWidth", "PetalLength", "PetalWidth", "Species"])


# Verify the dataset imported as expected

# In[15]:


df


# Check the row length and column count

# In[16]:


shape = df.shape
shape


# Check for missing, values, there are 150 entries per variable as expected.

# In[17]:


count = df.count()
count


# The data counts are split evenly across the class types as expected.

# In[18]:


countSpecies = df["Species"].value_counts()
countSpecies


# In[19]:


summary = df.describe().round(2)
summary


# Now that the data is imported as expected we can start plotting.

# ---
# ### Histograms
# [Official Documentation](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.hist.html)
# 
# matplotlib.pyplot.hist(x, bins=None, range=None, density=False, weights=None, cumulative=False, bottom=None, histtype='bar', align='mid', orientation='vertical', rwidth=None, log=False, color=None, label=None, stacked=False, *, data=None, **kwargs)

# A histogram is an approximate representation of the distribution of numerical data. Where bar charts are used specifically on categorical data, Histograms are a group of bars connected to each other, visualizing a distribution of a some continuous quantitative variable.
# ![image](https://keydifferences.com/wp-content/uploads/2016/04/bar-graph-vs-histogram.jpg)
# 
# As there are no defined bounds in continous data, to construct a histogram, the first step is to "bin" (or "bucket") the range of values, or divide the entire range of values into a series of intervals and then count how many values fall into each interval. This is done automatically in pyplot or the bin value can be set manually.

# Using the imported dataset we can plot the distribution of each variable and show some of the built in parameters.
# 
# * ```x``` : Input values, takes in arrays
# * ```bins``` : Set the bin count
# * ```range``` : The lower and upper range of the bins.
# * ```density``` : draw and return a probability density
# * ```weights``` : An array of weights, of the same shape as x.
# * ```cumulative``` : A histogram is computed where each bin gives the counts in that bin plus all bins for smaller values.
# * ```bottom``` : Location of where the bottom of each bin is drawn from
# * ```histtype```: The type of histogram to draw. {'bar', 'barstacked', 'step', 'stepfilled'}
# * ```align``` : The horizontal alignment of the histogram bars. {'left', 'mid', 'right'}, default: 'mid'
# * ```orientation``` : If 'horizontal', barh will be used for bar-type histograms
# * ```rwidth``` : The relative width of the bars as a fraction of the bin width.
# * ```log``` : If True, the histogram axis will be set to a log scale.
# * ```color``` : Color or sequence of colors, one per dataset.
# * ```label``` : String, or sequence of strings to match multiple datasets.
# * ```stackedbool``` : If True, multiple data are stacked on top of each other
# ---

# Plot a standard histogram with the x array being the Sepal Length of the dataset. Color set to "firebrick"

# In[20]:


ax = plt.axes()
plt.hist(df["SepalLength"], color = "firebrick")
plt.title("Sepal Length Histogram")
plt.xlabel("Sepal Length")
plt.show()


# Plot a standard histogram with the x array being the Sepal Width of the dataset. 
# 
# * Color set to "royalblue"
# * bins = 5 - sets the bin count to 5 
# * ec = "Black" - draws a line around each bin

# In[21]:


ax = plt.axes()
plt.hist(df["SepalWidth"], color = "royalblue", ec = "black", bins = 5)
plt.title("Sepal Width Histogram")
plt.xlabel("Sepal Width")
plt.show()


# Plot a standard histogram with the x array being the Petal Length of the dataset. 
# 
# * Color set to "forestgreen"
# * orientation='horizontal' - plot horizontally
# * log = True - plot to logarithmic scale

# In[22]:


ax = plt.axes()
plt.hist(df["PetalLength"], color = "forestgreen", ec = "black",orientation='horizontal',log = True)
plt.title("Petal Length Histogram")
plt.xlabel("Petal Length")
plt.show()


# Plot a standard histogram with the x array being the Petal Length of the dataset. 
# 
# * Color set to "darkorchid"
# * rwidth = 0.5 - make the bins half the width
# * align = 'left' - bars are centered on the left bin edges.

# In[23]:


ax = plt.axes()
plt.hist(df["PetalWidth"], color = "darkorchid", ec = "black", rwidth = 0.5, align = 'left')
plt.title("Petal Width Histogram")
plt.xlabel("Petal Width")
plt.show()


# This can be combined and plotted on one figure with 4 axes, all with the different parameter settings.

# In[24]:


plt.subplot(2,2,1)
plt.hist(df["SepalLength"], color = "firebrick")
plt.title("Sepal Length Histogram")
plt.xlabel("Sepal Length")

plt.subplot(2,2,2)
plt.hist(df["SepalWidth"], color = "royalblue", ec = "black", bins = 5)
plt.title("Sepal Width Histogram")
plt.xlabel("Sepal Width")

plt.subplot(2,2,3)
plt.hist(df["PetalLength"], color = "forestgreen", ec = "black",orientation='horizontal',log = True)
plt.title("Petal Length Histogram")
plt.xlabel("Petal Length")

plt.subplot(2,2,4)
plt.hist(df["PetalWidth"], color = "darkorchid", ec = "black", rwidth = 0.5, align = 'left')
plt.title("Petal Width Histogram")
plt.xlabel("Petal Width")

#tight layout stops the labels overlapping
plt.tight_layout()


# And while not advised in this case it can also be plotted onto one axis.

# In[25]:


ax = plt.axes()

plt.hist(df["SepalLength"], color = "firebrick", label = "Sepal Length")
plt.hist(df["SepalWidth"], color = "royalblue", label = "Sepal Width",ec = "black", bins = 5)
plt.hist(df["PetalLength"], color = "forestgreen", label = "Petal Length",log = True,orientation='horizontal')
plt.hist(df["PetalWidth"], color = "darkorchid", label = "Petal Width",rwidth = 0.5, align = 'left')

plt.legend()
plt.show()


# The below plot shows examples of different "histtypes" and the use of alpha to make the color transparent to a required level.

# In[26]:


plt.figure(figsize=(10,10))

plt.subplot(2,2,1)
plt.hist(df["SepalLength"], histtype = "bar")

plt.title("histtype = bar")
plt.xlabel("Sepal Length")

plt.subplot(2,2,2)
plt.hist(df["PetalLength"], histtype = "barstacked")
plt.hist(df["SepalLength"], histtype = "barstacked")

plt.title("histtype = barstacked")
plt.xlabel("Sepal Width")

plt.subplot(2,2,3)
plt.hist(df["PetalLength"], alpha=0.2)
plt.title("alpha=0.2")
plt.xlabel("Petal Length")

plt.subplot(2,2,4)
plt.hist(df["PetalWidth"], histtype = "step")

plt.title("histtype = step")
plt.xlabel("Petal Width")

#tight layout stops the labels overlapping
plt.tight_layout()


# We can use histogram plots to represent the whole dataset in one figure. First the class types are set as a variable to distinguish the seperate plots and colours. This shows the functionality of basic plots within pyplot, as it can summerize a whole dataset with all variables in one graphic.

# In[27]:


#Assign species class to a variable
setosa = df.loc [df ["Species"] == "Iris-setosa"]
versicolor = df.loc [df ["Species"] == "Iris-versicolor"]
virginica = df.loc [df ["Species"] == "Iris-virginica" ]


# In[28]:


#Plot Variable seperated by class
plt.figure(figsize=(10,10))
plt.suptitle ("Combined Histograms Seperated by Species")
plt.subplot(2,2,1)
plt.hist(setosa["SepalLength"], alpha = 0.75, label = "Iris-setosa")
plt.hist(versicolor["SepalLength"], alpha = 0.5, label = "Iris Versicolour")
plt.hist(virginica ["SepalLength"], alpha = 0.5, label = "Iris Virginica")
plt.xlabel ("Sepal Length")
plt.ylabel ("Frequency")

plt.subplot(2,2,2)
plt.hist(setosa["SepalWidth"], alpha = 0.75, label = "Iris-setosa")
plt.hist(versicolor["SepalWidth"], alpha = 0.5, label = "Iris Versicolour")
plt.hist(virginica ["SepalWidth"], alpha = 0.5, label = "Iris Virginica")
plt.xlabel ("Sepal Width")
plt.ylabel ("Frequency")

plt.subplot(2,2,3)
plt.hist(setosa["PetalLength"], alpha = 0.75, label = "Iris-setosa")
plt.hist(versicolor["PetalLength"], alpha = 0.5, label = "Iris Versicolour")
plt.hist(virginica ["PetalLength"], alpha = 0.5, label = "Iris Virginica")
plt.xlabel ("Petal Length")
plt.ylabel ("Frequency")

plt.subplot(2,2,4)
plt.hist(setosa["PetalWidth"], alpha = 0.75, label = "Iris-setosa")
plt.hist(versicolor["PetalWidth"], alpha = 0.5, label = "Iris Versicolour")
plt.hist(virginica ["PetalWidth"], alpha = 0.5, label = "Iris Virginica")
plt.xlabel ("Petal Width")
plt.ylabel ("Frequency")


plt.legend()
#tight layout stops the labels overlapping
plt.tight_layout()


# #### Seaborn

# Seaborn is another graphically plotting package that is built upon pyplot, it can be a powerful tool to represent advanced plots in a small amout of code. Below is a reconstruction of the above pyplot figure with much less code required.

# In[29]:


import seaborn as sns

distplot, axes = plt.subplots(2,2, figsize=(10,10), sharex=False)
sns.histplot( x="SepalLength", hue="Species", data = df, palette="BuPu_r", ax=axes[0,0])
sns.histplot( x="SepalWidth",  hue="Species", data = df, palette="BuPu_r", ax=axes[0,1])
sns.histplot( x="PetalLength", hue="Species", data = df, palette="BuPu_r", ax=axes[1,0])
sns.histplot( x="PetalWidth",  hue="Species", data = df, palette="BuPu_r", ax=axes[1,1])
plt.suptitle("Combined Histograms Seperated by Species")


# Another interesting plot type based around historam plots is the ```hist2d```, this takes in 2 arrays and creates a top down view of a histogram. 2D histograms are useful when you need to analyse the relationship between 2 numerical variables that have a huge number of values. It is useful for avoiding the over-plotted scatterplots. You can explicitly tell how many bins you want for the X and the Y axis.

# In[30]:


ax = plt.axes()
x = df["PetalLength"] 
y = df["PetalWidth"]
plt.hist2d(x, y, bins = (30,30))
plt.title ("2D Histogram: Petal Length - Width")
plt.show()


# ---
# ### Scatter Plots
# [Official Documentation](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.scatter.html)
# 
# matplotlib.pyplot.scatter(x, y, s=None, c=None, marker=None, cmap=None, norm=None, vmin=None, vmax=None, alpha=None, linewidths=None, *, edgecolors=None, plotnonfinite=False, data=None, **kwargs)

# A scatter plot uses dots to represent values for two different numeric variables. The position of each dot on the horizontal and vertical axis indicates values for an individual data point. Scatter plots are used to observe relationships between variables.

# 
# * ```x, y``` : The data positions.
# * ```s``` : The marker size
# * ```c``` : The marker colors.
# * ```marker``` : The marker style.
# * ```cmap``` : A Colormap instance
# * ```norm``` : If c is an array of floats, norm is used to scale the color data
# * ```vmin, vmax``` : vmin and vmax are used in conjunction with the default norm to map the color array c to the colormap cmap
# * ```alpha``` : The alpha blending value, between 0 (transparent) and 1 (opaque).
# * ```linewidths``` : The linewidth of the marker edges
# * ```edgecolors``` : The edge color of the marker
# 
# ---

# A basic scatter plot of Petal Length vs Petal Width

# In[31]:


ax = plt.axes()
#Set the x and y values
x = df["PetalLength"] 
y = df["PetalWidth"]
#Plot a scatter x to y
plt.scatter(x, y)
plt.show()


# A basic scatter plot of Sepal Length vs Sepal Width
# 
# * marker = "2" - change the dot type
# * c = "purple" - change the colour

# In[32]:


x = df["SepalLength"] 
y = df["SepalWidth"]
plt.scatter(x, y, marker = "2", c = "purple")
plt.show()


# Like before with the histograms we can plot the data seperated by class.
# 
# * edgecolors='black' - outline the dots
# * alpha=0.5 - set the transparency

# In[33]:


#Sepal sizes by species
plt.scatter(setosa["SepalLength"], setosa["PetalLength"], label='Setosa')
plt.scatter(versicolor["SepalLength"], versicolor["PetalLength"], label='Versicolor', edgecolors='black')
plt.scatter(virginica["SepalLength"], virginica["PetalLength"], label='Virginica', alpha=0.5)

#Set labels and title
plt.xlabel('Sepal Length')
plt.ylabel('Petal Length')
plt.title('Sepal vs Petal Lengths')

#Add a legend
plt.legend()
plt.show()


# Like the plot above but we can use s to set the size of the dot, in this example the size is related the the Petal Width variable which adds another dimension to the plot

# In[34]:


#Sepal Length sizes by species
plt.scatter(setosa["SepalLength"], setosa["PetalLength"], label='Setosa', s = 50 * setosa["PetalWidth"])
plt.scatter(versicolor["SepalLength"], versicolor["PetalLength"], label='Versicolor', s = 50 * versicolor["PetalWidth"])
plt.scatter(virginica["SepalLength"], virginica["PetalLength"], label='Virginica', s = 50 * virginica["PetalWidth"])

#Set labels and title
plt.xlabel('Sepal Length')
plt.ylabel('Petal Length')
plt.title('Sepal vs Petal Lengths')

#Add a legend
plt.legend()
plt.show()


# #### Seaborn

# As mentioned above Seaborn can produce powrful graphics using limited code, the plot below produces a Seaborn pairplot creating a scatter plot per each variable in the dataframe and a KDE of the single variables.  

# In[35]:


#Seaborn pairplot seperated by species
sns.pairplot(df,hue="Species", palette="BuPu_r", height=3)


# Another nice example using scatter plots is plotting coordinates as a scatter and mapping them to real life map data. In this example a csv of the Galway lifeboat callouts is mapped by their coordinates and plotted on a map using the plotly library. This is another independent library that shows the advanced features available when plotting using Python. 

# In[36]:


filename = "RNLI_Returns_of_Service_Galway.csv"

map_df = pd.read_csv(filename)


# In[37]:


#import plotly
import plotly.express as px

px.set_mapbox_access_token(open("./mapbox/mapbox_token").read())
fig = px.scatter_mapbox(map_df, lat="Y", lon="X", size_max=15, zoom=10, color = "YearOfCall", hover_name="LaunchTime")
fig.show()


# I have included a image of the above plot as the original interactive plot was not rendering on github.

# ![Galway Bay](./images/galwayBay.png)

# ---
# ### Box Plots
# [Official Documentation](https://matplotlib.org/3.1.1/api/_as_gen/matplotlib.pyplot.boxplot.html)
# 
# matplotlib.pyplot.boxplot(x, notch=None, sym=None, vert=None, whis=None, positions=None, widths=None, patch_artist=None, bootstrap=None, usermedians=None, conf_intervals=None, meanline=None, showmeans=None, showcaps=None, showbox=None, showfliers=None, boxprops=None, labels=None, flierprops=None, medianprops=None, meanprops=None, capprops=None, whiskerprops=None, manage_ticks=True, autorange=False, zorder=None, *, data=None)[source]

# In descriptive statistics, a box plot or boxplot is a method for graphically demonstrating the locality, spread and skewness groups of numerical data through their quartiles.
# 
# With a boxplot, we can extract the same insights as with an histogram. And while we can visualize the shape of the distribution with an histogram, a boxplot highlights the summary metrics that give the distribution its shape. The summary metrics we can extract from a boxplot are:
# 
# * Quantiles, specifically the first and third quantiles, which correspond to the 25th and 75th percentiles.
# * Median, the mid-point in the distribution, which also corresponds to the 50th percentile.
# * Interquartile range (IQR), the width between the third and first quantiles. Expressed mathematically, we have IQR = Q3 — Q1.
# * Min, minimum value in the dataset excluding outliers, which corresponds to Q1–1.5xIQR.
# * Max, maximum value in the dataset, excluding outliers, which corresponds to Q3+ 1.5xIQR.
# 
# ![image](https://miro.medium.com/max/1838/1*2c21SkzJMf3frPXPAR_gZA.png)
# 
# [7](https://towardsdatascience.com/create-and-customize-boxplots-with-pythons-matplotlib-to-get-lots-of-insights-from-your-data-d561c9883643)

# In[38]:


summary


# A basic boxplot of the 4 variables

# In[39]:


#Drop Species to make data all numerical
box_df = df.drop('Species', axis=1)

#Use boxplot() to plot the new dataframe
plt.boxplot(box_df)
plt.show()


# Simple boxplot with added labels

# In[40]:


#Assign ticks for labelling
ticks = range(1, len(box_df.columns)+1)
#Take labels from column headers
labels = list(box_df.columns)

#Plot with labels
plt.boxplot(box_df)
plt.xticks(ticks, labels)
plt.show()


# Like before assign the class to a variable

# In[41]:


#Take the seperate species dataframes for individual plots
setosa = setosa.drop('Species', axis=1)
versicolor = versicolor.drop('Species', axis=1)
virginica = virginica.drop('Species', axis=1)


# ##### Plots per Species

# Plots for Setosa
# 
# * patch_artist=True - colours the box

# In[42]:


#Plot for Setosa
plt.boxplot(setosa, patch_artist=True)
plt.xticks(ticks, labels)
plt.show()


# Plots for Versicolor
# 
# * vert=False - plots on horizontal plane

# In[43]:


plt.boxplot(versicolor, vert=False)
plt.xticks(ticks, labels)
plt.show()


# Plots for Virginica
# 
# * notch=True - applies the notch effect in the plot

# In[44]:


plt.boxplot(virginica, notch=True)
plt.xticks(ticks, labels)
plt.show()


# If we want to plot like with the Histogram and the Scatter plots comparing all the variables seperated by class, there is a few steps to take.
# 
# First we need to set each class to a variable per dataframe variable

# Sepal Length

# In[45]:


#Set each class to a variable
setosaSL = setosa['SepalLength']
versicolorSL = versicolor['SepalLength']
virginicaSL = virginica['SepalLength']


# Sepal Width

# In[46]:


#Set each class to a variable
setosaSW = setosa['SepalWidth']
versicolorSW = versicolor['SepalWidth']
virginicaSW = virginica['SepalWidth']


# Petal Length

# In[47]:


#Set each class to a variable
setosaPL = setosa['PetalLength']
versicolorPL = versicolor['PetalLength']
virginicaPL = virginica['PetalLength']


# Petal Width

# In[48]:


#Set each class to a variable
setosaPW = setosa['PetalWidth']
versicolorPW = versicolor['PetalWidth']
virginicaPW = virginica['PetalWidth']


# Now assign each of these variables to a variable to plot

# In[49]:


SL = [setosaSL, versicolorSL, virginicaSL]
SW = [setosaSW, versicolorSW, virginicaSW]
PL = [setosaPL, versicolorPL, virginicaPL]
PW = [setosaPW, versicolorPW, virginicaPW]


# Now to bring it together and plot.

# In[50]:


#Setup the figure
plt.figure(figsize=(30,20))
plt.suptitle ("Box Plot Split by Species")
labels = df['Species'].unique()

#Setup the subplots
plt.subplot(2,2,1)

#Plot defined variable and label
plt.boxplot(SL, labels=labels)
plt.subplot(2,2,2)
labels = df['Species'].unique()
plt.boxplot(SW, labels=labels)
plt.subplot(2,2,3)
labels = df['Species'].unique()
plt.boxplot(PL, labels=labels)
plt.subplot(2,2,4)
labels = df['Species'].unique()
plt.boxplot(PW, labels=labels)


plt.show()


# #### Seaborn

# In a more concise fashion Seaborn can produce the same with only 6 lines of code.

# In[51]:


boxPlot, axes = plt.subplots(1,4, figsize=(16,8))
sns.boxplot(x="Species", y="SepalLength", hue="Species", data=df, palette="BuPu_r", ax=axes[0], dodge=False)    
sns.boxplot(x="Species", y="SepalWidth" , hue="Species", data=df, palette="BuPu_r", ax=axes[1], dodge=False)
sns.boxplot(x="Species", y="PetalLength", hue="Species", data=df, palette="BuPu_r", ax=axes[2], dodge=False)
sns.boxplot(x="Species", y="PetalWidth" , hue="Species", data=df, palette="BuPu_r", ax=axes[3], dodge=False)
plt.suptitle("Box Plots")


# ### References:
# 
# 

# 1. https://matplotlib.org/
# 2. https://www.analyticsvidhya.com/blog/2021/10/introduction-to-matplotlib-using-python-for-beginners/
# 3. https://www.listendata.com/2019/06/matplotlib-tutorial-learn-plot-python.html
# 4. https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.hist.html
# 5. https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.scatter.html
# 6. https://matplotlib.org/3.1.1/api/_as_gen/matplotlib.pyplot.boxplot.html
# 7. https://towardsdatascience.com/create-and-customize-boxplots-with-pythons-matplotlib-to-get-lots-of-insights-from-your-data-d561c9883643

# In[ ]:




