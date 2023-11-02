# Regression Module

## Regression 
*In this module, we will analyze, visualize and model various labeled datasets that are being stored in SQL and have continuous target variables. This means we will do supervised machine learning (because the data is labeled) using regression (because the target variable we are analyzing is continuous) on structured data (because the data can be naturally stored in rows and columns).*

## Module Goals

### Acquisition

- **Acquire** structured data from SQL to Pandas
- **Summarize** Summarize the data through aggregates, descriptive stats and distribution plots (histograms, density plots, boxplots, e.g.). (pandas: .value_counts, .head, .shape, .describe, .info, matplotlib.pyplot.hist, seaborn.boxplot)

## Preparation

- **Clean** the data by converting datatypes and handle missing values. (pandas: .isnull, .value_counts, .dropna, .replace)
- **Split** our observations into 3 samples, Train, Validate, and Test. (sklearn.model_selection.train_test_split).

## Exploration

- **Hypothesize**: We will discuss the meaning of "drivers", variables vs. features, and the target variable. We will discuss the importance of documenting questions and hypotheses, obtaining answers for those questions, and documenting takeaways and findings at each step of exploration.
- **Visualize** the interaction of variables, especially independent variables with the dependent variable using charts such as scatterplots, jointplots, pairgrids, and heatmaps to identify drivers.
- **Test Hypotheses** that involve a continuous variable using t-tests and correlation tests.

## Preprocess

- **Encode** any string variables to 0 and 1. Utilize one hot encoding or label encoding.
- **Scale** our numeric data so that all variables are on the same scale, such as between 0 and 1. We will discuss the importance of "scaling", different methods for scaling data, and why to use one type over another. (sklearn.preprocessing: StandardScaler, QuantileTransformer, RobustScaler, MinMaxScaler)
- **Feature Engineering**: We will learn ways to identify, select, and create features through feature importance. We will discuss the "Curse of Dimensionality." (sklearn.feature_selection.f_regression).

## Modeling

- **Establish Baseline**: We will learn about the importance of establishing a "baseline model" or baseline score and ways to complete this task. The baseline for regression is often computed by predicting each observation's value to be the mean or median of the dependent variable.
- **Build Models**: We will build linear regression models. What does that mean? We will extract the patterns in the data using well established algorithms, so that we don't have to do that manually. An example of a regression algorithm is the glm (generalized linear model). The algorithm will return to us a mathematical model or function (e.g. y = 3x + 2). That function will be used to compute predictions for each observation. We will learn about the differences in the most common regression algorithms. (sklearn.linear_model)
- **Model Evaluation**: We will compare regression models by computing evaluation metrics, i.e. metrics that measure how well a model did at predicting the target variable. (sklearn.metrics, math.sqrt)
- **Model Selection and Testing**: We will learn how to select a model, and we will test the model on the unseen data sample (the out-of-sample data in the validate and then test datasets).

## Building a Data Product

We will end with an end-to-end project practicing steps of the data science pipeline from planning through model selection and delivery.