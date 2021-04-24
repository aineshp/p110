import statistics
import random
import csv
import pandas as pd
import plotly_express as px
import plotly.figure_factory as ff
import plotly.graph_objects as go
data1=pd.read_csv('medium_data.csv')
responses=data1['responses'].tolist()
def randommean(counter):
    dataset=[]
    for i in range(0,counter):
        randomindex=random.randint(0,len(responses))
        value=responses[randomindex]
        dataset.append(value)
        mean=statistics.mean(dataset)
        print(mean)
        return mean 
def setup():
    meanlist=[]
    for i in range(0,100):
        setofmeans=randommean(30)
        meanlist.append(setofmeans)
    show_fig(meanlist)
def show_fig(meanlist):
    df=meanlist
    fig1=ff.create_distplot([df],['Responses'],show_hist=False)
    fig1.show()       
randommean()
setup()
show_fig()
