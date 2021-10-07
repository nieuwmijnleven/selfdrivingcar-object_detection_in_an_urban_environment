## Submission

### Project overview
This section should contain a brief description of the project and what we are trying to achieve. Why is object detection such an important component of self driving car systems?

### Set up
This section should contain a brief description of the steps to follow to run the code for this repository.

### Dataset
#### Dataset analysis
This section should contain a quantitative and qualitative description of the dataset. It should include images, charts and other visualizations.


#### Cross validation
This section should detail the cross validation strategy and justify your approach.

### Training 
#### Reference experiment
This section should detail the results of the reference experiment. It should includes training metrics and a detailed explanation of the algorithm's performances.

#### 1. experiment#1 : finding an optimal learning_rate
##### (1) Learning Rate
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

##### (2) The relation between learning Rates and total losses 
* observing the relation between total loss and learning rate using cosine_decay_learning_rate
* I finally chosen **0.0004** as the learning rate for the **experiment#2**

<img src = "https://github.com/nieuwmijnleven/object_detection_in_an_urban_environment/blob/experiment_report/images/experiment1-finding-learning-rate1.png?raw=true" width=400 />
<img src = "https://github.com/nieuwmijnleven/object_detection_in_an_urban_environment/blob/experiment_report/images/experiment1-finding-learning-rate2.png?raw=true" width=400 />

#### 2. experiment#2 : applying data augmentation and using a constant learning_rate
##### (1) Data Augmentation : applied additional three data augmentation schemes to preprocessing steps
* random_horizontal_flip
* random_crop_image
* **applying gaussian filter**
* **adjusting brightness**
* **adjusting saturation**

<img src = "https://github.com/nieuwmijnleven/object_detection_in_an_urban_environment/blob/experiment_report/images/data_augmentaion.png?raw=true" width=400 />

##### (2) A constant learning_rate
* the constant learning rate : **0.0004**

<img src = "https://github.com/nieuwmijnleven/object_detection_in_an_urban_environment/blob/experiment_report/images/experiment2-learning_rate.png?raw=true" width=400 />

##### (3) Experimental Results : **LOSS**

<img src = "https://github.com/nieuwmijnleven/object_detection_in_an_urban_environment/blob/experiment_report/images/experiment2-loss.png?raw=true" width=600 />

##### (4) Experimental Results : **ACCURACY**


#### Improve on the reference
This section should highlight the different strategies you adopted to improve your model. It should contain relevant figures and details of your findings.

dropout
early stop
data augmentation

