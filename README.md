# Template Dash
## Aperçu

Ce script permet de créer un rapport dash à partir d'un template aux couleurs de B&D.

## Importation du template

```{commandline}
git clone https://github.com/HugoFromont/Dash_Template.git
pip install -r requirements.txt
```

## Explication des différentes partie du template

Voici un aperçut de l'application dash :

<img src = "https://github.com/HugoFromont/Dash_Template/blob/main/doc/apercu_appli.PNG?raw=true">


L'application est composée d'un menu statique à gauche et d'une partie qui contient le contenue de l'application. Cette partie est composée de différentes sections dans lesquelles nous retrouvons des conteneurs qui permettent de stocker différents éléments interactifs.

Les différents éléments de l'application sont paramétrés dans leur propre script :
* le corps de l'application : app.py
* Le menu : contenu/menu.py
* les sections : contenu/section.py

## Le corps de l'application

Le script **app.py** permet d'insérer les différents composants de l'application :
* le menu que nous allons paramétrer dans le script contenu/menu
* les différentes sections que nous allons définir dans la partie contenu/section.py

```{python}
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
```

## Le menu

Le menu est composé d'une première partie qui permet de faire des liens d'ancrage sur les différentes sections et d'une seconde partie pour afficher des filtres dans le menu.
Pour modifier les liens d'ancrage, il est nécessaire de modifier le paramètre href des balises html.A() en renseignant l'id de la section correspondantes précédé de "#".

## les sections

Dans le script **contenu/section.py** vous pouvez définir les différentes sections de votre application.
Voici le script de base pour définir une section composée uniquement d'un titre.

```{python}
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
                        html.H1('Partie 2', id="partie2", className="titre_menu")
                    ])
    return section
```
<img src = "https://github.com/HugoFromont/Dash_Template/blob/main/doc/apercu_section_vide.PNG?raw=true">

Les éléments que vous souhaitez rajouter à votre section sont à placer dans la liste du children après le titre.

Vous pouvez définir et organiser vos propres éléments en utilisant des balises div associé à du CSS dans les sections.
Mais vous pouvez aussi utiliser des conteneurs ayant déjà une mise en forme CSS de défini.
 
## les conteneurs

Vous pouvez utiliser des conteneurs déjà définis pour afficher des éléments dans votre application.
Il existe 3 conteneurs déjà implémenté.

## conteneur_3_infobox

La fonction conteneur_3_infobox permet d'afficher 3 infobox l'un à coté des autres :
!<img src = "https://github.com/HugoFromont/Dash_Template/blob/main/doc/apercu_infobox.PNG?raw=true">

Pour l'utiliser vous avez juste à utiliser la fonction dans une section :
```{python}
conteneur.conteneur_3_infobox(
                images_url=[
                    "https://github.com/HugoFromont/Tweet_Analysis_Application/blob/main/app/img/plus.png?raw=true",
                    "https://github.com/HugoFromont/Tweet_Analysis_Application/blob/main/app/img/moins.png?raw=true",
                    "https://github.com/HugoFromont/Tweet_Analysis_Application/blob/main/app/img/perf.png?raw=true"
                ],
                titres=["VALEUR MAX", "VALEUR MIN", "VALEUR MOYENNE"],
                id_output=["max_value", "min_value", "mean_value"]
            )
```
Vous devez renseigner 3 images à afficher sur chacun de vos infobox, de 3 titres et aussi de 3 valeurs. Les valeurs correspondent à un id d'output de votre callback. De ce fait, la valeur de votre infobox change en fonction de vos filtres.

Il existe le même conteneur avec 2 infobox. Le nom de la fonction est la suivante : **conteneur.conteneur_2_infobox**
!<img src = "https://github.com/HugoFromont/Dash_Template/blob/main/doc/apercu_2_infobox.PNG?raw=true">

## conteneur_1_graph
La fonction conteneur_1_graph permet d'afficher 1 graphique sur toute la largeur de la page.

<img src = "https://github.com/HugoFromont/Dash_Template/blob/main/doc/apercu_1_graph.PNG?raw=true">

Pour l'utiliser, vous avez juste à utiliser la fonction dans une section :
```{python}
conteneur.conteneur_1_graph("graph")
```
Vous devez juste renseigner l'id de l'output de votre graphique ou de votre data table.


## conteneur_2_graph
                     
La fonction conteneur_2_graph permet d'afficher 2 graphiques cote a cote sur toute la largeur de la page.

<img src = "https://github.com/HugoFromont/Dash_Template/blob/main/doc/apercu_2_graph.PNG?raw=true">

Pour l'utiliser, vous avez juste à utiliser la fonction dans une section :
```{python}
conteneur.conteneur_2_graph(["graph1", "graph2"])
```
Vous devez juste renseigner les 2 id des outputs de vos graphiques ou de vos data table.

## Elements interactifs

Pour ajouter des éléments interactifs, vous devez modifier la partie sur les éléments interactifs dans le scripts **app.py** 


# Déploiement

Pour déployer l'application sur une VM, vous devez importer votre application sur la VM.

```{commandline}
git clone your_app
pip install -r requirements.txt
```

Pour la déployer en publique, vous avez juste à changer les dernières lignes du script **app.py** :
```{python}
if __name__ == '__main__':
    app.run_server(debug=False, host='0.0.0.0:8050', port='8050')
```
Vous devez ensuite ouvir le port sur lequel votre application est accessible.
Vous pourez ensuite aller sur le lien : http://adresse_id_externe_VM:8050
