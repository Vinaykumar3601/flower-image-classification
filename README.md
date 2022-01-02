# flower-image-classification
Image Classification using Keras and Tensorflow with Tkinter gui
<hr>
<h2>Dataset used in this project</h2>
"https://storage.googleapis.com/download.tensorflow.org/example_images/flower_photos.tgz"

<h2>Installing the required packages and softwares</h2>
Step 1: Install Python and pip (package manager) <br>
Step 2: Download and install Anaconda Software from https://www.anaconda.com/products/individual <br><br><i>Note:any version of anaconda edition is supported</i><br><br>
Step 3: Run the following line on command prompt to install the Tensorflow and Keras packages.<h5> pip install tensorflow </h5> <br><b><i>Important Instruction: To install tensorflow package GPU enable device(Desktop/Laptop) is necessary.For more info check the system requirements of Tensorflow</i></b><br><br>
Step 4: Using Anaconda command prompt launch jupyter notebook in the directory you have the jupyter notebook document(.ipynb file) which is present in the folowing path.<br>
<b><i>/</i></b> <br><br>
Step 5: Run and Exceute the <h3>image_classification_on_flowers.ipynb</h3> <br>file to display the related findings and implentation of Sequential model using keras to identify and classify the flower species.

<hr>
<h2>Further more if you want to build a GUI for the built model.</h2>
<br>
Step 6: Save the model in HD5(Hierarchical Data Format) format. <br>
Step 7: Install <b>Tkinter</b> python package responsible to create GUI applications. <br>
Command - <h5> pip install tk </h5> <br><br>
Step 8: Create a <i>gui.py</i> file, load the saved model then create a dictionary to label all the flower dataset classes and use your styling preferences for the gui application. Or else download the <h3>gui.py</h3> in this repository for a simple gui code snippet. <br><br>
Step 9: Launch the <i>gui.py</i> using following command <h5> python gui.py </h5> <br>
Step 10: Now the application allows to open the any image and classify the flower image according to the results saved in the model.
