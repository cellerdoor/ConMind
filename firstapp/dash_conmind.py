import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd
import numpy as np
import plotly.graph_objs as go



level1=[1,2,3,3,4.1,3.9,4.05,3.88]
level2=[0,0.0,.1,-.1,.125,.075,-.125,-.075]
colour_tags = ['Full','Full','Full','Full','Half','Full','Half','Full']

toc = [122323,112739,50323,45908,13404,23545,23024,34234]

df = pd.read_pickle("../notebooks/main.pkl")

fig = px.scatter(df, x="Education", y="City", size="Clicks", color="PurchasePower",
           hover_name="User", log_x=True, size_max=30)


fig.update_layout(
    xaxis_title="",
    yaxis_title="",
    margin=dict(l=1, r=1, t=1, b=1),
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    xaxis=dict(
        autorange=True,
        showgrid=False,
        ticks='',
        showticklabels=False,
    ),
    yaxis=dict(
        autorange=True,
        showgrid=False,
        ticks='',
        showticklabels=False
    ),
)


data = [# Portfolio (inner donut)
        go.Pie(values=[60],
               labels=['Total clicks'],
               domain={'x':[0.2,0.8], 'y':[0.1,0.9]},
               hole=0.6,
               direction='clockwise',
               sort=False,
               marker={'colors':['#1f77b4']}),
        go.Pie(values=[60],
               labels=['Total clicks'],
               domain={'x':[0.2,0.8], 'y':[0.1,0.9]},
               hole=0.65,
               direction='clockwise',
               sort=False,
               marker={'colors':['white']}),
    # Portfolio (inner donut)
        go.Pie(values=[20,40],
               labels=['1 click','Multi click'],
               domain={'x':[0.2,0.8], 'y':[0.1,0.9]},
               hole=0.70,
               direction='clockwise',
               sort=False,
               marker={'colors':['#ffa07a','#ff8072']}),
        # Individual components (outer donut)
        go.Pie(values=[5,15,30,10],
               labels=['Purchase','Experience','Purchase','Experience'],
               domain={'x':[0.1,0.9], 'y':[0,1]},
               hole=0.80,
               direction='clockwise',
               sort=False,
               marker={'colors':['lightseagreen','darkcyan','darkseagreen','darkseagreen']},
               showlegend=False)]
fig1 = go.Figure(data=data)
fig1.update_layout(
    showlegend=False,
    autosize=False,
    width=300,
    margin=dict(l=1, r=1, t=1, b=1),
    height=300,
    title={
        'text': "Clicks",
        'y':0.5,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top'},
)

data = [# Portfolio (inner donut)
        go.Pie(values=[60,10],
               labels=['Data Available','Not Available'],
               domain={'x':[0.2,0.8], 'y':[0.1,0.9]},
               hole=0.80,
               direction='clockwise',
               sort=False,
               marker={'colors':['lightseagreen','darkcyan']}),
        ]
pie2 = go.Figure(data=data)
pie2.update_layout(
    showlegend=False,
    autosize=False,
    width=250,
    height=250,
    margin=dict(l=1, r=1, t=1, b=1),
    title={
        'text': "Purchases",
        'y':0.5,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top'},
)

data = [# Portfolio (inner donut)
        go.Pie(values=[60,10],
               labels=['Data Available','Not Available'],
               domain={'x':[0.2,0.8], 'y':[0.1,0.9]},
               hole=0.75,
               direction='clockwise',
               sort=False,
               marker={'colors':['lightseagreen','darkcyan']}),
        ]
pie3 = go.Figure(data=data)
pie3.update_layout(
    showlegend=False,
    autosize=False,
    width=150,
    height=150,
    margin=dict(l=1, r=1, t=1, b=1),
    title={
        'text': "Users",
        'y':0.5,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top'},
)




df_trail = pd.read_pickle("../notebooks/trial_df.pkl")
df_trail['E'] = df_trail['E'].astype(str)

fig_3d = px.scatter_3d(df_trail, x='A', y='B', z='C',color='E',opacity=0.3)


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__)
colors = {
    'background': '#ffffff',
    'text': '#7FDBFF'
}


app.layout = html.Div(style={'backgroundColor': colors['background']},children=[
    html.H1(children='Consumer Mindset analytics',style={
            'textAlign': 'center',
###            'color': colors['text']
    }),
#    html.Div(class = "box")

    html.Div([
        html.P('ConMind is a market segmentation tool for retail businesses that uses machine learning techniques on clickstream data to segregate online consumers as goal oriented versus experiential shoppers. It allows businesses to create adaptive web design tailored to increase shopper retention and reduce cart abandonment.'),
    ],style={
        'textAlign': 'center','width': '750px',
    }),
   
    html.Div(children=[
        dcc.Graph(
            style ={
                'height':450,
                'width':800
            },
            id='example-graph',
            figure=fig,
            config={
		'displayModeBar':False,
            }
        ),
    ], style={'backgroundColor': colors['background'],'width': '60%', 'display': 'inline-block', 'vertical-align': 'top'}),

    html.Div([
        html.P('This is a novel ML-based real-time customer segmentation tool for online retailers.  There are several customer segmentation tools out there, but traditionally, they rely on demographic or geographic differences, rather than differentiating consumers based on their distinct behavioral shopping attitudes. My tool segments customers who are visiting the website into two distinct types recognized by marketing practitioners: goal-oriented versus experiential shoppers.  Goal-oriented shoppers "desire to purchase what they want quickly and without distraction", whereas experiential customers are "foragers, tend to spend more time, and browse a larger variety of items".'),
    ],style={'position':'absolute','top':'65%','left':'2%','width':'750px' }),


    html.Div([
        html.P('Real-time click stream data of each individual shopper is observed and translated into a directed click stream network. Then, we extract carefully designed network features, grounded in complex network and graph theory. These network metrics then act as signatures that characterize the two distinct types of shoppers allowing us to adopt an unsupervised learning approach. We cluster using a mixture model that has been trained on a novel proprietary dataset from JD.com, Chinas largest e-retailer, comprising click stream data of over 2.5 million customers and 31,868 SKUs. '),
    ],style={'position':'absolute','top':'10%','left':'52%','width':'750px' }),

    

    html.Div([
        dcc.Graph(
            style ={
                'height':300,
                'width':300
            },
            id='pie1',
            figure=fig1,
            config= {'displayModeBar':False,
            }
        ),

         html.P('The tool identifies shoppers visiting the website as goal-oriented or experiential. This can be leveraged for adaptive web design that is tailored to increase shopper retention and reduce cart abandonment. Web design should be personalized based on whether a consumer is identified as goal-oriented or experiential. Goal-oriented consumers value ease and speed of purchase. Hence, the web interface should emphasize elements such as "one-click buying" to reduce cart abandonment. Experiential shoppers, on the other hand, should be targeted with interfaces that are designed for recommendations and "stickiness”, that aim to keep visitors on the site for as long as possible, to increase sales opportunities. This is why I view my tool as a simple and effective revenue driver. '),

        

        dcc.Graph(
            style ={
                'height':700,
                'width':700
            },
            id='new',
            figure=fig_3d,
            config= {'displayModeBar':False,
            }
        ),
    ], style={'position':'absolute','top':'30%','left':'52%','width':'750px' }),

    html.Div([
   
        dcc.Graph(
            id='pie2',
            style= {
                'height':200,
                'width':200
            },            
            figure=pie2,
            config= {'displayModeBar':False,
            }
        ),
        dcc.Graph(
            id='pie3',
            style= {
                'height':200,
                'width':200
            },            
            figure=pie3,
            config= {'displayModeBar':False,
            }
        ),
    ],style={'position':'absolute','top':'25%','left':'72%','width':'350px' }),

    
    

])

if __name__ == '__main__':
    app.run_server(debug=True)
