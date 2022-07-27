class AppStore:
    def __init__(self):
        self.app_list = []

    def add_application(self, app):
        self.app_list.append(app)

    def remove_application(self, app):
        self.app_list.remove(app)

    def block_application(self, app):
        app.blocked = True

    def total_apps(self):
        return len(self.app_list)

class Application:
    def __init__(self, name, blocked = False):
        self.name = name
        self.blocked = blocked
        