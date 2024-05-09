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
> + **LABEL**: one of three labels for intended shapes to detect (Straight_Line, Trapezoid, Oval)
> + **SENSOR**: Intertial (accelerometer data is needed)
> + **SAMPLE LENGTH (ms)**: 5000 ms (5 seconds)
> + **FREQUENCY:** 100 Hz (left this setting as the standard)



### Step 3: *Collecting samples*

+ **TRAINING DATA**: ...
+ **TESTING DATA**: ...

A general good rule of thumb is to balance your TRAINING and TESTING data into an 80/20 split - 80% of total collected data should go into the TRAIN section, and the remaining 20% should go into the TEST section.

> For this project, 25 total samples of each label will be collected (75 samples between the 3 labels). Of those 30 trials, 20 trials will be reserved as TRAIN data while 5 samples will be moved to the TEST data. This will result in a 80%/20% split.)

**Sample desired data.** Edit the sample label (if needed), set up your device, and click the `Start sampling` button to begin your sample. The button will then change to display `Sampling... (time left)`, and once the sample is finished, the sample's data will automatically be added to `Dataset` panel in the TRAINING area. Complete these samples on a specific label until you have reached the total number (both TRAIN and TEST sets) for that label, then move on to your next label.

> Since machine learning needs to be trained on specific  examples to complete a certain process, the way you collect samples should be similar to the way the device will be used. Therefore, samples for this project were collected by drawing out shapes on a flat surface using the device. Although a guide was originally used to trace the same shape every sample, it was discovered later that de-standardizing the data helped the ML model predict a wider variety of options. When sampling for projects, be diverse! Incorporate different sizes, speeds, etc. to provide the model with more information to learn from.

> "Make sure to perform variations on the motions. E.g. do both slow and fast movements and vary the orientation of the board. You'll never know how your user will use the device." ~ [EdgeImpulse](https://docs.edgeimpulse.com/docs/tutorials/end-to-end-tutorials/continuous-motion-recognition)

Upon clicking on a sample from the `Dataset` panel, you can view a *raw data graph* of the collected data. The graph is color-coded for each sensor that collected data, and a legend exists below the graph. Use these graphs to inspect and determine if the collected data appears as you would expect. 


![Graphed Data Ex](https://github.com/cjmason375/AI-in-Manufacturing-TU/assets/107148984/8d164b4c-7be0-4134-beff-2c7e1396f3da)




### Step 4: *Sorting data*

As mentioned in the previous step, the ML model will learn what is available as prediction options through the labeled data in the TRAINING set. However, since all data should currently be in the TRAINING set, the ML model currently has nothing to test its predictions against when it is training. Therefore, we need to move some of the TRAINING data to become TEST data.

Edge Impulse makes this process as easy as clicking on the 3-dot menu beside a sample and selecting `Move to test set`. However, it is important to randomize this process to ensure similar data (ex: 3 samples collected back-to-back) is not inflicting bias upon the model's TESTING set.

> Once all samples were collected, a Random Number Generator was used from 1 to the total number of samples for a label (NOT total number of samples overall) to move random samples.

As you move samples from the TRAINING section to the TEST section, the two graphs above the `Dataset` panel become increasingly important. The "DATA COLLECTED" graph displays the total seconds of data collected, but it also shows you how the total data is split up between label groups. The "TRAIN/TEST SPLIT" shows users a graphical and numerical view of the split between the TRAIN and TEST data. Hovering over either graph provides more specific details.

![Data Collected Graph and Test-Train Graph examples](https://github.com/cjmason375/AI-in-Manufacturing-TU/assets/107148984/153e7e24-7907-4f42-b41b-d3bbb07604f6)



### Step 5: *Designing an Impulse*
+ **IMPULSE**: ...
+ **PROCESSING BLOCKS**: ...
+ **LEARNING BLOCKS**: ...

With all data collected for training, it is now time to create an ***Impulse*** for your project. The Impulse serves as the central location for the important Machine Learning processes - raw data is interpreted and sliced into smaller windows, signal PROCESSING blocks extract features of training data and makes raw data easier to process, and LEARNING blocks learn from the training data to classify new data.

Select the waffle menu at the top left and navigate to the `Impulse design` tab, then select the `Create impulse`.

Here, you will see menus for editing time parameters of the raw data, adding a PROCESSING block and a LEARNING block, and the features that will be output. 

For this project, we will use a ***Spectral analysis*** signal processing block and a ***Classifier*** learning block. The *Spectral Analysis* block "applies a filter, performs spectral analysis on the signal, and extracts frequency and spectral power data". The *Classifer* block will evalaute these spectral features and learn to distinguish between the three classes (Straight_Line, Trapezoid, Oval). EdgeImpulse also suggests appropriate PROCESSING and LEARNING blocks based on the data you collected, signified by the yellow star under the RECOMMENDED column when selecting a block. For more information on the other options for [PROCESSING](https://docs.edgeimpulse.com/docs/edge-impulse-studio/processing-blocks) and [LEARNING](https://docs.edgeimpulse.com/docs/edge-impulse-studio/learning-blocks) blocks and to gain more insight, visit the attached links.  

> In the `Time series data` panel, adjust `Window size` to 2,500 ms., `Window increase` to 100 ms, and do not change the default values for `Frequency` and `Zero-pad data`.
> Select `Add a processing block` and select ***Spectral Analysis***. De-select all input axes beginning with "gyr..." as this is gyroscope data and is not needed for this project. Only *accX*, *accY*, and *accZ* should be left selected.
> Select `Add a learning block` and select ***Classifier***. Ensure "Spectral features" is selected as Input features.
> Under `Output features`, ensure all labels are showing. Then, select `Save Impulse`.


![Impulse Design Panel](https://github.com/cjmason375/AI-in-Manufacturing-TU/assets/107148984/29ff2baf-d92b-4aa0-ad5d-a068143d25bb)



### Step 6: *Training Model Using Impulse: Generating features*

Now, the true fun begins - training your Machine Learning model!

Select the waffle menu at the top left and, below the `Impulse design` tab, select `Spectral features`.

This menu will allow you to configure the selected PROCESSING block. At the top, the "Raw data" graph allows you to view the graphed data of each sample (accessed by drop-down menu at top rigth). The graph on the right, "DSP result", shows the processing results on the data. For more information about the [Spectral Features](https://docs.edgeimpulse.com/docs/edge-impulse-studio/processing-blocks/spectral-features) processing block, visit the attached link. 

> Set up your project as shown below, then click `Save parameters`:


![Spectral Features Parameters](https://github.com/cjmason375/AI-in-Manufacturing-TU/assets/107148984/5746fa06-6806-410d-aec8-2375c3e54382)


The next screen you are brought to is the ***"Feature generation"*** menu. Here, the data will be split into windows (based on the window size and increase), the spectral features block will be applied to those windows, and the *feature importance* will be calculated.

> Once satisfied with all settings, click `Generate features` and wait for your computer to finish the process.

After the feature generation process is completed, the `"Feature Explorer"` will populate on the screen. This graphed area displays the color-coded extracted features plotted with all generated windows. An important step here is to evaluate this data as this is what your ML model will be trained on. If you can visually identify clusters of similar features, then the ML model will likely be able to do so as well. However, if the data appears to be poorly seperated though, you might have bad data - consider adding more data or re-evaluating your data collection method.

Example of bad data:
![BAD Feature Generation Results](https://github.com/cjmason375/AI-in-Manufacturing-TU/assets/107148984/2e241f4a-5f01-49a7-8c92-8aa2c72fb925)


Example of good data:
![GOOD Feature Generation Results](https://github.com/cjmason375/AI-in-Manufacturing-TU/assets/107148984/cb193210-938c-42b0-9511-4404f50a1a90)





### Step 7: *Training Model Using Impulse: Training with Classifer*
+ **NEURAL NETWORK**: a collection of pattern-recognizing algorithms that follow a similar process as the human brain

Now that all data has been processed, it is time to start training the neural network (NN) of the ML model. The NN will take the PROCESSING data and attempt to map this data to the available classes (based on the 3 labels). To learn more about how the [Classifier](https://docs.edgeimpulse.com/docs/edge-impulse-studio/learning-blocks/classification) LEARNING block works, visit the attached link.

Select the waffle menu at the top left and, below the `Impulse design` tab, select `Classifier`.

Here, you will be faced with options to change settings for "Number of training cycles", "Use learned optimizer", "Learning rate", and "Training processor". Seeing as changing the settings for every option besides training cycles requires an Enterprise subscription, those settings will be left as default. When changing the number of training cycles, one must consider overfitting and underfitting.

+ **OVERFITTING**: Models that are *overfit* display a HIGH variance and LOW bias. Therefore, the model may be too complex and specific to training data, and may fail when used on testing or real-world data. To fix overfitting, you can improve the quality of training data,reduce the number of training cycles (epochs), reduce complexity, or stop the training as soon as loss begins to increase.
+ **UNDERFITTING**: Models that are *underfit* display a HIGH bias and LOW variance. Therefore, the model may be too simple and not properly represent data complexity. To fix underfitting, you can increase the model complexity or number of features, remove noise, or increase the number of training cycles (epochs).

> Set the "Number of training cycles" to 30. To see the effects of overfitting or underfitting, set the training cycles a number much higher and much lower than 30, respectively. 

With all parameters set, click `Start training` to begin training with the Classifier.

After the `Training output" panel finishes the job, accuracy and loss percentages will be displayed, as well as another confusion matrix. This confusion matrix, however, represents ... . Below the matrix, you can find the same graph from the Spectral Features tab, but it will now represent correctly and incorrectly labeled data.

...

![Screenshot 2024-05-09 at 1 55 42 PM](https://github.com/cjmason375/AI-in-Manufacturing-TU/assets/107148984/2f30644c-4bc1-4847-83ed-3f7a8713849d)

> Although the accuracy of the Classifier happens to be 100% for this model, that is not always a good thing - it may mean your model is overfit! It is important to not force your data into standardization through too many learning cycles, and having a diverse model is more important for classifying real-world data. Refer to the overfitting definition above for possible fixes.

Congratulations! You have successfully created a Neural Network and have trained your model!




### Step 8: *Testing your Model*

Now that your model is fully trained, it is time to put it to the test! There are two primary methods for testing your model: `Live Classification` and `Model Testing`. For the intents of this guide, we will use the Model Testing option - however, depending on the desired final result of your model, using both methods can lead to a more operational model and expose potential issues that may arise later in real-world use.

Select the waffle menu at the top left and select `Model testing`.

In the `Test data` panel, you will find the set of data you earlier moved into the TEST section. The `Model tesing` process works in a similar manner as the Classifer - however, the datasets that are used are different. The `Classifier` data uses training data to teach the model. However, throughout training, the `Model testing` data has not been accessed by the model as it serves a sole purpose - to be used as verifications of how well the model performs on unseen data.

> Edge Impulse automatically attaches the label of the sample as the "Expected Outcome", but review the "Expected Outcome" for each sample and ensure all labels are correct. Then, press `Classify all` to test the model against this unseen data.


![Screenshot 2024-05-09 at 2 34 44 PM](https://github.com/cjmason375/AI-in-Manufacturing-TU/assets/107148984/d94422e0-062d-4004-9481-c96ee9adf3fc)

As shown below, the `Model testing` results panel looks nearly identical to the `Classifier` panel - the key difference is the F1 score for each shape on the bottom row.

If your model testing results give bad results, consider any parameters that can be changed. Below are some possible fixes to improve the ability of your model to classify unseen data:

+ ***Add more unique data!*** Increasing the amount of unique data that a model is trained on exposes the model to more features, which often increases the ability of the model to classify new data.
+ ***Make sure the device is being used in the manner for which the ML model was trained!*** If the device is attempting to classify data that was captured in a different manner than data was collected, the model will be confused as it was not trained for that use case. Also, consider adding unique data so the model can classify a wider variety of data.
+ ***Ensure the model has been trained enough.*** Consider increasing the number of training cycles (epochs) and obseve the performance on impact. Be careful to not overfit your model, though (can reduce learning rate or add more data to reduce overfitting).
+ ***The neural network architecture is not a great fit for your data.*** Change the number of layers and neurons and observe performance improvement.

Once you have adjusted the model's parameters and received desired results from `Model testing`, you have sucessfully set up your Machine Learning model. Congratulations!











## *Deploying the Machine Learning Model*



## *Completed Research Tasks*



## *Update Log*

Please see (attach another read.me file where daily updates can be stored)


