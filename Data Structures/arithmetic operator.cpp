#include<iostream>
#include<math.h>
using namespace std;

template <typename T>
struct stack{
        T element;
        stack<T> *next;
};

stack<int> *valuestack;
stack<char> *operatorstack;

template<typename T>
stack<T>* newnode(T e){
    stack<T>* new_node = new stack<T>;
    new_node->element = e;
    new_node->next = NULL;
    return new_node;
}

template<typename T>
void push (stack<T>** top, stack<T>* node){
        node->next = *top;
        *top = node;
    
}   

template<typename T>
T pop(stack<T>** top){
    T temp = (*top)->element;
    *top = (*top)->next;
    return temp;
}

int operate(char o, int val1, int val2){
    switch(o){
        case '^':
            return (int)pow(val2, val1);
            break;
        case '*':
            return val2 * val1;
            break;
        case '/':
            return val2 / val1;
            break;
        case '+':
            return val2 + val1;
            break;
        case '-':
            return val2 - val1;
            break;
        default:
            break;
        }
}

void push_to_valuestack(int n){
    stack<int>* addnode = newnode<int>(n);
    push<int>(&valuestack, addnode);
}

int op_to_precedence(char c){
    switch(c){
        case '^':
            return 3;
            break;
        case '*':
            return 2;
            break;
        case '/':
            return 2;
            break;
        case '+':
            return 1;
            break;
        case '-':
            return 1;
            break;
        default:
            break;
}
}

void calc(){
    int val1 = pop<int>(&valuestack);
    int val2 = pop<int>(&valuestack);

    char op = pop<char>(&operatorstack);
    int res = operate(op, val1, val2);

    push_to_valuestack(res);
}
void push_to_operator_stack(char o){
    int opnow_prec = op_to_precedence(o);

    int opbef_prec = 0;
    if(operatorstack!=NULL) 
        opbef_prec = op_to_precedence(operatorstack->element);

    while(opnow_prec<=opbef_prec){
        calc();
        if(operatorstack!=NULL) 
            opbef_prec = operatorstack->element;
        else
            opbef_prec = 0;
    }

    stack<char>* addnode = newnode<char>(o);
    push<char>(&operatorstack, addnode);
}

int main(){
    

    int op_or_num = 1; //0 if operator   1 if num;
    int valinput;
    char charinput;
    int cont = 1;

    while(cont)
    {
        if(op_or_num ==1){
            cout << "Value:";
            cin >> valinput;
            push_to_valuestack(valinput);
            op_or_num = 0;
        }
        else
        {
            cout << "Operator:";
            cin >> charinput;
            push_to_operator_stack(charinput);
            op_or_num = 1;
        }

    if(op_or_num==0){
        cout << "press 0 if you want to stop entering expression\n";
        cin >> cont;
    }
        }

        while(valuestack->next!=NULL){
            calc();
        }

        cout << "Result is:" << valuestack->element;
        return 0;
}