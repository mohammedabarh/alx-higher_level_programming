#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * reverse_list - Reverses a linked list
 * @head: Pointer to the head of the list
 * Return: Pointer to the new head of the reversed list
 */
listint_t *reverse_list(listint_t *head)
{
    listint_t *prev = NULL;
    listint_t *current = head;
    listint_t *next = NULL;

    while (current != NULL)
    {
        next = current->next;
        current->next = prev;
        prev = current;
        current = next;
    }

    return prev;
}

/**
 * is_palindrome - Checks if a singly linked list is a palindrome
 * @head: Double pointer to the head of the list
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
    listint_t *slow = *head, *fast = *head;
    listint_t *second_half, *prev_of_slow = *head;
    listint_t *midnode = NULL;
    int is_palindrome = 1;

    if (*head == NULL || (*head)->next == NULL)
        return 1;

    /* Get the middle of the list */
    while (fast != NULL && fast->next != NULL)
    {
        fast = fast->next->next;
        prev_of_slow = slow;
        slow = slow->next;
    }

    /* Handle odd length list */
    if (fast != NULL)
    {
        midnode = slow;
        slow = slow->next;
    }

    /* Reverse the second half */
    second_half = reverse_list(slow);
    
    /* Compare first and second halves */
    listint_t *temp1 = *head;
    listint_t *temp2 = second_half;

    while (temp2 != NULL)
    {
        if (temp1->n != temp2->n)
        {
            is_palindrome = 0;
            break;
        }
        temp1 = temp1->next;
        temp2 = temp2->next;
    }

    /* Restore the list */
    second_half = reverse_list(second_half);

    if (midnode != NULL)
    {
        prev_of_slow->next = midnode;
        midnode->next = second_half;
    }
    else
    {
        prev_of_slow->next = second_half;
    }

    return is_palindrome;
}
