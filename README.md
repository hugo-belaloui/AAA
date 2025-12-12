(FRA)
Challenge Triple A

Description :
Ce projet a été réalisé dans le cadre du Challenge Triple A, consistant à développer un outil simple de monitoring système.
L’objectif est d’afficher, dans un dashboard web, différentes informations en temps réel concernant une machine virtuelle Linux :
Utilisation du CPU & de la RAM


Utilisation de la mémoire


Informations système : adresse IP


Analyse de fichiers


Prérequis
Pour utiliser ce projet, vous aurez besoin des outils suivants :
Virtualisation : VMware Workstation / Fusion


Système : Ubuntu Desktop 22.04 LTS


Outils :

-Python 3

-Pip

-Apache2

-Jinja2

-Visual Studio Code

Installation
Installez VMware via leur site (https://www.vmware.com/products/desktop-hypervisor/workstation-and-fusion), puis téléchargez l'ISO d'Ubuntu (https://www.ubuntu-fr.org/download/).
Commandes pour installer les dépendances

Voici les commandes pour installer les outils nécessaires :
Python : sudo apt install python3


Apache : sudo apt install apache2


Pip : sudo apt install python3-pip


Jinja2 : sudo pip3 install Jinja2


Utilisation
Comment lancer le script
Lancez le fichier monitor.py, qui créera un fichier HTML permettant de lancer le site.
Ouvrir index.html dans le navigateur
Une fois le fichier HTML généré, ouvrez-le dans votre navigateur pour voir le dashboard.

Fonctionnalités
Le dashboard affiche :
Système

-Nom de la machine

Nom du système d’exploitation

-Heure de démarrage

-Temps écoulé depuis le démarrage

-Nombre d’utilisateurs connectés

-Adresse IP principale


RAM

-RAM utilisée

-Pourcentage d’utilisation

-Applications qui consomment le plus


CPU

-Nombre de cœurs

-Pourcentage d’utilisation

-Applications qui consomment le plus


Captures d'écran

<img width="816" height="162" alt="image" src="https://github.com/user-attachments/assets/391cfb3a-3380-4e63-92d5-1823e241c1f8" />

<img width="1091" height="152" alt="image" src="https://github.com/user-attachments/assets/f89a7a5f-1c2e-4a2e-bb71-0ded51cf6bf0" />

<img width="1059" height="347" alt="image" src="https://github.com/user-attachments/assets/c9269caf-84d4-46fd-a25c-6a33ad89d496" />


<img width="709" height="138" alt="image" src="https://github.com/user-attachments/assets/bdb98e3a-080e-464e-8bf5-93eb2efb435a" />


Difficultés rencontrées


Améliorations possibles


Auteurs
Yaniss Aouri

Hugo Belaloui

Elyes Bessai

"ENG"

Challenge Triple A
Description

This project was developed as part of the Challenge Triple A, which consists of creating a simple system monitoring tool.
The objective is to display, in a web dashboard, various real-time information about a Linux virtual machine:

-CPU & RAM usage

-Memory usage

-System information: IP address

-File analysis

Prerequisites

To use this project, you will need the following tools:

Virtualization: VMware Workstation / Fusion
System: Ubuntu Desktop 22.04 LTS

Tools:

-Python 3

-Pip

-Apache2

-Jinja2

-Visual Studio Code

Installation

Install VMware from their official website (https://www.vmware.com/products/desktop-hypervisor/workstation-and-fusion), 
then download the Ubuntu ISO (https://www.ubuntu-fr.org/download/).

Commands to install the dependencies

-Here are the commands to install the required tools:

-Python: sudo apt install python3

-Apache: sudo apt install apache2

-Pip: sudo apt install python3-pip

-Jinja2: sudo pip3 install Jinja2

Usage
How to run the script

Run the monitor.py file. It will generate an HTML file that allows you to launch the website.

Open index.html in your browser

Once the HTML file is generated, open it in your browser to view the dashboard.

Features

The dashboard displays:

System:

-Machine name

-Operating system name

-Boot time

-Time since boot

-Number of connected users

-Main IP address

RAM:

-RAM usage

-Usage percentage

-Applications consuming the most RAM

CPU:

-Number of cores

-CPU usage percentage

-Applications consuming the most CPU

Screenshots :

Challenges Encountered:

Possible Improvements:

Authors:
Yaniss Aouri

Hugo Belaloui

Elyes Bessai
