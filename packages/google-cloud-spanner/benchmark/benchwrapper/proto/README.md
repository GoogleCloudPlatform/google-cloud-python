# Regenerating protos
Run the following command from python-spanner/ directory.
```
python3 -m grpc_tools.protoc -I . --python_out=. --grpc_python_out=. benchmark/benchwrapper/proto/*.proto
