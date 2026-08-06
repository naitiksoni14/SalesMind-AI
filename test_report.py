import pandas as pd
from modules.report_generator import generate_report

df = pd.read_csv("sales_data.csv")

report = generate_report(df)

print(report)
