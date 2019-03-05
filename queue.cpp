// trying to implement a queue as a refresher
// this will evolve (and hopefully improve) with time
// Date: March 4th, 2019

#include <stdio.h>
#include <stdlib.h>
 
 class Queue
 {
 	public:
 		// members
 		int* elements;

 		int size, front, rear, capacity;

 		// functions
 		bool enqueue(int e);
 		bool dequeue();
 		bool printQueue();

 		// constructor
 		Queue(int capacity)
 		{
 			this->capacity = capacity;
 			size = 0;
 			front = 0;
 			rear = 0;
 			elements = (int*) malloc(sizeof(int) * size); // todo: change to nullptr?
 		}

 	private:
 		bool isFull();
 };

 bool Queue::enqueue(int e)
 {
 	if(!isFull())
 	{
 		this->elements[rear] = e;
 		this->rear = rear+1 % capacity;
 		this->size = size+1; 		
 		return true;
 	}
 	else
 	{
 		printf("Queue is at capacity! Cannot enqueue element. \n"); // todo: implement dynamic growth
 		return false;
 	}
 }

 bool Queue::dequeue()
 {
 	if(this->size == 0)
 	{
 		return false;
 	}
 	else
 	{
 		this->front = front+1 % capacity;
 		this->size = size-1;
		return true;
 	} 	
 }

 bool Queue::isFull()
 {
 	if(size == capacity)
 	{
 		return true;
 	}
 	else
 	{
 		return false;
 	}
 }

 bool Queue::printQueue()
 {
 	for (int i = 0; i < this->size; i= i + 1 % this->capacity)
 	{
 		printf("Index: %d, Element: %d\n", i + this->front, this->elements[i + this->front]);
 	}
 	return true;
 }

int main() 
{
    printf("Beginning test...\n");
	Queue testQueue(5);

	printf("Enqueue element '100'...\n");
	testQueue.enqueue(100);
	testQueue.printQueue();

	printf("Enqueue element '200'...\n");
	testQueue.enqueue(200);
	testQueue.printQueue();

	printf("Enqueue element '300'...\n");
	testQueue.enqueue(300);
	testQueue.printQueue();

	printf("Enqueue element '400'...\n");
	testQueue.enqueue(400);
	testQueue.printQueue();

	printf("Dequeue element...\n");
	testQueue.dequeue();
	testQueue.printQueue();

	printf("Dequeue element...\n");
	testQueue.dequeue();
	testQueue.printQueue();

	printf("Enqueue element '101'...\n");
	testQueue.enqueue(101);
	testQueue.printQueue();

	printf("Enqueue element '201'...\n");
	testQueue.enqueue(201);
	testQueue.printQueue();

	printf("Enqueue element '301'...\n");
	testQueue.enqueue(301);
	testQueue.printQueue();

	printf("Enqueue element '401'...\n");
	testQueue.enqueue(401);
	testQueue.printQueue();

	return 0;
};