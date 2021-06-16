import pandas as pd
import plotly.express as px
df=pd.read_csv("data.csv")
fig = px.scatter(df,x="pouplation",y="per capita",size="Percentage",color="Country")
fig.show()