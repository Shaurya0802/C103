import pandas as pd
import plotly_express as px

# line chart code
#df = pd.read_csv("line_chart.csv")
#fig = px.line(df, x="Year", y="Per capita income",color="Country",title="Per Capita Income")

# df = pd.read_csv("data.csv")
# fig = px.bar(df, x="Country", y="Internet Users", title="Internet Users")
# fig.show()

df = pd.read_csv("data.csv")
fig = px.scatter(df, x="Population", y="Per capita", size="Percentage", color="Country", size_max=60)
fig.show()