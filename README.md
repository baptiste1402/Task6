# Script de Sauvegarde Automatisée de Serveur

Ce projet Python permet de sauvegarder automatiquement des fichiers/répertoires importants définis dans un fichier de configuration.

## Fonctionnalités

- 📁 Sauvegarde de plusieurs répertoires configurables
- 📂 Sauvegarde horodatée à chaque exécution
- ♻️ Suppression automatique des anciennes sauvegardes (configurable)
- 📄 Journalisation complète dans un fichier log
- 🕒 Compatible avec l'exécution planifiée (Windows/Linux)

---

## Fichier de configuration

Le fichier `config.json` contient :


```json
{
  "repertoires_a_sauvegarder": [
    "C:/Exemple/Documents",
    "D:/Photos"
  ],
  "dossier_de_sauvegarde": "D:/Sauvegardes",
  "nombre_max_sauvegardes": 3,
  "fichier_log": "sauvegarde.log"
}
```

## Exécution 
### Manuelle :
python sauvegarde.py
### Programmer :
1- Windows : 
  
    1/ Ouvre le Planificateur de tâches (taskschd.msc)
  
    2/ Clique sur Créer une tâche de base
  
    3/ Nom : Sauvegarde serveur
  
    4/ Déclencheur : Tous les jours à 02h00
  
    5/ Action : Lancer un programme
  
    6/ Programme/script : python
  
    7/ Argument : C:\chemin\vers\projet-sauvegarde\sauvegarde.py
  
    8/ Finis et teste.

2- Linux/Mac :
  
    1/ Taper crontab -e dans le terminal 
  
    2/ Puis taper 0 2 * * * /usr/bin/python3 /chemin/vers/sauvegarde.py dans le terminal (ici c'est tout les jours à 2h)



