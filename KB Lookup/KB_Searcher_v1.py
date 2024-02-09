import requests
import xml.etree.ElementTree as ET

def get_latest_superseded_patch(kb_number):
    # Construct the API URL to search for updates
    api_url = 'https://www.catalog.update.microsoft.com/api/v1/search'

    # Set the query parameters for the API request
    params = {
        'q': kb_number,
        'sort': 'lastUpdated',
        'order': 'desc',
        'pageSize': 50
    }

    # Send the API request and get the response
    response = requests.get(api_url, params=params)

    # Parse the XML response
    root = ET.fromstring(response.text)

    # Find the latest superseded update
    latest_update = None
    for update in root.iter('Update'):
        update_id = update.find('Identity').get('UpdateID')
        is_superseded = update.find('IsSuperseded').text == 'true'
        if is_superseded:
            latest_update = update_id
            break

    # Return the latest superseded update, if found
    return latest_update

# Example usage
kb_number = 'KB4534271'
latest_superseded_patch = get_latest_superseded_patch(kb_number)
print(f"Latest superseded patch for {kb_number}: {latest_superseded_patch}")
