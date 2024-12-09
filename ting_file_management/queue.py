from ting_file_management.abstract_queue import AbstractQueue


class Queue(AbstractQueue):
    def __init__(self):
        self.data=[]

    def enqueue(self, value):
        self.data.append(value)

    def dequeue(self ):
        if self.is_empty():
            raise IndexError("Índice Inválido ou Inexistente")
        return self.data.pop(0)

    def search(self, index):
        if index < 0 or index >= len(self.data):
            raise IndexError("Índice Inválido ou Inexistente")
        return self.data[index]

    def is_empty(self):
        return len(self.data) == 0

    def __len__(self):
        return len(self.data)
