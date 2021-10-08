# Submission

## Project overview
This section should contain a brief description of the project and what we are trying to achieve. Why is object detection such an important component of self driving car systems?

## Set up
This section should contain a brief description of the steps to follow to run the code for this repository.

## Dataset
### Dataset analysis
This section should contain a quantitative and qualitative description of the dataset. It should include images, charts and other visualizations.

#### Samples
<img src = "https://github.com/nieuwmijnleven/object_detection_in_an_urban_environment/blob/experiment_report/images/dataset_analysis-sample1.png?raw=true" width=400 />
<img src = "https://github.com/nieuwmijnleven/object_detection_in_an_urban_environment/blob/experiment_report/images/dataset_analysis-sample2.png?raw=true" width=400 />

#### The number of each objects
<img src = "https://github.com/nieuwmijnleven/object_detection_in_an_urban_environment/blob/experiment_report/images/dataset_analysis-count.png?raw=true" width=400 />

* The number of vehicles = 352694
* The number of pedestrians = 103664
* The number of cyclists = 2639

#### Conclusion
* Our training dataset has the lack of the number of pedestrian samples and cyclist samples comparing to that of vehicle samples.
* Especially, the count of cyclist samples is abolutely small.
* Therefore, it would be challenging for our model to dectect cyclists.

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

#### (2) The relation between learning rates and total losses 
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

#### (5) Experimental Result : **ANALYSIS**
* The training total loss : **HIGH**
    * 0.4719  
* The evaluation total loss : **HIGH**
    * 0.821058 
* The detection rate of small objects : **LOW**
    * DetectionBoxes_Precision/mAP (small): 0.057154
    * DetectionBoxes_Recall/AR@100 (small): 0.124982
* The detection rate of medium objects  : **LOW**
    * DetectionBoxes_Precision/mAP (medium): 0.477788
    * DetectionBoxes_Recall/AR@100 (medium): 0.555998

### Improve on the reference
This section should highlight the different strategies you adopted to improve your model. It should contain relevant figures and details of your findings.
### Experiment#3 : making a improved model
#### (1) Reducing total loss
* Changing Mementum optimizer to **Adam optimizer**
* Changing the constant learning rate to **the manual step learning rate** 
    * 0.0001(initial) -> 0.00005(15000 step) -> 0.00001(30000 step) -> 0.000005(60000 step) -> 0.000001(90000 step)      
* Changing the initial learning rate from 0.0004 to **0.0001**
```
  optimizer {
    adam_optimizer {
      learning_rate {
        manual_step_learning_rate {
          initial_learning_rate: .0001
          schedule {
            step: 15000
            learning_rate: .00005
          }
          schedule {
            step: 30000
            learning_rate: .00001
          }
          schedule {
            step: 60000
            learning_rate: .000005
          }
          schedule {
            step: 90000
            learning_rate: .000001
          }
       }
    }
   use_moving_average: false
  }
```
<img src = "https://github.com/nieuwmijnleven/object_detection_in_an_urban_environment/blob/experiment_report/images/experiment-improvement2-learning_rate.png?raw=true" width=400 />

#### (2) Enhancing Accuracy
* increase samples
    * increase the number of dataset files from 100 to **799**

#### (3) Experimental Results : **LOSS**

<img src = "https://github.com/nieuwmijnleven/object_detection_in_an_urban_environment/blob/experiment_report/images/experiment-improvement2-loss.png?raw=true" width=600 />

#### (4) Experimental Results : **ACCURACY**
```
```

#### (5) Experimental Result : **ANALYSIS**
* The training total loss : 0.4719 -> **0.2176**  
* The evaluation total loss : 0.821058 -> **** 
* The detection rate of small objects
    * DetectionBoxes_Precision/mAP (small): 0.057154 -> ****
    * DetectionBoxes_Recall/AR@100 (small): 0.124982 -> ****
* The detection rate of medium objects
    * DetectionBoxes_Precision/mAP (medium): 0.477788 -> ****
    * DetectionBoxes_Recall/AR@100 (medium): 0.555998 -> ****
