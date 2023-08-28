#include <iostream>
#include stdio

#define DECREACE_LEN -1
#define INCREASE_LEN  1


// Create the Node class

class Node {
    public:
        int node_value;
        int next_node;
        Node(int value, int next) { // Constructor
            node_value = value;
            next_node = next;
        }

};


// Linked List class
class LinkedList{
    public:
        Node head;
        Node tail;
        int length;

        LinkedList(int value){
            Node node = Node()
        } 

}


