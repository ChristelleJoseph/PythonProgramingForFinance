import datetime as dTime
import matplotlib.pyplot
from matplotlib import style
import pandas as pandas
import pandas_datareader.data as web


style.use('ggplot')

start = dTime.datetime(2000,1,1)
end = dTime.datetime(2020,12,31)

dataFrame = web.DataReader('TSLA', 'yahoo', start, end)
print(dataFrame.tail())
