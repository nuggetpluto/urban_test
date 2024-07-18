import multiprocessing

class WarehouseManager:
    def __init__(self):
        self.data = multiprocessing.Manager().dict()

    def process_request(self, request, queue):
        product, action, amount = request
        if action == "receipt":
            if product in self.data:
                self.data[product] += amount
            else:
                self.data[product] = amount
        elif action == "shipment":
            if product in self.data and self.data[product] >= amount:
                self.data[product] -= amount
        queue.put(self.data.copy())

    def run(self, requests):
        queue = multiprocessing.Queue()
        processes = []
        for request in requests:
            p = multiprocessing.Process(target=self.process_request, args=(request, queue))
            processes.append(p)
            p.start()

        for p in processes:
            p.join()

        while not queue.empty():
            self.data.update(queue.get())

if __name__ == "__main__":
    manager = WarehouseManager()

    requests = [
        ("product1", "receipt", 100),
        ("product2", "receipt", 150),
        ("product1", "shipment", 30),
        ("product3", "receipt", 200),
        ("product2", "shipment", 50)
    ]

    manager.run(requests)

    print(dict(manager.data))
