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
#### experiment-1 : applying data augmentation and finding an optimal learning_rate
##### (1) Data Augmentation : applied additional three data augmentation schemes to preprocessing steps
* applying gaussian filter
* adjusting brightness
* adjusting saturation
##### (2) Optimal Learning Rate
* observing the relation between total loss and learning rate using cosine_decay_learning_rate
* data visualization
* finding an optimal learning rate

#### Improve on the reference
This section should highlight the different strategies you adopted to improve your model. It should contain relevant figures and details of your findings.

dropout
early stop
data augmentation

