# imports
import numpy as np
import pandas as pd

import plotly.express as px
import plotly.graph_objects as go
import plotly.io as pio
from plotly.subplots import make_subplots

import matplotlib.pyplot as plt

# colors
monochrome_colors = ['#251616', '#760000', '#C63F3F', '#E28073', '#F1D3CF']
primary_colors = ['#C63F3F', '#F4B436', '#83BFCC', '#455574', '#E2DDDB']

# template
theme_hodp = go.layout.Template(
    layout=go.Layout(
        title = {'font':{'size':24, 'family':"Helvetica", 'color':monochrome_colors[0]}, 'pad':{'t':100, 'r':0, 'b':0, 'l':0}},
        font = {'size':18, 'family':'Helvetica', 'color':'#717171'},
        xaxis = {'ticks': "outside",
                'tickfont': {'size': 14, 'family':"Helvetica"},
                'showticksuffix': 'all',
                'showtickprefix': 'last',
                'showline': True,
                'title':{'font':{'size':18, 'family':'Helvetica'}, 'standoff':20},
                'automargin': True
                },
        yaxis = {'ticks': "outside",
                'tickfont': {'size': 14, 'family':"Helvetica"},
                'showticksuffix': 'all',
                'showtickprefix': 'last',
                'title':{'font':{'size':18, 'family':'Helvetica'}, 'standoff':20},
                'showline': True,
                'automargin': True
                },
        legend = {'bgcolor':'rgba(0,0,0,0)',
                'title':{'font':{'size':18, 'family':"Helvetica", 'color':monochrome_colors[0]}},
                'font':{'size':14, 'family':"Helvetica"},
                'yanchor':'bottom'
                },
        colorscale = {'diverging':monochrome_colors},
        coloraxis = {'autocolorscale':True,
                'cauto':True,
                'colorbar':{'tickfont':{'size':14,'family':'Helvetica'}, 'title':{'font':{'size':18, 'family':'Helvetica'}}},
                }
    )
)


def findLargerCategory(s):
    if ('astro-ph' in s) or ('cond-mat' in s) or ('gr-qc' in s) or ('hep-' in s) or ('nlin.' in s) or ('nucl' in s) or ('-ph' in s) or ('math-ph' in s) or ('.' not in s):
        return 'physics'
    
    i = 0
    cat = ''
    while s[i] != '.':
        cat += s[i]
        i += 1
        if i >= len(s):
            print(s)
    if (cat == "q-bio"):
        return "qbio"
    if (cat == "q-fin"):
        return "qfin"
    return cat
    
    
data = pd.read_csv("arxiv_harvard.csv")

# Convert data to pandas dataframe
data = pd.DataFrame(data)

# Select 2 relevant columns
data = np.array(data[['published', 'primary category']])

# Sort data by time
data = data[np.argsort(data[:,0])]

# Retrieve research categories
categories = set(data.transpose()[1].flatten())

for i in range(len(data)):
    data[i][1] = findLargerCategory(data[i][1])
    data[i][0] = int(data[i][0][:4])

histogram_data_5 = []
histogram_data = []
for i in range(len(data)):
    histogram_data_5.append([int((data[i][0] - 1990) / 5), data[i][1]])
    histogram_data.append([data[i][0], data[i][1]])

from sys import exit
yearAll = np.array(data[:,0])
nyears = np.amax(yearAll) - np.amin(yearAll)
categoryAll = np.array(data[:,1],dtype=object)
categoryNames = np.unique(categoryAll)
for category in categoryNames:
    vars()[category+'Freq'] = np.zeros(shape=(nyears))
    for year in range(np.amin(yearAll),np.amax(yearAll)):
        currentCategory = np.array(categoryAll==category)
        currentYear = np.array(yearAll==year)
        for i in range(len(currentCategory)):
            if currentCategory[i]==1 and currentYear[i]==1:
                vars()[category+'Freq'][year-np.amin(yearAll)]+=1


#Harvard Analysis
freq_data = []
for i in range(len(csFreq)):
    freq_data.append(['Computer Science', csFreq[i]/np.sum(csFreq), years[i]])
for i in range(len(mathFreq)):
    freq_data.append(['Math', mathFreq[i]/np.sum(mathFreq), years[i]])
for i in range(len(physicsFreq)):
    freq_data.append(['Physics', physicsFreq[i]/np.sum(physicsFreq), years[i]])
for i in range(len(qbioFreq)):
    freq_data.append(['Quantitative Biology', qbioFreq[i]/np.sum(qbioFreq), years[i]])
# for i in range(len(qfinFreq)):
#     freq_data.append(['Quantitative Finance', qfinFreq[i]/np.sum(qfinFreq), years[i]])
for i in range(len(statFreq)):
    freq_data.append(['Statistics', statFreq[i]/np.sum(statFreq), years[i]])

df_cat = pd.DataFrame(data=freq_data, columns=["Category", "Number of Papers", "Year"])

fig = px.line(df_cat, x="Year", y="Number of Papers", color='Category', title = "Harvard")
fig.show()


#MIT Analysis
freq_data = []
for i in range(len(csFreq)):
    freq_data.append(['Computer Science', csFreq[i]/np.sum(csFreq), years[i]])
for i in range(len(mathFreq)):
    freq_data.append(['Math', mathFreq[i]/np.sum(mathFreq), years[i]])
for i in range(len(physicsFreq)):
    freq_data.append(['Physics', physicsFreq[i]/np.sum(physicsFreq), years[i]])
for i in range(len(qbioFreq)):
    freq_data.append(['Quantitative Biology', qbioFreq[i]/np.sum(qbioFreq), years[i]])
# for i in range(len(qfinFreq)):
#     freq_data.append(['Quantitative Finance', qfinFreq[i]/np.sum(qfinFreq), years[i]])
for i in range(len(statFreq)):
    freq_data.append(['Statistics', statFreq[i]/np.sum(statFreq), years[i]])

df_cat = pd.DataFrame(data=freq_data, columns=["Category", "Number of Papers", "Year"])

fig = px.line(df_cat, x="Year", y="Number of Papers", color='Category', title = "MIT")
fig.show()


# Stanford Analysis
freq_data = []
for i in range(len(csFreq)):
    freq_data.append(['Computer Science', csFreq[i]/np.sum(csFreq), years[i]])
for i in range(len(mathFreq)):
    freq_data.append(['Math', mathFreq[i]/np.sum(mathFreq), years[i]])
for i in range(len(physicsFreq)):
    freq_data.append(['Physics', physicsFreq[i]/np.sum(physicsFreq), years[i]])
for i in range(len(qbioFreq)):
    freq_data.append(['Quantitative Biology', qbioFreq[i]/np.sum(qbioFreq), years[i]])
# for i in range(len(qfinFreq)):
#     freq_data.append(['Quantitative Finance', qfinFreq[i]/np.sum(qfinFreq), years[i]])
for i in range(len(statFreq)):
    freq_data.append(['Statistics', statFreq[i]/np.sum(statFreq), years[i]])

df_cat = pd.DataFrame(data=freq_data, columns=["Category", "Number of Papers", "Year"])

fig = px.line(df_cat, x="Year", y="Number of Papers", color='Category', title = "Stanford")
fig.show()
