import dash
from dash import dcc, html
import plotly.express as px
import pandas as pd
import os

# Load real processed dataset
file_path = os.path.join("..", "data", "processed", "documentation_metrics.csv")
df = pd.read_csv(file_path)

# Create Figures
# -----------------------------

fig_scatter = px.scatter(
    df,
    x="clarity_10",
    y="completeness_10",
    size="overall_avg",
    hover_name="repo_name",
    title="Documentation Quality (Clarity vs Completeness)"
)

fig_hist = px.histogram(
    df,
    x="overall_avg",
    nbins=5,
    title="Distribution of Documentation Quality"
)

# -----------------------------
# Dash App
# -----------------------------

app = dash.Dash(__name__)

app.layout = html.Div([

    html.H1("GitHub Documentation Quality Analysis Dashboard",
            style={"textAlign": "center"}),

    # --- Summary Cards ---
    html.Div([
        html.H3(f"Total Repositories: {len(df)}"),
        html.H3(f"Average Documentation Score: {round(df['overall_avg'].mean(), 2)}")
    ], style={
        "display": "flex",
        "justifyContent": "space-around",
        "marginBottom": "30px"
    }),

    html.Div([
        dcc.Graph(figure=fig_scatter),
    ]),

    html.Div([
        dcc.Graph(figure=fig_hist),
    ]),

    html.Hr(),

    html.P(
        "Built by Eman Shah | Data Collection → EDA → ML → Dashboard | 2026",
        style={"textAlign": "center", "color": "gray"}
    )

])
if __name__ == "__main__":
    app.run(debug=True)
