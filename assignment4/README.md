Comment ex�cuter les fichiers .pig
==================================

* Se connecter � AWS

* Dans Console Home (page principale), choisir en haut � droite la r�gion
* J'ai choisi Oregon car c'est l� que les fichiers du code sont stock�s

* Aller � EC2 pour cr�er une Key Pair, puis l'enregistrer dans un dossier (je l'appelerai oregonkey.pem par la suite)
* Changer les droits � priv� : chmod 600 oregonkey.pem

* Aller � Elastic Map Reduce afin de cr�er un cluster
* Lui donner un nom, enlever Termination protection et Logging
* Choisir AMI 2.4.2 afin d'utiliser Hadoop 1
* Dans Hardware Configuration, il faut choisir le nombre de nodes pour chaque type d'Instance, cela varie selon les donn�es � traiter
* Plus la taille et le nombre sont grands, plus rapide sera l'ex�cution des jobs, mais le prix augmentera
* Pour des valeurs trop petites, on risque une ex�cution trop longue, voire un plantage apr�s de longues minutes
* Valider par Create Cluster, et attendre environ 2-3 minutes que le status soit � "Running"
* dans mon exemple, le DNS sera ec2-54-191-22-191.us-west-2.compute.amazonaws.com (varie pour chaque cluster)

* Lancer un terminal afin de se connecter au cluster via ssh
* ex�cuter : ssh -o "ServerAliveInterval 10" -i oregonkey.pem hadoop@ec2-54-191-22-191.us-west-2.compute.amazonaws.com
* valider par "yes" si n�cessaire
* cr�er un dossier sur le cluster via : hadoop fs -mkdir /user/hadoop
* pour entrer le code, il suffit de rentrer : pig
* il convient ensuite de copier le code ligne par ligne, seules les lignes de type STORE lanceront l'algorithme de MapReduce, et prendront donc du temps

* Avant de lancer l'algorithme, ouvrir un autre terminal
* ex�cuter : ssh -L 9100:localhost:9100 -L 9101:localhost:9101  -i oregonkey.pem hadoop@ec2-54-191-22-191.us-west-2.compute.amazonaws.com
* cela permettra d'afficher [link](http://localhost:9101/jobtracker.jsp) dans un explorateur afin de suivre en temps r�el l'avancement, bien plus pr�cis que le terminal

* une fois l'ex�cution termin�e, pour r�cup�rer les fichiers :
* hadoop fs -copyToLocal /user/hadoop/example-results example-results o� example-result est le nom pr�cis� dans l'instruction STORE
* puis hors-hadoop (dans un autre terminal donc) r�cup�rer les donn�es via scp -o "ServerAliveInterval 10" -i oregonkey.pem -r hadoop@ec2-54-191-22-191.us-west-2.compute.amazonaws.com:example-results .
* Si les donn�es sont fragment�es � cause d'une instruction PARALLEL dans le code, aller dans le r�pertoire et concat�ner les fichiers via : cat * > bigfile
