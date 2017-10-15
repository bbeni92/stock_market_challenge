'''
Created on Oct 10, 2017

@author: beni
'''
import numpy
import matplotlib.pyplot as plt
from datetime import datetime
from pandas import read_csv
from pandas import to_datetime
import math
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_squared_error
from tensorflow.contrib.learn.python.learn.graph_actions import train

# load the train data
dataframe = read_csv('dataset/train.csv',
                     usecols=[0,1,2,3,4,5,6,7,8,9,10,11], 
                     parse_dates=[0],
                     infer_datetime_format=True,
                     engine='python', 
                     header=0)
trainData = dataframe.values
# load the test data
dataframe = read_csv('dataset/test_2.csv',
                     usecols=[0,1,2,3,4,5,6,7,8,9,10,11], 
                     parse_dates=[0],
                     infer_datetime_format=True,
                     engine='python', 
                     header=0)
testData = dataframe.values

print trainData;