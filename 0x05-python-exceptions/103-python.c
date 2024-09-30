#include <Python.h>
#include <stdio.h>
#include <stdlib.h>
#include <object.h>
#include <listobject.h>
#include <bytesobject.h>
#include <floatobject.h>
#include <string.h>

/**
 * display_python_bytes - Display information about a Python byte object
 * @p: PyObject pointer
 */
void display_python_bytes(PyObject *p)
{
	size_t length, index;
	char *byte_str;

	setbuf(stdout, NULL);
	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	byte_str = ((PyBytesObject *)(p))->ob_sval;
	length = PyBytes_Size(p);

	printf("  size: %ld\n  trying string: %s\n", length, byte_str);
	length = length >= 10 ? 10 : length + 1;

	printf("  first %ld bytes: ", length);
	for (index = 0; index < length - 1; index++)
		printf("%02hhx ", byte_str[index]);
	printf("%02hhx\n", byte_str[index]);
}

/**
 * display_python_float - Display information about a Python float object
 * @p: PyObject pointer
 */
void display_python_float(PyObject *p)
{
	double float_val;
	char *float_str;

	setbuf(stdout, NULL);
	printf("[.] float object info\n");
	if (!PyFloat_Check(p))
	{
		printf("  [ERROR] Invalid Float Object\n");
		return;
	}

	float_val = ((PyFloatObject *)(p))->ob_fval;
	float_str = PyOS_double_to_string(float_val, 'r', 0, Py_DTSF_ADD_DOT_0, NULL);

	printf("  value: %s\n", float_str);
}

/**
 * display_python_list - Display information about a Python list object
 * @p: PyObject pointer
 */
void display_python_list(PyObject *p)
{
	size_t size, allocated, index;
	const char *elem_type;
	PyListObject *list_obj;

	setbuf(stdout, NULL);
	printf("[*] Python list info\n");
	if (!PyList_Check(p))
	{
		printf("  [ERROR] Invalid List Object\n");
		return;
	}

	list_obj = (PyListObject *)p;
	size = PyList_GET_SIZE(p);
	allocated = list_obj->allocated;

	printf("[*] Size of the Python List = %ld\n[*] Allocated = %ld\n", size, allocated);

	for (index = 0; index < size; index++)
	{
		elem_type = list_obj->ob_item[index]->ob_type->tp_name;
		printf("Element %ld: %s\n", index, elem_type);

		if (strcmp(elem_type, "bytes") == 0)
			display_python_bytes(list_obj->ob_item[index]);
		else if (strcmp(elem_type, "float") == 0)
			display_python_float(list_obj->ob_item[index]);
	}
}

