Topic: Build a Machine Learning model to predict the order amount that customers can place in the upcoming days. 

Summary: Introduction to B2B Operations: 
The B2B world operates differently from the B2C or C2C world. Businesses work with other businesses on credit,
When a buyer business orders goods from the seller business, the seller business issues an invoice for the same. 
This invoice for the goods contains various information like the details of the goods purchased and when it should be paid. 


Hello Guys,
In this Project we have created a Order Amount Prediction WebApp using Python Streamlit which is a Regression Problem.
We have gone through several Machine Learning Processes like Data Sanity, EDA, Feature Engineering and Selection, ML Models and Evaluations.
Libraries used: Pandas, numPy, Sklearn, Matplotlib, Seaborn
Platform: Jupyter Notebook, VSCode.
Framework: Python Streamlit.

I have performed Sales Forecasting in above problem and finally selected features like Last Day Sales, Last Day Difference, Division, Unique Customer ID etc.
Coming to Machine Learning Model, I tried with several models like Linear Regression, Decision Tree Regressor, Random Forest Regressor, XGBoost, AdaBoost, Support Vector Machine etc.
Afterall,  I chose Decision Tree Regressor after Selecting best Hyperparameters, with R2 Score of 73%.

Moreover, there are lot many advantages of Decision Tree Model:
Interpretable:
Decision trees provide a clear and intuitive representation of the decision-making process, 
The tree structure with branches and leaf nodes makes it easy to understand the logic behind the predictions.
Each split in the tree represents a decision based on a specific feature and threshold.

Nonlinear relationships:
Decision trees can capture nonlinear relationships between features and the target variable,
They can handle complex interactions and nonlinearity in the data without the need for explicit feature engineering or transformation.

Robust to outliers: 
Decision trees are less sensitive to outliers compared to some other regression models,
Outliers do not heavily influence the decision boundaries since the tree structure considers multiple splits and does not rely on global statistics.
