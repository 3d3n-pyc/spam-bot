# Utils Bot

Un bot Discord simple utilisant [discord.py](https://discordpy.readthedocs.io/) qui propose la commande `/spam` pour envoyer un message plusieurs fois via un bouton.

> [!WARNING]
> Je ne suis pas responsable des actions effectuées avec ce bot.
> Je ne suis pas responsable de tout bannissement résultant de l'utilisation de ce bot.

## Fonctionnalités

- Commande slash `/spam` : Envoyez un message jusqu'à 5 fois par clic sur le bouton.
- Interface bouton pour spam facile.
- Validation de la longueur du message et du nombre d'envois.

## Installation

1. **Clonez le dépôt :**
   ```sh
   git clone https://github.com/3d3n-pyc/spam-bot.git
   cd spam-bot
   ```

2. **Installez les dépendances :**
   ```sh
   pip install discord.py python-dotenv
   ```

3. **Créez un fichier `.env` :**
   ```
   BOT_TOKEN=votre-token-bot-ici
   ```

4. **Lancez le bot :**
   ```sh
   python main.py
   ```

## Utilisation

- Utilisez `/spam` sur votre serveur Discord.
- Entrez votre message et le nombre (1-5).
- Cliquez sur le bouton 📩 pour envoyer votre message plusieurs fois.

## Remarques

- Assurez-vous que votre bot dispose des permissions nécessaires pour les commandes slash et l'envoi de messages.
- Le bot autorise uniquement les messages jusqu'à 2000 caractères et jusqu'à 5 répétitions par clic.

## Licence

MIT
