# AI-in-Manufacturing-TU
GitHub for sharing of files and updates for the ongoing AI in Manufacturing research project at Tuskegee.

(insert more information about the project, ongoing research, and goals)

## *What is Machine Learning?*

>"Machine Learning (ML) is a branch of artificial intelligence (AI) and computer science that focuses on using data and algorithms to enable AI to imitate the way that humans learn, gradually improving its accuracy." ~ [IBM](https://www.ibm.com/topics/machine-learning)

(put more info)



## *What is Edge Impulse and the BrickML?*

[Edge Impulse](https://edgeimpulse.com/) was founded in 2019 to "enable developers to create the next generation of intelligent devices". With bringing ML on the Edge to everyone is at the core of the company's principles, ...


> "The BrickML is a low-power high-performance self-contained embedded device designed to run machine learning operations at the edge in industry settings." ~ [Edge Impulse](https://edgeimpulse.com/reference-designs/brickml)
 
The BrickML device was developed in conjuction between Edge Impulse and Reloc to make be quickly implemented and make ML more accessible. It is a plug-and-play ML tool ...

## *Gathering and Sorting Data*

For this guide, the steps to creating a ML model will be stepped through an example of creating a supervised learning model capable of classifying 3 labeled shapes (add more later)...

### Step 1: *Create the model*

Navigate to the Edge Impulse [Log In](https://studio.edgeimpulse.com/login) page with valid credentials. If you do not already have an account, navigate to the [Sign Up](https://studio.edgeimpulse.com/signup) page and set up your account. 

Once logged into your Studio, click the `+ Create new project` button, enter a Project name, and select the proper parameters.
> For this project, we used a `Personal` project type and `Public` project setting. 

You have now successfully created a Machine Learning project! Now, let us look at how to gather the most important component of ML - data (and lots of it).

### Step 2: *Collect data*

Ensure you have a [compatible device](https://docs.edgeimpulse.com/docs/edge-ai-hardware/edge-ai-hardware). An alternate method for data collection would be to use the [Data forwarder](https://docs.edgeimpulse.com/docs/tools/edge-impulse-cli/cli-data-forwarder) or [Edge Impulse for Linux](https://docs.edgeimpulse.com/docs/tools/edge-impulse-for-linux) Software Development Kit (SDK) to collect data from another development board or mobile phone. 

Back in the Studio, select the waffle menu at the top left and navigate to the `Data acquisition` tab. 

**Connect your device to your computer**. For the sake of continuinity with the example project, all further references to the "data collection device" will reference specific instructions for the **BrickML module**. However, if using an alternate data collection device, instructions should be similar but may require extra steps.

For the BrickML module, plug a Type-C cable into the BrickML and connect the cable to your computer. Select the USB trident symbol (rightmost symbol on `Collect data` section) and connect to your device from here. Once connected, options for *Device, Label, Sensor, Sample length (ms.), and Frequency* should appear under the `Collect data` section. Definitions of each are provided below:
+ **DEVICE**: allows you to select the proper data collection device (should already display name of device you just connected)
+ **LABEL**: allows you to assign identifiers to groups of collected data so the computer can group together similar data
+ **SENSOR**: determines what family of sensors will be used to collect data during the sample
+ **SAMPLE LENGTH (ms.)**: determines the length of the sample, in milliseconds
+ **FREQUENCY:** determines how often you want the sensors to collect data within the sample, in Hertz

Select the proper parameters for your project based on the model intention and intended results.

> + **DEVICE**: BrickML device (displayed as serial code)
> + **LABEL**: one of three labels for intended shapes to detect (Straight_Line, Oval, Trapezoid)
> + **SENSOR**: Intertial (accelerometer data is needed)
> + **SAMPLE LENGTH (ms.)**: ...
> + **FREQUENCY:** 100 Hz (left this setting as the standard)



## *Setting Up a Machine Learning Model (with Edge Impulse)*



## *Deploying the Machine Learning Model*



## *Completed Research Tasks*



## *Update Log*

Please see (attach another read.me file where daily updates can be stored)


