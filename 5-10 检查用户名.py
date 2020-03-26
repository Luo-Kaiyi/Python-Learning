current_users = ['jarry','tom','bob','james','einstin']
new_users = ['Tom','Bob','Yanliulu','Benjieming','Xiqingwu']
for user in new_users:
    if user.lower() in current_users:
        print("Need to input another user name!")
    else:
        print("This name has not been used.")