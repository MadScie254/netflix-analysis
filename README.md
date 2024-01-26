# Project Overview

The main objective of this project is to analyze the historical stock data of Netflix and provide insights into the firm's growth over the past two decades. This includes examining key metrics such as stock prices, market capitalization, revenue, and profits, and building predictive models to forecast future trends.

## Project Structure

The project is organized into the following main components:

1. **Data Collection**: Historical stock data of Netflix is collected from reliable sources that is Yahoo Finance.

2. **Data Cleaning and Preprocessing**: The collected data is cleaned and preprocessed to handle missing values, outliers, and any inconsistencies.

3. **Exploratory Data Analysis (EDA)**: Visualizations and statistical analysis are performed to gain insights into the trends and patterns in the data.

4. **Model Development**: Machine learning models,  Random Forest developed to forecast future market trends based on historical data.

5. **Model Evaluation and Selection**: The performance of the developed models is evaluated using appropriate metrics, and the best-performing model is selected for deployment.

6. **Deployment**: The selected model is deployed using Streamlit to generate real-time forecasts or insights for end-users.

## Project Setup

To set up and run the project locally, follow these steps:


1. **Data Collection**: Collect historical stock data of Netflix from reliable sources and save it as a CSV file (e.g., `netflix_data.csv`) in the `data` directory.

2. **Data Cleaning and Preprocessing**: Clean and preprocess the collected data as per your requirements. You can use tools like pandas and scikit-learn for this purpose.

3. **Exploratory Data Analysis (EDA)**: Perform exploratory data analysis to visualize and analyze the trends and patterns in the data. Use matplotlib, seaborn, or Plotly for creating visualizations.

4. **Model Development**: Develop machine learning models using scikit-learn or TensorFlow/Keras for forecasting future market trends. Tune hyperparameters and evaluate model performance using appropriate metrics.

5. **Deployment**: Deploy the selected model using Streamlit for generating real-time forecasts or insights. Write the deployment code in `app.py` and run the Streamlit app using `streamlit run app.py`.


## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

