# AgriTech Crop Suggestions System

<p align="center">
  <img src="https://www.cropin.com/hubfs/Imported_Blog_Media/agriculture-to-agritech-1.jpg" alt="Crop Suggestions System">
</p>

## Overview

Welcome to the AgriTech Crop Suggestions System! This project provides an intelligent crop suggestion system and fertilizer recommendation based on input parameters such as soil nutrients, pH, rainfall, and location. Follow the steps below to set up and utilize the system effectively.

## 🚀 Setup

1. Download all the necessary libraries (Pandas, Numpy, sklearn, pickle, Flask).
2. Upload the entire `Crop_suggestion_system` folder into your preferred IDE, such as PyCharm (which we used).
   - **Note:** Upload the entire folder as it includes dataset folders and images for creating web pages.
3. Check for any errors related to package installations. If any, install the necessary libraries to resolve errors.

## 🏃 Running the Model and Web Interface

- For the classification report (accuracy or score) of the model, navigate to the `MLmodel.py` file and run it to see the obtained results.
- To run the entire project, go to the `myapp.py` file and execute it.


## Run the model
python MLmodel.py
## 🌐 Running the Web Interface
https://crop-suggestion-system-5exc.vercel.app/
# Execute the following command:
python myapp.py

 Visit the provided HTTP link in your browser; you will be redirected to a Chrome webpage with an interface.

## 🌱 Crop Suggestions
- Scroll down on the homepage and click on the image labeled with "Crop." 
- This will redirect you to another page where you can enter details like:
- Nitrogen: 3
- Phosphorous: 2
- Potassium: 4
- pH: 0.03
- Rainfall: 0.02
- City: Karlskrona
- Submit to get the crop suggestion.

## 💡 Fertilizer Recommendations
 Go back to the homepage, scroll down, and click on the image labeled "Fertilizer." 
- This will redirect you to another page where you can enter details like:
- Crop Name: Rice
- Nitrogen: 3
 -Phosphorous: 2
  - Potassium: 4
 Submit to get the fertilizer recommendation.

 Note: When entering the crop name, use exact names (including lowercase) from the given list below, or you may encounter an error:
 [rice, maize, chickpea, kidneybeans, pigeonpeas, mothbeans, mungbean, blackgram, lentil, pomegranate, banana, mango, apple, grapes, watermelon, muskmelon, orange, papaya, coconut, cotton, jute, coffee]
