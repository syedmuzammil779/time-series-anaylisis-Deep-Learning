# Time-Series-Analysis-Web-App
This Repo Contain a web app which accept the NASDAQ name of a company or a CSV file to check the current metrices of shares , past trends and to train a prediction model
Clone the repository:
```bash
git clone https://github.com/MuhammadUmer241/Time-Series-Analysis-Web-App
```
Create a Virtual Enviroment
```bash
python -m venv my_env
```
Navigate to the project directory:
```Bash
cd Time-Series-Analysis-Web-App\src\app.py
```
Install dependencies:
```bash
pip install -r requirements.txt
```
Running the App
```commandline
python -m streamlit run main.py
```

# Glimpse of Project

![image](https://github.com/user-attachments/assets/d70a04a6-daaa-4e7a-9f2e-173d3dc71799)
### either upload a file or directly enter the NASDAQ name of the project.
![image](https://github.com/user-attachments/assets/99bd7075-87ed-4ac4-a9f3-7c6fab5ef2d8)
### After retrieving the NASDAQ name, we can analyze the company's metrics, such as the current close price and trading volume, and explore past stock trends
![image](https://github.com/user-attachments/assets/a9d5aba4-532c-434e-9805-ec9e7ce33fd1)
### Non-seasonal Parameters (p, d, q):
- #### p (Auto-Regressive Order):

This is the number of lagged observations included in the model. It captures the relationship between a value and its past values.
For example, if p=1, the current value is influenced by the value from the previous time step.
- #### d (Differencing Order):

The number of times the data is differenced to make it stationary (remove trends).
If d=1, the model works on the differences between consecutive observations. For a stronger trend, higher values like d=2 might be required.
- #### q (Moving Average Order):

The number of lagged forecast errors in the model. It adjusts the model based on past prediction errors.
For example, if q=1, the model considers the previous forecast error when predicting the next value.
Seasonal Parameters (P, D, Q, s):
- #### P (Seasonal Auto-Regressive Order):

Similar to p, but for seasonal patterns. It captures the influence of past observations at the seasonal lag (e.g., monthly or yearly patterns).
- #### D (Seasonal Differencing Order):

Similar to d, but it focuses on removing seasonal trends. If there’s a yearly pattern in monthly data, applying D=1 removes this seasonality.
- #### Q (Seasonal Moving Average Order):

Similar to q, but for seasonal patterns. It accounts for forecast errors at the seasonal lag.


