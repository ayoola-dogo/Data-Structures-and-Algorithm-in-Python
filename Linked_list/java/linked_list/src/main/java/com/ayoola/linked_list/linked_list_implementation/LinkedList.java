package com.ayoola.linked_list.linked_list_implementation;

public class LinkedList {
    Node head;
    int number_of_nodes;

    public LinkedList(){
        this.head = null;
        this.number_of_nodes = 0;
    }

    @Override
    public String toString() {
        return "LinkedList with " + this.size_of_linked_list() + " number of nodes";
    }


    private Node create_node(int parameter){
        Node new_node;
        new_node = new Node(parameter);
        return new_node;
    }

    public int size_of_linked_list(){
        return this.number_of_nodes;
    }

    // traversing a linked list is an Ordo N O(N) running time complexity operation
    public void transverse() {
        Node actual_node = this.head;

        while (actual_node != null){
            System.out.println(actual_node.data);
            actual_node = actual_node.pointer;
        }
    }


    // constant running time complexity O(1)
    public void insert_start(int user_value){
        Node node = this.create_node(user_value);
        if (this.head != null) {
            node.pointer = this.head;
        }
        this.head = node;
        this.number_of_nodes++;
    }

    // linear running time complexity O(N)
    public void insert_end(int user_value){
        Node node = this.create_node(user_value);
        Node actual_node = this.head;

        while (actual_node.pointer != null){
            actual_node = actual_node.pointer;
        }
        actual_node.pointer = node;
        this.number_of_nodes++;
    }
}


class Node {
    int data;
    Node pointer;

    public Node(int value){
        this.data = value;
        this.pointer = null;
    }
}
