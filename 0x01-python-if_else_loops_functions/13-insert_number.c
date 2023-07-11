#include <stddef.h>
#include "lists.h"
#include <stdlib.h>

/**
 * insert_node - Puts a number into a sorted singly-linked list.
 * @head: The head of the linked list is a pointer
 * @number: Insert the number
 *
 * Return: the address of the new node
 * Or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node = *head, *new;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;

	if (node == NULL || node->n >= number)
	{
		new->next = node;
		*head = new;
		return (new);
	}

	while (node && node->next && node->next->n < number)
		node = node->next;

	new->next = node->next;
	node->next = new;

	return (new);
}
