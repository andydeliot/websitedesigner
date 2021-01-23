
# Installation du nécéssaire.
sudo apt install python3-pip
pip3 install django
sudo apt install git
git init

echo ""

# Git.
name="admin"
email="votre@email.com"
echo "Votre nom git : "
read name
echo "Votre email git : "
read email

git config --global user.name "$name"
git config --global user.email $email
git config -l

echo ""

# Mot de passe admin.
cd mysite
python3 manage.py changepassword admin




