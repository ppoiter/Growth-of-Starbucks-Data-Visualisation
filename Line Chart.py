
# coding: utf-8

# In[1]:


import plotly.plotly as py
import plotly.graph_objs as go
import pandas as pd


# In[2]:


df = pd.read_csv('starbucks.csv')
df.head()


# In[3]:


x = df['Year']
y_usa = df['USA']
y_intl = df['Intl']


# In[17]:


# Create traces
trace0 = go.Scatter(
    x = x,
    y = y_usa,
    mode = 'lines',
    name = 'USA'
)
trace1 = go.Scatter(
    x = x,
    y = y_intl,
    mode = 'lines',
    name = 'International'
)
data = [trace0, trace1]

layout = dict(title = 'Growth of Starbucks 1994 - 2013',
              yaxis = dict(title = 'Stores', showgrid=False, showline = True),
              xaxis = dict(showgrid=False, showline = False)
              )
fig = dict(data = data, layout = layout)
py.iplot(fig, filename='line-mode')





#fig = dict(data=data, layout=layout)
#py.iplot(fig, filename='styled-line')

