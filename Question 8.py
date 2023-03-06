import pandas as pd
import re

# Load the dataset into a Pandas DataFrame
df = pd.read_csv('Stats_Access_Link.csv')

# Define the regular expression pattern to match the URL
pattern = r'^[a-z]+://[a-z0-9_\.]+/[a-z0-9_\.]+'

# Define a function to extract the URL from a given Stats_Access_Link
def extract_url(access_link):
    match = re.search(pattern, access_link.lower())
    if match:
        return match.group(0)
    else:
        return None

# Filter the dataset to only include rows for the desired device type
device_type = 'AXO145'
filtered_df = df[df['Device_Type'] == device_type]

# Apply the extract_url function to the Stats_Access_Link column
filtered_df['URL'] = filtered_df['Stats_Access_Link'].apply(extract_url)

# Display the extracted URLs
print(filtered_df['URL'])
