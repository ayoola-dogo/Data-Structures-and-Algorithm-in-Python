package com.ayoola.linked_list;
import com.ayoola.linked_list.linked_list_implementation.LinkedList;

public class LinkedListApp {
    public static void main(String[] args) {
        LinkedList linked_list;
        linked_list = new LinkedList();
        linked_list.insert_start(10);
        linked_list.insert_start(5);
        linked_list.insert_start(39);
        linked_list.insert_end(78);
        System.out.println(linked_list);
        linked_list.transverse();
    }
}
