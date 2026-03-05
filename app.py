import pandas as pd
import dash
from dash import dcc,html
import plotly.express as px


df=pd.read_csv("data/processed1_data.csv")

df["date"]=pd.to_datetime(df["date"])
df=df.sort_values("date")

fig=px.line(df,x="date",y="sales",
            title="pink morsel sales over time",
            labels={"date":"Date","sales":"Sales"}
)

app=dash.Dash(__name__)

app.layout=html.Div([
    html.H1("Pink Morsel Sales Dashboard"),
    dcc.Graph(id="sales-Chart",
              figure=fig
           )
])

if __name__ == "__main__":
    app.run(debug=True)