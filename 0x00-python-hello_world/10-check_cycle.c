#include "lists.h"

/**
 * check_cycle - check for cycle in single link list
 * @list: singly linked list to be checked
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *curr;

	if (list == NULL)
		return (0);
	
	curr = list->next;

	while (curr != NULL)
	{
		if (curr == list)
			return (1);
		curr = curr->next;
	}

	return (0);
}
