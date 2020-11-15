class Observable():
    def __init__(self):
        self._observers = []

    def attach(self, observer):
        self._observers.append(observer)

    def notifyAll(self, *args, **kwargs):
        for observer in self._observers:
            observer.notify(self, *args, **kwargs)

class Observer():
    def __init__(self, observable):
        observable.attach(self)

    def notify(self, *args, **kwargs):
        print("Unhandled observation.")