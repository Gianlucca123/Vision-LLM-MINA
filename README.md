# Projet industriel

Ce projet a pour objectif de développer un système embarqué capable d’analyser des flux vidéo et de générer des descriptions précises grâce à l’intégration de modèles LLM. 

Le développement est réalisé sur une carte **Jetson Orin Nano Developer Kit** avec les contraites liées au edge-computing.

## Mise en place d’une carte Jetson

1. Flasher sur la carte microSD avec [Balena Etcher](https://etcher.balena.io) le firmware de [JetPack 6.1](https://developer.nvidia.com/embedded/jetpack).

2. Insérer la carte microSD dans la carte Jetson, brancher un clavier et un moniteur, puis l’alimentation.

3. Suivre le programme d’installation d'Ubuntu :
- **Langue** : English
- **Clavier** : French / French (AZERTY)
- **Identifiant** : xxx (xxx-desktop)
- **Mot de passe** : xxx
- **Ne pas installer Chromium** car cela donne une erreur (on le fera via le Terminal après).
- **Se connecter à internet** (on installera eduroam plus tard mais en attendant, utiliser un partage de connexion).

4. Mise à jour apt et installation de pip :
   ```bash
   sudo apt update
   sudo apt upgrade
   sudo reboot
   ```
   ```bash
   sudo apt-get install python3-pip
   ```

5. Installer Chromium :
   ```bash
   sudo apt-get install chromium-browser
   ```
   "INFO Waiting…" peut prendre jusqu’à 5 minutes.

6. Configurer eduroam pour l'accès au Wi-Fi de l'école :

   Télécharger le [configurateur eduroam](https://cat.eduroam.org) de l’Université de Lorraine (fichier `.py` à exécuter).
   ```bash
   python ~/Downloads/eduroam-linux-eduroam_et_Personnels_Univ-Lorraine.py
   ```
   Si la fenêtre paraît vide après avoir entré les identifiants, quitter la fenêtre (l'installation est réussie).

6. Installer VS Code :
   ```bash
   wget -N -O vscode-linux-deb.arm64.deb https://update.code.visualstudio.com/latest/linux-deb-arm64/stable
   sudo apt install ./vscode-linux-deb.arm64.deb
   ```

7. Installer la commande jtop :
   ```bash
   sudo pip install -U jetson-stats
   sudo reboot
   ```
   Au redémarrage, essayer la commande `jtop` (pour monitorer le GPU).

8. Installer les composants JetPack (facultatif) :
   ```bash
   sudo apt install nvidia-jetpack
   ```

9. Vérifier l’espace disque restant :
   
   Naviguer vers **System Monitor -> File Systems**.
