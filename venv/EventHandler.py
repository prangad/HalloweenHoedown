#The most basic example of an observable structure.
class Observable():
    def __init__(self):
        self._observers = []

    def attach(self, observer):
        self._observers.append(observer)

    def notifyAll(self, *args, **kwargs):
        for observer in self._observers:
            observer.receive(self, *args, **kwargs)

#The most basic example of an observer structure.
class Observer():
    def __init__(self, observable):
        observable.attach(self)

    def receive(self, *args, **kwargs):
        print("Unhandled observation.")