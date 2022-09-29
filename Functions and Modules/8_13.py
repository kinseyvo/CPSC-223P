def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info


my_profile = build_profile('kinsey', 'vo',school='csuf',major='computer science',hobby='funko')
print(my_profile)