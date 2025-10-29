user_data = {'name': 'Mehrshad', 'department': 'IT', 'access_level': 3}

# user_data['office_loc'] this gonna give us this error ---> KeyError: 'office_loc'

if 'health_insurance' in user_data:
    proccess_insurance(user_data['health_insurance'])

clearance = user_data.get('security_level', 'basic')

bonus_elegible = user_data['status'] if 'status' in user_data else 'contractor'

