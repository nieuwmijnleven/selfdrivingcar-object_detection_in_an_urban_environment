# Submission

## Project overview
This section should contain a brief description of the project and what we are trying to achieve. Why is object detection such an important component of self driving car systems?

### Project Introduction
In this project, we will apply the skills you have gained in this course to create a convolutional neural network to detect and classify objects using data from Waymo. We will be provided with a dataset of images of urban environments containing annotated cyclists, pedestrians and vehicles.

* We will practice the following schemes : 
   * Analysis what augmentations are meaningful for this project
   * Train a neural network to detect and classify objects
   * Monitor the training with TensorBoard and decide when to end it 
   * Experiment with different hyperparameters to improve your model's performance

### Why is object detection such an important component of self driving car systems?
The object detection is one of the most important part of autonomous driving system, because this task is in charge of detecting obstables to keep driving safely.
* The object detection system makes the followings possible :
   * recognize categories of object instances
   * locate them spatially
   * avoid obstables

## Set up
This section should contain a brief description of the steps to follow to run the code for this repository.

### 1. Cloning the project repository
```
$> git clone -b main https://github.com/nieuwmijnleven/object_detection_in_an_urban_environment.git
$> cd ./object_detection_in_an_urban_environment
```
### 2. Unziping a pretrained model
```
$> cd ./training/pretrained-models/
$> wget http://download.tensorflow.org/models/object_detection/tf2/20200711/ssd_resnet50_v1_fpn_640x640_coco17_tpu-8.tar.gz
$> tar xvfz ssd_resnet50_v1_fpn_640x640_coco17_tpu-8.tar.gz
```
### 3. Cloning the tensorflow object detection api
```
$> cd ../../
$> mkdir tensorflow
$> git clone https://github.com/tensorflow/models.git
```
### 4. Installing the object detection api  
```
$> wget https://github.com/protocolbuffers/protobuf/releases/download/v3.18.0/protoc-3.18.0-linux-x86_64.zip 
$> unzip protoc-3.18.0-linux-x86_64.zip
$> cd models/research
$> ./../../bin/protoc object_detection/protos/*.proto --python_out=.
$> cp object_detection/packages/tf2/setup.py .
$> python -m pip install --use-feature=2020-resolver .
$> cd ../../../
```
### 5. Running train
```
$> python experiments/model_main_tf2.py --model_dir=./training/experiment2-reference/ --pipeline_config_path=./pipeline_experiment2.config
```
### 6. Running evaluation
```
$> python experiments/model_main_tf2.py --model_dir=./training/experiment3-reference/ --pipeline_config_path=./pipeline_experiment3.config --checkpoint_dir=./training/experiment3-reference/
```

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

## Cross validation
This section should detail the cross validation strategy and justify your approach.

### Cross validation strategy
Given the initial samples(unshuffled data), your model finds some unfavorable local minima and it is hard for it to unlearn it when looking at the latter sample. So, we first shuffle the data to make the order of dataset random and then split into train, validation, and test sets. 

We generally use 7:2:1 or 8:1:1 as the proportion of training, validation, and test datasets. However, in the waymo dataset, one image includes many samples from 10 to 67 cars. so, we considered that it is reasonable to adjust the proportion of the datasets to 6:2:2. Moreover, we increase the number dataset files from 100 to 799. Finally, any overfitting issues were not found from experimental results.     

### Sigmoid Focal Cross Entropy Loss
* Focal loss is extremely useful for classification when you have **highly imbalanced classes**
    * The loss value is much high for a sample which is misclassified by the classifier as compared to the loss value corresponding to a well-classified example.
        * Focal loss **addresses this class imbalance by reshaping the standard cross entropy loss** such that it down-weights the loss assigned to well-classified examples
* Focal Loss focuses training on a sparse set of hard examples and prevents the vast number of easy negatives from overwhelming the detector during training
* One of **the best use-cases** of focal loss is its usage in **object detection** where the imbalance between the background class and other classes is extremely high

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
* I finally chosen **0.00047572** as the learning rate for the **experiment#2**

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

## Improve on the reference
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
DetectionBoxes_Precision/mAP (small): 0.127566
DetectionBoxes_Precision/mAP (medium): 0.596757
DetectionBoxes_Precision/mAP (large): 0.764074
DetectionBoxes_Recall/AR@1: 0.041750
DetectionBoxes_Recall/AR@10: 0.204503
DetectionBoxes_Recall/AR@100: 0.301717
DetectionBoxes_Recall/AR@100 (small): 0.216469
DetectionBoxes_Recall/AR@100 (medium): 0.655430
DetectionBoxes_Recall/AR@100 (large): 0.802555
Loss/localization_loss: 0.214834
Loss/classification_loss: 0.173316
Loss/regularization_loss: 0.042890
Loss/total_loss: 0.431040
```

#### (5) Experimental Result : **ANALYSIS**
* The training total loss : 0.4719 -> **0.2176**  
* The evaluation total loss : 0.821058 -> **0.431040** 
* The detection rate of small objects
    * DetectionBoxes_Precision/mAP (small): 0.057154 -> **0.127566**
    * DetectionBoxes_Recall/AR@100 (small): 0.124982 -> **0.216469**
* The detection rate of medium objects
    * DetectionBoxes_Precision/mAP (medium): 0.477788 -> **0.596757**
    * DetectionBoxes_Recall/AR@100 (medium): 0.555998 -> **0.655430**
* The detection rate of large objects
    * DetectionBoxes_Precision/mAP (large): 0.751707 -> **0.764074**
    * DetectionBoxes_Recall/AR@100 (large): 0.805090 -> **0.802555**

#### (6) Conclusion
* The training total loss is decreased less than about half of the experiment#2 result
* The evaluation total loss is decreased less than about half of the experiment#2 result
* The detection rate of small objects is increased more than about twice of the experiment#2 result
* The detection rate of medium objects is increased more than about 10 percents of the experiment#2 result
