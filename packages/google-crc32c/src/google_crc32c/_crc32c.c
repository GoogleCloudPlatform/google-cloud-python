#define PY_SSIZE_T_CLEAN
#include <Python.h>
#include <crc32c/crc32c.h>

/* The minimum buffer size in bytes (1MB) required to justify the overhead of releasing the GIL. */
static const Py_ssize_t gil_threshold = 1024 * 1024;

static int
_should_release_gil(const Py_buffer *chunk)
{
    /* Release the GIL only for chunks of at least gil_threshold bytes backed
     * by an immutable bytes object (a bytes instance or a memoryview of one). */
    PyObject *owner = chunk->obj;

    if (chunk->len < gil_threshold || owner == NULL) {
        return 0;
    }
    if (PyMemoryView_Check(owner)) {
        owner = PyMemoryView_GET_BASE(owner);
    }
    return owner != NULL && PyBytes_Check(owner);
}

static uint32_t
_extend_buffer(uint32_t crc, const Py_buffer *chunk)
{
    PyThreadState *save = NULL;

    if (_should_release_gil(chunk)) {
        save = PyEval_SaveThread();
    }

    crc = crc32c_extend(crc, (const uint8_t*)chunk->buf, (size_t)chunk->len);

    if (save) {
        PyEval_RestoreThread(save);
    }

    return crc;
}

static PyObject *
_crc32c_extend(PyObject *self, PyObject *args)
{
    unsigned long crc_input;
    uint32_t crc;
    Py_buffer chunk;

    /* "y*" accepts any C-contiguous object supporting the buffer protocol
     * (bytes, bytearray, memoryview, array.array, mmap, ...). */
    if (!PyArg_ParseTuple(args, "ky*", &crc_input, &chunk))
        return NULL;

    crc = _extend_buffer((uint32_t)crc_input, &chunk);
    PyBuffer_Release(&chunk);

    return PyLong_FromUnsignedLong(crc);
}


static PyObject *
_crc32c_value(PyObject *self, PyObject *args)
{
    uint32_t crc;
    Py_buffer chunk;

    if (!PyArg_ParseTuple(args, "y*", &chunk))
        return NULL;

    /* crc32c_value(data, n) is crc32c_extend(0, data, n). */
    crc = _extend_buffer(0, &chunk);
    PyBuffer_Release(&chunk);

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
    PyObject *m = PyModule_Create(&crc32cmodule);
    if (m == NULL) {
        return NULL;
    }
    if (PyModule_AddIntConstant(m, "GIL_RELEASE_THRESHOLD", (long)gil_threshold) < 0) {
        Py_DECREF(m);
        return NULL;
    }
    return m;
}
