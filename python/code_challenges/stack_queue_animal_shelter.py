from data_structures.queue import Queue


class AnimalShelter:
    def __init__(self):
        self.dog_queue = Queue()
        self.cat_queue = Queue()

    def enqueue(self, animal):
        if isinstance(animal, Dog):
            self.dog_queue.enqueue(animal)
        elif isinstance(animal, Cat):
            self.cat_queue.enqueue(animal)

    def dequeue(self, preferred):
        if preferred == "dog":
            return self.dog_queue.dequeue()
        elif preferred == "cat":
            return self.cat_queue.dequeue()


class Dog:
    pass


class Cat:
    pass
