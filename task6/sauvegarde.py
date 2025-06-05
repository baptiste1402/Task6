import os
import shutil
import json
from datetime import datetime
import logging

# Charger la configuration
def charger_config(fichier_config):
    with open(fichier_config, 'r') as f:
        return json.load(f)

# Créer une sauvegarde horodatée
def creer_sauvegarde(config):
    timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    dossier_destination = os.path.join(config["dossier_de_sauvegarde"], f"sauvegarde_{timestamp}")
    
    os.makedirs(dossier_destination, exist_ok=True)

    for dossier in config["repertoires_a_sauvegarder"]:
        if os.path.exists(dossier):
            try:
                nom = os.path.basename(os.path.normpath(dossier))
                shutil.copytree(dossier, os.path.join(dossier_destination, nom))
                logging.info(f"Sauvegarde de {dossier} réussie.")
            except Exception as e:
                logging.error(f"Erreur lors de la sauvegarde de {dossier} : {e}")
        else:
            logging.warning(f"Dossier introuvable : {dossier}")

    logging.info(f"Sauvegarde complétée dans {dossier_destination}")
    return dossier_destination

# Supprimer les sauvegardes les plus anciennes si besoin
def nettoyer_sauvegardes(config):
    sauvegardes = sorted([
        d for d in os.listdir(config["dossier_de_sauvegarde"])
        if d.startswith("sauvegarde_")
    ])

    surplus = len(sauvegardes) - config["nombre_max_sauvegardes"]
    for i in range(surplus):
        chemin = os.path.join(config["dossier_de_sauvegarde"], sauvegardes[i])
        try:
            shutil.rmtree(chemin)
            logging.info(f"Sauvegarde supprimée : {chemin}")
        except Exception as e:
            logging.error(f"Erreur suppression {chemin} : {e}")

# Configurer le log
def configurer_logging(fichier_log):
    logging.basicConfig(
        filename=fichier_log,
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )

def main():
    config = charger_config("config.json")
    configurer_logging(config["fichier_log"])
    logging.info("Début de la sauvegarde.")
    creer_sauvegarde(config)
    nettoyer_sauvegardes(config)
    logging.info("Fin du processus de sauvegarde.")

if __name__ == "__main__":
    main()
