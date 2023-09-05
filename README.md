# image_quality_detection

Data Analysis, Model Training, and Evaluation 

1. Data Preparation and Augmentation 

   - Load and preprocess images using an ImageDataGenerator for training, validation, and testing. 

   - Apply data augmentation techniques like rotation, shifting, shearing, zooming, and flipping. 

  

2. Data Visualization 

   - Generate visualizations to understand the distribution of different classes in the dataset using bar plots. 

   - Visualize batches of images from the training and test datasets. 

  

3. Model Architecture 

   - Create a convolutional neural network (CNN) model using Keras with layers like Conv2D, MaxPooling2D, Flatten, Dense, and Dropout. 

  

4. Model Compilation and Training 

   - Compile the model using the Adam optimizer and binary cross-entropy loss. 

   - Train the model using the fit_generator method with training and validation data, specifying the number of steps and epochs. 

   - Utilize a ModelCheckpoint callback to save the best model during training. 

  

5. Training Evaluation 

   - Plot training metrics (loss and accuracy) using a line plot. 

  

6. Model Evaluation 

   - Load the best model from the saved checkpoints. 

   - Predict class probabilities using the test dataset. 

   - Define a threshold and convert probabilities into class predictions. 

   - Display a confusion matrix and classification report to evaluate the model's performance. 

  

7. Visualization of Misclassified Images 

   - Display misclassified images along with their true and predicted labels. 

   - Calculate and visualize the probability of the predicted class.
  

Flask (app.py) 
1. Flask Setup 

   - Import required modules and load the trained Keras model. 

  

2. App Routes 

   - Define routes for different functionalities of the web application. 

  

3. Index Route 

   - Render the imgindex.html template for uploading an image. 

  

4. Prediction Route 

   - Receive an uploaded image, preprocess it, and make predictions using the loaded model. 

   - Display the predicted class and the uploaded image along with the prediction. 

  

5. Run the Flask App 

   - Run the Flask application on the specified host and port
