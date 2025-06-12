import numpy as np
import pandas as pd
data = pd.read_excel("missing.xlsx")
cul = ["a", "c", "d"]
data[cul] = data[cul].fillna(data[cul].mean())
print(data)

array_data = data.to_numpy()
np.save("data.npy", array_data)
