                                                 Read Me
Process of Execution:

1. Upload the dataset Zip file containing two folders (images of wearing masks and images of people not wearing masks) in google collab or Jupyter notebook .
2. Name of the zip file should be Dataset.Dataset should contain images of a person wearing and without wearing masks.
3. Now run all the cells consecutively.
 
Steps Followed :

1. Did Data importing using zip file and extracted the zip file.
2. Converted all the images into numpy arrays and allotted their class labels.
3. Splitted the dataset into training,testing and validation datasets.
4. Did GridSearchCv on MLP,SVM AND KNN classifiers by validation data and
computed best hyperparameters.
5. Fitted the training dataset into these classifiers built by the respective best
hyperparameters and computed the accuracy of the model using testing data.
6. Compared the models and tried to improve the accuracy of each and every model.
7. Compared the models using cross validation by plotting box plot.



| Name                                            | Roll Number | Year      | Department             |
| ----------------------------------------------- | ----------- | --------- | ---------------------- |
| [Sujitha Guvvala](https://github.com/SujithaGuvvala) | B19EE033   | 3rd Year | Electrical Engineering |
| [Hari Bhuthanadhu](https://github.com/haribhutanadhu) | B19EE017   | 3rd Year | Electrical Engineering |
