# YT-DLP Testing

## Description
**yt-dlp** est un logiciel permettant de télécharger des vidéos à partir de sites de partage de vidéos en ligne tels que YouTube, en fournissant des fonctionnalités supplémentaires par rapport à la version standard de youtube-dl.

## Démarrage

Ces instructions vous donneront une copie du projet à des fins de test.

### Pré-requis

- Python 3.8+
- un environnement virtuel
- IDE tel que Visuel Studio Code ou autres

### Test

Voici les instructions pour tester le code source de `yt-dlp`.

- Cloner le répo GitHub :
```shell
$ git clone https://github.com/emilejanssens/Projet_yt_dlp.git
```

- Se rendre dans le dossier `test` :
```shell
$ cd test
```

- Lancer les tests

Pour lancer le "Mutation-Based fuzzing" :
```shell
python test_fuzzing.py
```
Pour lancer les tests unitaires :
```shell
python test_unit.py
```

Ces commandes lanceront les différents tests et affichera les résultats dans la console (ou dans un fichier log pour le fuzzing).