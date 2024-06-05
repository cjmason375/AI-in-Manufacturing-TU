# Summer Research at Purdue, 2024
*By Everett "CJ" Mason, Jr.*

#### [BrickML Box Official User Manual](https://www.reloc.it/download/products/RD-BML/R22P04P1XDT00_BrickML-Box_UserManual_r11.pdf)

## Details about BrickML

> "***BrickML*** is a low-power high-performance self-contained embedded device designed to run machine learning operations at the edge in industry settings." ~ [Reloc](https://www.reloc.it/download/products/RD-BML/R22P04P1XDT00_BrickML-Box_UserManual_r11.pdf)

The BrickML module is designed to be mounted directly onto equipment for environmental, sound, and motion-related Machine Learning (ML) data collection. With on-board computing, sensing, and communication capabilities, the BrickML is also resistant to rugged use (dust and moisture resistant). Direct interfacing with Edge Impulse ML software allows for less development time while also allowing users a flexible suite for custom development. 


## Technical Specifications
+ *Sensors*:
  + AUDIO: Microphone (100 Hz - 80,000 Hz)
  + MOTION: 9-axis inertial sensor (accelerometer, gyroscope, geomagnetic sensor)
  + CURRENT: voltage input to ADC for MCSA applications
  + ENVIRONMENT: Temperature/Humidity (T/H) sensor
+ *Microcontroller unit (MCU)*: 32-bit ARM Cortex-M33 core with FPU and 200 MHz clock speed
  + Up to 2-MB program memory
  + Up to 8-KB data flash
  + Up to 128-Mbit on-board serial flash
  + Up to 512-KB data memory
+ *Communication*: Bluetooth low energy (BLE) 5.1
+ *Supply Voltage*: +5.0 V to +24 V single power supply
+ *Operating temperature range*: -20 C to +70 C
+ *Dimensions*: 89 mm x 79 mm x 33 mm

![Left Side - Sensors / Right Side - Connectivity / Middle - MCU and BLE](https://github.com/cjmason375/AI-in-Manufacturing-TU/assets/107148984/9e85f5ea-b1f2-4ef5-aaf2-a82c6c48329d)


## Industrial IoT
(*Purdue ME597, IIot Implementation for Smart Manufacturing*)

### Pipeline:
1. ***Data Collection*** : implementing IoT sensor CONNECTIVITY and COMMUNICATION on target machines following industry standard protocols
2. ***Middleware*** : allow hardware devices (some of which are legacies) to communicate and integrate technologies (the "glue for service-oriented application") 
3. ***Database and visualization*** : ??
4. ***Machine Learning*** : training ML model and implementing model on an edge computer to perform real-time recognition
    + **Data Analysis:** handling, indexing, graph plotting, signal processing, feature extraction and selection, and visualization 
    + **ML Training:** neural network, hyperparameter optimization
    + **Real-Time Implementation:** continous data preprocessing, autoencoder-guided data visualization, multi-classification for process monitoring
  

## BrickML for Continuous Data Collection

### [Predictive Maintenance w/ Sony Spresense and CommonSense](https://edgeimpulse.com/case-studies/predictive-maintenance-with-sony-spresense-and-commonsense)
+ Sony Spresense MCU - "powerhouse dev. board", compact, ample I/O pins and hookups for camera, mic, and speakers (designed for Sony's smart earbuds), can connect to GPS, energy efficient
  + processing of sensor inputs and ML model predictions occur onboard
+ CommonSense sensor board (SensiEDGE) - stacks 10 additional environmental sensors onto Spresense
  + w/ two boards coupled together, data from sensors is directly accessible for users in EdgeImpulse
  + Air quality, Accelerometer, Magnetometer, Gyro, Temperature, Microphone, Proximity, Humidity, Pressure, Light
+ use EdgeImpulse for creating and running AI algorithms directly on edge devices
  + web-based platform and Python SDK allow ability to gather and label data, train and optimize model, and load directly onto Edge device
  + offers built-in algorithms (classification, object detection, anomaly detection)
  + able to reduce development time and resources
  + natively supported devices allow you to access the board and sensors directly in platform (to gather data, build algorithm, deploy onto board)

### [Serial Daemon](https://docs.edgeimpulse.com/docs/tools/edge-impulse-cli/cli-daemon)
### [EI CLI](https://docs.edgeimpulse.com/docs/tools/edge-impulse-cli/cli-installation)
### [Industry Reference Design - BrickML](https://docs.edgeimpulse.com/docs/edge-ai-hardware/production-ready/the-brickml)
### [Data Sources](https://docs.edgeimpulse.com/docs/edge-impulse-studio/data-acquisition/data-sources)
### [Sensor Fusion](https://docs.edgeimpulse.com/docs/tutorials/end-to-end-tutorials/sensor-fusion)
### [Visualizing Complex Datasets](https://edgeimpulse.com/blog/visualizing-complex-datasets-in-edge-impulse/)


#### [Recognizing sound from audio](https://docs.edgeimpulse.com/docs/tutorials/end-to-end-tutorials/audio-classification)
### [Continous Sampling](https://docs.edgeimpulse.com/docs/tutorials/advanced-inferencing/continuous-audio-sampling)

