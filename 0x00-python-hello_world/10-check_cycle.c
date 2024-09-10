#include "lists.h"

/**
 * check_cycle - checks if a linked list has a cycle.
 * @list: pointer to the head of the list.
 *
 * Return: 1 if there is a cycle, 0 if there is not.
 */
int check_cycle(listint_t *list)
{
    listint_t *slow = list;
    listint_t *fast = list;

    while (fast != NULL && fast->next != NULL)
    {
        slow = slow->next;          /* Move slow pointer by 1 */
        fast = fast->next->next;    /* Move fast pointer by 2 */

        if (slow == fast)           /* Cycle detected */
            return (1);
    }

    return (0);                    /* No cycle */
}
