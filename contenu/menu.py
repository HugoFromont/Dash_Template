
import dash_html_components as html
import dash_core_components as dcc

def lef_menu():
    """Création du menu gauche du dashboard
    Les differentes classe CSS :
        - "logo" à affecter aux logos ou images du menu
        - "titre1_menu" à affeter aux menu de type 1 du menu
        - "menu_lien_boite" à affceter aux balise LI des élements du menu
        - "menu_lien_text" à affecter aux balise A des éléments du menu
        - "titre_filtre_menu" à affceter aux titres des filtres

    Pour faire le lien vers les differentes sections du dashboard, pensez à modifier le paramètre href des balse A pour quelle renvoit vers l'id des titre de section
    """
    menu = html.Div(
            className="left_menu",
            children=[

                ###### Logo B&D
                html.Img(className="logo", src="https://rh.businessdecision.com/include/bandeauHtml5/img/logo-bd.gif"),

                ###### Menu
                html.H1("Menu", className="titre1_menu"),
                # Lien vers les sections du dashbaord
                html.Ul(
                    className="menu_lien",
                    children=[
                        # Section 1
                        html.Li([
                            html.A(className="menu_lien_text", href="#partie1", children="Partie 1")
                        ],className="menu_lien_boite"),
                        # Section 2
                        html.Li([
                            html.A(className="menu_lien_text", href="#partie2", children="Partie 2")
                        ],className="menu_lien_boite"),
                        # Section 3
                        html.Li([
                            html.A(className="menu_lien_text", href="#partie3", children="Partie 3")
                        ],className="menu_lien_boite")
                    ]
                ),

                ##### Filtres du dashbaord
                html.H1("Filtres", className="titre2_menu"),
                # Filtre 1
                html.H2("Filtre1", className="titre_filtre_menu"),
                dcc.Dropdown(id='select_file',
                             options=[
                                 {'label': "fichier 1", 'value': "file1"},
                                 {'label': "fichier 2", 'value': "file2"}], value='file1'),
                # Filtre 2
                html.H2("Filtre1", className="titre_filtre_menu")
    ])

    return menu