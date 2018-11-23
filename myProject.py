import pandas as pd
pd.set_option('max_columns', 105)
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
# % matplotlib inline
sns.set()

import warnings
warnings.filterwarnings('ignore', category=FutureWarning)
warnings.filterwarnings('ignore', category=DeprecationWarning)

from subprocess import check_output
print(check_output(['ls', '../'])).decode('utf8')

# Project: Predicting purchase dollar amount

dataset = pd.read_csv('BlackFriday.csv')

# print(dataset.describe())
# print(dataset.info())

