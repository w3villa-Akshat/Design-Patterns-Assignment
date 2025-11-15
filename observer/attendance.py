# Subject
class AttendanceSubject:
    def __init__(self):
        self.observers = []

    def add_observer(self, obs):
        self.observers.append(obs)

    def notify_all(self, message):
        for o in self.observers:
            o.update(message)

    def employee_check_in(self, name):
        print(f"{name} checked in")
        self.notify_all(f"{name} just checked in")


# Observer 1
class HRSystemObserver:
    def update(self, msg):
        print("[HR] Notification:", msg)


# Observer 2
class SecuritySystemObserver:
    def update(self, msg):
        print("[Security] Alert:", msg)