#include <stdio.h>
 
 class Queue
 {
 	public:
 		// members
 		int* elements;

 		// functions
 		bool enqueue(int e);
 		bool dequeue();

 		// constructor
 		Queue()
 		{
 			elements = NULL; // todo: change to nullptr?
 		}

 	private:
 };

 bool Queue::enqueue(int e)
 {
 	// stub 
 	return true;
 }

 bool Queue::dequeue()
 {
 	// stub 
 	return true;
 }

int main() {
    printf("Beginning test...\n");
    Queue testQueue;
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