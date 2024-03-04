class Smartphone:
    def __init__(self, memory: float):
        self._memory = memory
        self._apps = list()
        self._is_on = False

    def power(self):
        self._is_on = True

    def install(self, app, app_memory):
        if self._is_on:
            if self._memory >= app_memory:
                self._apps.append(app)
                self._memory -= app_memory
                return f"Installing {app}"
            return f"Not enough memory to install {app}"
        else:
            return f"Turn on your phone to install {app}"

    def status(self):
        return f"Total apps: {len(self._apps)}. Memory left: {self._memory}"


smartphone = Smartphone(100)
print(smartphone.install("Facebook", 60))
smartphone.power()
print(smartphone.install("Facebook", 60))
print(smartphone.install("Messenger", 20))
print(smartphone.install("Instagram", 40))
print(smartphone.status())
