 Churn Analysis
---
---
Team w\: Andrea Huscher, [Gaetano Costa](https://www.linkedin.com/search/results/all/?keywords=gaetano%20costa&origin=GLOBAL_SEARCH_HEADER), [Federico Porcu](https://www.linkedin.com/in/federico-porcu-30b45119b/)

churn analysis for Data Mining proj module 2 [Matteo Calia](https://www.linkedin.com/in/matteo-calia-625954b0/?originalSubdomain=it)
The teacher provides us unstructured data, so we were supposed to clean it, visualize it and then process it. The aim was also to provide economic insights to the 'management' so that
the statistical models and all the visualization works were not for their own sake, indeed oriented to a target and ready-to-go management decision.


1. **EDA** part:
    1. explorative distribution histograms,  bar plots
    1. interactive [Plotly](https://plot.ly/) 
    1. 3D data analysis, multivariate data visualization
    1. economic implications through visualization
1. **Feature Engineering**: 
    1. fill missing obs and NAs, imputer, binned means (TotalCharges and Tenure)
    1. generate offer packages combination to cluster offers (reverse engineering)
    1. clustering Tenure both economic intuition (1 y rule of thumb) and kmeans algo
    1. compute the variable _unnkown costs_ (given the inequality between monthlycharges * tenure != totalcharges )
1. **Variable Importance**:
    1. Correlation matrix 
    1. HeatMap w\ `Seaborn`
1. **Encoding**:
    1. OneHot
    1. MeanEnc
1. **Train Test Splitting**:
    1. sss `StratifiedShuffleSplit`
    1. k fold cross
    1. upsampling to solve unbalance 
1. **Models and hyper tuning**:
    1. Random Forest
    1. XGBOOST
    1. Gradient Boosting
    1. Logistic l1 penalty
    1. Logistic l2 penalty
    1. SVM
1. **Radar plt to compare performance**:
1. **Summarize results**:
    1. [LIME](https://github.com/marcotcr/lime) interpretation
    1. what data suggest to CMO
