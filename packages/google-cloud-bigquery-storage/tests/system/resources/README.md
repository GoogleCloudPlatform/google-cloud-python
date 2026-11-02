Steps to update `person_pb2.py`

1 . Ensure that your environment is using python 3.10 or older which is needed
for step 2.

2. Use pip install `grpcio-tools`

3. cd into this directory and run 
```
python -m grpc_tools.protoc --proto_path=. --python_out=. person.proto
```

4. Add license header to `person_pb2.py`
