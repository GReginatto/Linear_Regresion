import pandas as pd
import math
import matplotlib.pyplot as plt
from google.colab import drive
from sklearn.linear_model import LinearRegression
import numpy as np

drive.mount('/content/drive', force_remount=True)



caminho = '/content/Salary.csv'

df = pd.read_csv(caminho)

df.head()

anos = df["YearsExperience"]
salario = df["Salary"]
