from datetime import datetime

def getCurrentTime():
    return datetime.now().strftime("%m-%d-%Y %H:%M:%S")


class Messenger:
    def __init__(self, listeners=[]):
        self.listeners = listeners
    
    def send(self, message):
        for listener in self.listeners:
            listener.receive(message)

    def receive(self, message):
        # Must be implemented by extending classes
        pass

# Coded Class deriving from the above pre-exisiting Class
class SaveMessages(Messenger):
    def __init__(self, listeners=[]):
        super().__init__(listeners)
        self.savedMessages = []

    def receive(self, message):
        self.savedMessages.append({'message': message, 'time': getCurrentTime()})

    def printMessages(self):
        for m in self.savedMessages:
            print(f'Message "{m["message"]}" was received at this Time: {m["time"]}')
        self.savedMessages = []



# Testing code with below
listener = SaveMessages()

sender = Messenger([listener])

sender.send('Hello, there! This is the first message')

sender.send('Oh hi! This is the second message!')

sender.send('Hola! This is the third and final message!')

listener.printMessages()

