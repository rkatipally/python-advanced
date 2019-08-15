import pandas as pd
import numpy as np

from numpy.random import randn
np.random.seed(101)
print('A B C D E'.split())
df = pd.DataFrame(randn(5, 4), index='A B C D E'.split(), columns='W, X, Y, Z'.split())

print(df)
