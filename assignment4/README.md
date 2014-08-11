Comment exécuter les fichiers .pig
==================================

* Se connecter à AWS

* Dans Console Home (page principale), choisir en haut à droite la région
* J'ai choisi Oregon car c'est là que les fichiers du code sont stockés

* Aller à EC2 pour créer une Key Pair, puis l'enregistrer dans un dossier (je l'appelerai oregonkey.pem par la suite)
* Changer les droits à privé : chmod 600 oregonkey.pem

* Aller à Elastic Map Reduce afin de créer un cluster
* Lui donner un nom, enlever Termination protection et Logging
* Choisir AMI 2.4.2 afin d'utiliser Hadoop 1
* Dans Hardware Configuration, il faut choisir le nombre de nodes pour chaque type d'Instance, cela varie selon les données à traiter
* Plus la taille et le nombre sont grands, plus rapide sera l'exécution des jobs, mais le prix augmentera
* Pour des valeurs trop petites, on risque une exécution trop longue, voire un plantage après de longues minutes
* Valider par Create Cluster, et attendre environ 2-3 minutes que le status soit à "Running"
* dans mon exemple, le DNS sera ec2-54-191-22-191.us-west-2.compute.amazonaws.com (varie pour chaque cluster)

* Lancer un terminal afin de se connecter au cluster via ssh
* exécuter : ssh -o "ServerAliveInterval 10" -i oregonkey.pem hadoop@ec2-54-191-22-191.us-west-2.compute.amazonaws.com
* valider par "yes" si nécessaire
* créer un dossier sur le cluster via : hadoop fs -mkdir /user/hadoop
* pour entrer le code, il suffit de rentrer : pig
* il convient ensuite de copier le code ligne par ligne, seules les lignes de type STORE lanceront l'algorithme de MapReduce, et prendront donc du temps

* Avant de lancer l'algorithme, ouvrir un autre terminal
* exécuter : ssh -L 9100:localhost:9100 -L 9101:localhost:9101  -i oregonkey.pem hadoop@ec2-54-191-22-191.us-west-2.compute.amazonaws.com
* cela permettra d'afficher [link](http://localhost:9101/jobtracker.jsp) dans un explorateur afin de suivre en temps réel l'avancement, bien plus précis que le terminal

* une fois l'exécution terminée, pour récupérer les fichiers :
* hadoop fs -copyToLocal /user/hadoop/example-results example-results où example-result est le nom précisé dans l'instruction STORE
* puis hors-hadoop (dans un autre terminal donc) récupérer les données via scp -o "ServerAliveInterval 10" -i oregonkey.pem -r hadoop@ec2-54-191-22-191.us-west-2.compute.amazonaws.com:example-results .
* Si les données sont fragmentées à cause d'une instruction PARALLEL dans le code, aller dans le répertoire et concaténer les fichiers via : cat * > bigfile
