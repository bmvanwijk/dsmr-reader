��    c      4              L  t   M     �  �   �  �   �  I   �  N   �  �   &	       
     !
     0
     @
     T
  !   p
     �
  $   �
     �
     �
  ?   �
  2  2  �   e     �     	  &     �   9  ,   �  \       i     }  =   �     �  2   �  e        }  �   �  �   ~  9   s  �   �  C   9  S   }  �   �  $   V  ?   {  #   �  �   �  r   �  �        �     �  �     K   �  /   �  s   '  U   �  W   �  _   I  L   �  /   �  R   &  l   y  Q   �  �   8  �     =   �  /     1   3  z   e  
   �  �   �  b   �  _      0   �      �  "   �  �   �  �   �      ~!  "   �!  r   �!  �   ("    �"  �   �#  g   �$  �   &%  U   �%  �   ?&  �   �&  �   M'  s   �'  "   b(  R   �(  q   �(  1   J)  �   |)    *  `   )+  v   �+  -   ,     /,  f  M,  y   �-     ..  �   E.  -  E/  H   s0  M   �0  �   
1     �1     2     2     /2     F2  "   b2     �2     �2     �2     �2  <   �2  j  3  d   �4     �4     �4  )   5  �   55  2   �5  �   �5  6  �6     �7  V   �7     .8  4   A8  s   v8     �8  +  9  2  3:  ?   f;  �   �;  B   :<  `   }<  �   �<  1   p=  .   �=     �=  �   �=  u   �>  �   ?     �?     �?  �   �?  v   �@  0   A  �   MA  ^   �A  i   -B  {   �B  n   C  1   �C  r   �C  ^   'D  Y   �D  �   �D  �   �E  I   }F  5   �F  1   �F  �   /G  
   �G     �G  k   �H  j   +I  5   �I  +   �I  (   �I  �   !J  �   K  #   �K  "   L  �   9L  �   �L  �   ^M  �   BN  i   )O  �   �O  j   5P  �   �P  �   JQ  �   �Q  �   �R  &   <S  f   cS  �   �S  E   [T  �   �T  ?  6U  z   vV  y   �V  3   kW  !   �W   (!) Ignore any '*could not change directory to "/root": Permission denied*' errors for the following three commands. (Legacy) MySQL/MariaDB **Installation of the requirements below might take a while**, depending on your Internet connection, RaspberryPi speed and resources (generally CPU) available. Nothing to worry about. :] **OPTIONAL**: You may skip this section as it's not required for the application to install. However, if you have never read your meter's P1 telegram port before, I recommend to perform an initial reading to make sure everything works as expected. **Optional**: Do you need to restore a **MySQL** database backup as well? **Optional**: Do you need to restore a **PostgreSQL** database backup as well? *We will now prepare the webserver, Nginx. It will serve all application's static files directly and proxy any application requests to the backend, Gunicorn controlled by Supervisor, which we will configure later on.* 1. Database backend (PostgreSQL) 10. Supervisor 2. Dependencies 3. Application user 4. Webserver/Nginx (part 1) 5. Clone project code from Github 6. Virtualenv 7. Application configuration & setup 8. Bootstrapping 9. Webserver/Nginx (part 2) :doc:`Finished? Go to setting up the application<application>`. Although it's just a folder inside our user's homedir, it's very effective as it allows us to keep dependencies isolated or to run different versions of the same package on the same machine. `More information about this subject can be found here <http://docs.python-guide.org/en/latest/dev/virtualenvs/>`_. Because you have shell access you may reset your user's password at any time (in case you forget it). Just enter this for a password reset:: Clone the repository:: Contents Continue to chapter 8 (Bootstrapping). Copy application vhost, **it will listen to any hostname** (wildcard), but you may change that if you feel like you need to. It won't affect the application anyway:: Copy the configuration file for Supervisor:: Create a new virtualenv, we usually use the same name for it as the application or project:: Create an application superuser. Django will prompt you for a password. The credentials generated can be used to access the administration panel inside the application. Alter username and email if you prefer other credentials, but email is not used in the application anyway. Create database user:: Create database, owned by the database user we just created:: Create database:: Create folder for the virtualenv(s) of this user:: Create user with homedir. The application code and virtualenv will reside in this directory as well:: Create your user:: Did everything install without fatal errors? If the database client refuses to install due to missing files/configs, make sure you've installed ``libmysqlclient-dev`` earlier in the process, when you installed the database server itself. Did everything install without fatal errors? If the database client refuses to install due to missing files/configs, make sure you've installed ``postgresql-server-dev-all`` earlier in the process, when you installed the database server itself. Did you choose PostgreSQL? Then execute these two lines:: Django will later copy all static files to the directory below, used by Nginx to serve statics. Therefor it requires (write) access to it:: Does PostgreSQL not start/create the cluster due to locales? I.e.:: Either proceed to the next heading **for a test reading** or continue at chapter 4. Enter these commands (**listed after the** ``>``). It will ask Supervisor to recheck its config directory and use/reload the files:: Example of everything running well:: Execute this to initialize the database we've created earlier:: Flush privileges to activate them:: Install MariaDB. You can also choose to install the closed source MySQL, as they should be interchangeable anyway. ``libmysqlclient-dev`` is required for the virtualenv installation later in this guide. Install PostgreSQL, ``postgresql-server-dev-all`` is required for the virtualenv installation later in this guide. Install ``cu``. The CU program allows easy testing for your DSMR serial connection. It's very basic but also very effective to simply test whether your serial cable setup works properly:: Install database:: Installation: Extended It's possible to have other applications use Nginx as well, but that requires you to remove the wildcard in the ``dsmr-webinterface`` vhost, which you will copy below. Let Nginx verify vhost syntax and reload Nginx when ``configtest`` passes:: Login to ``supervisorctl`` management console:: Make sure you are acting here as ``root`` or ``sudo`` user. If not, press CTRL + D to log out of the ``dsmr`` user. Make sure you are now acting as ``dsmr`` user (if not then enter: ``sudo su - dsmr``) Make sure you are still acting as ``dsmr`` user (if not then enter: ``sudo su - dsmr``) Make sure you've read and executed the note above, because you'll need it for the next chapter. Note that it's important to specify **Python 3** as the default interpreter. Now continue at chapter 2 below (Dependencies). Now is the time to clone the code from the repository into the homedir we created. Now it's time to bootstrap the application and check whether all settings are good and requirements are met. Now login as the user we have just created, to perform our very first reading! :: Now we configure `Supervisor <http://supervisord.org/>`_, which is used to run our application's web interface and background jobs used. It's also configured to bring the entire application up again after a shutdown or reboot. Now you'll have to install several utilities, required for the Nginx webserver, Gunicorn application server and cloning the application code from the Github repository:: Or did you choose MySQL/MariaDB? Execute these two commands:: Or restore a compressed (``.gz``) backup with:: Or test with ``cu`` for **DSMR 2.2** (untested):: Our user also requires dialout permissions. So allow the user to perform a dialout by adding it to the ``dialout`` group:: PostgreSQL Prepare static files for webinterface. This will copy all static files to the directory we created for Nginx earlier in the process. It allows us to have Nginx serve static files outside our project/code root. Put both commands below in the ``dsmr`` user's ``~/.bashrc`` file with your favorite text editor:: Remove the default Nginx vhost (**only when you do not use it yourself, see the note above**):: Restore an uncompressed (``.sql``) backup with:: Set password for database user:: Set privileges for database user:: Still no luck? Try editing ``/etc/environment``, add ``LC_ALL="en_US.utf-8"`` and reboot. Then try ``pg_createcluster 9.4 main --start`` again (or whatever version you are using). Support for the MySQL database backend is deprecated and will be removed in a later release. Please use a PostgreSQL database instead. Users already running MySQL will be supported in migrating at a later moment. Sync static files:: Test with ``cu`` for **DSMR 4+**:: The ``base.txt`` contains requirements which the application needs anyway, no matter which backend you've choosen. The application runs as ``dsmr`` user by default. This way we do not have to run the application as ``root``, which is a bad practice anyway. The application stores by default all readings taken from the serial cable. There is support for **PostgreSQL**, and there used to be support for **MySQL/MariaDB** as well. The latter is currently deprecated by this project and support will be discontinued in a future release. The application will also need the appropriate database client, which is not installed by default. For this I created two ready-to-use requirements files, which will also install all other dependencies required, such as the Django framework. The dependencies our application uses are stored in a separate environment, also called **VirtualEnv**. The installation guide may take about *15 to 30 minutes* (for raspberryPi 2/3), but it greatly depends on your Linux skills and whether you need to understand every step described in this guide. This installation guide asumes you run the Nginx webserver for this application only. This may take a few seconds. When finished, you should see a new folder called ``dsmr-reader``, containing a clone of the Github repository. This will both **activate** the virtual environment and cd you into the right directory on your **next login** as ``dsmr`` user. Three processes should be started or running. Make sure they don't end up in ``ERROR`` or ``BACKOFF`` state, so refresh with the ``status`` command a few times. To exit cu, type "``q.``", hit Enter and wait for a few seconds. It should exit with the message ``Disconnected.``. Try: ``dpkg-reconfigure locales``. Want to check whether the datalogger works? Just tail its log in supervisor with:: Want to quit supervisor? ``CTRL + C`` to stop tailing and then ``CTRL + D`` once to exit supervisor command line. When still in ``supervisorctl``'s console, type:: You can easily test whether you've configured this correctly by logging out the ``dsmr`` user (CTRL + D) and login again using ``sudo su - dsmr``. You now should see something similar to ``Connected.`` and a wall of text and numbers *within 10 seconds*. Nothing? Try different BAUD rate, as mentioned above. You might also check out a useful blog, `such as this one (Dutch) <http://gejanssen.com/howto/Slimme-meter-uitlezen/>`_. You should see similar output as the ``cu``-command printed earlier in the installation process. You should see the terminal have a ``(dsmrreader)`` prefix now, for example: ``(dsmrreader)dsmr@rasp:~/dsmr-reader $`` You've almost completed the installation now. Your first reading (optional) Project-Id-Version: PROJECT VERSION
Report-Msgid-Bugs-To: EMAIL@ADDRESS
POT-Creation-Date: 2018-10-09 20:07+0200
PO-Revision-Date: YEAR-MO-DA HO:MI+ZONE
Last-Translator: 
Language: nl
Language-Team: 
Plural-Forms: nplurals=2; plural=(n != 1)
MIME-Version: 1.0
Content-Type: text/plain; charset=utf-8
Content-Transfer-Encoding: 8bit
Generated-By: Babel 2.5.1
 (!) Negeer voor de volgende drie commando's de foutmelding: '*could not change directory to "/root": Permission denied*'. (Legacy) MySQL/MariaDB **De installatie van de volgende afhankelijkheden kan enige tijd in beslag nemen**. Dit varieert en is sterk afhankelijk van de snelheid van je Internet-verbinding en je RaspberryPi. Je hoeft je dus niet zorgen te maken wanneer dit lang lijkt te duren. :] **OPTIONEEL**: Je kunt deze stap overslaan wanneer je al eerder een (test)meting hebt gedaan met je slimme meter. Ik raad het dus vooral aan als je nog nooit eerder je P1-poort hebt uitgelezen. Hiermee verzeker je jezelf ook dat de applicatie straks dezelfde (werkende) toegang heeft voor de metingen. **Optioneel**: Wil je ook nog een **MySQL** database back-up herstellen? **Optioneel**: Wil je ook nog een **PostgreSQL** database back-up herstellen? *We configureren vervolgens de webserver (Nginx). Deze serveert alle statische bestanden en geeft de applicatie-verzoeken door naar de backend, waar de applicatie in Gunicorn draait onder Supervisor. Deze stellen we later in.* 1. Databaseopslag (PostgreSQL) 10. Supervisor 2. Afhankelijkheden 3. Applicatiegebruiker 4. Webserver/Nginx (deel 1) 5. Kloon project code vanaf Github 6. VirtualEnv 7. Applicatieconfiguratie 8. Initialisatie 9. Webserver/Nginx (deel 2) :doc:`Klaar? Ga dan naar applicatie instellen<application>`. Dit is allemaal erg handig, ondanks dat het feitelijk niets meer voorstelt dan een aparte map binnen de homedir van onze gebruiker. Hierdoor kunnen we namelijk meerdere versie van software op hetzelfde systeem installeren, zonder dat dat elkaar bijt. Meer informatie hierover `kan hier gevonden worden <http://docs.python-guide.org/en/latest/dev/virtualenvs/>`_. Wachtwoord ooit vergeten? Via de command line kun je je wachtwoord (bij verlies) hiermee aanpassen:: Kloon de repository:: Inhoudsopgave Ga door naar hoofdstuk 8 (Bootstrapping). Kopieer de vhost voor de applicatie. Deze luistert standaard naar **elke hostname** (wildcard), maar dat is natuurlijk naar eigen wens aan te passen:: Kopieer het configuratie-bestand voor Supervisor:: Maak een nieuwe VirtualEnv aan. Het is gebruikelijk om hiervoor dezelfde naam te gebruiken als die van de applicatie of het project. Maak een gebruiker aan voor binnen de applicatie. Django vraagt je om een wachtwoord te kiezen. Met deze gegevens kun je het beheerderspaneel binnen de applicatie gebruiken. Indien gewenst kun je een andere gebruikersnaam kiezen. Het e-mailadres maakt niet uit, want de applicatie ondersteunt toch geen e-mail. Creëer databasegebruiker:: Creëer database, met als eigenaar de databasegebruiker die we net hebben aangemaakt:: Creëer database:: Maak map aan voor de VirtualEnv van deze gebruiker:: Maak een aparte gebruiker aan met eigen homedir. De code voor de applicatie en VirtualEnv zetten we later hier in:: Creëer je eigen gebruiker:: Zonder problemen alles kunnen installeren? Mocht de database client niet willen installeren wegens missende bestanden, controleer dan of je eerder tijdens de installatie het volgende hebt uitgevoerd: als het goed is heb je ``libmysqlclient-dev`` geïnstalleerd, tegelijkertijd met de databaseserver. Zonder problemen alles kunnen installeren? Mocht de database client niet willen installeren wegens missende bestanden, controleer dan of je eerder tijdens de installatie het volgende hebt uitgevoerd: als het goed is heb je ``postgresql-server-dev-all`` geïnstalleerd, tegelijkertijd met de databaseserver. Heb je gekozen voor PostgreSQL? Voer dan deze twee regels uit:: Django kopieert alle statische bestanden naar een aparte map, die weer door Nginx gebruikt wordt. Daarom is er tevens (schrijf)toegang voor nodig:: Start PostgreSQL niet wegens een fout in 'locales'? Bijvoorbeeld:: Ga ofwel door naar het volgende hoofdstuk **voor een testmeting** of ga direct door naar stap 4. Voer de volgende commando's in (**degene na de** ``>``). Dit zorgt ervoor dat Supervisor zijn eigen configuratie opnieuw controleert en toepast:: Voorbeeld van wanneer alles naar behoren draait:: Voer dit uit om de database te initialiseren:: Pas de databaserechten toe:: Installeer MariaDB. Je kunt er ook voor kiezen om het closed-source MySQL te installeren. Welke je ook kiest, ``libmysqlclient-dev`` is later nodig voor de VirtualEnv. Installeer PostgreSQL. Daarnaast is ``postgresql-server-dev-all`` nodig voor het installeren van de VirtualEnv later. Installeer ``cu``. Met dit programmaatje kunnen kun je vrij gemakkelijk de DSMR-verbinding testen naar je slimme meter toe. Erg handig om te kijken of dat überhaupt al lekker werkt:: Installeer database:: Installatie: Uitgebreid Het is uiteraard mogelijk dat andere applicaties ook Nginx gebruiken, maar daarvoor zul je de wildcard moet weghalen in de ``dsmr-webinterface`` vhost, die je hieronder kopieert. Laat Nginx controleren of je geen typefouten hebt gemaakt en herlaad Nginx vervolgens wanneer de ``configtest`` lukt:: Wissel naar de ``supervisorctl`` beheerconsole:: Zorg ervoor dat je hier ``root``- of ``sudo``-gebruiker bent. Zo niet, druk op CTRL + D om uit te loggen als ``dsmr`` gebruiker. Zorg ervoor dat je ingelogd bent als ``dsmr``-gebruiker (zo niet, typ dan: ``sudo su - dsmr``) Zorg ervoor dat je nog steeds ingelogd bent als ``dsmr``-gebruiker (zo niet, typ dan: ``sudo su - dsmr``) Zorg ervoor dat je de bovenstaande notitie hebt gelezen en uitgevoerd, aangezien ze nodig zijn voor het volgende hoofdstuk. N.B.: het is belangrijk dat je voor deze VirtualEnv aangeeft dat **Python 3** de gewenste standaardversie is:: Ga door naar hoofdstuk 2 verderop (Dependencies). Nu kunnen we de code van de applicatie van Github downloaden en in de homedir zetten die we net aangemaakt hebben. Tijd om te kijken of alles goed is ingesteld. We gaan de applicatie proberen te initialiseren. Log nu in als de gebruiker die we zojuist hebben aangemaakt voor de eerste testmeting! :: We gaan nu `Supervisor <http://supervisord.org/>`_ configureren, die gebruikt wordt om de applicatie en achtergrondprocessen te draaien. Tevens zorgt Supervisor ervoor dat deze processen bij het (opnieuw) opstarten automatisch draaien. Tijd om diverse tools te installeren. Deze zijn nodig voor de Nginx webserver, de Gunicorn applicatieserver en voor het binnenhalen van de code van de applicatie vanaf Github:: Of heb je gekozen voor MySQL/MariaDB? Voer dan deze twee commando's uit:: Of herstel een gecomprimeerde (``.gz``) back-up met:: Of test met ``cu`` voor **DSMR 2.2** (ongetest):: De gebruiker heeft ook toegang nodig om de kabel te kunnen uitlezen. Hiervoor voegen de we gebruiker toe aan de groep ``dialout``:: PostgreSQL Ga nu bezig met de statische bestanden voor de webinterface. Dit kopieert alle statische bestanden in de map die we eerder, vlak na de installatie voor Nginx, hebben aangemaakt. Het zorgt ervoor dat Nginx deze bestanden kan hosten buiten de code-bestanden. Zet beide commands in het ``~/.bashrc`` bestand van de ``dsmr`` gebruiker met je favoriete bestandseditor:: Verwijder de standaard vhost van Nginx **wanneer je deze niet zelf gebruikt** (zie de notitie hierboven):: Herstel een ongecomprimeerde (``.sql``) back-up met:: Stel wachtwoord in voor databasegebruiker:: Stel rechten in voor databasegebruiker:: Werkt het nog steeds niet? Open dan dit bestand ``/etc/environment``, voeg onderaan de regel ``LC_ALL="en_US.utf-8"`` toe en herstart het systeem. Probeer daarna ``pg_createcluster 9.4 main --start`` (of welke versie je ook gebruikt). Gebruik van  MySQL-databases wordt afgeraden en de ondersteuning hiervoor stopt in een latere release. Gebruik daarom PostgreSQL. Gebruikers die dit project al op MySQL draaien krijgen in de toekomst ondersteuning om te migreren. Synchroniseer statische bestanden:: Test met ``cu`` voor **DSMR 4+**:: Het bestand ``base.txt`` bevat alle afhankelijkheden die de applicatie sowieso nodig heeft, ongeacht de databasekeuze die je gemaakt hebt. De applicatie draait standaard onder de gebruiker ``dsmr``. Hierdoor heeft het geen ``root``-rechten (nodig), wat over het algemeen zeer afgeraden wordt. De applicatie slaat de P1-metingen standaard op. Er is ondersteuning voor **PostgreSQL**, en vroeger ook voor **MySQL/MariaDB**.  Alleen wordt de laatstgenoemde momenteel afgeraden om te gebruiken (ondersteuning vervalt later). De applicatie heeft een databaseconnector nodig om de gegevens te kunnen opslaan. Daarvoor heb ik een tweetal requirements-bestanden gemaakt, waar alles al in staat wat nodig is. Zoals bijvoorbeeld Django en de databaseverbinding. Alle (externe) afhankelijkheden worden opgeslagen in een aparte omgeving, ook wel **VirtualEnv** genoemd. Het installeren duurt naar verwachting zo'n *15 a 30 minuten* (op een RaspberryPi 2/3), maar hangt natuurlijk ook af van je eigen vaardigheid op de command line. Deze installatiehandleiding gaat er vanuit dat je de Nginx webserver alleen gebruikt voor deze applicatie. Dit kan enkele seconden in beslag nemen. Als het goed is zie je hierna een map genaamd ``dsmr-reader``, met daarin een kopie van de repository zoals die op Github staat. Hiermee wordt zowel de VirtualEnv geactiveerd en ga je direct naar de juiste map. Dit werkt de **eerstvolgende keer** dat je inlogt als ``dsmr`` gebruiker. Er draaien als het goed is altijd **drie** processen. Kijk goed of ze uiteindelijk niet in ``ERROR`` of ``BACKOFF`` status terecht zijn gekomen. Je kunt het overzicht verversen door ``status`` te typen. Om cu af te sluiten, typ "``q.``", druk op Enter en wacht voor een paar seconden. Het programma sluit af met de melding ``Disconnected.``. Probeer: ``dpkg-reconfigure locales``. Wil je controleren of de datalogger zijn werk goed doet? Bekijk dan het logbestand in supervisor met:: Wil je uit supervisor? Druk dan op ``CTRL + C`` om het logbestand niet meer te bekijken en vervolgens op ``CTRL + D`` om uit supervisor te gaan. Typ het volgende wanneer je nog in ``supervisorctl``'s console bent:: Je kunt dit vrij gemakkelijk testen door uit te loggen als ``dsmr`` gebruiker (met CTRL + D) en vervolgens weer in te loggen met ``sudo su - dsmr``. Je zou nu iets moeten zien als ``Connected.``. Vervolgens krijg je, als het goed is, binnen tien seconden een hele lap tekst te zijn met een hoop cijfers. Werkt het niet? Probeer dan een andere BAUD-waarde, zoals hierboven beschreven. Of `kijk op een nuttig weblog <http://gejanssen.com/howto/Slimme-meter-uitlezen/>`_. Uiteindelijk zou je ongeveer dezelfde lap tekst moeten zien als toen we handmatig gemeten hebben met het ``cu``-programma. Als het goed is heeft je terminal nu een ``(dsmrreader)`` prefix, bijvoorbeeld: ``(dsmrreader)dsmr@rasp:~/dsmr-reader $`` Je bent op dit punt bijna klaar met de installatie. Je allereerste (optionele) meting 