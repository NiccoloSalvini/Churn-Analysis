import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import dash_table

import base64
import datetime
import io
import pandas as pd

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

colors = {
    'background': '#ffffff',
    'text': '#7FDBFF',
    'text1': '#FA1414'
}

app.layout = html.Div(style={'backgroundColor': colors['background']}, children=[
    html.H2(
        children='Churn Analysis',
        style={
            'textAlign': 'center',
            'color': colors['text']
        }
    ),

    html.Div(children='An interactive Dashboard Designed to Explore',
             style={
                 'textAlign': 'center',
                 'color': colors['text']
             }),

    dcc.Upload(
        id='upload-data',
        children=html.Div([
            'Drag and Drop or ',
            html.A('Select Files')
        ]),
        style={
            'width': '100%',
            'height': '60px',
            'lineHeight': '60px',
            'borderWidth': '1px',
            'borderStyle': 'dashed',
            'borderRadius': '5px',
            'textAlign': 'center',
            'margin': '10px'
        },
        # Allow multiple files to be uploaded
        multiple=True
    ),
    html.Div(id='output-data-upload'),

    html.H2(
        children='Fill In the blanks gievn the customer chars and see if He will be back or NOT',
        style={'textAlign': 'center'
               },
    ),



    html.H2(
        children='PARTE 1: CATEGORICAL VARIABLES',
        style={'textAlign': 'center',
               'color': colors['text']
               },
    ),
    html.H3(
        children='Ricevute ed altri avvisi di pagamento non onorate alla scadenza',
        style={
            'textAlign': 'center'
        }
    ),
    dcc.RadioItems(
        id='question 1',
        options=[
            {'label': 'Sì', 'value': 'NYC'},
            {'label': 'No', 'value': 'MTL'}
        ],
        value='MTL',
        labelStyle={'display': 'inline-block'},
        style={
            'textAlign': 'center'
        }
    ),
    html.H3(
        children='Ritardi nei pagamenti concordati superiori a 90 giorni',
        style={
            'textAlign': 'center'
        }
    ),
    dcc.RadioItems(
        id='question 2',
        options=[
            {'label': 'Sì', 'value': 'NYC'},
            {'label': 'No', 'value': 'MTL'}
        ],
        value='MTL',
        labelStyle={'display': 'inline-block'},
        style={
            'textAlign': 'center'
        }
    ),
    html.H3(
        children='Pagamenti Parziali rispetto al prezzo concordarto',
        style={
            'textAlign': 'center'
        }
    ),
    dcc.RadioItems(
        id='question 3',
        options=[
            {'label': 'Sì', 'value': 'NYC'},
            {'label': 'No', 'value': 'MTL'}
        ],
        value='MTL',
        labelStyle={'display': 'inline-block'},
        style={
            'textAlign': 'center'
        }
    ),
    html.H3(
        children='Richieste di riscadenzamento nei pagamenti concordati',
        style={
            'textAlign': 'center'
        }
    ),
    dcc.RadioItems(
        id='question 4',
        options=[
            {'label': 'Sì', 'value': 'NYC'},
            {'label': 'No', 'value': 'MTL'}
        ],
        value='MTL',
        labelStyle={'display': 'inline-block'},
        style={
            'textAlign': 'center'
        }
    ),
    html.H3(
        children='Compensazioni, abbuoni derivanti da resi, controversi derivanri dalla quantità del prodotto o da ritardi',
        style={
            'textAlign': 'center'
        }
    ),
    dcc.RadioItems(
        id='question 5',
        options=[
            {'label': 'Sì', 'value': 'NYC'},
            {'label': 'No', 'value': 'MTL'}
        ],
        value='MTL',
        labelStyle={'display': 'inline-block'},
        style={
            'textAlign': 'center'
        }
    ),
    html.H3(
        children='Sconti o promozioni di ogni tipi in misura superiore al 50%del prezzo di listino considerati anomali',
        style={
            'textAlign': 'center'
        }
    ),
    dcc.RadioItems(
        id='question 6',
        options=[
            {'label': 'Sì', 'value': 'NYC'},
            {'label': 'No', 'value': 'MTL'}
        ],
        value='MTL',
        labelStyle={'display': 'inline-block'},
        style={
            'textAlign': 'center'
        }
    ),
    html.H3(
        children='sensibile aumento della dilazione concessa ai clienti',
        style={
            'textAlign': 'center'
        }
    ),
    dcc.RadioItems(
        id='question 7',
        options=[
            {'label': 'Sì', 'value': 'NYC'},
            {'label': 'No', 'value': 'MTL'}
        ],
        value='MTL',
        labelStyle={'display': 'inline-block'},
        style={
            'textAlign': 'center'
        }
    ),
    html.H3(
        children='sensibile diminuziione della dilazione concessa ai fornitori ',
        style={
            'textAlign': 'center'
        }
    ),
    dcc.RadioItems(
        id='question 8',
        options=[
            {'label': 'Sì', 'value': 'NYC'},
            {'label': 'No', 'value': 'MTL'}
        ],
        value='MTL',
        labelStyle={'display': 'inline-block'},
        style={
            'textAlign': 'center'
        }
    ),
    html.H3(
        children='esistenza di procedure conocorsuali a carico di clienti chiave',
        style={
            'textAlign': 'center'
        }
    ),
    dcc.RadioItems(
        id='question 9',
        options=[
            {'label': 'Sì', 'value': 'NYC'},
            {'label': 'No', 'value': 'MTL'}
        ],
        value='MTL',
        labelStyle={'display': 'inline-block'},
        style={
            'textAlign': 'center'
        }
    ),
    html.H3(
        children='esistenza di procedure conocorsuali a carico di fornitori chiave',
        style={
            'textAlign': 'center'
        }
    ),
    dcc.RadioItems(
        id='question 10',
        options=[
            {'label': 'Sì', 'value': 'NYC'},
            {'label': 'No', 'value': 'MTL'}
        ],
        value='MTL',
        labelStyle={'display': 'inline-block'},
        style={
            'textAlign': 'center'
        }
    ),
    html.H2(
        children='PARTE 2: ANOMALIE NEI RAPPORTI CON ALTRI SOGGETTI FINANZIARI',
        style={'textAlign': 'center',
               'color': colors['text']
               }
    ),
    html.H3(
        children='significativo e concordante deterioramento dei ratign interni asseganti dalle banche ',
        style={
            'textAlign': 'center'
        }
    ),
    dcc.RadioItems(
        id='question 11',
        options=[
            {'label': 'Sì', 'value': 'NYC'},
            {'label': 'No', 'value': 'MTL'}
        ],
        value='MTL',
        labelStyle={'display': 'inline-block'},
        style={
            'textAlign': 'center'
        }
    ),
    html.H3(
        children='sconfini rilevanti  e ripetuti inc eentrale dei rischi (nell\'arco din 12 mesi',
        style={
            'textAlign': 'center'
        }
    ),
    dcc.RadioItems(
        id='question 12',
        options=[
            {'label': 'Sì', 'value': 'NYC'},
            {'label': 'No', 'value': 'MTL'}
        ],
        value='MTL',
        labelStyle={'display': 'inline-block'},
        style={
            'textAlign': 'center'
        }
    ),
    html.H3(
        children='anomale aumento delle richeiste di garanzie su beni aziendali o di soggetti terzi',
        style={
            'textAlign': 'center'
        }
    ),
    dcc.RadioItems(
        id='question 13',
        options=[
            {'label': 'Sì', 'value': 'NYC'},
            {'label': 'No', 'value': 'MTL'}
        ],
        value='MTL',
        labelStyle={'display': 'inline-block'},
        style={
            'textAlign': 'center'
        }
    ),
html.H3(
        children='anomale aumento delle segnalazioni in CR di insoluti su anticipo crediti',
        style={
            'textAlign': 'center'
        }
    ),
    dcc.RadioItems(
        id='question 14',
        options=[
            {'label': 'Sì', 'value': 'NYC'},
            {'label': 'No', 'value': 'MTL'}
        ],
        value='MTL',
        labelStyle={'display': 'inline-block'},
        style={
            'textAlign': 'center'
        }
    ),
html.H3(
        children='anomale richieste di fido oltre gli ordinari fabbisogni di cassa attesi',
        style={
            'textAlign': 'center'
        }
    ),
    dcc.RadioItems(
        id='question 15',
        options=[
            {'label': 'Sì', 'value': 'NYC'},
            {'label': 'No', 'value': 'MTL'}
        ],
        value='MTL',
        labelStyle={'display': 'inline-block'},
        style={
            'textAlign': 'center'
        }
    ),
html.H3(
        children='anomala e continuativa crescite di fidi utilizzati  sovrautilizzo dei fidi di smobilizzo crediti commerciali',
        style={
            'textAlign': 'center'
        }
    ),
    dcc.RadioItems(
        id='question 16',
        options=[
            {'label': 'Sì', 'value': 'NYC'},
            {'label': 'No', 'value': 'MTL'}
        ],
        value='MTL',
        labelStyle={'display': 'inline-block'},
        style={
            'textAlign': 'center'
        }
    ),
html.H3(
        children='rientri nelle linee di credito per cassa ',
        style={
            'textAlign': 'center'
        }
    ),
    dcc.RadioItems(
        id='question 17',
        options=[
            {'label': 'Sì', 'value': 'NYC'},
            {'label': 'No', 'value': 'MTL'}
        ],
        value='MTL',
        labelStyle={'display': 'inline-block'},
        style={
            'textAlign': 'center'
        }
    ),
html.H3(
        children='anomale aumento delle richeiste di garanzie su beni aziendali o di soggetti terzi',
        style={
            'textAlign': 'center'
        }
    ),
    dcc.RadioItems(
        id='question 18',
        options=[
            {'label': 'Sì', 'value': 'NYC'},
            {'label': 'No', 'value': 'MTL'}
        ],
        value='MTL',
        labelStyle={'display': 'inline-block'},
        style={
            'textAlign': 'center'
        }
    ),
html.H3(
        children='anomale aumento delle richeiste di garanzie su beni aziendali o di soggetti terzi',
        style={
            'textAlign': 'center'
        }
    ),
    dcc.RadioItems(
        id='question 19',
        options=[
            {'label': 'Sì', 'value': 'NYC'},
            {'label': 'No', 'value': 'MTL'}
        ],
        value='MTL',
        labelStyle={'display': 'inline-block'},
        style={
            'textAlign': 'center'
        }
    ),
html.H3(
        children='anomale aumento delle richeiste di garanzie su beni aziendali o di soggetti terzi',
        style={
            'textAlign': 'center'
        }
    ),
    dcc.RadioItems(
        id='question 20',
        options=[
            {'label': 'Sì', 'value': 'NYC'},
            {'label': 'No', 'value': 'MTL'}
        ],
        value='MTL',
        labelStyle={'display': 'inline-block'},
        style={
            'textAlign': 'center'
        }
    ),
html.H3(
        children='anomale aumento delle richeiste di garanzie su beni aziendali o di soggetti terzi',
        style={
            'textAlign': 'center'
        }
    ),
    dcc.RadioItems(
        id='question 21',
        options=[
            {'label': 'Sì', 'value': 'NYC'},
            {'label': 'No', 'value': 'MTL'}
        ],
        value='MTL',
        labelStyle={'display': 'inline-block'},
        style={
            'textAlign': 'center'
        }
    ),
html.H3(
        children='anomale aumento delle richeiste di garanzie su beni aziendali o di soggetti terzi',
        style={
            'textAlign': 'center'
        }
    ),
    dcc.RadioItems(
        id='question 22',
        options=[
            {'label': 'Sì', 'value': 'NYC'},
            {'label': 'No', 'value': 'MTL'}
        ],
        value='MTL',
        labelStyle={'display': 'inline-block'},
        style={
            'textAlign': 'center'
        }
    ),


    dcc.Graph(
        id='example-graph-2',
        figure={
            'data': [
                {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'SF'},
                {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': 'Montréal'},
            ],
            'layout': {
                'plot_bgcolor': colors['text'],
                'paper_bgcolor': colors['background'],
                'font': {
                    'color': colors['text']
                }
            }
        }
    )

])


def parse_contents(contents, filename, date):
    global df
    content_type, content_string = contents.split(',')

    decoded = base64.b64decode(content_string)
    try:
        if 'csv' in filename:
            # Assume that the user uploaded a CSV file
            df = pd.read_csv(
                io.StringIO(decoded.decode('utf-8')))
        elif 'xls' in filename:
            # Assume that the user uploaded an excel file
            df = pd.read_excel(io.BytesIO(decoded))
    except Exception as e:
        print(e)
        return html.Div([
            'There was an error processing this file.'
        ])

    return html.Div([
        html.H5(filename),
        html.H6(datetime.datetime.fromtimestamp(date)),

        dash_table.DataTable(
            style_data={
                'whiteSpace': 'normal',
                'height': 'auto'
            },
            style_cell={
                'height': 'auto',
                'minWidth': '0px', 'maxWidth': '180px',
                'whiteSpace': 'normal'
            },

            data=df.to_dict('records'),
            columns=[{'name': i, 'id': i} for i in df.columns],
            fixed_rows={'headers': True, 'data': 0},

        ),

        html.Hr(),  # horizontal line

        # For debugging, display the raw contents provided by the web browser
        html.Div('Raw Content'),
        html.Pre(contents[0:200] + '...', style={
            'whiteSpace': 'pre-wrap',
            'wordBreak': 'break-all'
        })
    ])


@app.callback(Output('output-data-upload', 'children'),
              [Input('upload-data', 'contents')],
              [State('upload-data', 'filename'),
               State('upload-data', 'last_modified')])
def update_output(list_of_contents, list_of_names, list_of_dates):
    if list_of_contents is not None:
        children = [
            parse_contents(c, n, d) for c, n, d in
            zip(list_of_contents, list_of_names, list_of_dates)]
        return children


if __name__ == '__main__':
    app.run_server(debug=False)
