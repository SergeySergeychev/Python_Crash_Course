# Start with a copy of user_profile.py.
# Build profile of your self by calling build_profile().
# Provide parametres as first and last names and three others key-value pairs
# that describe you.

def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key,value in user_info.items():
        profile[key] = value
    return profile

my_profile = build_profile('sergey',
                           'sergeychev',
                           age=34,
                           field='electrical power engineering',
                           marital_status='married',
                           )
print(my_profile)
