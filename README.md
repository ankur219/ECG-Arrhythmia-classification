# ECG-Arrhythmia-classification
## ECG arrhythmia classification using a 2-D convolutional neural network

I have implemented this paper https://arxiv.org/pdf/1804.06812.pdf in which we classify ECG into seven categories, one being normal and the other six being different types of arrhythmia using deep two-dimensional CNN with grayscale ECG images. By transforming one-dimensional ECG signals into two-dimensional ECG images, noise filtering and feature extraction are no longer required. This is important since some of ECG beats are ignored in noise filtering and feature extraction. In addition, training data can be enlarged by augmenting the ECG images which results in higher classification accuracy. Data augmentation is hard to be applied in 1-d signals since the distortion of 1-d ECG signal could downgrade the performance of the classifier. However, augmenting two-dimensional ECG images with different cropping methods helps the CNN model to train with different viewpoints of the single ECG images. Using ECG image as an input data of the ECG arrhythmia classification also benefits in the sense of robustness.


## METHOD
![alt text](https://cdn-images-1.medium.com/max/1000/1*3SGHOVg_ycSOH-NN6OI8Tg.png)

## MODEL
Here is the link to the model: https://drive.google.com/open?id=1aFKVKz41A9fu8dX2KfwlEGV8vz9ljiuZ
## Deploying the model
1. Clone my repository.
2. Clone this https://github.com/mtobeiyf/keras-flask-deploy-webapp repository. 
3. Download the weights.
4. Replace app.py in the other repository you have downloaded with the app.py from my repository.
5. Replace index.html as well that is present in the other repository with the index.html that is provided in my repo. index.html in present in the "templates" folder of the repository.

If you face any other problem related to deploying you can check https://github.com/mtobeiyf/keras-flask-deploy-webapp repository.

The model works only if your data is similar to # sample.csv

## Here is a screenshot of the app from my system
![alt text](https://cdn-images-1.medium.com/max/1400/1*DbcZlDPIfRYLZknTrjcJLw.png)

## Medium Blog
You can find all the details of this project on my Medium post. Link to my Medium post is over here: https://medium.com/datadriveninvestor/ecg-arrhythmia-classification-using-a-2-d-convolutional-neural-network-33aa586bad67


