# GitHub Self Analysis – AI Powered Repository Review
## Overview
This project analyzes personal GitHub repositories using data science techniques and locally hosted large language models (LLMs).

The main objective is to evaluate documentation quality, repository structure, and development patterns in a systematic and measurable way.

Instead of reviewing repositories manually, this project combines traditional data science methods with AI-generated evaluation to produce structured insights.

## Tools and Technologies Used
Python

Pandas

Scikit-learn

KMeans Clustering

Plotly Dash

Ollama (Local LLM runtime)

Phi-3 (Local model)

Mistral (Local model)

## Project Structure
github-self-analysis/ │ ├── dashboard/ # Plotly Dash application ├── data/ # Raw and processed repository data ├── notebooks/ # Analysis notebooks ├── prompts/ # LLM evaluation prompts ├── reports/ # Technical report (PDF) ├── requirements.txt # Dependencies └── README.md Setup Instructions

## Clone the repository:
git clone

https://github.com/emanzahrashah/github-self-analysis.git

Navigate into the folder:
cd github-self-analysis

Install dependencies:

pip install -r requirements.txt Running Local LLM Models

Local models were executed using Ollama.

To run models locally:

ollama run phi3 ollama run mistral

## These models were prompted to evaluate repositories on:
Clarity

Completeness

Reproducibility

Each model produced structured scoring and reasoning output.

## Running the Dashboard

To launch the interactive dashboard:
python dashboard/app.py

Then open your browser at:

http://127.0.0.1:8050

## The dashboard displays:

Documentation score distribution

Correlation matrix of evaluation metrics

KMeans clustering visualization

Project topic trends

LLM Execution Proof
Phi-3 Local Evaluation
Phi3

Mistral Local Evaluation
Mistral

## Top 5 Key Insights
Documentation clarity has the strongest correlation with overall repository quality.

Projects with structured README files score significantly higher in completeness.

KMeans clustering separates beginner-style repositories from advanced structured projects.

Mistral produces more detailed reasoning and structured explanations.

Phi-3 responds faster and provides concise evaluations.

Model Comparison Feature Phi-3 Mistral Speed Fast Moderate Response Length Concise Detailed Reasoning Depth Moderate High Consistency Good Very Good Future Improvements

Add automated scoring pipeline

Expand clustering features

Compare additional local LLMs

Deploy dashboard online

## YouTube Video LINK
https://youtu.be/gCOyImxMf8s

Author

Eman Zahra
