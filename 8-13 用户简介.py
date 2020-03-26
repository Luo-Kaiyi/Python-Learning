def build_profile(first, last, **user_info):
    profile = {'first_name': first, 'last_name': last}
    for key, value in user_info.items():
        profile[key] = value
    return profile


my_profile = build_profile('luo', 'kaiyi', location='chengdu', age=22, major='computer')
print(my_profile)