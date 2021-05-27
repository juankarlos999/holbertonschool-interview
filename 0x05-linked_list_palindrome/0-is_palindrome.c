#include "lists.h"
#include <stddef.h>
/**
 * recurPalindrome - Checks if singly linked list is palindrome
 * @left: Pointer to head of singly linked list
 * @right: Head of singly linked list
 * Return: 0 if it's not a palindrome, 1 if it's a palindrome
 */

int recursionPalindrome(listint_t **left, listint_t *right)
{
	int aux;

	if (right == NULL)
		return (1);

	aux = recursionPalindrome(left, right->next);
	if (aux == 0)
		return (0);

	aux = (right->n == (*left)->n);

	*left = (*left)->next;
	return (aux);
}
/**
 * is_palindrome - Checks if singly linked list is palindrome
 * @head: Pointer to head of singly linked list
 * Return: 0 if it's not a palindrome, 1 if it's a palindrome
 */
int is_palindrome(listint_t **head)
{
	if (!head)
		return (0);
	return (recursionPalindrome(head, *head));
}