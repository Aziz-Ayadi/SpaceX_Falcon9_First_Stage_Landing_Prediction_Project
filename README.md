# SpaceX Falcon9 First Stage Landing Prediction : Project Overview

The commercial space age is here, companies are making space travel affordable for everyone. Perhaps the most successful is SpaceX. One reason SpaceX can do this is the rocket launches are relatively inexpensive. SpaceX advertises Falcon 9 rocket launches on its website with a cost of 62 million dollars; other providers cost upward of 165 million dollars each, much of the savings is because SpaceX can reuse the first stage. Therefore if we can determine if the first stage will land, we can determine the cost of a launch. This information can be used if an alternate company wants to bid against SpaceX for a rocket launch.
In this project, we will predict if the Falcon 9 first stage will land successfully and we will collect and make sure the data is in the correct format and then we will start working with it.

## The workflow of this project

* Collecting a dataset to work with using two methodologies (Wikipedia Web scraping and data collection using SpaceX public API).
* Data wrangling and preprocessing to make it suitable and prepared for machine learning modeling and prediction.
* Applying EDA to our collected data to try to get insights from it using SQL (SQLITE3 & IBM DB2) and data visualization tools (matplotlib, seaborn & folium).
* Creating a web-based interactive dashboard to help stakeholders understand more the data using dash framework and plotly
* Training some classification models (Logistic Regression, SVM, KNN & Decision Tree Classfier) on the data we have to be able to predict whether first stage of Falcon9 rocket will land successfully on the upcoming launches or not.

## Code and Resources used

<b>Python Version: </b>3.9<br>
<b>Packages: </b>pandas, numpy, matplotlib, seaborn, scikit-learn, BeautifulSoup, requests, datetime, folium, ipython-sql, sqlalchemy, sqlite3, ibm_db, dash, plotly<br>
<b>For Web Framework Requirements: </b><code>pip install -r requirements.txt</code>
