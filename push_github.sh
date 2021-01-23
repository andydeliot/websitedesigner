
# Git.
name="admin"
email="votre@email.com"
echo "Nom d'utilisateur github : "
read username
echo "nom de répertoire : "
read repertoire

echo ""

git remote add origin https://github.com/"$username"/"$repertoire".git
git branch -M main
git push -u origin main




