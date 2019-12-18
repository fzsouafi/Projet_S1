 [![License: CC BY-NC-SA 4.0](https://img.shields.io/badge/License-CC%20BY--NC--SA%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-nc-sa/4.0/)
 
 Mon Potager est une application permettant de simuler son potager en insérant les diverses espèces de fruits et légumes,
 et de savoir si les interactions seront favorables ou défavorables. Mon Potager permet également d'obtenir facilement des informations 
sur la façon dont un parasite peut être éliminé par des plants compagnes.

Ce prototype est une amélioration de l'interface web MonPotager pour la rendre participative. L'application initiale est actuellement accessible sur [https://monpotager.org](https://monpotager.org).
 
>### Améliorations apportées
>
>
>-   `Dynamisme de l'interface web` : nous avons apporté des modifications aux fichiers: **Monpotager.html**, **Monpotager.css** et **Monpotager.js**. 
>
>     -Nous avons réussi à ajouter deux boutons. Un pour ajouter des espèces et un autre pour ajouter des interactions. Chaque bouton est relié à un formulaire 
>     permettant la saisie de ces informations. 
>
>     -Une autocompletion est automatique dans la saisie des espèces (dans les deux formulaires). 
>
>     -Correction de certains bugs graphiques ( Masquage par défault de la légende et affichage complet du panel en bas à gauche).
>
>
>-   `Mise en place d'un serveur web FLASK` : l'interface est structurée avec un répertoire template et static pour permettre au serveur Flask de fonctionner. Le serveur permet:
>
>     - de modifier **associations.csv** et **especes_v2.csv**. Les données saisies dans les formulaires sont donc prises en compte.
> 
>     - Une erreur s'affiche quand un problème survient dans l'ajout des espèces ou des interactions.  
>
>
>-    `Modification de la base de données des espèces`: le fichier **especes.csv** a été changé en **espece2v.csv** et enrichi avec :
>
>       -le nom latin
>
>      -le taxId
> 
>      -lien NCBI 
>
>       Ces informations sont trouvées grâce aux fonctions contenues dans **function_search_taxonomy.py**. Quand une espèce est ajoutée, le serveur lance ces fonctions et insère les résultats dans la base de données. 
>
>
>-   `Taxid` : Le taxID est important pour faire le lien entre les espèces.
>
>     Nous avons implémenté une fonction dans le script **function_search_taxonomy.py** qui prend le nom commum de l'espèce et retourne le taxid et le nom scientifique en consultant wikipedia grâce à son API.
>     En consultant les informations de l'espèce au niveau de panel gauche, l'utilisateur a accès au lien du NCBI lié au TaxID.    
>



### Arborescence des fichiers utilisés pour l'amélioration de l'interface


 * [serving_static](./serving_static)
     * [static](./static)
       * [EasterEgg](./static/EasterEgg)
       * [css](./static/css)
         * [bootstrap.css](./css/bootstrap.css)
       * [database](./static/database)
         * [IO.py](./database/Io.py)
         * [associations.csv](./database/associations.csv)
         * [create_db.sql](./database/create_db.sql)
         * [especes.csv](./database/especes.csv)
         * [especes_v2.csv](./database/especes_v2.csv)
         * [import.py](./database/import.py)
         * [sage.csv](./database/sage.csv)
         * [sage.py](./database/sage.py)
         * [script_generate_espece_v2.py](./database/script_generate_espece_v2.py)
       * [fonts](./static/fonts)
       * [images](./static/images)
       * [js](./static/js)
         * [MonPotager.js](./js/MonPotager.js)
         * [bootstrap.js](./js/bootstrap.js)
         * [cookie.js](./js/cookie.js)
         * [d3.js](./js/d3.js)
         * [data.js](./js/data.js)
         * [jets.js](./js/jets.js)
         * [jquery-3.1.1.js](./js/jquery-3.1.1.js)
         * [jquery.scrollTo.js](./js/jquery.scrollTo.js)
       * [MonPotager.css.css](./static/MonPotager.css.css)
       * [MonPotager.html](./static/MonPotager.html)
       * [MonPotager.py](./static/MonPotager.py)
       * [association2json.py](./static/association2json.py)
       * [quelques_bugs.txt](./static/quelques_bugs.txt)
       * [requierements.txt](./static/requirements.txt)
       * [runtime.txt](./static/runtime.txt)
       * [update_csv.sh](./static/update_csv.sh)
     * [templates](./templates)
       * [index.html](./templates/index.html)
     * [function_search_taxonomy.py](./function_search_taxonomy.py)
     * [serve.py](./serve.py)
 * [README.md](./README.md)
 * [DataSets.md](./DataSets.md)
 * [LICENCE.md](./LICENCE.md)
 
**association2json.py** utilise les fichiers **.csv** pour créer le **data.js**.

**MonPotager.html** utilise les informations de **bootstrap.css**, **MonPotager.css** et des scripts contenus dans le répertoire **./js**.

**MonPotager.py** fabrique l'**index.html**  en utilisant **MonPotager.html** et relance à chaque fois fois **association2json.py** pour la prise en compte des mises à jours dans les **.csv**.

Le serveur FLASK exécute à chaque fois **MonPotager.py**.
 
 
# Pour développer MonPotager en local (linux version)


### Installer les dépendances et packages

```
$ git clone http://pedago-service.univ-lyon1.fr:2325/ttesseraud/projetS1.git
$ cd projetS1

```
Voici la liste des packages indispensables à installer pour le fonctionnement de l'interface:
`
$ pip3 install (package)
`
libsass,jsmin,jinja2,Flask, 



### Générer le fichier index.html 
 
```
$ cd serving_static/static/
$ python3 MonPotager.py    # si vous le générez à la main 

$ cd serving_static/       # si vous le générez avec le serveur 
$ python3 serve.py 

```


## License

Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International (CC BY-NC-SA 4.0). Voir [LICENSE.md](https://github.com/ThibaultLatrille/MonPotager/blob/master/LICENSE.md) pour plus d'informations.