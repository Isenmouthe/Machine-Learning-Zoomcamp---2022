# Breast Cancer Prediction
This is a midterm project for the Zoomcamp 2022. 

## Source of the data:

[Kaggle](https://www.kaggle.com/datasets/yasserh/breast-cancer-dataset?datasetId=1829286)

[UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/datasets/Breast+Cancer+Wisconsin+%28Diagnostic%29)

## Brief Description
Breast cancer is the most common cancer amongst women in the world. It accounts for 25% of all cancer cases, and affected over 2.1 Million people in 2015 alone. It starts when cells in the breast begin to grow out of control. These cells usually form tumors that can be seen via X-ray or felt as lumps in the breast area.

The key challenges against it’s detection is how to classify tumors into malignant (cancerous) or benign(non cancerous).


## According to the data providers: 
>Features are computed from a digitized image of a fine needle aspirate (FNA) of a breast mass. They describe characteristics of the cell nuclei present in the image. 
>Separating plane described above was obtained using Multisurface Method-Tree (MSM-T), a classification method which uses linear programming to construct a decision tree. Relevant features were selected using an exhaustive search in the space of 1-4 features and 1-3 separating planes.

> ### Attribute Information:
- 1) ID number
- 2) Diagnosis (M = malignant, B = benign)

>Ten real-valued features are computed for each cell nucleus (columns: 3-32):

- a) radius (mean of distances from center to points on the perimeter)
- b) texture (standard deviation of gray-scale values)
- c) perimeter
- d) area
- e) smoothness (local variation in radius lengths)
- f) compactness (perimeter^2 / area - 1.0)
- g) concavity (severity of concave portions of the contour)
- h) concave points (number of concave portions of the contour)
- i) symmetry
- j) fractal dimension ("coastline approximation" - 1)

### Problem approach
we need find the best model to predict malignant cancerous cells. 
Try different classification algorithms (RandomForest, XGBoost, maybe(Catboost))