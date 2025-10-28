managing_staff = {
    'name': {
        'first': 'mehrshad',
        'last': 'o'
    },
    'access_roles': [
        'CEO',
        'CO Founder'
    ],
    'clearance_level': 10
}
accsess_cart = managing_staff['name']['last']
role0 = managing_staff['access_roles'][-1]

managing_staff['access_roles'].append('Manager_Partner')
role1 = managing_staff['access_roles'][-1]
print(accsess_cart)
print(f"{role0}, {role1}")