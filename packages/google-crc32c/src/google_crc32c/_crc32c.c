#define PY_SSIZE_T_CLEAN
#include <Python.h>
#include <crc32c/crc32c.h>

/* The minimum buffer size in bytes (1MB) required to justify the overhead of releasing the GIL. */
static const Py_ssize_t gil_threshold = 1024 * 1024;

static int
_should_release_gil(Py_ssize_t length, PyObject *chunk_obj)
{
    /* Checks if the chunk is immutable (bytes) to prevent concurrent modification,
     * and large enough to benefit from releasing the GIL. */
    return (length >= gil_threshold && PyBytes_Check(chunk_obj));
}

static PyObject *
_crc32c_extend(PyObject *self, PyObject *args)
{
    unsigned long crc_input;
    uint32_t crc;
    const char *chunk;
    Py_ssize_t length;
    PyThreadState *save = NULL;

    if (!PyArg_ParseTuple(args, "ky#", &crc_input, &chunk, &length))
        return NULL;

    if (_should_release_gil(length, PyTuple_GET_ITEM(args, 1))) {
        save = PyEval_SaveThread();
    }

    crc = crc32c_extend((uint32_t)crc_input, (const uint8_t*)chunk, length);

    if (save) {
        PyEval_RestoreThread(save);
    }

    return PyLong_FromUnsignedLong(crc);
}


static PyObject *
_crc32c_value(PyObject *self, PyObject *args)
{
    uint32_t crc;
    const char *chunk;
    Py_ssize_t length;
    PyThreadState *save = NULL;

    if (!PyArg_ParseTuple(args, "y#", &chunk, &length))
        return NULL;

    if (_should_release_gil(length, PyTuple_GET_ITEM(args, 0))) {
        save = PyEval_SaveThread();
    }

    crc = crc32c_value((const uint8_t*)chunk, length);

    if (save) {
        PyEval_RestoreThread(save);
    }

    return PyLong_FromUnsignedLong(crc);
}


static PyMethodDef Crc32cMethods[] = {
    {"extend",  _crc32c_extend, METH_VARARGS,
     "Return an updated CRC32C checksum."},
    {"value",  _crc32c_value, METH_VARARGS,
     "Return an initial CRC32C checksum."},
    {NULL, NULL, 0, NULL}        /* Sentinel */
};


static struct PyModuleDef crc32cmodule = {
    PyModuleDef_HEAD_INIT,
    "_crc32c",   /* name of module */
    NULL, /* module documentation, may be NULL */
    -1,       /* size of per-interpreter state of the module,
                 or -1 if the module keeps state in global variables. */
    Crc32cMethods
};


PyMODINIT_FUNC
PyInit__crc32c(void)
{
    return PyModule_Create(&crc32cmodule);
}
