# ECG-Arrhythmia-classification
## ECG arrhythmia classification using a 2-D convolutional neural network

I have implemented this paper https://arxiv.org/pdf/1804.06812.pdf in which we classify ECG into seven categories, one being normal and the other six being different types of arrhythmia using deep two-dimensional CNN with grayscale ECG images. By transforming one-dimensional ECG signals into two-dimensional ECG images, noise filtering and feature extraction are no longer required. This is important since some of ECG beats are ignored in noise filtering and feature extraction. In addition, training data can be enlarged by augmenting the ECG images which results in higher classification accuracy. Data augmentation is hard to be applied in 1-d signals since the distortion of 1-d ECG signal could downgrade the performance of the classifier. However, augmenting two-dimensional ECG images with different cropping methods helps the CNN model to train with different viewpoints of the single ECG images. Using ECG image as an input data of the ECG arrhythmia classification also benefits in the sense of robustness.


## METHOD
![alt text](https://cdn-images-1.medium.com/max/1000/1*3SGHOVg_ycSOH-NN6OI8Tg.png)

## MODEL
I will soon provide the link to the model's weights.

## Deploying the model
Once you have the model's weights you can provide the path to the model in app.py. You will need to clone this repository: https://github.com/mtobeiyf/keras-flask-deploy-webapp and replace the app.py in this repository with the app.py from my repository.
Other details of deploying the model are given in the above mentioned repository.

## Here is a screenshot of the app from my system
![alt text](https://cdn-images-1.medium.com/max/1400/1*DbcZlDPIfRYLZknTrjcJLw.png)

## Medium Blog
Link to my Medium post is over here: https://medium.com/datadriveninvestor/ecg-arrhythmia-classification-using-a-2-d-convolutional-neural-network-33aa586bad67


