import json
import requests
import constants


def user_login(email, password):
    print('trying2')
    data = {
        "username": email,
        "password": password
    }

    try:
        response = requests.post(constants.BASE_URL + '/login', data=data)
        print(response.text)
        print(constants.BASE_URL + '/login')
        return response
    except requests.exceptions.HTTPError as errh:
        print(f"HTTP Error: {errh}")
    except requests.exceptions.ConnectionError as errc:
        print(f"Error Connecting: {errc}")
    except requests.exceptions.Timeout as errt:
        print(f"Timeout Error: {errt}")
    except requests.exceptions.RequestException as err:
        print(f"An unexpected error occurred: {err}")


def dashboard(file_list, access_token: str):
    headers = {'Authorization': f'Bearer {access_token}'}
    try:
        response = requests.post(constants.BASE_URL + '/process-resume/', files=file_list, headers=headers)
        return response

    except requests.exceptions.RequestException as e:
        # Handle request errors
        print(f"Error: {e}")


def user_register(username, email, password):
    print('trying3')
    headers = {'Content-Type': 'application/json'}
    data = {
        "username": username,
        "email": email,
        "password": password,
        "role": "user"
    }

    try:
        response = requests.post(constants.BASE_URL + f'/register', data=json.dumps(data), headers=headers)
        print(response.text)
        return response
    except requests.exceptions.HTTPError as errh:
        print(f"HTTP Error: {errh}")
    except requests.exceptions.ConnectionError as errc:
        print(f"Error Connecting: {errc}")
    except requests.exceptions.Timeout as errt:
        print(f"Timeout Error: {errt}")
    except requests.exceptions.RequestException as err:
        print(f"An unexpected error occurred: {err}")


def admin_register(username, email, password):
    print('trying9')
    headers = {'Content-Type': 'application/json'}
    data = {
        "username": username,
        "email": email,
        "password": password,
        "role": "admin"
    }

    try:
        # response = requests.post(constants.BASE_URL + '/register', data=json.dumps(data), headers=headers)
        response = requests.post(constants.BASE_URL + '/register-admin', data=json.dumps(data), headers=headers)

        print(response.text)
        return response
    except requests.exceptions.HTTPError as errh:
        print(f"HTTP Error: {errh}")
    except requests.exceptions.ConnectionError as errc:
        print(f"Error Connecting: {errc}")
    except requests.exceptions.Timeout as errt:
        print(f"Timeout Error: {errt}")
    except requests.exceptions.RequestException as err:
        print(f"An unexpected error occurred: {err}")


def get_user_profile(access_token: str):
    headers = {'Authorization': f'Bearer {access_token}'}

    try:
        response = requests.get(constants.BASE_URL + '/user-profile', headers=headers)
        return response
    except requests.exceptions.HTTPError as errh:
        print(f"HTTP Error: {errh}")
    except requests.exceptions.ConnectionError as errc:
        print(f"Error Connecting: {errc}")
    except requests.exceptions.Timeout as errt:
        print(f"Timeout Error: {errt}")
    except requests.exceptions.RequestException as err:
        print(f"An unexpected error occurred: {err}")


def get_all_users(access_token: str):
    headers = {'Authorization': f'Bearer {access_token}'}
    try:
        response = requests.get(constants.BASE_URL + '/admin/users', headers=headers)
        print(response.text)
        return response
    except requests.exceptions.HTTPError as errh:
        print(f"HTTP Error: {errh}")
    except requests.exceptions.ConnectionError as errc:
        print(f"Error Connecting: {errc}")
    except requests.exceptions.Timeout as errt:
        print(f"Timeout Error: {errt}")
    except requests.exceptions.RequestException as err:
        print(f"An unexpected error occurred: {err}")


def admin_login(email, password):
    print('trying3')
    data = {
        "username": email,
        "password": password
    }

    try:
        response = requests.post(constants.BASE_URL + '/admin/login', data=data)
        print(response.text)
        print(constants.BASE_URL + '/admin/login')

        return response
    except requests.exceptions.HTTPError as errh:
        print(f"HTTP Error: {errh}")
    except requests.exceptions.ConnectionError as errc:
        print(f"Error Connecting: {errc}")
    except requests.exceptions.Timeout as errt:
        print(f"Timeout Error: {errt}")
    except requests.exceptions.RequestException as err:
        print(f"An unexpected error occurred: {err}")


# Endpoint only accessible to admin
def add_user(username, email, password, role, access_token: str):
    print('trying3')
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {access_token}'
    }

    data = {
        "username": username,
        "email": email,
        "password": password,
        "role": role
    }

    try:
        response = requests.post(constants.BASE_URL + '/admin/add-user', data=json.dumps(data), headers=headers)
        print(response.text)
        return response
    except requests.exceptions.HTTPError as errh:
        print(f"HTTP Error: {errh}")
    except requests.exceptions.ConnectionError as errc:
        print(f"Error Connecting: {errc}")
    except requests.exceptions.Timeout as errt:
        print(f"Timeout Error: {errt}")
    except requests.exceptions.RequestException as err:
        print(f"An unexpected error occurred: {err}")


def admin_trash_user(access_token: str, user_id: int):
    headers = {'Authorization': f'Bearer {access_token}'}

    try:
        response = requests.delete(constants.BASE_URL + f'/admin/trash-user/{user_id}', headers=headers)
        print(response.text)
        return response
    except requests.exceptions.HTTPError as errh:
        print(f"HTTP Error: {errh}")
    except requests.exceptions.ConnectionError as errc:
        print(f"Error Connecting: {errc}")
    except requests.exceptions.Timeout as errt:
        print(f"Timeout Error: {errt}")
    except requests.exceptions.RequestException as err:
        print(f"An unexpected error occurred: {err}")


def admin_restore_user(access_token: str, user_id: int):
    headers = {'Authorization': f'Bearer {access_token}'}

    try:
        response = requests.put(constants.BASE_URL + f'/admin/restore-user/{user_id}', headers=headers)
        print(response.text)
        return response
    except requests.exceptions.HTTPError as errh:
        print(f"HTTP Error: {errh}")
    except requests.exceptions.ConnectionError as errc:
        print(f"Error Connecting: {errc}")
    except requests.exceptions.Timeout as errt:
        print(f"Timeout Error: {errt}")
    except requests.exceptions.RequestException as err:
        print(f"An unexpected error occurred: {err}")


def admin_delete_user_permanently(access_token: str, user_id: int):
    headers = {'Authorization': f'Bearer {access_token}'}

    try:
        response = requests.delete(constants.BASE_URL + f'/admin/delete-user/{user_id}', headers=headers)
        print(response.text)
        return response
    except requests.exceptions.HTTPError as errh:
        print(f"HTTP Error: {errh}")
    except requests.exceptions.ConnectionError as errc:
        print(f"Error Connecting: {errc}")
    except requests.exceptions.Timeout as errt:
        print(f"Timeout Error: {errt}")
    except requests.exceptions.RequestException as err:
        print(f"An unexpected error occurred: {err}")


def admin_get_any_user(access_token: str, user_id: int):
    headers = {'Authorization': f'Bearer {access_token}'}
    try:
        response = requests.get(constants.BASE_URL + f'/admin/view-user/{user_id}', headers=headers)
        if response.status_code == 200:
            return response.json()
    except requests.exceptions.HTTPError as errh:
        print(f"HTTP Error: {errh}")
    except requests.exceptions.ConnectionError as errc:
        print(f"Error Connecting: {errc}")
    except requests.exceptions.Timeout as errt:
        print(f"Timeout Error: {errt}")
    except requests.exceptions.RequestException as err:
        print(f"An unexpected error occurred: {err}")


def update_user_password(current_password, new_password, confirm_new_password, access_token: str):
    print('trying3')
    headers = {
        'Authorization': f'Bearer {access_token}',
        'Content-type': 'application/json'

    }

    data = {
        "current_password": current_password,
        "new_password": new_password,
        "confirm_new_password": confirm_new_password
    }

    try:
        response = requests.put(constants.BASE_URL + '/update-password', params=data, headers=headers)
        print(response.text)
        return response
    except requests.exceptions.HTTPError as errh:
        print(f"HTTP Error: {errh}")
    except requests.exceptions.ConnectionError as errc:
        print(f"Error Connecting: {errc}")
    except requests.exceptions.Timeout as errt:
        print(f"Timeout Error: {errt}")
    except requests.exceptions.RequestException as err:
        print(f"An unexpected error occurred: {err}")


def forgot_password(email):
    print('trying6')

    headers = {
        'Content-type': 'application/json'
    }
    data = {
        "email": email,
    }

    try:
        response = requests.post(constants.BASE_URL + '/forgot-password', params=data, headers=headers)
        print(response.text)
        return response
    except requests.exceptions.HTTPError as errh:
        print(f"HTTP Error: {errh}")
    except requests.exceptions.ConnectionError as errc:
        print(f"Error Connecting: {errc}")
    except requests.exceptions.Timeout as errt:
        print(f"Timeout Error: {errt}")
    except requests.exceptions.RequestException as err:
        print(f"An unexpected error occurred: {err}")


def reset_password(token, new_password):
    print('trying7')

    headers = {
        'Content-type': 'application/json'
    }
    data = {
        "token": token,
        "new_password": new_password
    }

    try:
        response = requests.post(constants.BASE_URL + '/reset-password', params=data, headers=headers)
        print(response.text)
        return response
    except requests.exceptions.HTTPError as errh:
        print(f"HTTP Error: {errh}")
    except requests.exceptions.ConnectionError as errc:
        print(f"Error Connecting: {errc}")
    except requests.exceptions.Timeout as errt:
        print(f"Timeout Error: {errt}")
    except requests.exceptions.RequestException as err:
        print(f"An unexpected error occurred: {err}")


def admin_edit_any_user(access_token: str, user_id: int, username, role, status):
    print("trying")
    headers = {'Authorization': f'Bearer {access_token}'}

    data = {
        "user_id": user_id,
        "username": username,
        "role": role,
        "status": status
    }

    try:
        print("try")
        response = requests.put(constants.BASE_URL + f'/admin/edit-user', headers=headers, params=data)
        return response
    except requests.exceptions.HTTPError as errh:
        print(f"HTTP Error: {errh}")
    except requests.exceptions.ConnectionError as errc:
        print(f"Error Connecting: {errc}")
    except requests.exceptions.Timeout as errt:
        print(f"Timeout Error: {errt}")
    except requests.exceptions.RequestException as err:
        print(f"An unexpected error occurred: {err}")


def user_update_profile(access_token: str, username, email, profile_picture):
    print("working")
    headers = {'Authorization': f'Bearer {access_token}'}

    data = {

        "username": username,
        "email": email,

    }

    files = {
        "profile_picture": profile_picture
    }

    try:
        print("try")
        response = requests.put(constants.BASE_URL + f'/update-profile', files=files, headers=headers, data=data)
        return response
    except requests.exceptions.HTTPError as errh:
        print(f"HTTP Error: {errh}")
    except requests.exceptions.ConnectionError as errc:
        print(f"Error Connecting: {errc}")
    except requests.exceptions.Timeout as errt:
        print(f"Timeout Error: {errt}")
    except requests.exceptions.RequestException as err:
        print(f"An unexpected error occurred: {err}")


def get_companies():
    try:
        response = requests.get(constants.BASE_URL + f'/companies')
        if response.status_code == 200:
            return response.json()
    except requests.exceptions.HTTPError as errh:
        print(f"HTTP Error: {errh}")
    except requests.exceptions.ConnectionError as errc:
        print(f"Error Connecting: {errc}")
    except requests.exceptions.Timeout as errt:
        print(f"Timeout Error: {errt}")
    except requests.exceptions.RequestException as err:
        print(f"An unexpected error occurred: {err}")


def get_company_details(company_id: int):
    try:
        response = requests.get(constants.BASE_URL + f'/companies/{company_id}')
        if response.status_code == 200:
            return response.json()
    except requests.exceptions.HTTPError as errh:
        print(f"HTTP Error: {errh}")
    except requests.exceptions.ConnectionError as errc:
        print(f"Error Connecting: {errc}")
    except requests.exceptions.Timeout as errt:
        print(f"Timeout Error: {errt}")
    except requests.exceptions.RequestException as err:
        print(f"An unexpected error occurred: {err}")


def company_register(name, location, access_token):
    print('trying3')
    headers = {'Authorization': f'Bearer {access_token}'}
    params = {
        "name": name,
        "location": location,

    }
    try:
        response = requests.post(constants.BASE_URL + f'/companies/create-company', params=params, headers=headers)
        print(response.text)
        return response
    except requests.exceptions.HTTPError as errh:
        print(f"HTTP Error: {errh}")
    except requests.exceptions.ConnectionError as errc:
        print(f"Error Connecting: {errc}")
    except requests.exceptions.Timeout as errt:
        print(f"Timeout Error: {errt}")
    except requests.exceptions.RequestException as err:
        print(f"An unexpected error occurred: {err}")


def services():
    try:
        response = requests.get(constants.BASE_URL + '/services/all-services')
        return response

    except requests.exceptions.RequestException as e:
        # Handle request errors
        print(f"Error: {e}")


def add_service(name, description):
    headers = {
        'Content-Type': 'application/json',
    }

    params = {
        "name": name,
        "description": description,
    }

    try:
        response = requests.post(constants.BASE_URL + '/services/create-service', params=params, headers=headers)
        print(response.text)
        return response
    except requests.exceptions.HTTPError as errh:
        print(f"HTTP Error: {errh}")
    except requests.exceptions.ConnectionError as errc:
        print(f"Error Connecting: {errc}")
    except requests.exceptions.Timeout as errt:
        print(f"Timeout Error: {errt}")
    except requests.exceptions.RequestException as err:
        print(f"An unexpected error occurred: {err}")


def admin_delete_service(service_id: int):
    try:
        response = requests.delete(constants.BASE_URL + f'/services/delete-service/{service_id}')
        return response
    except requests.exceptions.HTTPError as errh:
        print(f"HTTP Error: {errh}")
    except requests.exceptions.ConnectionError as errc:
        print(f"Error Connecting: {errc}")
    except requests.exceptions.Timeout as errt:
        print(f"Timeout Error: {errt}")
    except requests.exceptions.RequestException as err:
        print(f"An unexpected error occurred: {err}")


def admin_get_any_service(service_id: int):
    try:
        response = requests.get(constants.BASE_URL + f'/services/{service_id}')
        if response.status_code == 200:
            return response.json()
    except requests.exceptions.HTTPError as errh:
        print(f"HTTP Error: {errh}")
    except requests.exceptions.ConnectionError as errc:
        print(f"Error Connecting: {errc}")
    except requests.exceptions.Timeout as errt:
        print(f"Timeout Error: {errt}")
    except requests.exceptions.RequestException as err:
        print(f"An unexpected error occurred: {err}")


def admin_edit_any_service(service_id, service_name, service_description):
    print("trying")

    data = {
        "name": service_name,
        "description": service_description
    }

    try:
        print("try")
        response = requests.put(constants.BASE_URL + f'/services/update-service/{service_id}', json=data)
        return response
    except requests.exceptions.HTTPError as errh:
        print(f"HTTP Error: {errh}")
    except requests.exceptions.ConnectionError as errc:
        print(f"Error Connecting: {errc}")
    except requests.exceptions.Timeout as errt:
        print(f"Timeout Error: {errt}")
    except requests.exceptions.RequestException as err:
        print(f"An unexpected error occurred: {err}")


def admin_get_resume_history():
    try:
        response = requests.get(constants.BASE_URL + '/admin/resume-history')
        return response
    except requests.exceptions.HTTPError as errh:
        print(f"HTTP Error: {errh}")
    except requests.exceptions.ConnectionError as errc:
        print(f"Error Connecting: {errc}")
    except requests.exceptions.Timeout as errt:
        print(f"Timeout Error: {errt}")
    except requests.exceptions.RequestException as err:
        print(f"An unexpected error occurred: {err}")


def admin_get_all_companies():
    print("trying")
    try:
        print("try")
        response = requests.get(constants.BASE_URL + '/companies/')
        return response
    except requests.exceptions.HTTPError as errh:
        print(f"HTTP Error: {errh}")
    except requests.exceptions.ConnectionError as errc:
        print(f"Error Connecting: {errc}")
    except requests.exceptions.Timeout as errt:
        print(f"Timeout Error: {errt}")
    except requests.exceptions.RequestException as err:
        print(f"An unexpected error occurred: {err}")


def get_trash_users(access_token: str):
    headers = {'Authorization': f'Bearer {access_token}'}
    try:
        response = requests.get(constants.BASE_URL + '/admin/trash-users', headers=headers)
        print(response.text)
        return response
    except requests.exceptions.HTTPError as errh:
        print(f"HTTP Error: {errh}")
    except requests.exceptions.ConnectionError as errc:
        print(f"Error Connecting: {errc}")
    except requests.exceptions.Timeout as errt:
        print(f"Timeout Error: {errt}")
    except requests.exceptions.RequestException as err:
        print(f"An unexpected error occurred: {err}")


def admin_delete_company(company_id: int):
    try:
        response = requests.delete(constants.BASE_URL + f'/companies/delete-company/{company_id}')
        return response
    except requests.exceptions.HTTPError as errh:
        print(f"HTTP Error: {errh}")
    except requests.exceptions.ConnectionError as errc:
        print(f"Error Connecting: {errc}")
    except requests.exceptions.Timeout as errt:
        print(f"Timeout Error: {errt}")
    except requests.exceptions.RequestException as err:
        print(f"An unexpected error occurred: {err}")


def admin_get_any_company(company_id: int):
    try:
        response = requests.get(constants.BASE_URL + f'/companies/{company_id}')
        if response.status_code == 200:
            return response.json()
    except requests.exceptions.HTTPError as errh:
        print(f"HTTP Error: {errh}")
    except requests.exceptions.ConnectionError as errc:
        print(f"Error Connecting: {errc}")
    except requests.exceptions.Timeout as errt:
        print(f"Timeout Error: {errt}")
    except requests.exceptions.RequestException as err:
        print(f"An unexpected error occurred: {err}")


def admin_edit_any_company(company_id, name, location):
    print("trying")

    data = {
        "name": name,
        "location": location
    }

    try:
        print("try")
        response = requests.put(constants.BASE_URL + f'/companies/update-company/{company_id}', params=data)
        return response
    except requests.exceptions.HTTPError as errh:
        print(f"HTTP Error: {errh}")
    except requests.exceptions.ConnectionError as errc:
        print(f"Error Connecting: {errc}")
    except requests.exceptions.Timeout as errt:
        print(f"Timeout Error: {errt}")
    except requests.exceptions.RequestException as err:
        print(f"An unexpected error occurred: {err}")


def admin_get_email_setup(access_token: str):
    headers = {'Authorization': f'Bearer {access_token}'}
    try:
        print("try")
        response = requests.get(constants.BASE_URL + f'/smtp_settings/', headers=headers)
        return response
    except requests.exceptions.HTTPError as errh:
        print(f"HTTP Error: {errh}")
    except requests.exceptions.ConnectionError as errc:
        print(f"Error Connecting: {errc}")
    except requests.exceptions.Timeout as errt:
        print(f"Timeout Error: {errt}")
    except requests.exceptions.RequestException as err:
        print(f"An unexpected error occurred: {err}")





def admin_update_email_setup(access_token: str, smtp_server, smtp_port, smtp_username, smtp_password, sender_email):
    headers = {'Authorization': f'Bearer {access_token}'}
    data = {
        "smtp_server": smtp_server,
        "smtp_port": smtp_port,
        "smtp_username": smtp_username,
        "smtp_password": smtp_password,
        "sender_email": sender_email
    }

    try:
        response = requests.put(constants.BASE_URL + f'/admin/update-email-settings/', headers=headers, json=data)
        response.raise_for_status()  # Raises an HTTPError if the response was unsuccessful
        return response
    except requests.exceptions.HTTPError as errh:
        print(f"HTTP Error: {errh}")
        raise  # Re-raise the exception to be handled by the caller
    except requests.exceptions.ConnectionError as errc:
        print(f"Error Connecting: {errc}")
        raise  # Re-raise the exception to be handled by the caller
    except requests.exceptions.Timeout as errt:
        print(f"Timeout Error: {errt}")
        raise  # Re-raise the exception to be handled by the caller
    except requests.exceptions.RequestException as err:
        print(f"An unexpected error occurred: {err}")
        raise  # Re-raise the exception to be handled by the caller


def admin_assign_service(user_id, service_ids: list):
    params = {
        "user_id": user_id

    }

    try:
        response = requests.post(constants.BASE_URL + f'/users/assign_services/', params=params, json=service_ids)
        response.raise_for_status()  # Raises an HTTPError if the response was unsuccessful
        return response
    except requests.exceptions.HTTPError as errh:
        print(f"HTTP Error: {errh}")
        raise  # Re-raise the exception to be handled by the caller
    except requests.exceptions.ConnectionError as errc:
        print(f"Error Connecting: {errc}")
        raise  # Re-raise the exception to be handled by the caller
    except requests.exceptions.Timeout as errt:
        print(f"Timeout Error: {errt}")
        raise  # Re-raise the exception to be handled by the caller
    except requests.exceptions.RequestException as err:
        print(f"An unexpected error occurred: {err}")
        raise  # Re-raise the exception to be handled by the caller


def user_specific_services(user_id):
    try:
        print("try")
        response = requests.get(constants.BASE_URL + f'/users/{user_id}/services')
        return response
    except requests.exceptions.HTTPError as errh:
        print(f"HTTP Error: {errh}")
    except requests.exceptions.ConnectionError as errc:
        print(f"Error Connecting: {errc}")
    except requests.exceptions.Timeout as errt:
        print(f"Timeout Error: {errt}")
    except requests.exceptions.RequestException as err:
        print(f"An unexpected error occurred: {err}")


############################################################### PLANS ##############################################################################
def get_all_plans():
    try:
        response = requests.get(constants.BASE_URL + '/plans/')
        if response.status_code == 200:
            result = response.json()
            return result

    except requests.exceptions.RequestException as e:
        # Handle request errors
        print(f"Error: {e}")


def create_plan(plan_name, time_period, fees, num_resume_parse, plan_details):
    print("inside api call")
    headers = {
        'Content-Type': 'application/json',
    }

    data = {
        "plan_type_name": plan_name,
        "time_period": time_period,
        "fees": fees,
        "num_resume_parse": num_resume_parse,
        "plan_details": plan_details
    }

    try:
        response = requests.post(constants.BASE_URL + '/plans/create-plan', json=data, headers=headers)
        if response.status_code == 200:
            print("successful")
            return response.json
    except requests.exceptions.HTTPError as errh:
        print(f"HTTP Error: {errh}")
    except requests.exceptions.ConnectionError as errc:
        print(f"Error Connecting: {errc}")
    except requests.exceptions.Timeout as errt:
        print(f"Timeout Error: {errt}")
    except requests.exceptions.RequestException as err:
        print(f"An unexpected error occurred: {err}")


def delete_plan(plan_id: int):
    try:
        response = requests.delete(constants.BASE_URL + f'/plans/delete-plan/{plan_id}')
        if response.status_code == 200:
            return response.json()
    except requests.exceptions.HTTPError as errh:
        print(f"HTTP Error: {errh}")
    except requests.exceptions.ConnectionError as errc:
        print(f"Error Connecting: {errc}")
    except requests.exceptions.Timeout as errt:
        print(f"Timeout Error: {errt}")
    except requests.exceptions.RequestException as err:
        print(f"An unexpected error occurred: {err}")


def get_plan_by_id(plan_id: int):
    try:
        response = requests.get(constants.BASE_URL + f'/plans/{plan_id}')
        if response.status_code == 200:
            return response.json()
    except requests.exceptions.HTTPError as errh:
        print(f"HTTP Error: {errh}")
    except requests.exceptions.ConnectionError as errc:
        print(f"Error Connecting: {errc}")
    except requests.exceptions.Timeout as errt:
        print(f"Timeout Error: {errt}")
    except requests.exceptions.RequestException as err:
        print(f"An unexpected error occurred: {err}")


def update_plan(plan_id: int, plan_name: str, time_period: str, fees: int, num_resume_parse: str, plan_details: str):
    data = {
        "plan_type_name": plan_name,
        "time_period": time_period,
        "fees": fees,
        "num_resume_parse": num_resume_parse,
        "plan_details": plan_details
    }
    try:
        print("try")
        response = requests.put(constants.BASE_URL + f'/plans/update-plan/{plan_id}', json=data)
        if response.status_code == 200:
            return response.json()
    except requests.exceptions.HTTPError as errh:
        print(f"HTTP Error: {errh}")
    except requests.exceptions.ConnectionError as errc:
        print(f"Error Connecting: {errc}")
    except requests.exceptions.Timeout as errt:
        print(f"Timeout Error: {errt}")
    except requests.exceptions.RequestException as err:
        print(f"An unexpected error occurred: {err}")


##################################################### SUBSCRIPTION #################################################################

def start_subscription(plan_id, stripe_token, access_token):
    headers = {'Authorization': f'Bearer {access_token}'}

    params = {
        "plan_id": plan_id,
    }

    if stripe_token is not None:
        params["stripe_token"] = stripe_token

    try:
        print("try")
        response = requests.post(constants.BASE_URL + '/subscriptions/create-subscription', params=params, headers=headers)
        response.raise_for_status()  # This will raise an HTTPError for bad responses
        return response.json()
    except requests.exceptions.HTTPError as errh:
        print(f"HTTP Error: {errh}")
    except requests.exceptions.ConnectionError as errc:
        print(f"Error Connecting: {errc}")
    except requests.exceptions.Timeout as errt:
        print(f"Timeout Error: {errt}")
    except requests.exceptions.RequestException as err:
        print(f"An unexpected error occurred: {err}")


def cancel_subscription(subscription_id):
    try:
        print("try")
        response = requests.post(constants.BASE_URL + f'/subscriptions/{subscription_id}/cancel')
        if response.status_code == 200:
            return response.json()
    except requests.exceptions.HTTPError as errh:
        print(f"HTTP Error: {errh}")
    except requests.exceptions.ConnectionError as errc:
        print(f"Error Connecting: {errc}")
    except requests.exceptions.Timeout as errt:
        print(f"Timeout Error: {errt}")
    except requests.exceptions.RequestException as err:
        print(f"An unexpected error occurred: {err}")


def resume_subscription(subscription_id):
    try:
        print("try")
        response = requests.post(constants.BASE_URL + f'/subscriptions/{subscription_id}/resume')
        if response.status_code == 200:
            return response.json()
    except requests.exceptions.HTTPError as errh:
        print(f"HTTP Error: {errh}")
    except requests.exceptions.ConnectionError as errc:
        print(f"Error Connecting: {errc}")
    except requests.exceptions.Timeout as errt:
        print(f"Timeout Error: {errt}")
    except requests.exceptions.RequestException as err:
        print(f"An unexpected error occurred: {err}")


def purchase_history(access_token):
    headers = {'Authorization': f'Bearer {access_token}'}

    try:
        print("try")
        response = requests.get(constants.BASE_URL + f'/subscriptions/purchase_history', headers=headers)
        if response.status_code == 200:
            return response.json()
    except requests.exceptions.HTTPError as errh:
        print(f"HTTP Error: {errh}")
    except requests.exceptions.ConnectionError as errc:
        print(f"Error Connecting: {errc}")
    except requests.exceptions.Timeout as errt:
        print(f"Timeout Error: {errt}")
    except requests.exceptions.RequestException as err:
        print(f"An unexpected error occurred: {err}")


def get_all_subscriptions(access_token):
    headers = {'Authorization': f'Bearer {access_token}'}

    try:
        print("try")
        response = requests.get(constants.BASE_URL + f'/subscriptions/all-subscriptions', headers=headers)
        if response.status_code == 200:
            return response.json()
    except requests.exceptions.HTTPError as errh:
        print(f"HTTP Error: {errh}")
    except requests.exceptions.ConnectionError as errc:
        print(f"Error Connecting: {errc}")
    except requests.exceptions.Timeout as errt:
        print(f"Timeout Error: {errt}")
    except requests.exceptions.RequestException as err:
        print(f"An unexpected error occurred: {err}")


def get_all_posts():
    try:
        response = requests.get(constants.BASE_URL + '/all-posts/')
        print("Response Status Code:", response.status_code)  # Debug: Print status code
        if response.status_code == 200:
            result = response.json()
            print("API Result:", result)  # Debug: Print API result
            return result
        else:
            print("API Error:", response.text)  # Debug: Print error message from API
    except requests.exceptions.HTTPError as errh:
        print(f"HTTP Error: {errh}")
    except requests.exceptions.ConnectionError as errc:
        print(f"Error Connecting: {errc}")
    except requests.exceptions.Timeout as errt:
        print(f"Timeout Error: {errt}")
    except requests.exceptions.RequestException as err:
        print(f"An unexpected error occurred: {err}")


def get_user_all_posts(access_token):
    headers = {'Authorization': f'Bearer {access_token}'}
    try:
        response = requests.get(constants.BASE_URL + f'/user-all-posts', headers=headers)
        print("Response Status Code:", response.status_code)  # Debug: Print status code
        if response.status_code == 200:
            result = response.json()
            print("API Result:", result)  # Debug: Print API result
            return result
        else:
            print("API Error:", response.text)  # Debug: Print error message from API
    except requests.exceptions.HTTPError as errh:
        print(f"HTTP Error: {errh}")
    except requests.exceptions.ConnectionError as errc:
        print(f"Error Connecting: {errc}")
    except requests.exceptions.Timeout as errt:
        print(f"Timeout Error: {errt}")
    except requests.exceptions.RequestException as err:
        print(f"An unexpected error occurred: {err}")


def admin_delete_post(post_id, access_token):
    headers = {'Authorization': f'Bearer {access_token}'}
    try:
        response = requests.delete(constants.BASE_URL + f'/posts/delete-post/{post_id}', headers=headers)
        return response
    except requests.exceptions.HTTPError as errh:
        print(f"HTTP Error: {errh}")
    except requests.exceptions.ConnectionError as errc:
        print(f"Error Connecting: {errc}")
    except requests.exceptions.Timeout as errt:
        print(f"Timeout Error: {errt}")
    except requests.exceptions.RequestException as err:
        print(f"An unexpected error occurred: {err}")


def create_post(title, content, category_id, subcategory_id, tag_id, status, access_token):
    print('trying to create post')
    headers = {'Authorization': f'Bearer {access_token}'}
    params = {
        "title": title,
        "content": content,
        "category_id": category_id,
        "subcategory_id": subcategory_id,
        "tag_id": tag_id,
        "status": status
    }
    try:
        response = requests.post(constants.BASE_URL + '/posts/create-post', json=params, headers=headers)
        print(response.text)
        return response
    except requests.exceptions.HTTPError as errh:
        print(f"HTTP Error: {errh}")
    except requests.exceptions.ConnectionError as errc:
        print(f"Error Connecting: {errc}")
    except requests.exceptions.Timeout as errt:
        print(f"Timeout Error: {errt}")
    except requests.exceptions.RequestException as err:
        print(f"An unexpected error occurred: {err}")


def admin_update_post(post_id, title, content, category_id, subcategory_id, tag_id, status, access_token):
    print('trying3')
    headers = {'Authorization': f'Bearer {access_token}'}
    params = {
        "title": title,
        "content": content,
        "category_id": category_id,
        "subcategory_id": subcategory_id,
        "tag_id": tag_id,
        "status": status
    }
    try:
        response = requests.put(constants.BASE_URL + f'/posts/update-post/{post_id}', json=params, headers=headers)
        print(response.text)
        return response
    except requests.exceptions.HTTPError as errh:
        print(f"HTTP Error: {errh}")
    except requests.exceptions.ConnectionError as errc:
        print(f"Error Connecting: {errc}")
    except requests.exceptions.Timeout as errt:
        print(f"Timeout Error: {errt}")
    except requests.exceptions.RequestException as err:
        print(f"An unexpected error occurred: {err}")




def get_post(post_id: int):
    try:
        response = requests.get(constants.BASE_URL + f'/posts/{post_id}')
        if response.status_code == 200:
            return response.json()
    except requests.exceptions.HTTPError as errh:
        print(f"HTTP Error: {errh}")
    except requests.exceptions.ConnectionError as errc:
        print(f"Error Connecting: {errc}")
    except requests.exceptions.Timeout as errt:
        print(f"Timeout Error: {errt}")




def get_user_post_by_username(username: str):
    try:
        response = requests.get(constants.BASE_URL + f'/user-posts/{username}')
        if response.status_code == 200:
            return response.json()
    except requests.exceptions.HTTPError as errh:
        print(f"HTTP Error: {errh}")
    except requests.exceptions.ConnectionError as errc:
        print(f"Error Connecting: {errc}")
    except requests.exceptions.Timeout as errt:
        print(f"Timeout Error: {errt}")


def get_subcategories_by_category(category_id):
    try:
        response = requests.get(constants.BASE_URL + f'/categories/{category_id}/subcategories/')
        if response.status_code == 200:
            return response.json()
    except requests.exceptions.HTTPError as errh:
        print(f"HTTP Error: {errh}")
    except requests.exceptions.ConnectionError as errc:
        print(f"Error Connecting: {errc}")
    except requests.exceptions.Timeout as errt:
        print(f"Timeout Error: {errt}")


def get_all_categories():
    try:
        response = requests.get(constants.BASE_URL + '/categories/')
        print("Response Status Code:", response.status_code)  # Debug: Print status code
        if response.status_code == 200:
            result = response.json()
            print("API Result:", result)  # Debug: Print API result
            return result
        else:
            print("API Error:", response.text)  # Debug: Print error message from API
    except requests.exceptions.HTTPError as errh:
        print(f"HTTP Error: {errh}")
    except requests.exceptions.ConnectionError as errc:
        print(f"Error Connecting: {errc}")
    except requests.exceptions.Timeout as errt:
        print(f"Timeout Error: {errt}")
    except requests.exceptions.RequestException as err:
        print(f"An unexpected error occurred: {err}")


def add_category(category, access_token):
    headers = {'Authorization': f'Bearer {access_token}'}
    params = {
        "category": category,
    }

    try:
        response = requests.post(constants.BASE_URL + f'/user/create_category', json=params, headers=headers)
        print(response.text)
        return response
    except requests.exceptions.HTTPError as errh:
        print(f"HTTP Error: {errh}")
    except requests.exceptions.ConnectionError as errc:
        print(f"Error Connecting: {errc}")
    except requests.exceptions.Timeout as errt:
        print(f"Timeout Error: {errt}")
    except requests.exceptions.RequestException as err:
        print(f"An unexpected error occurred: {err}")


def update_category(category_id, category, access_token):
    headers = {'Authorization': f'Bearer {access_token}'}
    params = {
        "category": category,
    }

    try:
        response = requests.put(constants.BASE_URL + f'/category/update-category/{category_id}', json=params,
                                headers=headers)
        print(response.text)
        return response
    except requests.exceptions.HTTPError as errh:
        print(f"HTTP Error: {errh}")
    except requests.exceptions.ConnectionError as errc:
        print(f"Error Connecting: {errc}")
    except requests.exceptions.Timeout as errt:
        print(f"Timeout Error: {errt}")
    except requests.exceptions.RequestException as err:
        print(f"An unexpected error occurred: {err}")


def get_user_all_categories(access_token):
    headers = {'Authorization': f'Bearer {access_token}'}
    try:
        response = requests.get(constants.BASE_URL + '/user-all-categories', headers=headers)
        print("Response Status Code:", response.status_code)  # Debug: Print status code
        if response.status_code == 200:
            result = response.json()
            print("API Result:", result)  # Debug: Print API result
            return result
        else:
            print("API Error:", response.text)  # Debug: Print error message from API
    except requests.exceptions.HTTPError as errh:
        print(f"HTTP Error: {errh}")
    except requests.exceptions.ConnectionError as errc:
        print(f"Error Connecting: {errc}")
    except requests.exceptions.Timeout as errt:
        print(f"Timeout Error: {errt}")
    except requests.exceptions.RequestException as err:
        print(f"An unexpected error occurred: {err}")


def user_delete_category(category_id, access_token):
    headers = {'Authorization': f'Bearer {access_token}'}
    try:
        response = requests.delete(constants.BASE_URL + f'/category/delete-category/{category_id}', headers=headers)
        return response
    except requests.exceptions.HTTPError as errh:
        print(f"HTTP Error: {errh}")
    except requests.exceptions.ConnectionError as errc:
        print(f"Error Connecting: {errc}")
    except requests.exceptions.Timeout as errt:
        print(f"Timeout Error: {errt}")
    except requests.exceptions.RequestException as err:
        print(f"An unexpected error occurred: {err}")


def add_subcategory(subcategory, category_id, access_token):
    headers = {'Authorization': f'Bearer {access_token}'}
    params = {
        "subcategory": subcategory,
        "category_id": category_id
    }

    try:
        response = requests.post(constants.BASE_URL + '/user/create_subcategory', json=params, headers=headers)
        print(response.text)
        return response
    except requests.exceptions.HTTPError as errh:
        print(f"HTTP Error: {errh}")
    except requests.exceptions.ConnectionError as errc:
        print(f"Error Connecting: {errc}")
    except requests.exceptions.Timeout as errt:
        print(f"Timeout Error: {errt}")
    except requests.exceptions.RequestException as err:
        print(f"An unexpected error occurred: {err}")


def update_subcategory(subcategory_id, subcategory, category_id, access_token):
    headers = {'Authorization': f'Bearer {access_token}'}
    params = {
        "subcategory": subcategory,
        "category_id": category_id
    }

    try:
        response = requests.put(constants.BASE_URL + f'/user/update_subcategory/{subcategory_id}', json=params,
                                headers=headers)
        response.raise_for_status()  # Raise an exception for HTTP errors
        return response.json()  # Return the response as JSON
    except requests.exceptions.HTTPError as errh:
        print(f"HTTP Error: {errh}")
    except requests.exceptions.ConnectionError as errc:
        print(f"Error Connecting: {errc}")
    except requests.exceptions.Timeout as errt:
        print(f"Timeout Error: {errt}")
    except requests.exceptions.RequestException as err:
        print(f"An unexpected error occurred: {err}")


def user_delete_subcategory(subcategory_id, access_token):
    headers = {'Authorization': f'Bearer {access_token}'}
    try:
        response = requests.delete(constants.BASE_URL + f'/user/delete_subcategory/{subcategory_id}', headers=headers)
        return response
    except requests.exceptions.HTTPError as errh:
        print(f"HTTP Error: {errh}")
    except requests.exceptions.ConnectionError as errc:
        print(f"Error Connecting: {errc}")
    except requests.exceptions.Timeout as errt:
        print(f"Timeout Error: {errt}")
    except requests.exceptions.RequestException as err:
        print(f"An unexpected error occurred: {err}")


def get_category_name(category_id):
    try:
        response = requests.delete(constants.BASE_URL + f'/category/{category_id}')
        return response.json
    except requests.exceptions.HTTPError as errh:
        print(f"HTTP Error: {errh}")
    except requests.exceptions.ConnectionError as errc:
        print(f"Error Connecting: {errc}")
    except requests.exceptions.Timeout as errt:
        print(f"Timeout Error: {errt}")
    except requests.exceptions.RequestException as err:
        print(f"An unexpected error occurred: {err}")


def get_user_all_tags(access_token):
    headers = {'Authorization': f'Bearer {access_token}'}
    try:
        response = requests.get(constants.BASE_URL + '/user-all-tags', headers=headers)
        print("Response Status Code:", response.status_code)  # Debug: Print status code
        if response.status_code == 200:
            result = response.json()
            print("API Result:", result)  # Debug: Print API result
            return result
        else:
            print("API Error:", response.text)  # Debug: Print error message from API
    except requests.exceptions.HTTPError as errh:
        print(f"HTTP Error: {errh}")
    except requests.exceptions.ConnectionError as errc:
        print(f"Error Connecting: {errc}")
    except requests.exceptions.Timeout as errt:
        print(f"Timeout Error: {errt}")
    except requests.exceptions.RequestException as err:
        print(f"An unexpected error occurred: {err}")


def add_tag(tag, access_token):
    headers = {'Authorization': f'Bearer {access_token}'}
    params = {
        "tag": tag,
    }

    try:
        response = requests.post(constants.BASE_URL + f'/user/add-tags', json=params, headers=headers)
        print(response.text)
        return response
    except requests.exceptions.HTTPError as errh:
        print(f"HTTP Error: {errh}")
    except requests.exceptions.ConnectionError as errc:
        print(f"Error Connecting: {errc}")
    except requests.exceptions.Timeout as errt:
        print(f"Timeout Error: {errt}")
    except requests.exceptions.RequestException as err:
        print(f"An unexpected error occurred: {err}")


def edit_tag(tag_id, new_tag, access_token):
    headers = {'Authorization': f'Bearer {access_token}'}
    params = {
        "tag": new_tag,
    }

    try:
        response = requests.put(constants.BASE_URL + f'/user/edit-tag/{tag_id}', json=params, headers=headers)
        print(response.text)
        return response
    except HTTPError as errh:
        print(f"HTTP Error: {errh}")
    except ConnectionError as errc:
        print(f"Error Connecting: {errc}")
    except Timeout as errt:
        print(f"Timeout Error: {errt}")
    except RequestException as err:
        print(f"An unexpected error occurred: {err}")


def delete_tag(tag_id, access_token):
    headers = {'Authorization': f'Bearer {access_token}'}

    try:
        response = requests.delete(constants.BASE_URL + f'/user/delete-tag/{tag_id}', headers=headers)
        print(response.text)
        return response
    except HTTPError as errh:
        print(f"HTTP Error: {errh}")
    except ConnectionError as errc:
        print(f"Error Connecting: {errc}")
    except Timeout as errt:
        print(f"Timeout Error: {errt}")
    except RequestException as err:
        print(f"An unexpected error occurred: {err}")


def get_all_email_templates(access_token):
    print("trying")
    headers = {'Authorization': f'Bearer {access_token}'}
    try:
        print("try")
        response = requests.get(constants.BASE_URL + '/email-templates/all', headers=headers)
        if response.status_code == 200:
            result = response.json()
            return result

    except requests.exceptions.HTTPError as errh:
        print(f"HTTP Error: {errh}")
    except requests.exceptions.ConnectionError as errc:
        print(f"Error Connecting: {errc}")
    except requests.exceptions.Timeout as errt:
        print(f"Timeout Error: {errt}")
    except requests.exceptions.RequestException as err:
        print(f"An unexpected error occurred: {err}")


def get_subcategory_name(subcategory_id):
    try:
        response = requests.delete(constants.BASE_URL + f'/subcategory/{subcategory_id}')
        return response.json
    except requests.exceptions.HTTPError as errh:
        print(f"HTTP Error: {errh}")
    except requests.exceptions.ConnectionError as errc:
        print(f"Error Connecting: {errc}")
    except requests.exceptions.Timeout as errt:
        print(f"Timeout Error: {errt}")
    except requests.exceptions.RequestException as err:
        print(f"An unexpected error occurred: {err}")


def create_template(name, subject, body, access_token):
    print('trying3')
    headers = {'Authorization': f'Bearer {access_token}'}
    params = {
        "name": name,
        "subject": subject,
        "body": body
    }
    try:
        response = requests.post(constants.BASE_URL + f'/email-templates/create-template', json=params, headers=headers)
        if response.status_code == 200:
            result = response.json()
            return result

    except requests.exceptions.HTTPError as errh:
        print(f"HTTP Error: {errh}")
    except requests.exceptions.ConnectionError as errc:
        print(f"Error Connecting: {errc}")
    except requests.exceptions.Timeout as errt:
        print(f"Timeout Error: {errt}")
    except requests.exceptions.RequestException as err:

        print(f"An unexpected error occurred: {err}")

        print(f"An unexpected error occurred: {err}")


def edit_eamil_template(access_token: str, name, subject, body, template_id):
    print("trying")
    headers = {'Authorization': f'Bearer {access_token}'}

    data = {
        "name": name,
        "subject": subject,
        "body": body
    }

    try:
        print("try")
        response = requests.put(constants.BASE_URL + f'/email-templates/update-template/{template_id}', headers=headers,
                                json=data)
        if response.status_code == 200:
            result = response.json()
            return result
    except requests.exceptions.HTTPError as errh:
        print(f"HTTP Error: {errh}")
    except requests.exceptions.ConnectionError as errc:
        print(f"Error Connecting: {errc}")
    except requests.exceptions.Timeout as errt:
        print(f"Timeout Error: {errt}")
    except requests.exceptions.RequestException as err:
        print(f"An unexpected error occurred: {err}")


def get_email_template_by_id(access_token, template_id):
    print("trying")
    headers = {'Authorization': f'Bearer {access_token}'}
    try:
        print("try")
        response = requests.get(constants.BASE_URL + f'/email-templates/{template_id}', headers=headers)
        if response.status_code == 200:
            result = response.json()
            return result
    except requests.exceptions.HTTPError as errh:
        print(f"HTTP Error: {errh}")
    except requests.exceptions.ConnectionError as errc:
        print(f"Error Connecting: {errc}")
    except requests.exceptions.Timeout as errt:
        print(f"Timeout Error: {errt}")
    except requests.exceptions.RequestException as err:
        print(f"An unexpected error occurred: {err}")


def delete_template(access_token, template_id):
    print("trying")
    headers = {'Authorization': f'Bearer {access_token}'}
    try:
        print("try")
        response = requests.delete(constants.BASE_URL + f'/email-templates/delete-template/{template_id}',
                                   headers=headers)
        if response.status_code == 200:
            result = response.json()
            return result
    except requests.exceptions.HTTPError as errh:
        print(f"HTTP Error: {errh}")
    except requests.exceptions.ConnectionError as errc:
        print(f"Error Connecting: {errc}")
    except requests.exceptions.Timeout as errt:
        print(f"Timeout Error: {errt}")
    except requests.exceptions.RequestException as err:
        print(f"An unexpected error occurred: {err}")


def send_email(access_token: str, to, subject, body):
    print("trying")
    headers = {'Authorization': f'Bearer {access_token}'}

    data = {
        "to": to,
        "subject": subject,
        "body": body
    }

    try:
        print("try")
        response = requests.post(constants.BASE_URL + f'/email-templates/send-mail', headers=headers, json=data)
        if response.status_code == 200:
            result = response.json()
            return result
    except requests.exceptions.HTTPError as errh:
        print(f"HTTP Error: {errh}")
    except requests.exceptions.ConnectionError as errc:
        print(f"Error Connecting: {errc}")
    except requests.exceptions.Timeout as errt:
        print(f"Timeout Error: {errt}")
    except requests.exceptions.RequestException as err:
        print(f"An unexpected error occurred: {err}")


def is_service_access_allowed(access_token):
    print("trying")
    headers = {'Authorization': f'Bearer {access_token}'}
    try:
        print("try")
        response = requests.get(constants.BASE_URL + "/subscriptions/is-service-allowed", headers=headers)
        if response.status_code == 200:
            is_allowed = response.json()
            print(is_allowed)
            return is_allowed
    except requests.exceptions.HTTPError as errh:
        print(f"HTTP Error: {errh}")
    except requests.exceptions.ConnectionError as errc:
        print(f"Error Connecting: {errc}")
    except requests.exceptions.Timeout as errt:
        print(f"Timeout Error: {errt}")
    except requests.exceptions.RequestException as err:
        print(f"An unexpected error occurred: {err}")



def upload_medias(file_list, access_token):
    print(file_list)
    print('Trying to upload medias')

    headers = {'Authorization': f'Bearer {access_token}'}

    try:
        response = requests.post(constants.BASE_URL + f"/upload-multiple-files/", files=file_list, headers=headers)

        print('Response status code:', response.status_code)
        print('Response text:', response.text)

        if response.status_code == 200:
            print('Media uploaded successfully.')
        else:
            print('Failed to upload media.')
        return response
    except requests.exceptions.HTTPError as errh:
        print(f"HTTP Error: {errh}")
    except requests.exceptions.ConnectionError as errc:
        print(f"Error Connecting: {errc}")
    except requests.exceptions.Timeout as errt:
        print(f"Timeout Error: {errt}")
    except requests.exceptions.RequestException as err:
        print(f"An unexpected error occurred: {err}")


def subscribe_to_newsletter(name, email, username):
    print("inside api call")

    data = {
      "subscriber_name": name,
      "subscriber_email": email,
      "username":username
    }
    print(data)

    try:
        print('trying to send')
        response = requests.post(constants.BASE_URL + '/newsletter/subscribe_newsletter', json=data)
        print(response.status_code)
        if response.status_code == 200:
            print("successful")
            return response.json

    except requests.exceptions.HTTPError as errh:
        print(f"HTTP Error: {errh}")
    except requests.exceptions.ConnectionError as errc:
        print(f"Error Connecting: {errc}")
    except requests.exceptions.Timeout as errt:
        print(f"Timeout Error: {errt}")
    except requests.exceptions.RequestException as err:
        print(f"An unexpected error occurred: {err}")



def get_user_all_medias(access_token):
    headers = {'Authorization': f'Bearer {access_token}'}
    try:
        response = requests.get(constants.BASE_URL + '/user-all-medias', headers=headers)
        print("Response Status Code:", response.status_code)  # Debug: Print status code
        if response.status_code == 200:
            result = response.json()
            print("API Result:", result)  # Debug: Print API result
            return result
        else:
            print("API Error:", response.text)  # Debug: Print error message from API
    except requests.exceptions.HTTPError as errh:
        print(f"HTTP Error: {errh}")
    except requests.exceptions.ConnectionError as errc:
        print(f"Error Connecting: {errc}")
    except requests.exceptions.Timeout as errt:
        print(f"Timeout Error: {errt}")
    except requests.exceptions.RequestException as err:
        print(f"An unexpected error occurred: {err}")


def get_all_newsletter_subscribers(access_token):
    print("trying")
    headers = {'Authorization': f'Bearer {access_token}'}
    try:
        print("try")
        response = requests.get(constants.BASE_URL + '/newsletter/newsletter-subscribers-for-user', headers=headers)
        if response.status_code == 200:
            result = response.json()
            return result


    except requests.exceptions.HTTPError as errh:
        print(f"HTTP Error: {errh}")
    except requests.exceptions.ConnectionError as errc:
        print(f"Error Connecting: {errc}")
    except requests.exceptions.Timeout as errt:
        print(f"Timeout Error: {errt}")
    except requests.exceptions.RequestException as err:
        print(f"An unexpected error occurred: {err}")


def send_newsletter(access_token: str, subject, body):
    print("trying")
    headers = {'Authorization': f'Bearer {access_token}'}

    data = {
        "to": 'subscribers',
        "subject": subject,
        "body": body
    }

    try:
        print("try")
        response = requests.post(constants.BASE_URL + '/newsletter/send-newsletter', headers=headers, json=data)
        if response.status_code == 200:
            result = response.json()
            return result
    except requests.exceptions.HTTPError as errh:
        print(f"HTTP Error: {errh}")
    except requests.exceptions.ConnectionError as errc:
        print(f"Error Connecting: {errc}")
    except requests.exceptions.Timeout as errt:
        print(f"Timeout Error: {errt}")
    except requests.exceptions.RequestException as err:
        print(f"An unexpected error occurred: {err}")
