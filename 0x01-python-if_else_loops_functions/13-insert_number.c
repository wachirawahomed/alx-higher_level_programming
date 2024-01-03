#include "lists.h"
/**
 * insert_node - Inserts a number into a sorted singly-linked list.
 * @head: A pointer the head of the linked list.
 * @number: The number to insert.
 *
 * Return: NULL if it fails otherwise pointer to the new node.
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current, *new;
	if (head == NULL)
		return NULL;

	new = malloc(sizeof(listint_t));

	if (new == NULL)
		return (NULL);
	current = *head;
	new->n = number;
	new->next = NULL;
	if (*head == NULL)
	{
		*head = new;
		return (new);
	}
	if (current->n > number)
	{
		new->next = current;
		*head = new;
		return (new);
	}

	while (current->next != NULL)
	{
		if(current->next->n > number)
		{
			new->next = current->next;
			current->next = new;
			return new;
		}
		current = current->next;
	}
	current->next = new;
	return (new);
}
