class EventManager:
    def __init__(self):
        self.subscribers = {}
    
    def subscribe(self, eventType, callback):
        if eventType not in self.subscribers:
            self.subscribers[eventType] = []
        self.subscribers[eventType].append(callback)
    
    def publish(self, eventType, data=None):
        if eventType in self.subscribers:
            for callback in self.subscribers[eventType]:
                callback(data)