#include "lists.h"

/**
 * is_palindrome - Checks if a singly linked list is a palindrome.
 * @head: A pointer to the head of the linked list.
 *
 * Return: If the linked list is not a palindrome - 0.
 *         If the linked list is a palindrome - 1.
 */

int is_palindrome(listint_t **head)
{

	if (!*head || !(*head))
	{
		return (1);
	}

	if (p_check(head, *head))
	{
		return (1);
	}
	return (0);
}

/**
 *  p_check - Check for palindrome
 *
 *  @left: Go left
 *
 *  @right: Go right
 *
 *  Return: Integer
 */


int p_check(listint_t **left, listint_t *right)
{
	int is_p = 0;

	if (right)
	{
		is_p = p_check(left, right->next);
	}
	else
	{
		return (1);
	}

	if (is_p == 1)
	{
		if ((*left)->n == right->n)
		{
			(*left) = (*left)->next;
			return (1);
		}
	}
	return (0);
}
