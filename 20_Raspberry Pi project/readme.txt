Installation der RoboPiCam Applikation (see English Version below)
===================================================================
Voraussetzung: Raspberry Pi 2/3 Model B/B+ und 4 mit 
  - Raspbian Stretch und Python 3.5.3 oder
  - Raspbian Buster  und Python 3.7.3
  - Raspberry Pi Camera V2
  - Coral USB Accelerator (Edge TPU)
  - Lego Mindstorms EV3

Empfohlen: Update von Raspbian (Stretch oder Buster)
- sudo apt update
- sudo apt full-upgrade

Die Installation der RoboPiCam besteht aus:

1) Anmeldung als user "pi". 
 
2) Setup der Raspberry Pi Camera V2:
   Siehe https://www.raspberrypi.org/documentation/configuration/camera.md

3) Optional: Zugriff auf den Pi über VNC von einem PC aus:
   https://www.raspberrypi.org/documentation/remote-access/vnc/README.md

4) Installation der Edge TPU:
   Achtung: Erst SW installieren, dann Edge TPU über USB anschließen!
   Siehe den Get Started Giude:
   https://coral.withgoogle.com/docs/accelerator/get-started/
   Minimale Installation:
        1) Install Edge TPU Runtime
        2) Install Edge TPU Python API unter:
           https://coral.withgoogle.com/docs/edgetpu/api-intro/
   Es reicht aus, die Edge TPU mit "default operating frequency" zu installieren.
   
5) Zusätzlichen Bluetooth-Manager installieren:
      - Bluetooth Manager installieren
          - sudo apt-get install bluetooth bluez blueman
      - Bluetooth Name anpassen:
         sudo nano /etc/machine-info
         Folgende Zeile einfügen dann sichern und schließen:
         PRETTY_HOSTNAME=pi4robo
      - Raspberry Pi neu starten
      - Jetzt sollten zwei Bluetooth Icons (neu und alt) in der 
        Startleiste zu sehen sein. 
   
6) Einmaliges Bluetooth Pairing von Raspbery Pi und EV3-Stein
      - EV3-Stein: Im Menü Einstellungen:
          - Eintrag "Visibility" aktivieren
          - Eintrag "Bluetooth" aktivieren
          - Auf dem Display wird oben links ein BT-Icon und direkt 
            daneben ein "<" angezeigt.
          - EV3 ausschalten
      - Raspberry Pi: Pairing einleiten
          -  Altes Bluetooth Icon anklicken
          -  "Make Discoverable" anklicken
          -  EV3 einschalten 
          -  Altes Bluetooth Menu:
             - "Add Device" auswählen und kurz warten 
             - EV3-Stein auswählen und "Pair" klicken
             - EV3: Pairing bestätigen
             - EV3: Schnell 1234 eingeben (falls es nicht schon angezeigt wird)
                    und schnell bestätigen
             - Pi: Schnell 1234 in Dialog eingeben und schnell ok klicken 
             - Pi: Meldung "Pairing successfully"             
7) Serielle Bluetooth Verbindung einrichten
       - Nach jedem Booten neu einrichten!
       - Altes Bluetooth-Icon: Make Discovearable anklicken
       - EV3 einschalten
       - Neuen BT-Manager anklicken
       - Eintrag "Geräte" (Devices) anklicken
       - Der EV3-Stein ist nach erfolgreichem Pairing in der
         Liste der BT-Geräte enthalten.
       - EV3-Stein auswählen und "Einrichten" (Setup) auswählen
       - Option "Connect to serial port" auswählen
       - Klick "Weiter (Next)"
       - Eine Erfolgsmeldung sollte nun angezeigt werden.
       - Fenster schließen. 
       - EV3-Stein: Auf dem Display wird oben links ein BT-Icon und direkt 
         daneben "<" und ">" angezeigt. Im Raspberry Pi ist /etc/rfcomm0 vorhanden.
                    
8) Download des GitHub-Repository 
   auf dem Raspberry Pi unter dem user "pi":
   https://github.com/robodhhb/RoboPiCam
   und auch auf einem PC mit Verbindung zum EV3-Roboter

9) PC: Lego Mindstorms Projekt "AB_Gripp3r_V1.ev3" auf den Roboter laden.

10) Pi: LXTerminal öffnen und zip-Datei mit unzip in einem Ordner Ihrer Wahl entpacken
    und in den Ordner "RoboPiCamPi" mit cd wechseln

11) Programme starten:
    - Auf dem EV3 Roboter: main im Projekt AB_Gripp3r.ev3
    - Auf dem Raspberry Pi: python3 roboPiCamMain.py
      Temperatur mit vcgencmd measure_temp überprüfen. 
    
------------------    
Bekannte Probleme:
a)  Falls das Paket "ImageTk" nicht gefunden wird, muss es noch
    installiert werden mit:
    sudo aptitude install python3-pil.imagetk

b) Meldung nach dem Laden des Modells:
   W0422 10:54:13.042898    2007 package_registry.cc:65] 
   Minimum runtime version required by package (5) is lower than expected (10)
   Google arbeitet an diesem Progblem, das jedoch kein Auswirkung auf das Program hat.
   Die Meldung kann ignoriert werden. 


    
========================English Version====================================
Installation of the application "RoboPiCam"
--------------------------------------------
Prerequisite: Raspberry Pi 2/3 Model B/B+ and 4 with:
   - Raspbian Stretch and Python 3.5.3 or
   - Raspbian Buster and Python 3.7.3
   - Raspberry Pi Camera V2
   - Coral USB Accelerator (Edge TPU)
   - Lego Mindstorms EV3
   
Recommended: Update Raspbian (Stretch or Buster)
- sudo apt update
- sudo apt full-upgrade

Installation steps:
   
1) Login as user "pi". 
 
2) Setup  Raspberry Pi Camera V2:
   See https://www.raspberrypi.org/documentation/configuration/camera.md

3) Optional: Access the Pi desktop with VNC via a PC:
   https://www.raspberrypi.org/documentation/remote-access/vnc/README.md

4) Installation of the Edge TPU:
   Caution: First install the software then connect Edge TPU to the USB-Port!
   See: Get started guide:
   https://coral.withgoogle.com/docs/accelerator/get-started/
   Minimal installation:
        1) Install Edge TPU Runtime
        2) Install Edge TPU Python API on:
           https://coral.withgoogle.com/docs/edgetpu/api-intro/
   It is sufficient to install the Edge TPU with default operating frequency.

5) Install additional Bluetooth-Manager:
    - Install Bluetooth-Manager with:
       - sudo apt-get install bluetooth bluez blueman
    - Change Bluetooth name:
       sudo nano /etc/machine-info
       Add the following line and save/close editor:
       PRETTY_HOSTNAME=pi4robo
    - Reboot Raspberry Pi
    - Now you should see two bluetooth icons: The new and the old one
    
6) One-time job: BT-Pairing of Raspberry Pi and EV3 
      - EV3: Menu Settings:
          - Check "Visibility"
          - Check  "Bluetooth"
          - On the EV3-Display you see a BT-Icon and a "<"
          - Switch off EV3
      - Raspberry Pi: Initiate pairing
          - Click on the "old" BT-Icon
          - Select "Make Discoverable"
          - Switch on EV3
          - Old Bluetooth Icon:
              - Select "Add Device" and wait until it shows your EV3
              - Select EV3 and click "Pair"
              - On EV3: Confirm pairing
              - On EV3: Quickly enter 1234 (if it is not already displayed)
                         and confirm quickly
              - On Pi: Quickly enter 1234 in the dialog and quickly enter OK
              - On Pi: Message "Pairing successfully"

7) Configure serial BT connection
      - Configure after each booting
      - Click on the "old" BT-Icon
          - Select "Make Discoverable"
      - Switch on EV3
      - Click on new BT-Manager
      - Select menu entry "Devices"
      - EV3 is listed
      - Select your EV3 and select "Setup"
      - Select option "Connect to serial port"
      - Click "Next"
      - A success message is displayed.
      - Close Window
      - On EV3: On display you see at the top a BT-icon and "<>". 
      - On Pi: /etc/rfcomm0  is present.

8) Download the GitHub-Repository 
   on the Raspberry Pi under the user "pi":
   https://github.com/robodhhb/RoboPiCam
   and also on a PC with connection to the EV3-robot

9) PC: Load EV3-project "AB_Gripp3r_V1.ev3" on the EV3
   
10) On Pi: Open LXTerminal and unzip downloaded file in a folder of your choice
   
11) Change directory to "RoboPiCam"

12) Run the programs:
       - On EV3: Start main in project "AB_Gripp3r_V1"
       - On Pi:  python3 roboPiCamMain.py
       Check temperature with vcgencmd measure_temp
       
--------------       
Known issues:
a)  If the paket "ImageTk" cannot be found, it has to be installed with:
    sudo aptitude install python3-pil.imagetk

b) After loading the model, the following message can be ignored. 
   Google is working on it.
   W0422 10:54:13.042898    2007 package_registry.cc:65] 
   Minimum runtime version required by package (5) is lower than expected (10)


 
      
   

