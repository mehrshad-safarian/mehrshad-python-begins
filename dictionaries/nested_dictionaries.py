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




# --------------------------------------------
# 🧠 Notes for future reference:
#
# Managing staff structure example:
# managing_staff = {
#     'name': {
#         'first': 'mehrshad',
#         'last': 'o'
#     },
#     'access_roles': ['CEO', 'CO Founder'],
#     'clearance_level': 10
# }
#
# Accessing data:
# accsess_cart = managing_staff['name']['last']          # gets 'o'
# role0 = managing_staff['access_roles'][-1]             # gets 'CO Founder'
#
# ✅ Correct way to add and access a new role:
# managing_staff['access_roles'].append('Manager_Partner')   # append adds new role
# role1 = managing_staff['access_roles'][-1]                 # get the last added role
#
# print(accsess_cart)
# print(f"{role0}, {role1}")
# # Output:
# # o
# # CO Founder, Manager_Partner
#
# ❌ Common mistake (misspelled key and append misuse):
# role1 = managing_staff['access_roles'].append('Manager_Partner')  # returns None
# role1 = managing_staff['accsess_role'][-1]                        # KeyError
#
# 🧩 Remember:
# - .append() modifies the list but returns None.
# - Always use correct key names (here: 'access_roles', not 'accsess_role').
# - 'roles' is plural because it holds multiple role names.
# --------------------------------------------
