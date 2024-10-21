#include "lists.h"
#include <stdlib.h>

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: pointer to pointer of first node of listint_t list
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
    listint_t *slow = *head, *fast = *head, *prev = NULL, *temp;
    listint_t *second_half, *first_half = *head;
    int is_palindrome = 1;

    if (*head == NULL || (*head)->next == NULL)
        return (1);

    /* Find the middle and reverse the second half */
    while (fast != NULL && fast->next != NULL)
    {
        fast = fast->next->next;
        temp = slow->next;
        slow->next = prev;
        prev = slow;
        slow = temp;
    }

    /* If the list has odd number of elements */
    if (fast != NULL)
    {
        slow = slow->next;
    }

    second_half = slow;
    first_half = prev;

    /* Compare the first and second halves */
    while (second_half != NULL)
    {
        if (first_half->n != second_half->n)
        {
            is_palindrome = 0;
            break;
        }
        first_half = first_half->next;
        second_half = second_half->next;
    }

    /* Restore the list to its original state */
    prev = NULL;
    while (first_half != NULL)
    {
        temp = first_half->next;
        first_half->next = prev;
        prev = first_half;
        first_half = temp;
    }
    *head = prev;

    return is_palindrome;
}
