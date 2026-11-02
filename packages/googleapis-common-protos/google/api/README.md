## API Protos

This folder contains the schema of the configuration model for Google's
internal API serving platform, which handles routing, quotas, monitoring,
logging, and the like.

Google refers to this configuration colloquially as the "service config",
and the `service.proto` file in this directory is the entry point for
understanding these.

## Using these protos

To be honest, we probably open sourced way too much of this (basically by
accident). There are a couple files in here you are most likely to be
interested in: `http.proto`, `documentation.proto`, `auth.proto`, and
`annotations.proto`.

### HTTP and REST

The `http.proto` file contains the `Http` message (which then is wrapped
in an annotation in `annotations.proto`), which provides a specification
for REST endpoints and verbs (`GET`, `POST`, etc.) on RPC methods.
We recommend use of this annotation for describing the relationship
between RPCs and REST endpoints.

### Documentation

The `documentation.proto` file contains a `Documentation` message which
provides a mechanism to fully describe an API, allowing a tool to build
structured documentation artifacts.

### Authentication

The `auth.proto` file contains descriptions of both authentication rules
and authenticaion providers, allowing you to describe what your services
expect and accept from clients.

## api-compiler

Google provides a tool called [api-compiler][], which is a tool that accepts
a protocol buffer descriptor and a YAML file specifying some of the
options described in `service.proto`, and outputs a much more thorough
`Service` descriptor based on the information it infers from the protos
themselves.

  [api-compiler]: https://github.com/googleapis/api-compiler
