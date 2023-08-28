#include <iostream>
#include stdio

#define DECREACE_LEN -1
#define INCREASE_LEN  1


// Create the Node class

class Node {
    public:
        int node_value;
        int next_node;
        Node(int value = NULL, int next = NULL) { // Constructor
            node_value = value;
            next_node = next;
        }

        bool isEmpty(){
            if node_value == NULL return false;
            else return true;
        }

};


// Linked List class
class LinkedList{
    public:
        Node head;
        Node tail;
        int length;

        LinkedList(int value = NULL){
            Node node = Node(value)
            head = node;
            tail = node;
            
            if node.isEmpty{
                length = 0;
            } else{
                length = 1;
            }
        }


         bool append(){

         }

         bool prepend(){

         }

         bool insert(){

         }

         Node pop(){

         }

         Node popFirst(){

         }

         Node get(){

         }

         bool set(){

         }

         Node remove(){

         }

         void reverse(){

         }

    private:
        void _updateLenght(int value){
            length += value;
        }

};


