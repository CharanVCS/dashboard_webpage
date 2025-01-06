#dashboard layout
import plotly.express as px
from dash import Dash, dcc, html


def dlayout(expense_data, sales_data, ap_ar_data):
    return html.Div(style={"fontFamily": "Arial, sans-serif", "padding": "20px"}, children=[
        
        # Header
        html.Div([
            html.H1("Dashboard", 
                    style={"textAlign": "center", "color": "#ffffff", 
                           "backgroundColor": "#4CAF50", "padding": "20px", 
                           "borderRadius": "10px"})
        ]),

        # KPI Section
        html.Div([
            html.Div([
                html.H3("Total Expenses", style={"textAlign": "center"}),
                html.H4(f"${round(expense_data['Amount'].sum() / 1000)}k", style={"textAlign": "center", "color": "#FF5733"})
            ], style={"width": "30%", "display": "inline-block", "padding": "10px", "backgroundColor": "#f9f9f9", "borderRadius": "10px"}),

            html.Div([
                html.H3("Total Sales", style={"textAlign": "center"}),
                html.H4(f"${round(sales_data['Sales'].sum()/1000):,}k", style={"textAlign": "center", "color": "#33C3F0"})
            ], style={"width": "30%", "display": "inline-block", "padding": "10px", "backgroundColor": "#f9f9f9", "borderRadius": "10px"}),

            html.Div([
                html.H3("Net AR/AP Difference", style={"textAlign": "center"}),
                html.H4(f"${round(ap_ar_data['Amount'].sum()/1000)}K", style={"textAlign": "center", "color": "#28a745"})
            ], style={"width": "30%", "display": "inline-block", "padding": "10px", "backgroundColor": "#f9f9f9", "borderRadius": "10px"}),
        ], style={"textAlign": "center", "marginBottom": "30px"}),

        # Charts Row 1
        html.Div([
            html.Div([
                html.H3("Expense Summary", style={"textAlign": "center"}),
                dcc.Graph(
                    id="expense-chart",
                    figure=px.bar(expense_data, x="Expense Category", y="Amount", 
                                  title="Expense Summary", color="Expense Category", 
                                  text="Amount", color_discrete_sequence=px.colors.qualitative.G10)
                )
            ], style={"width": "48%", "display": "inline-block", "padding": "10px", "backgroundColor": "#ffffff", "borderRadius": "10px", "boxShadow": "2px 2px 5px #aaaaaa"}),

            html.Div([
                html.H3("Sales Summary", style={"textAlign": "center"}),
                dcc.Graph(
                    id="sales-chart",
                    figure=px.pie(sales_data, names="Region", values="Sales", 
                                  title="Sales by Region", hole=0.4,
                                  color_discrete_sequence=px.colors.sequential.deep_r)
                )
            ], style={"width": "48%", "display": "inline-block", "padding": "10px", "backgroundColor": "#ffffff", "borderRadius": "10px", "boxShadow": "2px 2px 5px #aaaaaa"}),
        ], style={"display": "flex", "justifyContent": "space-between", "marginBottom": "30px"}),

        # Charts Row 2
        html.Div([
            html.Div([
                html.H3("AP and AR Aging Summary", style={"textAlign": "center"}),
                dcc.Graph(
                    id="ap-ar-chart",
                    figure=px.bar(ap_ar_data, x="Category", y="Amount", 
                                  title="AP and AR Aging", color="Category", 
                                  text="Amount", color_discrete_sequence=px.colors.qualitative.G10_r)
                )
            ], style={"padding": "10px", "backgroundColor": "#ffffff", "borderRadius": "10px", "boxShadow": "2px 2px 5px #aaaaaa"})
        ], style={"marginBottom": "30px"}),

        # Footer
        html.Div([
            html.P("CFO Dashboard © 2025", style={"textAlign": "center", "color": "#555555"})
        ])

    ])
