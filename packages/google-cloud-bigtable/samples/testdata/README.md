#### To generate singer_pb2.py and descriptors.pb file from singer.proto using `protoc`
```shell
cd samples
protoc --proto_path=testdata/ --include_imports --descriptor_set_out=testdata/descriptors.pb --python_out=testdata/ testdata/singer.proto 
```