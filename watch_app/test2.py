from dotenv import load_dotenv
import os
def load_switchbot_credentials():
    """
    Load SwitchBot credentials from environment variables
    """
    # Load environment variables from .env file if it exists
    load_dotenv()

    # Get environment variables
    api_token = os.getenv('SWITCHBOT_API_TOKEN')
    api_secret = os.getenv('SWITCHBOT_API_SECRET')
    device_id = os.getenv('SWITCHBOT_DEVICE_ID')

    if not all([api_token, api_secret, device_id]):
        raise EnvironmentError("Missing required environment variables")

    return {
        'token': api_token,
        'secret': api_secret,
        'device_id': device_id
    }

credentials = load_switchbot_credentials()
SWITCHBOT_API_TOKEN = credentials['token']
SWITCHBOT_API_SECRET = credentials['secret']
SWITCHBOT_DEVICE_ID = credentials['device_id']

print(SWITCHBOT_API_TOKEN)