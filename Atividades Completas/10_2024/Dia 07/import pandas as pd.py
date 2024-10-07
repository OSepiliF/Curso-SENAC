import pandas as pd
print(pd.__version__)

df = pd.read_csv('https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv')

print(df.head(500))