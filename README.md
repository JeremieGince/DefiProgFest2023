# DefiProgFest2023

Dans l'objectif de mettre en pratique les connaissances acquises lors du ProgFest 2023, nous vous proposons 
d'effectuer un projet pouvant être réalisé en équipe. Nous recommandons des équipes de 2 à 4 personnes. Le projet 
consiste à résoudre
un problème à plusieurs échelles de difficultés, tout en collaborant avec vos coéquipiers et en utilisant de 
bonnes pratiques de programmation. Le défi sera de faire atterrir un Lunar Lander à l'aide d'un
programme Python. Le simulateur de l'engin spatial que vous utiliserez sera le populaire LunarLander-v2 de Gym.

Si vous ne connaissez pas déjà Gym, vous pouvez vous familiariser avec l'environnement avec 
l'[exemple d'utilisation de l'environnement](https://github.com/JeremieGince/DefiProgFest2023/blob/main/Gym-Tutorial.ipynb).
N'ayant pas de restriction sur le modèle de prédiction d'actions à utiliser, vous pouvez comprendre qu'il existe 
énormément de solutions possibles à un tel problème. C'est pourquoi nous allons diviser les solutions en deux classes
distinctes:

- Solutions basées sur des algorithmes d'apprentissage par renforcement (Q-Learning, SARSA, DQN, etc.)
- Solutions basées sur des algorithmes de contrôle (PID, MPC, etc.)

Si vous n'avez aucune idée de ce que sont ces algorithmes, ce n'est pas grave. Vous n'avez qu'à essayer de résoudre
le problème avec vos aptitudes de physicien et ingénieur et nous allons prendre la responsabilité de classifier votre
solution selon l'explication que vous nous fournirez.

## But du défi
Le but du défi est de faire atterrir un Lunar Lander sur une plateforme de manière sécuritaire. Ce problème a lieu dans 
un simulateur 2D permettant d'appliquer différentes contraintes et ainsi tester vos algorithmes dans plusieurs 
environnements. Pour accomplir la tâche, vous devez faire un programme Python qui prend en entrée les observations de 
l'environnement et qui produit en sortie les actions à effectuer. Pour ce faire, votre lander est composé de deux 
moteurs (central et latéral), d'un détecteur pour la position du lander, d'un détecteur pour sa vitesse, 
d'un détecteur de sa rotation, d'un détecteur de sa vitesse angulaire et d'un détecteur sur chaque pied pour savoir si 
celui-ci touche à terre. Votre programme aura donc accès à ces détecteurs et devra utiliser ces informations pour 
transmettre différentes actions (voir la section `Actions`) au lander pour le faire atterrir de façon sécuritaire. 
Finalement, 5 échelons de difficultés seront disponibles pour vous permettre de tester votre programme. Bien qu'il 
ne soit pas obligatoire de réussir tous les échelons, il est fortement recommandé d'essayer différents échelons afin
de s'assurer de la généralisation de votre programme (et obtenir un maximum de point lors de l'évaluation).


## Installer gym
| OS | Commande                 |
| --- |--------------------------|
| Windows | `pip install gym[box2d]` |
| MacOS | `pip install gym\[box2d\]` |
| Linux | `pip install gym\[box2d\]` |


## À faire
Vous avez à implémenter votre propre agent dans la classe `LunarLanderAgent` du fichier 
[lunar_lander_agent.py](lunar_lander_agent.py) et implémenter sa méthode 
`get_action(observation: np.ndarray) -> Union[int, np.ndarray]`.


## Critères d'évaluation
- Cumulative Rewards (somme des récompenses obtenues durant un épisode): 50%
- Explication de la solution : 30%
- Qualité du code : 10%
- Utilisation d'environnement virtuel (venv): 5%
- Utilisation de Git : 5%

Les cumulative rewards seront calculé à l'aide de l'objet `LunarLanderPerformanceTest` fournit dans le fichier 
[tester.py](tools/tester.py). Vous aurez donc à implémenter votre propre agent dans la classe 
`LunarLanderAgent` du fichier [lunar_lander_agent.py](lunar_lander_agent.py) et implémenter sa méthode 
`get_action(observation: np.ndarray) -> Union[int, np.ndarray]` afin que 
nous puissions rouler les mêmes tests de performances que vous. Si l'interface n'est pas respecté (le type de sortie de 
la méthode `get_action`, le nom de l'objet) ou si le code rouler avec un/des erreur(s), la performance de votre code 
sera malheureusement égal à zéro. Dans ce cas, assurez-vous de bien respecter l'interface et de rouler les tests afin
de vous assurez de ne pas avoir de problème lors de la correction. Le score utilisé pour l'évaluation sera:
```
score = clip(mean_cumulative_rewards/200, 0.0, 1.0) * 100 [%]
```
où `mean_cumulative_rewards` est la moyenne des cumulative rewards obtenues sur les 100 épisodes de test.

L'explication de la solution devra être contenue dans le fichier `README.md` de votre projet qui explique la solution 
que vous avez utilisé pour résoudre le problème. Cette explication sert essentiellement à nous permettre de savoir si
vous comprenez vraiment ce que vous avez fait ou si vous avez juste volé du code sur internet. Veuillez tout de même 
rester concis dans vos explications.

La qualité du code sera évalué à l'aide de l'outil [pycodestyle](https://pycodestyle.pycqa.org/en/latest/intro.html). 
Si votre code ne respecte pas les normes de [PEP8](https://peps.python.org/pep-0008/), vous perdrez des points. 

Afin de voir votre résultat sur les différents critères/échelons , vous pouvez lancer le script `main.py` qui va 
rouler les tests et vous afficher vos résultats.


## Actions
Dans le cas d'un "Action Space" discrète, les actions possibles sont :
- Ne rien faire (`0`)
- Activer le moteur de droite (`1`)
- Activer le moteur central (`2`)
- Activer le moteur de gauche (`3`)

Dans le cas d'un "Action Space" continu, les actions sont des vecteurs de 2 valeurs avec les entrées suivantes :
- Moteur principal (intervalle `[-1, 1]`)
- Moteur latéral (intervalle `[-1, 1]`)


## Observations
Dans le cas d'un "Observation Space" de type `Box`, les observations possibles sont :
- Position horizontale (intervalle `[-1.5, 1.5]`)
- Position verticale (intervalle `[1.5, -1.5]`)
- Vitesse horizontale (intervalle `[-5, 5]`)
- Vitesse verticale (intervalle `[-5, 5]`)
- Angle (intervalle  `[-3.14, 3.14]`)
- Vitesse angulaire (intervalle `[-5, 5]`)
- Contact pied gauche (`True` or `False`)
- Contact pied droite (`True` or `False`)

Dans le cas d'un "Observation Space" de type `rgb_array`, les observations sont des images de 64x64 pixels obtenues
en utilisant la fonction `render()` de l'environnement et le `render_mode` comme étant `rgb_array`.


## Échelles de difficultés
Pour chaque échelon le "Cumulative Rewards" se doit d'être égal ou supérieur à 200 afin de considérer l'échelon
comme réussi. Les échelons sont classés par ordre croissant de difficulté.

- Échelon 0:
    * Action Space: Discrete
    * Observation Space: Box
    * gravity: -10.0
    * enable_wind: False
- Échelon 1:
    * Action Space: Discrete
    * Observation Space: Box
    * gravity: -10.0
    * enable_wind: True
    * wind_power: 5.0
    * turbulence_power: 0.0
- Échelon 2:
    * Action Space: Discrete
    * Observation Space: Box
    * gravity: -10.0
    * enable_wind: True
    * wind_power: 5.0
    * turbulence_power: 0.5
- Échelon 3:
    * Action Space: Continuous
    * Observation Space: Box
    * gravity: -10.0
    * enable_wind: True
    * wind_power: 5.0
    * turbulence_power: 0.5



## Remise du projet
Le projet devra être remis dans un dossier nommé avec votre nom d'équipe ou le nom de votre agent
(vous pouvez choisir le nom que vous voulez). Ce dossier devra contenir tous les fichiers que votre agent aura besoin
pour exécuter ses actions. Le plus important sera que votre fichier `lunar_lander_agent.py` devra
être dans le dossier racine de la soumission. De plus, un fichier `README.md` contenant les explications de votre 
solution devra être présent dans le dossier
afin que nous puission évaluer votre compréhension de la solution que vous avez utilisé. Finalement, n'oubliez pas de
mettre un fichier `requirements.txt` dans votre dossier afin que nous puissions installer les dépendances de votre
code. Afin de générer ce fichier facilement, vous pouvez utiliser la librairie [pipreqs](https://pypi.org/project/pipreqs/).
Vous pouvez vous fier au format de [exemple_soumission](soumissions/exemple_soumission) pour vous aider à comprendre
comment organiser votre soumission.

### Soumission via GitHub
Vous devrez faire un "[fork](https://docs.github.com/en/get-started/quickstart/fork-a-repo)" du 
[dépôt GitHub du défi](https://github.com/JeremieGince/DefiProgFest2023) et créer un 
"[pull request](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-pull-requests)" 
avec votre dossier contenant les fichiers demandés dans le dossier `soumissions`.


**ATTENTION** : Puisque le dépôt est public, vous pouvez voir les soumissions des autres équipes. Vous ne pouvez en aucun cas
modifier ou copier le code d'une autre équipe. Sachez que nous avons des moyens de détecter si vous avez copié
ou modifié le code d'une autre équipe. Si vous êtes pris en flagrant délit, vous serez disqualifié.


## Ressources
- L'environnement [LunarLander-v2](https://www.gymlibrary.dev/environments/box2d/lunar_lander/).
- [Discord server](https://discord.gg/F8kcefP3my) où vous pouvez poser vos questions et/ou
    collaborer avec vos coéquipiers.
- [GitHub](https://github.com/JeremieGince/DefiProgFest2023) du défi.
- [Exemple d'utilisation de l'environnement](https://github.com/JeremieGince/DefiProgFest2023/blob/main/Gym-Tutorial.ipynb).
