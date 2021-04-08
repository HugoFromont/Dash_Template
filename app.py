# -*- coding: utf-8 -*-

from dash import Dash
import dash_html_components as html
from dash.dependencies import Input, Output

import plotly.express as px


from contenu import menu
from contenu import section

from interaction import data_process



#################### Création de l'application ####################
app = Dash(
    __name__,
    assets_folder= 'assets/'
)


#################### Design de l'application ####################
app.layout = html.Div(
    className="body_app",
    children=[

        # Menu du dashboard
        menu.lef_menu(),

        # Contenu du dashboard
        html.Div(
            className="right_content",
            children=[
                html.Header([html.H1("Titre Dashboard", className="titre_dashboard")], className="block_titre_dashboard"),
                section.section_1(),
                section.section_2(),
                section.section_3()
            ]
        )
    ])



#################### Elements interactifs ####################

@app.callback(
    [Output('max_value', 'children'),
     Output('min_value', 'children'),
     Output('mean_value', 'children'),
     Output('graph', 'figure'),
     Output('graph1', 'figure'),
     Output('graph2', 'figure')
     ],
    [Input('select_file', 'value')]
)
def affiche_max_value(file):
    df = data_process.create_dataset(file)
    fig = px.line(df, x="var1", y="var2", title="TITRE GRAPHIQUE")
    fig.update_traces(line_color='#df6036')
    fig.update_layout(
        xaxis=dict(showline=False, showticklabels=True,
                   tickfont=dict(family='Arial', size=12, color='rgb(25, 29, 63)')),
        yaxis=dict(showline=False, showticklabels=True,
                   tickfont=dict(family='Arial', size=12, color='rgb(25, 29, 63)')),
        autosize=False, showlegend=False, paper_bgcolor='rgba(255,255,255,255)', plot_bgcolor='rgba(255,255,255,255)', title_x=0.5,
        xaxis_showgrid=False, yaxis_showgrid=False
    )
    fig1 = fig
    fig2 = fig
    return df.var2.max(), df.var2.min(), df.var2.mean(), fig, fig1, fig2


#################### Lancement de l'application ####################

if __name__ == '__main__':
    # Déploiement en privé
    app.run_server(debug=True)

    # Déploiement en public
    #app.run_server(debug=False, host='0.0.0.0', port='8050')