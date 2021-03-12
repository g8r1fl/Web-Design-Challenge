import pandas as pd 

csv = pd.read_csv("Resources/cities.csv")

csv.to_html("cities.htm", index=False)

html_file = csv.to_html()