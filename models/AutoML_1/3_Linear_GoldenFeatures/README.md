# Summary of 3_Linear_GoldenFeatures

[<< Go back](../README.md)


## Logistic Regression (Linear)
- **n_jobs**: -1
- **explain_level**: 2

## Validation
 - **validation_type**: split
 - **train_ratio**: 0.75
 - **shuffle**: True
 - **stratify**: True

## Optimized metric
logloss

## Training time

7.5 seconds

## Metric details
|           |    score |     threshold |
|:----------|---------:|--------------:|
| logloss   | 0.453837 | nan           |
| auc       | 0.891705 | nan           |
| f1        | 0.790419 |   0.445206    |
| accuracy  | 0.825871 |   0.445206    |
| precision | 1        |   0.999684    |
| recall    | 1        |   2.02563e-07 |
| mcc       | 0.648748 |   0.445206    |


## Metric details with threshold from accuracy metric
|           |    score |   threshold |
|:----------|---------:|------------:|
| logloss   | 0.453837 |  nan        |
| auc       | 0.891705 |  nan        |
| f1        | 0.790419 |    0.445206 |
| accuracy  | 0.825871 |    0.445206 |
| precision | 0.733333 |    0.445206 |
| recall    | 0.857143 |    0.445206 |
| mcc       | 0.648748 |    0.445206 |


## Confusion matrix (at threshold=0.445206)
|              |   Predicted as 0 |   Predicted as 1 |
|:-------------|-----------------:|-----------------:|
| Labeled as 0 |              100 |               24 |
| Labeled as 1 |               11 |               66 |

## Learning curves
![Learning curves](learning_curves.png)

## Permutation-based Importance
![Permutation-based Importance](permutation_importance.png)

## SHAP Importance
![SHAP Importance](shap_importance.png)

## SHAP Dependence plots

### Dependence (Fold 1)
![SHAP Dependence from Fold 1](learner_fold_0_shap_dependence.png)

## SHAP Decision plots

### Top-10 Worst decisions for class 0 (Fold 1)
![SHAP worst decisions class 0 from Fold 1](learner_fold_0_shap_class_0_worst_decisions.png)
### Top-10 Best decisions for class 0 (Fold 1)
![SHAP best decisions class 0 from Fold 1](learner_fold_0_shap_class_0_best_decisions.png)
### Top-10 Worst decisions for class 1 (Fold 1)
![SHAP worst decisions class 1 from Fold 1](learner_fold_0_shap_class_1_worst_decisions.png)
### Top-10 Best decisions for class 1 (Fold 1)
![SHAP best decisions class 1 from Fold 1](learner_fold_0_shap_class_1_best_decisions.png)

[<< Go back](../README.md)
