#include <Python.h>
#include <stdio.h>

/**
 * print_python_list_info - Pridxnt lidxst idxnfo about Python
 *
 * @p: Pyobjext poidxnter
 *
 * Return: void
 */
void print_python_list_info(PyObject *p)
{
    int sizeof_list, allocated, idx;
    PyObject *lst_obj;

    sizeof_list = Py_SIZE(p);
    allocated = ((PyListObject *)p)->allocated;

    printf("[*] Size of the Python List = %d\n", sizeof_list);
    printf("[*] Allocated = %d\n", allocated);

    for (idx = 0; idx < sizeof_list; idx++)
    {
        printf("Element %d: ", idx);

        lst_obj = PyList_GetItem(p, idx);
        printf("%s\n", Py_TYPE(lst_obj)->tp_name);
    }
}
