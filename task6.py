import pandas as pd
import numpy as np

a = pd.read_csv(r"C:\Users\devec\Desktop\P.I. Works Application\country_vaccination_stats.csv")

i = a["country"]
country_list = a["country"].unique()
l = []
in_idx = []
for x in range(0,len(country_list)):
    l.append(list(range(1,len(a[a["country"]==country_list[x]])+1)))
for y in l:
    for j in y:
        in_idx.append(j)

hier_index = list(zip(i,in_idx))
hier_index = pd.MultiIndex.from_tuples(hier_index)

df = a[["date","daily_vaccinations","vaccines"]]
df.set_index(hier_index, inplace = True)
df.index.names = ["Countries","Data Number"]

for x in range(0,len(country_list)):
    if np.sum(df.xs(country_list[x])["daily_vaccinations"]) == 0:
        df.xs(country_list[x])["daily_vaccinations"].fillna(value=0,inplace = True)
    df.xs(country_list[x])["daily_vaccinations"].fillna(value=np.min(df.xs(country_list[x])["daily_vaccinations"]),inplace = True)
    
print(np.sum(df[df["date"] == "1/6/2021"]["daily_vaccinations"]))
