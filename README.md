# ECG-Arrhythmia-classification
## ECG arrhythmia classification using a 2-D convolutional neural network

I have implemented this paper https://arxiv.org/pdf/1804.06812.pdf in which we classify ECG into seven categories, one being normal and the other six being different types of arrhythmia using deep two-dimensional CNN with grayscale ECG images. By transforming one-dimensional ECG signals into two-dimensional ECG images, noise filtering and feature extraction are no longer required. This is important since some of ECG beats are ignored in noise filtering and feature extraction. In addition, training data can be enlarged by augmenting the ECG images which results in higher classification accuracy. Data augmentation is hard to be applied in 1-d signals since the distortion of 1-d ECG signal could downgrade the performance of the classifier. However, augmenting two-dimensional ECG images with different cropping methods helps the CNN model to train with different viewpoints of the single ECG images. Using ECG image as an input data of the ECG arrhythmia classification also benefits in the sense of robustness.


## METHOD
![alt text](https://cdn-images-1.medium.com/max/1000/1*3SGHOVg_ycSOH-NN6OI8Tg.png)
