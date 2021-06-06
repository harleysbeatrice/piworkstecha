import pandas as pd
import numpy as np

a = pd.read_csv(r"C:\Users\devec\Desktop\country_vaccination_stats.csv")

i = np.ones(1502,dtype = "a64")
i[:] = np.nan
l = np.ones(1502,dtype = int)

i[:28] = "Argentina"
i[28:48] = "Austria"
i[48:77] = "Bahrain"
i[77:103] = "Belgium"
i[103:113] = "Brazil"
i[113:141] = "Bulgaria"
i[141:184] = "Canada"
i[184:217] = "Chile"
i[217:254] = "China"
i[254:280] = "Costa Rica"
i[280:307] = "Croatia"
i[307:324] = "Cyprus"
i[324:354] = "Czechia"
i[354:384] = "Denmark"
i[384:386] = "Ecuador"
i[386:422] = "England"
i[422:451] = "Estonia"
i[451:477] = "Finland"
i[477:499] = "France"
i[499:528] = "Germany"
i[528:543] = "Gibraltar"
i[543:572] = "Greece"
i[572:600] = "Hungary"
i[600:627] = "Iceland"
i[627:638] = "India"
i[638:652] = "Indonesia"
i[652:677] = "Ireland"
i[677:682] = "Isle of Man"
i[682:720] = "Israel"
i[720:750] = "Italy"
i[750] = "Kuwait"
i[751:780] = "Latvia"
i[780:812] = "Lithuania"
i[812:838] = "Luxembourg"
i[838:866] = "Malta"
i[866:899] = "Mexico"
i[899:916] = "Netherlands"
i[916:959] = "Northern Ireland"
i[959:988] = "Norway"
i[988:1016] = "Oman"
i[1016:1022] = "Panama"
i[1022:1050] = "Poland"
i[1050:1079] = "Portugal"
i[1079:1108] = "Romania"
i[1108:1138] = "Russia"
i[1138:1150] = "Saudi Arabia"
i[1150:1193] = "Scotland"
i[1193:1211] = "Serbia"
i[1211:1226] = "Seychelles"
i[1226:1238] = "Singapore"
i[1238:1256] = "Slovakia"
i[1256:1278] = "Slovenia"
i[1278:1300] = "Spain"
i[1300:1322] = "Sweden"
i[1322:1352] = "Switzerland"
i[1352:1365] = "Turkey"
i[1365:1386] = "United Arab Emirates"
i[1386:1422] = "United Kingdom"
i[1422:1459] = "United States"
i[1459:] = "Wales"

l[0:28] = list(range(1,29))
l[28:48] = list(range(1,21))
l[48:77] = list(range(1,30))
l[77:103] = list(range(1,27))
l[103:113] = list(range(1,11))
l[113:141] = list(range(1,29))
l[141:184] = list(range(1,44))
l[184:217] = list(range(1,34))
l[217:254] = list(range(1,38))
l[254:280] = list(range(1,27))
l[280:307] = list(range(1,28))
l[307:324] = list(range(1,18))
l[324:354] = list(range(1,31))
l[354:384] = list(range(1,31))
l[384:386] = [1,2]
l[386:422] = list(range(1,37))
l[422:451] = list(range(1,30))
l[451:477] = list(range(1,27))
l[477:499] = list(range(1,23))
l[499:528] = list(range(1,30))
l[528:543] = list(range(1,16))
l[543:572] = list(range(1,30))
l[572:600] = list(range(1,29))
l[600:627] = list(range(1,28))
l[627:638] = list(range(1,12))
l[638:652] = list(range(1,15))
l[652:677] = list(range(1,26))
l[677:682] = list(range(1,6))
l[682:720] = list(range(1,39))
l[720:750] = list(range(1,31))
l[750] = 1
l[751:780] = list(range(1,30)) 
l[780:812] = list(range(1,33))
l[812:838] = list(range(1,27))
l[838:866] = list(range(1,29))
l[866:899] = list(range(1,34))
l[899:916] = list(range(1,18))
l[916:959] = list(range(1,44))
l[959:988] = list(range(1,30))
l[988:1016] =list(range(1,29))
l[1016:1022] = list(range(1,7))
l[1022:1050] = list(range(1,29))
l[1050:1079] = list(range(1,30))
l[1079:1108] = list(range(1,30))
l[1108:1138] = list(range(1,31))
l[1138:1150] = list(range(1,13))
l[1150:1193] = list(range(1,44))
l[1193:1211] = list(range(1,19))
l[1211:1226] = list(range(1,16))
l[1226:1238] = list(range(1,13))
l[1238:1256] = list(range(1,19))
l[1256:1278] = list(range(1,23))
l[1278:1300] = list(range(1,23))
l[1300:1322] = list(range(1,23))
l[1322:1352] = list(range(1,31))
l[1352:1365] = list(range(1,14))
l[1365:1386] = list(range(1,22))
l[1386:1422] = list(range(1,37))
l[1422:1459] = list(range(1,38))
l[1459:] = list(range(1,44))

hier_index = list(zip(i.astype("U64"),l))
hier_index = pd.MultiIndex.from_tuples(hier_index)

df = a[["date","daily_vaccinations","vaccines"]]
df.set_index(hier_index, inplace = True)
df.index.names = ["Countries","Data Number"]
country_list = df.index.unique(level = "Countries")
for x in range(0,len(country_list)):
    if np.sum(df.xs(country_list[x])["daily_vaccinations"]) == 0:
        df.xs(country_list[x])["daily_vaccinations"].fillna(value=0,inplace = True)
    df.xs(country_list[x])["daily_vaccinations"].fillna(value=np.min(df.xs(country_list[x])["daily_vaccinations"]),inplace = True)

    
print(np.sum(df[df["date"] == "1/6/2021"]["daily_vaccinations"]))
