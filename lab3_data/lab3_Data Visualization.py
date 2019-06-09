import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.graph_objs as go
import numpy as np

# CSS样式
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# MarkDown说明
markdown_text1 = '''
## Bar Graph For Google Play Store APP
'''
markdown_text2 = '''
## Scatter Graph For Google Play Store APP
'''
markdown_text3 = '''
## Pie Graph For Google Play Store APP
'''

# pandas读取csv文件，utf8格式有问题，选用ISO8859
df = pd.read_csv(
    './dataset/googleplaystore.csv', encoding="ISO-8859-1")

# html页面布局
app.layout = html.Div([
    # 第一个图的说明
    dcc.Markdown(markdown_text1),
    # 图一下拉框
    html.Div([dcc.Dropdown(id='product-selected1',
                                     options=[{'label': i.title(), 'value': i} for i in df.columns.values[2:]],
                                     value="Reviews")],
             className="row", style={"width": "60%", "margin-left": "auto", "margin-right": "auto"}),
    # 图一，条形图
    dcc.Graph(id='test'),
    # 图二说明
    dcc.Markdown(markdown_text2),
    # 图二，散点图
    html.Div([dcc.Graph(
                id='scatter',
                figure={
                    'data': [
                        go.Scatter(
                            x=df['Rating'],
                            y=df['Reviews'],
                            text=df['App'],
                            mode='markers',
                            opacity=0.7,
                            marker=dict(
                                size=16,
                                colorscale='Viridis',
                                color=np.random.randn(500)[np.random.randint(500)],
                            )
                        )
                    ],
                    'layout': go.Layout(
                        xaxis={'title': 'Rating', 'range': [0, 5]},
                        yaxis={'title': 'Reviews'},
                        margin={'l': 40, 'b': 40, 't': 10, 'r': 10},
                        legend={'x': 0, 'y': 1},
                        hovermode='closest'
                    )
                }
            )]),
    # 图三说明
    dcc.Markdown(markdown_text3),
    # 图三下拉框
    html.Div([dcc.Dropdown(id='product-selected2',
             options=[{'label': 'Installs', 'value': 'Installs'},
                        {'label': 'Rating', 'value': 'Rating'},
                        {'label': 'Category', 'value': 'Category'},
                      {'label': 'Type', 'value': 'Type'},
                      {'label': 'Price', 'value': 'Price'},
                      {'label': 'Content Rating', 'value': 'Content Rating'},
                      {'label': 'Genres', 'value': 'Genres'}],
             value="Installs")],
             className="row", style={"width": "60%", "margin-left": "auto", "margin-right": "auto"}),
    # 图三，饼图
    dcc.Graph(id="pie")
])


# 图一的回调函数
@app.callback(
    dash.dependencies.Output('test', 'figure'),
    [dash.dependencies.Input('product-selected1', 'value')])
def update_graph(selected_product1):
    trace = [go.Bar(x=df['App'],
                    y=df[selected_product1],
                    name=selected_product1.title()
                    )]
    return {
        'data': trace,
        'layout': go.Layout(title=f'App in Google Play Store: {selected_product1.title()}',
                            colorway=["#EF963B"],
                            hovermode="closest",
                            xaxis={'title': "App Name", 'titlefont': {'color': 'black', 'size': 14},
                                   'tickfont': {'size': 9, 'color': 'black'}},
                            yaxis={'title': selected_product1.title(), 'titlefont': {'color': 'black', 'size': 14, },
                                   'tickfont': {'color': 'black'}}
                            )
    }


# 图三的回调函数
@app.callback(
    dash.dependencies.Output("pie", "figure"),
    [dash.dependencies.Input("product-selected2", "value")]
)
def update_graph(selected):
    x = []
    for i in df[selected].unique().tolist():
        count = 0
        array = df[selected].values
        for j in array:
            if j == i:
                count += 1
        x.append(count)
    return {
        "data": [go.Pie(labels=df[selected].unique().tolist(), values=x,
                        marker={'colors': ['#EF963B', '#C93277', '#349600', '#EF533B', '#57D4F1']}, textinfo='label',
                        text=[selected], textposition="inside", name=selected, hole=0.4, type="pie")],
        "layout": go.Layout(title=f"Google App Play Store", margin={"l": 300, "r": 300, },
                            legend={"x": 1, "y": 0.7}, annotations=[{"text": selected, "showarrow": False,
                                                                     "font": {
                                                                         "size": 20
                                                                     }, "x": 0.50, "y": 0.5}])}


if __name__ == '__main__':
    app.run_server(debug=True)
