import pandas as pd

df = pd.read_excel("support files/censuspopdata.xlsx")
df.groupby("County").agg({"State": "last", "CensusTract": "count", "POP2010": "sum"})

#               State  CensusTract  POP2010
# County
# San Francisco    CA            7    31060