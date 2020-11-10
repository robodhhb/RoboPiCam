# RoboPiCam

## Willkommen bei der RoboPiCam - ein Auge für den EV3-Roboter! (See English-Version below)

Die RoboPiCam ist eine smarte offline Pi-Kamera, die einen Lego Mindstorms EV3-Roboter über Bluetooth kommandiert. Ihre Aufgabe ist es, eine Flasche oder einen Apfel zu erkennen, die direkt vor dem Roboter hingestellt wurde. Anschließend beauftragt die smarte Pi-Kamera den Roboter, den Apfel bzw. die Flasche in den jeweils richtigen Korb zu bringen. Die smarte Pi-Kamera nutzt für die Objekterkennung ein neuronales Netz. Das Video "Video RoboPiCam two views HD" zeigt den Ablauf aus der Perspektive der Pi-Kamera und aus der Perspektive einer Kamera im Raum. 

Das neuronale Netz basiert auf einem von Google trainierten Modell auf Basis des COCO-Datensatzes mit der Architektur "MobileNet SSD v2". Das Inferencing findet auf der Edge TPU (Coral USB Accellerator) über das PyCoral-API statt. Der Raspberry Pi kann dadurch 6 Bilder pro Sekunde anzeigen und erkannte Objekte kennzeichnen(TPU Konfiguration mit normaler Geschwindigkeit). Die Bilder haben eine Auflösung von 300 x 300 Pixel. 
Im Ordner "Lego Mindstorms EV3 project" ist der Code für den EV3-Roboter abgelegt. Die Quellen für die smarte Pi-Kamera liegen im Ordner "Raspberry Pi project". Dort befinden sich auch Installationsanleitungen für die Programme. Das Projekt ist ausführlich beschrieben im Sonderheft "Robotik" (14.11.2019) des deutschen Make Magazins: https://www.heise.de/select/make/2019/7/1573929070378454

## Welcome to the RoboPiCam - an eye for an EV3-robot!

The RoboPiCam is a smart offline Pi camera that commands a Lego Mindstorms EV3 robot via Bluetooth. The task is to detect a bottle or an apple placed in front of the robot and then instruct the robot to bring an apple or a bottle into the correct basket. The smart Pi camera uses a neural network for object detection. The video "Video RoboPiCam two views HD" shows the process from the perspective of the Pi camera and from the perspective of a camera shooting the whole scene.

The neural network is based on a Google-trained model based on the COCO dataset with the MobileNet SSD v2 architecture. Inferencing takes place on the Edge TPU (Coral USB Accellerator) via the PyCoral API. The Raspberry Pi can display 6 frames per second and mark recognized objects (TPU configuration with normal speed). The pictures have a resolution of 300 x 300 pixels.
Please find the code and installation instructions for the Lego EV3 robot in the folder " Lego Mindstorms EV3 project" and for the RoboPiCam in the folder "Raspberry Pi project". This project is described in detail in the special edition "Robotik" of the German Make magazin (14.11.2019): https://www.heise.de/select/make/2019/7/1573929070378454
