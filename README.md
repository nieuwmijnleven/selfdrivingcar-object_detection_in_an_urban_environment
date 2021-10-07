# Submission

## Project overview
This section should contain a brief description of the project and what we are trying to achieve. Why is object detection such an important component of self driving car systems?

## Set up
This section should contain a brief description of the steps to follow to run the code for this repository.

## Dataset
### Dataset analysis
This section should contain a quantitative and qualitative description of the dataset. It should include images, charts and other visualizations.


### Cross validation
This section should detail the cross validation strategy and justify your approach.

## Training 
### Reference experiment
This section should detail the results of the reference experiment. It should includes training metrics and a detailed explanation of the algorithm's performances.

### 1. experiment#1 : finding an optimal learning_rate
#### (1) Learning Rate
* strategy : **SGD Optimizer** + **momentum** + **cosine_decay_learning_rate**
* configuration 
```
optimizer {
    momentum_optimizer {
      learning_rate {
        cosine_decay_learning_rate {
          learning_rate_base: 0.04
          total_steps: 25000
          warmup_learning_rate: 0.013333
          warmup_steps: 2000
        }
      }
      momentum_optimizer_value: 0.9
    }
    use_moving_average: false
  }
```
<img src = "https://github.com/nieuwmijnleven/object_detection_in_an_urban_environment/blob/experiment_report/images/experiment1-learning_rate.png?raw=true" width=400 />

#### (2) The relation between learning Rates and total losses 
* observing the relation between total loss and learning rate using cosine_decay_learning_rate
* I finally chosen **0.0004** as the learning rate for the **experiment#2**

<img src = "https://github.com/nieuwmijnleven/object_detection_in_an_urban_environment/blob/experiment_report/images/experiment1-finding-learning-rate1.png?raw=true" width=400 />
<img src = "https://github.com/nieuwmijnleven/object_detection_in_an_urban_environment/blob/experiment_report/images/experiment1-finding-learning-rate2.png?raw=true" width=400 />

### 2. experiment#2 : applying data augmentation and using a constant learning_rate
#### (1) Data Augmentation : applied additional three data augmentation schemes to preprocessing steps
* random_horizontal_flip
* random_crop_image
* **applying gaussian filter**
* **adjusting brightness**
* **adjusting saturation**

<img src = "https://github.com/nieuwmijnleven/object_detection_in_an_urban_environment/blob/experiment_report/images/data_augmentaion.png?raw=true" width=400 />

#### (2) A constant learning_rate
* the constant learning rate : **0.0004**

<img src = "https://github.com/nieuwmijnleven/object_detection_in_an_urban_environment/blob/experiment_report/images/experiment2-learning_rate.png?raw=true" width=400 />

#### (3) Experimental Results : **LOSS**

<img src = "https://github.com/nieuwmijnleven/object_detection_in_an_urban_environment/blob/experiment_report/images/experiment2-loss.png?raw=true" width=600 />

#### (4) Experimental Results : **ACCURACY**
```
DetectionBoxes_Precision/mAP: 0.194451
DetectionBoxes_Precision/mAP@.50IOU: 0.384055
DetectionBoxes_Precision/mAP@.75IOU: 0.164196
DetectionBoxes_Precision/mAP (small): 0.057154
DetectionBoxes_Precision/mAP (medium): 0.477788
DetectionBoxes_Precision/mAP (large): 0.751707
DetectionBoxes_Recall/AR@1: 0.060288
DetectionBoxes_Recall/AR@10: 0.206005
DetectionBoxes_Recall/AR@100: 0.264424
DetectionBoxes_Recall/AR@100 (small): 0.124982
DetectionBoxes_Recall/AR@100 (medium): 0.555998
DetectionBoxes_Recall/AR@100 (large): 0.805090
Loss/localization_loss: 0.339901
Loss/classification_loss: 0.258205
Loss/regularization_loss: 0.222951
Loss/total_loss: 0.821058
```

### Improve on the reference
This section should highlight the different strategies you adopted to improve your model. It should contain relevant figures and details of your findings.
### Experiment#3 : making a improved model
#### (1) Reducing total loss
* Changing Mementum optimizer to **Adam optimizer**
* Changing the constant learning rate to **the manual step learning rate** 
```
  optimizer {
    adam_optimizer {
      learning_rate {
        manual_step_learning_rate {
          initial_learning_rate: .0001
          schedule {
            step: 25000
            learning_rate: .00005
          }
          schedule {
            step: 60000
            learning_rate: .00001
          }
          schedule {
            step: 85000
            learning_rate: .000005
          }
       }
    }
   use_moving_average: false
  }
```
#### (2) Increase Accuracy 
* increase the number of dataset files from 100 to **799**

dropout
early stop
data augmentation

