UCSB Dining Hall Data Science Project
==========

Abstract
==========
Quantify trends in student dining, most importantly relative popularity by time.

Contributors 
==========
-   Alex Lai
-   Matt Luckenbihl
-   Roy Luengas

Motivation
==========
Frustrated of waiting in long lines at dining halls? Wouldn't you like to know when they are less busy?
<img src='https://github.com/dining-hall-warriors/dining-hall-ds/blob/master/figure-markdown/93d1c681483b130b5f1c72ed2cbadb2b.jpg'>      

We do too.                                                                                                                          
                                                                                                                               
Dependencies
=============
ImageAI
https://github.com/OlafenwaMoses/ImageAI

Pandas Library

YoloV3 (place in dining-hall-ds directory):
https://github.com/OlafenwaMoses/ImageAI/releases/download/1.0/yolo.h5

Image acquisition is thanks to the UCSB Mealtime project by Tim Nguyen:
https://github.com/timothydnguyen/ucsb-mealtime

Methodology
==========
Objective: Informing students about the relative popularity of each dining hall.
First, the UCSB Mealtime library pulls images from the cameras of Carillo, DLG, and Ortega dining halls.
Next, our script uses ImageAI and the Yolo model to count the number of people in a frame, and outputs
this data to a CSV. Now we can use statistical analysis to compare the current count of humans to a 
moving average, and find correlations between popularity and other factors.


Graphing Data
=============
Sample Ortega Scatter Data:


<img src ='https://github.com/dining-hall-warriors/dining-hall-ds/blob/master/figure-markdown/Figure_4.png'>

Future Work
=============
Method to count people in vs. out with frame to frame analysis for more accurate popularity tracking.
Correlations between weather, menu items, day/time, etc. will be analyzed.
Eventually the script will update live to a web interface to give an estimated relative popularity and 
predicted number of people in line.
