# Automatic fire extinguisher robot
This project aims to create an automatic fire extinguisher robot using Arduino, various electronic components, and sensors. The robot detects fire using a sensor and automatically sprays water to extinguish it. Additionally, it sends a call alert using a GSM module to notify concerned authorities or individuals about the fire incident.

Components Used:

1. Arduino (Microcontroller)

2. Motor Driver (To control DC motors)

3. GSM Module (For sending call alerts)

4. Relay (To control water pump)

5. Water Pump (To spray water)

6. SG90 Servo Motor (For controlling sensor movement)

7. DC Motors (For robot movement)

8. Power Supply (To power up the entire system)


Project Structure:

Main Code (Main.ino): This file contains the main Arduino code responsible for controlling the entire system. It includes the setup and loop functions to initialize components and continuously monitor for fire detection.

Libraries Folder: This folder contains any necessary libraries required for the project to function correctly. Make sure to include these libraries in your Arduino IDE.

Schematics Folder: This folder contains schematic diagrams of the circuit connections. It provides a visual guide for assembling the hardware components.

Documentation Folder: This folder includes any additional documentation related to the project, such as datasheets for components used, instructions for assembly, and usage guidelines.


Installation and Setup:

Hardware Assembly:

* Connect the components according to the schematic diagrams provided in the Schematics folder.

* Ensure all connections are secure and correctly wired to the Arduino board.

Software Setup:

* Install the Arduino IDE on your computer if not already installed.

* Open the Main.ino file in the Arduino IDE.

* Connect the Arduino board to your computer via USB.

* Select the appropriate board and port from the Arduino IDE's Tools menu.

* Upload the code to the Arduino board.

Testing:

* Power on the system and ensure all components are functioning correctly.

* Test the fire detection sensor by simulating a fire source near it.

* Verify that the water pump activates automatically upon fire detection.

* Test the GSM module's call alert functionality by triggering a simulated fire and observing the notification.

Usage:

* Place the robot in an area prone to fire hazards, ensuring the fire detection sensor has adequate coverage.

* Power on the robot and leave it to monitor the surroundings.

* In the event of a fire, the robot will automatically activate, spray water to extinguish the fire, and notify concerned individuals via a call alert.

Contributing:
Contributions to this project are welcome. If you have any improvements, bug fixes, or feature additions, please submit them via pull requests on GitHub.

Acknowledgments:
https://github.com/guptaakshat2002/fire_extinguisher_robot/blob/main/ACKNOWLEDGEMENT.pdf

Authors:
This project is fully supervise and maintain my Akshat Gupta. 

Disclaimer:
This project is for educational and demonstration purposes only. It should not be relied upon as a primary means of fire protection. Always follow proper fire safety protocols and use certified fire extinguishing equipment when necessary.

Contact:
For any inquiries or support, please contact [akshatg989@gmail.com].
