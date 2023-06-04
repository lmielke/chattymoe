"""
This returns the openai api key
NOTE: This uses a password tool which is not available to you! So you have to replace
the content of this get_api_key with your openai api key retrieval.
"""

from joringels.src.actions import fetch

def get_api_key():
    """
    provides your API key using joringels api
    NOTE: 
    if you dont use joringels or any other password tool,
    you can remove the content of this function and return your api-key directly instead:
    return "apiKey as proviced by openai"
    """
    creds = {
            'safeName': 'digiserver',
            'entryName': 'chatgptApi',
    }

    # add your openAi API-key here as a string
    return fetch.alloc(**creds, retain=True).get('password').strip()