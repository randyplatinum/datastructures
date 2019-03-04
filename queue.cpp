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

 		// constructor
 		Queue(int size)
 		{
 			size = this->size;
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
 		this->rear = rear+1 % capacity;
 		this->elements[rear] = e;
 		this->size = size+1; 		
 		return true;
 	}
 	else
 	{
 		return false;
 	}
 }

 bool Queue::dequeue()
 {
 	// stub 
 	return true;
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

int main() {
    printf("Beginning test...\n");
    Queue testQueue(5);
    if(!testQueue.enqueue(0) || !testQueue.dequeue())
    {
    	printf("Test failed!\n");
    	return 1;
    }
    else
    {
    	printf("Test succeeded!\n");
    	return 0;
    }
};