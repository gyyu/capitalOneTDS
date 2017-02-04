import pandas as pd
import numpy as np

df = pd.read_csv("first.csv")

bad = df[df["loan_status"] == 1]
bad.to_csv("bad.csv")
