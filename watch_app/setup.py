##
# @file setup.py
# @brief Interactive setup script for SwitchBot API environment variables
# @details This script prompts user for SwitchBot API credentials and sets them
#          as environment variables. The variables are also saved to a .env file
#          for persistence.
#
# Copyright (c) 2025. All rights reserved.
##

import os
import json
from pathlib import Path

##
# @brief Get user input with validation
# @param prompt      Prompt message to display to user
# @param var_name    Name of the environment variable
# @param allow_empty Whether empty input is allowed
#
# @retval str User input value
##
def get_validated_input(prompt: str, var_name: str, allow_empty: bool = False) -> str:
    while True:
        value = input(prompt).strip()
        if value or allow_empty:
            return value
        print(f"Error: {var_name} cannot be empty. Please try again.")

##
# @brief Set up environment variables for SwitchBot API credentials
# @details Prompts user for API token, secret, and device ID
#          Sets these as environment variables and saves to .env file
#
# @retval dict Dictionary containing the set environment variables
##
def setup_environment() -> dict:
    # Define the required environment variables
    env_vars = {
        'SWITCHBOT_API_TOKEN': 'API Token',
        'SWITCHBOT_API_SECRET': 'API Secret',
        'SWITCHBOT_DEVICE_ID': 'Device ID'
    }
    
    # Dictionary to store the user input
    user_values = {}
    
    print("Please enter your SwitchBot credentials:")
    print("-" * 40)
    
    # Get user input for each environment variable
    for env_var, description in env_vars.items():
        current_value = os.getenv(env_var, '')
        prompt = f"Enter {description}"
        if current_value:
            prompt += f" (current: {current_value})"
        prompt += " (press Enter to skip): "
        
        value = get_validated_input(prompt, description, allow_empty=bool(current_value))
        if value:
            user_values[env_var] = value
        elif current_value:
            user_values[env_var] = current_value
    
    # Set environment variables
    for key, value in user_values.items():
        os.environ[key] = value
    
    # Save to .env file
    env_file = Path('.env')
    with env_file.open('w') as f:
        for key, value in user_values.items():
            f.write(f'{key}={value}\n')
    
    print("\nEnvironment variables have been set successfully.")
    print(f"Variables saved to: {env_file.absolute()}")
    
    return user_values

##
# @brief Verify that all required environment variables are set
# @details Checks if all SwitchBot API credentials are present
#
# @retval bool True if all variables are set, False otherwise
##
def verify_environment() -> bool:
    required_vars = ['SWITCHBOT_API_TOKEN', 'SWITCHBOT_API_SECRET', 'SWITCHBOT_DEVICE_ID']
    missing_vars = [var for var in required_vars if not os.getenv(var)]
    
    if missing_vars:
        print("Warning: The following environment variables are not set:")
        for var in missing_vars:
            print(f"- {var}")
        return False
    return True

if __name__ == "__main__":
    try:
        user_values = setup_environment()
        if verify_environment():
            print("\nVerification successful. All required variables are set.")
        print("\nSetup complete.")
    except KeyboardInterrupt:
        print("\nSetup cancelled by user.")
    except Exception as e:
        print(f"\nError during setup: {e}")