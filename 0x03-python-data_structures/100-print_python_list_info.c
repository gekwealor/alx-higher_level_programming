#include <Python.h>

/**
 * print_python_list_info - Basic info about Python lists printed.
 * @p: A PyObject list.
 */
void print_python_list_info(PyObject *p)
{
	int size, alloc, g;
	PyObject *obj;

	size = Py_SIZE(p);
	alloc = ((PyListObject *)p)->allocated;

	printf("[*] Size of the Python List = %d\n", size);
	printf("[*] Allocated = %d\n", alloc);

	for (g = 0; g < size; g++)
	{
		printf("Element %d: ", g);

		obj = PyList_GetItem(p, g);
		printf("%s\n", Py_TYPE(obj)->tp_name);
	}
}
