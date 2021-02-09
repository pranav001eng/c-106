import csv
import plotly.express as px
import numpy as np

def plotfigure(data_path):
    with open(data_path) as csv_file:
        df = csv.DictReader(csv_file)
        fig = px.scatter(df ,x = "Days Present" ,y = "Marks In Percentage")
        fig.show()

def getDataSource(data_path):
    Marks_In_Percentage = []
    Days_Present = []
    with open(data_path)as csv_file:
        csv_reader = csv.DictReader(csv_file)
        
        for row in csv_reader:
            Marks_In_Percentage.append(float(row["Marks In Percentage"]))
            Days_Present.append(float(row["Days Present"]))

    return{"x":Marks_In_Percentage,"y":Days_Present}

def findCorelation(data_source):
    corr = np.corrcoef(data_source["x"],data_source["y"])
    print (corr[0,1])

def setup(): 
    data_path = "data1.csv"
    data_source = getDataSource(data_path)
    findCorelation(data_source)
    plotfigure(data_path)

setup()