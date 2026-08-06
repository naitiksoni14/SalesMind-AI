import pandas as pd
from modules.llm import ask_llm


def generate_report(df):

    summary = f"""
Dataset Shape:
{df.shape}

Columns:
{list(df.columns)}

Statistics:
{df.describe().to_string()}

First 5 Rows:
{df.head(5).to_string()}
"""

    prompt = f"""
You are a senior business analyst.

Analyze the following sales dataset.

{summary}

Generate an Executive Business Report.

Include:

1. Executive Summary
2. Key Insights
3. Best Performing Products
4. Worst Performing Products
5. Revenue Analysis
6. Recommendations

Use professional business language.
"""

    return ask_llm(prompt)