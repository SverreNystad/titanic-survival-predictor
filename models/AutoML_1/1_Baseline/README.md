# Summary of 1_Baseline

[<< Go back](../README.md)


## Baseline Classifier (Baseline)
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

0.1 seconds

## Metric details
|           |    score |   threshold |
|:----------|---------:|------------:|
| logloss   | 0.665558 |    nan      |
| auc       | 0.5      |    nan      |
| f1        | 0.553957 |      0.3435 |
| accuracy  | 0.383085 |      0.3435 |
| precision | 0.383085 |      0.3435 |
| recall    | 1        |      0.3435 |
| mcc       | 0        |      0.3435 |


## Metric details with threshold from accuracy metric
|           |    score |   threshold |
|:----------|---------:|------------:|
| logloss   | 0.665558 |    nan      |
| auc       | 0.5      |    nan      |
| f1        | 0.553957 |      0.3435 |
| accuracy  | 0.383085 |      0.3435 |
| precision | 0.383085 |      0.3435 |
| recall    | 1        |      0.3435 |
| mcc       | 0        |      0.3435 |


## Confusion matrix (at threshold=0.3435)
|              |   Predicted as 0 |   Predicted as 1 |
|:-------------|-----------------:|-----------------:|
| Labeled as 0 |                0 |              124 |
| Labeled as 1 |                0 |               77 |

## Learning curves
![Learning curves](learning_curves.png)

[<< Go back](../README.md)
