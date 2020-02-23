 Churn Analysis
---
churn analysis for Data Mining proj module 2 [Matteo Calia](https://www.linkedin.com/in/matteo-calia-625954b0/?originalSubdomain=it)
The teacher provides us a semi messed up dataset, so we were supposed to clean it, visualize it and the process it. 
the following points summarize what we did during the proj. The aim was also to provide economic insights to the 'management' so that
the statistical model and all the visualization works was not for its own sake, indeed oriented to an applicable potential management choice.


1. **EDA** part bar plots, distribution histograms, interactive [Plotly](https://plot.ly/) and following economic implications 
1. Feature Engineering: 
    1. fill missing obs and NAs, binned means and so on for TotalCharges
    1. comparing == MonthlyCharges economic contract offers to replace the missings
    1. segmenting Internet Service NO wrt to the MonthlyCharges
    1. segmenting tenure so that they are grouped in a 5 level category
    1. compute the variable _unnkown costs_ (inequality between monthlycharges * tenure != totalcharges )
1. Variable Importance:
    1. Correlation matrix 
    1. HeatMap w\ `Seaborn`
    1. `RandomForestClassifier` 
    1. [LIME](https://github.com/marcotcr/lime) technique
 1. Train Test Splitting 
    1. sss `StratifiedShuffleSplit` 
 1. Models
    1. Random Forest
    1. XGBOOST
    1. Decision Trees
    1. NNs
1. Hyper parameter tuning
1. Summarize results.