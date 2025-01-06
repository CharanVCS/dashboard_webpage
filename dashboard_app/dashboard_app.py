# Import libraries
from dash import Dash, dcc, html
import pandas as pd
import plotly.express as px
from dlayout import dlayout


# Data Preparation
expense_data = pd.DataFrame({
    "Expense Category": ["IT", "Marketing", "Operations", "Research"],
    "Amount": [95380, 143776, 121405, 71762]
})

sales_data = pd.DataFrame({
    "Region": ["East", "North", "South", "West"],
    "Sales": [439632, 294082, 215759, 102866]
})

ap_ar_data = pd.DataFrame({
    "Category": ["AP Due", "AR Due", "AP Past Due", "AR Past Due"],
    "Amount": [80000, 90000, 50000, 40000]
})

# Initialize the Dash app
app = Dash(__name__)

# Layout of the dashboard
app.layout = dlayout(expense_data, sales_data, ap_ar_data)

# Run the app locally
if __name__ == "__main__":
    app.run_server(debug=True)
