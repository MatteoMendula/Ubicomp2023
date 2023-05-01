import pickle
import pandas as pd 
import matplotlib.pyplot as plt
import os
import pandas as pd

path='/home/sharon/Documents/Research/Ubicomp_Experiments/github_experiments/Ubicomp2023/results/1-containers/'
dir_list = os.listdir(path)

for file in dir_list:
    #print(file)
    unpickled_df = pd.read_pickle(path+file)

