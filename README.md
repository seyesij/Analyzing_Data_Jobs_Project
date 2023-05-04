# Data Analyst Jobs in the UK: 
## Exploring Trends and Predicting Salaries with NLP

    * Adeseye Sijuwade
    * Iron Hack, April - 2023

In this project, I conducted an exploratory analysis and developed a predictive model for Data Analyst Jobs in the UK using data scraped from [Reed.co.uk](https://www.reed.co.uk). The primary goal was to leverage natural language processing (NLP) techniques to analyze job descriptions and predict whether a job is high or low paying. I also aimed to gain insights into the data analyst job market by exploring the dataset and identifying patterns and trends. As a bonus, I created a mini job search portal with filtering capabilities. By combining NLP techniques and data analysis, this project offers valuable insights and predictive power for job seekers and employers in the data analyst job market in the UK.

## Overview
Technologies Used: 
  * Python(Pandas, Numpy, Matplotlib, Seaborn, etc.)
  * Jupyter Notebook
  * BeautifulSoup
  * Requests
  * NLTK
  * Machine Learning (Sklearn, NLP, MultinomialNB, Logistic Regression)
  * Tableau
  * Streamlit

### Part 1: Data Collection - Web Scraping
A web scraping python script was developed to retrieve information from Reed on Data Analyst jobs in the Uk using BeautifulSoup. Data scraped included job title, company, location, salary, job type, remote status, description and job link.

### Part 2: Data Cleaning and Wrangling
Data cleaning and wrangling were done on the collected dataset to prepare it for analysis. This included removing any invalid, incorrect, or duplicate data points, fixing structural errors, data formatting, filtering unwanted outliers, handling missing data, and converting data types.

### Part 3: Exploratory Data Analysis
In this part, exploratory data analysis (EDA) was performed to analyze and investigate the data and summarize its main characteristics. Data visualization techniques were used for this process including wordclouds for keywords analysis and barcharts and boxplots for salary analysis. 

### Part 4: Modeling (NLP)
Models for predicting the class label for salary (high or low) based on the text data (job description) were developed using Multinomial Naive Bayes and Logistic Regression. CountVectorizer was used to convert text data into a matrix of token counts which were used as input to train the machine learning model for text classification. The model's performance was evaluated using various performance metrics such as AUC, F1_score, Accuracy, Precision and Recall.

### Final Part (Bonus): Filtered Job App
In the final part of the project, a mini job portal was developed as a bonus feature. This portal allows users to filter for jobs based on their preferences such as junior, senior, remote, and contract positions. This was developed using Streamlit, providing a user-friendly interface for filtering and searching through job listings.

### Conclusion
This project generated valuable insights into the data analyst job market in the UK by analyzing job descriptions and predicting whether a job is high or low paying. This information can be valuable for job seekers who want to find high paying jobs or for employers who want to attract talented data analysts by offering competitive salaries. Additionally, the project's job search app using streamlit provides a user-friendly interface for job seekers to filter for jobs based on their preferences, which can save them time and effort in finding suitable job opportunities. 

### Future Work
There are a lot of opportunities for future work for this project:
  * Improving the accuracy of the salary prediction model by incorporating more data features such as company size, location etc.
  * Extending the analysis to other job markets or regions outside the UK to compare and contrast job trends and salaries.
  * Developing more advanced NLP techniques to extract more meaningful information from job descriptions.
  * Using deep learning techniques to improve the accuracy of the salary prediction model. 
  * Incorporating user feedback to improve the job search portal's functionality and user interface.
