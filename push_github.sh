
# Git.
name="admin"
email="votre@email.com"
echo "Nom d'utilisateur github : "
read username
echo "nom de répertoire : "
read repertoire

echo ""

git status
echo "Ctrl+c pour quitter si l'ajout de ses fichiers ne conviennent pas."
read nothing
git add --all
git status
echo "Message de commit : "
read message
git commit -m "$message"

git remote add origin https://github.com/"$username"/"$repertoire".git
git branch -M main
git push -u origin main




