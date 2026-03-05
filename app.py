import pandas as pd
import dash
from dash import dcc,html
from dash.dependencies import Input,Output
import plotly.express as px


df=pd.read_csv("data/processed1_data.csv")

df["date"]=pd.to_datetime(df["date"])
df=df.sort_values("date")


app=dash.Dash(__name__)

app.layout=html.Div([
    html.H1("Pink Morsel Sales Dashboard",style={"textAlign":"center"}),
    html.Label("select Region:"),
    dcc.RadioItems(id="region-filter",
                   options=[
                       {"label":"All","value":"all"},
                       {"label":"North","value":"north"},
                       {"label":"South","value":"south"},
                       {"label":"East","value":"east"},
                       {"label":"West","value":"west"}
                   ],
                   value="all",
                   inline=True
                   ),
    dcc.Graph(id="sales-chart")
])

@app.callback(
    Output("sales-chart","figure"),
    Input("region-filter","value")
)

def update_chart(selected_region):
    if selected_region =="all":
        filtered_df=df
    else:
        filtered_df=df[df["region"]==selected_region]

    sales_data =filtered_df.groupby("date")["sales"].sum().reset_index()
    fig=px.line(df,x="date",y="sales",
            title="pink morsel sales over time",
          
            labels={"date":"Date","sales":"Sales"}
    )
    return fig
if __name__ == "__main__":
    app.run(debug=True)