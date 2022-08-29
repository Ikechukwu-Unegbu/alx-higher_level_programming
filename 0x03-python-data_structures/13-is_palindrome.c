#include "lists.h"

/**
 * reverse_listint - will reverse a linked list
 * @head: pointer to the first node in the linked list
 *
 * Return: pointer to the first node in newly created list
 */
void reverse_listint(listint_t **head)
{
	listint_t *previous = NULL;
	listint_t *curr = *head;
	listint_t *next = NULL;

	while (curr)
	{
		next = curr->next;
		curr->next = previous;
		previous = curr;
		curr = next;
	}

	*head = previous;
}

/**
 * is_palindrome - checks if a linked list is a palindrome
 * @head: double pointer to the linked list
 *
 * Return: 1 if it is, 0 if not
 */
int is_palindrome(listint_t **head)
{
	listint_t *slow = *head, *fast = *head, *temporary = *head, *dup = NULL;

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	while (1)
	{
		fast = fast->next->next;
		if (!fast)
		{
			dup = slow->next;
			break;
		}
		if (!fast->next)
		{
			dup = slow->next->next;
			break;
		}
		slow = slow->next;
	}

	reverse_listint(&dup);

	while (dup && temporary)
	{
		if (temporary->n == dup->n)
		{
			dup = dup->next;
			temporary = temporary->next;
		}
		else
			return (0);
	}

	if (!dup)
		return (1);

	return (0);
}
