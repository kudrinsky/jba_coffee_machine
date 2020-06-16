class User:
    users = []
    n_active = 0


    def __init__(self, active, user_name):
        self.active = active
        self.user_name = user_name
        User.users.append(self.user_name)
        if self.active:
            User.n_active += 1