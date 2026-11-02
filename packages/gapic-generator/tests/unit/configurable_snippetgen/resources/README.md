# Resources for testing Configurable SnippetGen

Each subdirectory should correspond to an API and contain three types of files.  For example:

```
.
├── README.md
└── speech
    ├── request.desc
    ├── speech_createCustomClass.json
    └── speech_v1_generated_adaptation_create_custom_class_basic_async.py
```

### `request.desc`:

This is a copy of the CodeGeneratorRequest message used by the GAPIC generator.  To generate it:

1. Install `protoc`.
1. Install [gapic-generator-python](https://github.com/googleapis/gapic-generator-python).
1. Run the following command from the root of a local copy of [googleapis](https://github.com/googleapis/googleapis):

    ```
    API=speech
    VERSION=v1

    protoc google/cloud/$API/$VERSION/*.proto \
    --experimental_allow_proto3_optional \
    --proto_path=. \
    --dump_out=.
    ```

### Snippet config files

Handwritten json file containing the configuration of a code snippet.  Each config file typically represents both `sync` and `async` Python snippets, and could specify more than one API version.

### Golden files

One or more expected snippet for each config file.
