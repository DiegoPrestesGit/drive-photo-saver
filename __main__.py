import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

base_credit = pd.read_csv('./credit_data.csv')

# np.unique(base_credit['default'], return_counts=True)
# sns.countplot(x = base_credit['default'])
# plt.hist(x = base_credit['age'])

graphic = px.scatter_matrix(base_credit, dimensions=['age', 'income', 'loan'])
graphic.show()
# plt.show()
