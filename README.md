<h2> Human-pose-detection-using-Neural-networks-</h2>
<hr>
A Human Pose Skeleton represents the orientation of a person in a graphical format. Essentially, it is a set of coordinates that can be connected to describe the pose of the person. Each coordinate in the skeleton is known as a part (or a joint, or a keypoint). A valid connection between two parts is known as a pair (or a limb). Note that, not all part combinations give rise to valid pairs.
<hr>
<img src = '/images/1.jpg'>
<h2> Deep learning methods </h2>

1. OpenPose
 
OpenPose is one of the most popular bottom-up approaches for multi-person human pose estimation, partly because of their well documented GitHub implementation.
As with many bottom-up approaches, OpenPose first detects parts (key points) belonging to every person in the image, followed by assigning parts to distinct individuals. Shown below is the architecture of the OpenPose model.

2. DeepCut
 
DeepCut is a bottom-up approach for multi-person human pose estimation. The authors approached the task by defining the following problems:
Produce a set of D body part candidates. This set represents all possible locations of body parts for every person in the image. Select a subset of body parts from the above set of body part candidates.
Label each selected body part with one of C body part classes. The body part classes represent the types of parts, such as “arm”, “leg”, “torso” etc.
Partition body parts that belong to the same person.

3. RMPE (AlphaPose)
RMPE is a popular top-down method of Pose Estimation. The authors posit that top-down methods are usually dependent on the accuracy of the person detector, as pose estimation is performed on the region where the person is located. Hence, errors in localization and duplicate bounding box predictions can cause the pose extraction algorithm to perform sub-optimally.

<h2> Some applications </h2>

                  1. Robotics
                  2. Gaming 
                  3. Animations 
