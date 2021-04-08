import dash_html_components as html

from contenu import conteneur

def section_1():
    """
    Création d'une section
    Les differentes classe CSS :
        - "titre_section" à affeter au titre de la section

    Pensez à modifier l'id du titre de la section pour qu'il coresponde au paramètre href du menu
    """
    section = html.Section(
        className="section_content",
        children=[
            html.H1('Partie 1', id="partie1", className="titre_menu"),

            html.P("text explicatif ..."),
            conteneur.conteneur_3_infobox(
                images_url=[
                    "https://github.com/HugoFromont/Tweet_Analysis_Application/blob/main/app/img/plus.png?raw=true",
                    "https://github.com/HugoFromont/Tweet_Analysis_Application/blob/main/app/img/moins.png?raw=true",
                    "https://github.com/HugoFromont/Tweet_Analysis_Application/blob/main/app/img/perf.png?raw=true"
                ],
                titres=["VALEUR MAX", "VALEUR MIN", "VALEUR MOYENNE"],
            id_output=["max_value", "min_value", "mean_value"]
            ),
            conteneur.conteneur_1_graph("graph"),
            conteneur.conteneur_2_graph(["graph1", "graph2"]),
            html.P("texte explicatif")
        ])

    return section




def section_2():
    """
    Création d'une section
    Les differentes classe CSS :
        - "titre_section" à affeter au titre de la section

    Pensez à modifier l'id du titre de la section pour qu'il coresponde au paramètre href du menu
    """
    section = html.Section(
                    className="section_content",
                    children=[
                        html.H1('Partie 2', id="partie2", className="titre_menu"),
                        conteneur.conteneur_2_infobox(
                            images_url=[
                                "https://github.com/HugoFromont/Tweet_Analysis_Application/blob/main/app/img/plus.png?raw=true",
                                "https://github.com/HugoFromont/Tweet_Analysis_Application/blob/main/app/img/moins.png?raw=true"
                            ],
                            titres=["VALEUR MAX", "VALEUR MIN"],
                            id_output=["max_value2", "min_value2"]
                        )
                    ])
    return section



def section_3():
    """
    Création d'une section
    Les differentes classe CSS :
        - "titre_section" à affeter au titre de la section

    Pensez à modifier l'id du titre de la section pour qu'il coresponde au paramètre href du menu
    """
    section = html.Section(
        className="section_content",
        children=[
            html.H1('Partie 3', id="partie3", className="titre_menu")
        ])
    return section