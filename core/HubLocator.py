import requests


def active_browsers(hub_url):
    # Query Selenium Hub for the list of available nodes and browsers
    status_url = f"{hub_url}/status"
    response = requests.get(status_url)
    response_data = response.json()

    # Extract the active browsers from the response
    active_browsers = []
    for node in response_data['value']['nodes']:
        for capability in node['slots']:
            browser_name = capability['stereotype'].get('browserName')
            if browser_name and browser_name not in active_browsers:
                active_browsers.append(browser_name)
    
    return active_browsers
