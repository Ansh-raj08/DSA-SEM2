class Queue:
	def __init__(self, capacity):
		self.front = 0
		self.rear = 0
		self.size = 0
		self.capacity = capacity
		self.items = [None] * capacity

	def enqueue(self, value):
		if self.is_full():
			print("Queue overflow")
			return
		self.items[self.rear] = value
		self.rear = (self.rear + 1) % self.capacity
		self.size += 1

	def dequeue(self):
		if self.is_empty():
			print("Queue underflow")
			return
		value = self.items[self.front]
		self.items[self.front] = None
		self.front = (self.front + 1) % self.capacity
		self.size -= 1
		return value

	def peek(self):
		if self.is_empty():
			return
		return self.items[self.front]

	def is_empty(self):
		return self.size == 0

	def is_full(self):
		return self.size == self.capacity

	def contents(self):
		# Snapshot current queue from front to rear in order.
		result = []
		idx = self.front
		for _ in range(self.size):
			result.append(self.items[idx])
			idx = (idx + 1) % self.capacity
		return result


if __name__ == "__main__":
	q = Queue(3)
	print("empty?", q.is_empty())
	q.dequeue()  # underflow demo
	q.enqueue(1)
	q.enqueue(2)
	q.enqueue(3)
	q.enqueue(4)  # overflow demo
	print("front:", q.peek())
	print("contents:", q.contents())
	print("dequeued:", q.dequeue())
	print("dequeued:", q.dequeue())
	q.enqueue(5)
	print("contents now:", q.contents())
	print("front now:", q.peek())
