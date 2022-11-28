#include<stdlib.h>
#include<stdio.h>

struct Node{
    int data;
    struct Node *next;
};

void deleteStart(struct Node** head){
    struct Node* temp = *head;

    // If head is NULL it means Singly Linked List is empty
    if(*head == NULL){
        printf("Impossible to delete from empty Singly Linked List");
        return;
    }

    // move head to next node
    *head = (*head)->next;
    printf("Deleted: %d\n", temp->data);
    free(temp);
}

void insertStart(struct Node** head, int data){

    // dynamically create memory for this newNode
    struct Node* newNode = (struct Node*) malloc(sizeof(struct Node));

    // assign data value
    newNode->data = data;
    // change the next node of this newNode
    // to current head of Linked List
    newNode->next = *head;

    //re-assign head to this newNode
    *head = newNode;
    printf("Inserted %d\n",newNode->data);
}

void display(struct Node* node){
    printf("\nLinked List: ");
    // as linked list will end when Node is Null
    while(node!=NULL){
        printf("%d ",node->data);
        node = node->next;
    }
    printf("\n");
}

void printReverse(struct Node* head)
{
    // Base case
    if (head == NULL)
       return;

    // print the list after head node
    printReverse(head->next);

    // After everything else is printed, print head
    printf(" %d ", head->data);
}



int main()
{
    int choice,value;
    struct Node* head = NULL;

    while(1==1)
    {
    printf("\t \t 1.INSERT HEAD  \n");
    printf("\t \t 2.DELETE HEAD \n");
    printf("\t \t 3.DISPLAY REVERSE  \n");
    printf("\t \t 4.DISPLAY  \n \n \n");

    printf("\t \t Enter your choice:");
    scanf("%d",&choice);



    switch(choice)
    {
        case 1:
        printf(" \n \n Enter the value to be inserted: ");
        scanf("%d",&value);
        insertStart(&head,value);
        break;

        case 2:
        deleteStart(&head);
        printf("\n \n Head deleted successfully \n \n ");
        break;

        case 3:
        printReverse(head);
        break;

        case 4:
        display(head);
        break;


        default:
        printf(" \n \n Oops...Invalid input");
        break;

    }
    }

    return 0;
}
