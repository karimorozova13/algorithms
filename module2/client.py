from queue import Queue
import random

class Client:
    def __init__(self, name) -> None:
        self.name = name
        self.operations = random.randint(1,5)
        
class Bank:
    def __init__(self) -> None:
        self.clients = Queue()
    def new_client(self, client):
        self.clients.put(client)
    def serve_clients(self):
        while not self.clients.empty():
            current_client = self.clients.get()
            print(f'Serve {current_client.name} with {current_client.operations} operations')
            
            
bank = Bank()

for i in range(5):
    bank.new_client(Client(f'Client - {i + 1}'))
    
bank.serve_clients()