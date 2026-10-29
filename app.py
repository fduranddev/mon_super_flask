from flask import Flask, request

# 1. On crée l'instance de l'application Flask
app = Flask(__name__)

# 2. On définit une route
@app.route('/')
def index():
    return 'Page d\'accueil'

@app.route('/hello')
def hello():
    return 'Bonjour tout le monde !'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return "Tu essaies de te connecter (POST)"
    else:
        return "Affiche le formulaire de connexion (GET)"

@app.route('/projets/')
def projets():
    return 'La liste des projets'

@app.route('/a-propos/')
def about():
    return 'À propos de nous'

@app.route('/user/<username>')
def show_user_profile(username):
    # username est passé comme argument à la fonction
    return f'Profil de l\'utilisateur : {username}'

# 3. On lance l'application (si ce fichier est exécuté directement)
if __name__ == "__main__":
    app.run(debug=True)

