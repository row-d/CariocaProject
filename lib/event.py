""" Event emitter class
    Description: Esta clase permite emitir eventos y escucharlos. Util para la comunicacion entre modulos.
    Usage:
        from event import EventEmitter
        class MyClass(EventEmitter):
            def __init__(self):
                super().__init__()
            def myMethod(self):
                self.emit('myEvent', 'Hello World')
        myClass = MyClass()
        myClass.on('myEvent', lambda msg: print(msg))
"""

class EventEmitter:
    def __init__(self):
        self._listeners = {}
    def emit(self, event, *args, **kwargs):
        for listener in self._listeners.get(event, ()):
            listener(*args, **kwargs)
    def on(self, event, listener):
        self._listeners.setdefault(event, []).append(listener)
    def once(self, event, listener):
        def onetime(*args, **kwargs):
            self.remove(event, onetime)
            listener(*args, **kwargs)
        self.on(event, onetime)
        
    def remove(self, event, listener):
        self._listeners.get(event, []).remove(listener)
        
    def removeAll(self, event):
        self._listeners[event] = []
    
        