
Dans ce même dossier, vous devez trouver :
* un dossier mysite, correspondant au dossier du projet django.
* un fichier .gitignore, correpondant aux fichiers et dossiers à ignorer lors des commits.
* un fichier init.sh, permettant d'initialiser le site internet.


Il ne faut pas modifier le nom des dossiers nommés mysite.
Les applications doivent se trouver dans le dossier applications.
Elles sont ajoutés à installed_apps automatiquement.


Les environnements virtuels, c'est de la merde.
Installer Scipy en dehors d'un environnement virtuel,
et vous constaterez que votre environnement virtuel possède quand même scipy.
(j'ai fait le teste)
Donc ça sert à rien.

------------------------------------
Étapes pour commencer à travailler :
0) Copier coller le dossier Djangoing vx.y, puis le renommer.

1) Installer les composants nécéssaire à djangoing.
- Ouvrir un cmd.
- Glisser puis exécuter le fichier init.sh dans le cmd.
- Remplissez les champs correspondants.

2) Démarrer le serveur.
- Ouvrir un cmd au dessus de ce readme.txt.
- Taper : cd mysite
- Taper : python3 manage.py runserver
- Ouvrir une page internet.
- Taper http://127.0.0.1:8000/ dans la barre d'addresse.
Vous tomberez normalement sur une jolie page web Progressus : bravo tout fonctionne.

3) Accéder à la page d'administration.
- Rendez vous sur la page http://127.0.0.1:8000/admin
- Taper admin dans username.
- Taper votre mot de passe dans password.
Vous tomberez normalement sur une page web clair et épurée : bravo tout fonctionne.

4) Sauver ses modifications sur git.
- Ouvrir un cmd au dessus du dossier .git.
- Taper : git status
- Taper : git add --all
- Taper : git status pour vérifier que les fichiers ont bien été prit en compte.
- Taper : git commit -m "Ajoutez un message ici"
A partir de maintenant, vous pouvez commencer à travailler sans souci.





Pour réaliser le front-end, il est très intéréssant d'utiliser des templates :
Voici un site qui en propose.
https://www.webdesignertrends.com/2015/07/12-templates-html5-css3-gratuits-a-telecharger/



Pour intégrer un payement paypal, voici un tuto expliquant comment faire :
https://studygyaan.com/django/django-paypal-payment-gateway-integration-tutorial




Credits
-------
* Développement : **Andy Déliot**
























