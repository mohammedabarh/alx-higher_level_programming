#include <stdlib.h>
#include "lists.h"

/**
 * insert_node - Inserts a number into a sorted singly linked list
 * @head: Pointer to pointer of first node of listint_t list
 * @number: Integer to be included in new node
 * Return: Address of the new node or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
    listint_t *new_node, *current, *prev;

    /* Create new node */
    new_node = malloc(sizeof(listint_t));
    if (new_node == NULL)
        return (NULL);
    new_node->n = number;
    new_node->next = NULL;

    /* If list is empty or new node should be inserted at beginning */
    if (*head == NULL || (*head)->n >= number)
    {
        new_node->next = *head;
        *head = new_node;
        return (new_node);
    }

    /* Traverse the list to find the insertion point */
    current = *head;
    prev = NULL;
    while (current != NULL && current->n < number)
    {
        prev = current;
        current = current->next;
    }

    /* Insert the new node */
    prev->next = new_node;
    new_node->next = current;

    return (new_node);
}
