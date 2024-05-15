# Restaurant Rating Prediction 

## ABSTRACT
Zomato is one of the best online food delivery apps which gives the users the ratings and the reviews on restaurants all over India.These ratings and the Reviews are considered as one of the most important deciding factors which determine how good a restaurant is. We will therefore use the real time Dataset with variuos features a user would look into regarding a restaurant. We will be considering Banglore City in this analysis.

**The main agenda of this project is:**
1. Perform extensive Exploratory Data Analysis(EDA) on the Zomato Dataset.
2. Build an appropriate Machine Learning Model that will help various Zomato Restaurants to predict their respective Ratings based on certain features

## Feature description
1. url: contains the url of the restaurant in the zomato website
2. address: contains the address of the restaurant in Bengaluru
3. name: contains the name of the restaurant
4. online_order: whether online ordering is available in the restaurant or not
5. book_table: table book option available or not
6. rate: contains the overall rating of the restaurant out of 5
7. votes: contains total number of rating for the restaurant as of the above mentioned date
8. phone: contains the phone number of the restaurant
9. location: contains the neighborhood in which the restaurant is located
10. rest_type: restaurant type
11. dish_liked: dishes people liked in the restaurant
12. cuisines: food styles, separated by comma
13. approx_cost(for two people): contains the approximate cost of meal for two people
14. reviews_list: list of tuples containing reviews for the restaurant, each tuple
15. menu_item: contains list of menus available in the restaurant
16. listed_in(type): type of meal
17. listed_in(city): contains the neighborhood in which the restaurant is listed

**Restaurant Rating has become the most commonly used parameter for judging a restaurant for any individual. Rating of a restaurant depends on factors like reviews, area situated, average cost for two people, votes, cuisines and the type of restaurant.**


## 🔗 Links

 - [Github Link](https://github.com/Namsrkive/Machine-Learning-Project.git)
 - [Kaggle Dataset link](https://www.kaggle.com/datasets/himanshupoddar/zomato-bangalore-restaurants)
 - [Application Link](https://machine-learning-project-pp8842gk6ncaehwarg5wxk.streamlit.app/)

## 🛠 Skills
Python, Pandas, Numpy, Matplotlib, Scikit-learn, Streamlit, Git

## Directory Tree
```bash

├── pages
│   ├── Prediction.py
│   └── Visualization.py
├── resources
│   ├── display.csv
│   └── images.jpg
│    
├── Introduction.py
├── README.md
├── model.pkl
├── Restaurant Rating Prediction.ipynb
└── requirements.txt
```

## Run Locally

Clone the project

```bash
  git clone https://github.com/Namsrkive/Machine-Learning-Project.git
```

Change to project directory

```bash
  cd Machine-Learning-Project
```
Now install all requirements

```bash
  pip install -r requirements.txt

```

