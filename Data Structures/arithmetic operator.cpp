#include<iostream>
using namespace std;

template <typename T>
struct stack{
        T element;
        stack *next;
};

template<typename T>
stack<T>* push(T e){
    stack<T>* newnode = new stack<T>;
    newnode->element = e;
    newnode->next = NULL;
    return newnode;
}

template<typename T>
void push (stack<T>* top, stack<T>* node){
    if(top==NULL){
        top = node;
    }
    else
    {
        top->next = node;
        top = node;
    }
}   

template<typename T>
T pop(stack<T>*t top){
    
}