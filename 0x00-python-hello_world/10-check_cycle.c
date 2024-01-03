#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * check_cycle - checks if a linked list contains a cycle
 * @list: a linked list
 * Return: 1 if the list has a cycle, 0 otherwise
 */
int check_cycle(listint_t *list)
{
	listint_t *first = list;
	listint_t *second = list;

	if (list = NULL)
		return (0);

	second = second->next;
	while (second != NULL && second->next != NULL && first != NULL)
	{
		if (first == iter2)
		{
			return (1);
		}
		first = first->next;
		second = second->next->next;
	}

	return (0);
}
