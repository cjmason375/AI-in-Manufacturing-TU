# AI-in-Manufacturing-TU
GitHub for sharing of files and updates for the ongoing AI in Manufacturing research project at Tuskegee.

(insert more information about the project, ongoing research, and goals)

## *What is Machine Learning?*

>"Machine Learning (ML) is a branch of artificial intelligence (AI) and computer science that focuses on using data and algorithms to enable AI to imitate the way that humans learn, gradually improving its accuracy." ~ [IBM](https://www.ibm.com/topics/machine-learning)

supervised v. unsupervised learning definitions

(put more info)



## *What is Edge Impulse and the BrickML?*

[Edge Impulse](https://edgeimpulse.com/) was founded in 2019 to "enable developers to create the next generation of intelligent devices". With bringing ML on the Edge to everyone is at the core of the company's principles, ...


> "The BrickML is a low-power high-performance self-contained embedded device designed to run machine learning operations at the edge in industry settings." ~ [Edge Impulse](https://edgeimpulse.com/reference-designs/brickml)
 
The BrickML device was developed in conjuction between Edge Impulse and Reloc to make be quickly implemented and make ML more accessible. It is a plug-and-play ML tool ...


## *Gathering and Sorting Data*

### ***Example Project***

For this guide, steps will be provided to create an example ML model capable of classifying 3 labeled shapes using a device's accelerometer data. With the device, you will be able to draw out the shape, and the model will be able to predict what shape it suspects is being drawn.

(add more later)...



### Step 1: *Create the model*

Navigate to the Edge Impulse [Log In](https://studio.edgeimpulse.com/login) page with valid credentials. If you do not already have an account, navigate to the [Sign Up](https://studio.edgeimpulse.com/signup) page and set up your account. 

Once logged into your Studio, click the `+ Create new project` button, enter a Project name, and select the proper parameters.
> For this project, we used a `Personal` project type and `Public` project setting. 

You have now successfully created a Machine Learning project! Now, let us look at how to gather the most important component of ML - data (and lots of it).




### Step 2: *Connecting device and setting up samples*

Ensure you have a [compatible device](https://docs.edgeimpulse.com/docs/edge-ai-hardware/edge-ai-hardware). An alternate method for data collection would be to use the [Data forwarder](https://docs.edgeimpulse.com/docs/tools/edge-impulse-cli/cli-data-forwarder) or [Edge Impulse for Linux](https://docs.edgeimpulse.com/docs/tools/edge-impulse-for-linux) Software Development Kit (SDK) to collect data from another development board or mobile phone. 

Back in the Studio, select the waffle menu at the top left and navigate to the `Data acquisition` tab. 

**Connect your device to your computer**. For the sake of continuinity with the example project, all further references to the "data collection device" will reference specific instructions for the **BrickML module**. However, if using an alternate data collection device, instructions should be similar but may require extra steps.

For the BrickML module, plug a Type-C cable into the BrickML and connect the cable to your computer. Select the USB trident symbol (rightmost symbol on `Collect data` section) and connect to your device from here. Once connected, options for *Device, Label, Sensor, Sample length (ms.), and Frequency* should appear under the `Collect data` section. Definitions of each are provided below:

+ **DEVICE**: allows you to select the proper data collection device (should already display name of device you just connected)
+ **LABEL**: allows you to assign identifiers to groups of collected data so the computer can group together similar data
+ **SENSOR**: determines what family of sensors will be used to collect data during the sample
+ **SAMPLE LENGTH (ms)**: determines the length of the sample, in milliseconds
+ **FREQUENCY:** determines how often you want the sensors to collect data within the sample, in Hertz

Select the proper parameters for your project based on the model intention and intended results.

![Collect new data screen](https://github.com/cjmason375/AI-in-Manufacturing-TU/assets/107148984/862cff44-882f-40ac-9c32-ef30d7a6dbd8)

> + **DEVICE**: BrickML device
> + **LABEL**: one of three labels for intended shapes to detect (Circle, Triangle, Square)
> + **SENSOR**: Intertial (accelerometer data is needed)
> + **SAMPLE LENGTH (ms)**: 5000 ms (5 seconds)
> + **FREQUENCY:** 100 Hz (left this setting as the standard)



### Step 3: *Collecting samples*

+ **TRAINING DATA**: ...
+ **TESTING DATA**: ...

A general good rule of thumb is to balance your TRAINING and TESTING data into an 80/20 split - 80% of total collected data should go into the TRAIN section, and the remaining 20% should go into the TEST section.

> For this project, 30 total samples of each label will be collected (90 samples between the 3 labels). Of those 30 trials, 25 trials will be reserved as TRAIN data while 5 samples will be moved to the TEST data. This will result in a 83%/17% split.)

**Sample desired data.** Edit the sample label (if needed), set up your device, and click the `Start sampling` button to begin your sample. The button will then change to display `Sampling... (time left)`, and once the sample is finished, the sample's data will automatically be added to `Dataset` panel in the TRAINING area. Complete these samples on a specific label until you have reached the total number (both TRAIN and TEST sets) for that label, then move on to your next label.

> Since machine learning needs to be trained on specific  examples to complete a certain process, the way you collect samples should be similar to the way the device will be used. Therefore, samples for this project were collected by drawing out shapes on a flat surface using the device. Although a guide was originally used to trace the same shape every sample, it was discovered later that de-standardizing the data helped the ML model predict a wider variety of options. When sampling for projects, be diverse! Incorporate different sizes, speeds, etc. to provide the model with more information to learn from.

> "Make sure to perform variations on the motions. E.g. do both slow and fast movements and vary the orientation of the board. You'll never know how your user will use the device." ~ [EdgeImpulse](https://docs.edgeimpulse.com/docs/tutorials/end-to-end-tutorials/continuous-motion-recognition)

Upon clicking on a sample from the `Dataset` panel, you can view a *raw data graph* of the collected data. The graph is color-coded for each sensor that collected data, and a legend exists below the graph. Use these graphs to inspect and determine if the collected data appears as you would expect. 

(insert image of graphed data)


### Step 4: *Sorting data*

As mentioned in the previous step, the ML model will learn what is available as prediction options through the labeled data in the TRAINING set. However, since all data should currently be in the TRAINING set, the ML model currently has nothing to test its predictions against when it is training. Therefore, we need to move some of the TRAINING data to become TEST data.

Edge Impulse makes this process as easy as clicking on the 3-dot menu beside a sample and selecting `Move to test set`. However, it is important to randomize this process to ensure similar data (ex: 3 samples collected back-to-back) is not inflicting bias upon the model's TESTING set.

> Once all samples were collected, a Random Number Generator was used from 1 to the total number of samples for a label (NOT total number of samples overall) to move random samples.

As you move samples from the TRAINING section to the TEST section, the two graphs above the `Dataset` panel become increasingly important. The "DATA COLLECTED" graph displays the total seconds of data collected, but it also shows you how the total data is split up between label groups. The "TRAIN/TEST SPLIT" shows users a graphical and numerical view of the split between the TRAIN and TEST data. Hovering over either graph provides more specific details.




### Step 5: *Designing an Impulse*
+ **IMPULSE**: ...

## *Setting Up a Machine Learning Model (with Edge Impulse)*



## *Deploying the Machine Learning Model*



## *Completed Research Tasks*



## *Update Log*

Please see (attach another read.me file where daily updates can be stored)


