import heapq

def convert_img(file_path, target_format):
    print(f"Конвертація {file_path} до {target_format} формату...")
    return f"{file_path.split('.')[0]}.{target_format}"

class PriorityQueue:
    def __init__(self) -> None:
        self.queue = []
    def enqueue(self, task, priority):
        heapq.heappush(self.queue, (-priority, task))
    def dequeue(self):
        return heapq.heappop(self.queue)[1]
    def is_empty(self):
        return not bool(self.queue)
    
pq = PriorityQueue()

pq.enqueue(("sample1.jpg", "png"), 1)  
pq.enqueue(("premium_sample.jpg", "bmp"), 10) 
pq.enqueue(("sample2.jpg", "tiff"), 1) 

while not pq.is_empty():
    file_name, target_format = pq.dequeue()
    output = convert_img(file_name, target_format)
    print(f"Зображення було успішно конвертовано і збережено як {output}!")