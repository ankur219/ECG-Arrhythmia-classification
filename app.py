from __future__ import division, print_function
import json
# coding=utf-8
import sys
import os
import glob
import re
import numpy as np
import cv2
import pandas as pd
import numpy as np
import biosppy
import matplotlib.pyplot as plt
# Keras
from keras.applications.imagenet_utils import preprocess_input, decode_predictions
from keras.models import load_model
from keras.preprocessing import image

# Flask utils
from flask import Flask, redirect, url_for, request, render_template
from werkzeug.utils import secure_filename
from gevent.pywsgi import WSGIServer

# Define a flask app
app = Flask(__name__)


# Model saved with Keras model.save()

# Load your trained model
model = load_model('path to the model')
model._make_predict_function()          # Necessary
print('Model loaded. Start serving...')
output = []
# You can also use pretrained model from Keras
# Check https://keras.io/applications/
#from keras.applications.resnet50 import ResNet50
#model = ResNet50(weights='imagenet')
#print('Model loaded. Check http://127.0.0.1:5000/')

def model_predict(uploaded_files, model):
    flag = 1
    
    for path in uploaded_files:
        #index1 = str(path).find('sig-2') + 6
        #index2 = -4
        #ts = int(str(path)[index1:index2])
        APC, NORMAL, LBB, PVC, PAB, RBB, VEB = [], [], [], [], [], [], []
        output.append(str(path))
        result = {"APC": APC, "Normal": NORMAL, "LBB": LBB, "PAB": PAB, "PVC": PVC, "RBB": RBB, "VEB": VEB}

        
        indices = []
        
        kernel = np.ones((4,4),np.uint8)
        
        csv = pd.read_csv(path)
        csv_data = csv[' Sample Value']
        data = np.array(csv_data)
        signals = []
        count = 1
        peaks =  biosppy.signals.ecg.christov_segmenter(signal=data, sampling_rate = 200)[0]
        for i in (peaks[1:-1]):
           diff1 = abs(peaks[count - 1] - i)
           diff2 = abs(peaks[count + 1]- i)
           x = peaks[count - 1] + diff1//2
           y = peaks[count + 1] - diff2//2
           signal = data[x:y]
           signals.append(signal)
           count += 1
           indices.append((x,y))

            
        for count, i in enumerate(signals):
            fig = plt.figure(frameon=False)
            plt.plot(i) 
            plt.xticks([]), plt.yticks([])
            for spine in plt.gca().spines.values():
                spine.set_visible(False)

            filename = 'fig' + '.png'
            fig.savefig(filename)
            im_gray = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)
            im_gray = cv2.erode(im_gray,kernel,iterations = 1)
            im_gray = cv2.resize(im_gray, (128, 128), interpolation = cv2.INTER_LANCZOS4)
            cv2.imwrite(filename, im_gray)
            im_gray = cv2.imread(filename)
            pred = model.predict(im_gray.reshape((1, 128, 128, 3)))
            pred_class = pred.argmax(axis=-1)
            if pred_class == 0:
                APC.append(indices[count]) 
            elif pred_class == 1:
                NORMAL.append(indices[count]) 
            elif pred_class == 2:    
                LBB.append(indices[count])
            elif pred_class == 3:
                PAB.append(indices[count])
            elif pred_class == 4:
                PVC.append(indices[count])
            elif pred_class == 5:
                RBB.append(indices[count]) 
            elif pred_class == 6:
                VEB.append(indices[count])
        


        result = sorted(result.items(), key = lambda y: len(y[1]))[::-1]   
        output.append(result)
        data = {}
        data['filename'+ str(flag)] = str(path)
        data['result'+str(flag)] = str(result)

        json_filename = 'data.txt'
        with open(json_filename, 'a+') as outfile:
            json.dump(data, outfile) 
        flag+=1 
    



    with open(json_filename, 'r') as file:
        filedata = file.read()
    filedata = filedata.replace('}{', ',')
    with open(json_filename, 'w') as file:
        file.write(filedata) 
    os.remove('fig.png')      
    return output
    
    

    
    


@app.route('/', methods=['GET'])
def index():
    # Main page
    return render_template('index.html')


@app.route('/predict', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        # Get the file from post request
        uploaded_files = []

        # Save the file to ./uploads
        print(uploaded_files)
        for f in request.files.getlist('file'):

            basepath = os.path.dirname(__file__)
            file_path = os.path.join(
            basepath, 'uploads', secure_filename(f.filename))
            print(file_path)
            if file_path[-4:] == '.csv':
                uploaded_files.append(file_path)
                f.save(file_path)
        print(uploaded_files)        
        # Make prediction
        pred = model_predict(uploaded_files, model)


        # Process your result for human
                    # Simple argmax
        #pred_class = decode_predictions(pred, top=1)   # ImageNet Decode
        #result = str(pred_class[0][0][1])               # Convert to string
        result = str(pred)
        

        return result
    return None


if __name__ == '__main__':
    # app.run(port=5002, debug=True)

    # Serve the app with gevent
    http_server = WSGIServer(('', 5000), app)
    http_server.serve_forever()
