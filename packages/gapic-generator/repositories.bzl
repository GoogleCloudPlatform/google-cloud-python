load("@bazel_tools//tools/build_defs/repo:http.bzl", "http_archive")

_PANDOC_BUILD_FILE = """
filegroup(
    name = "pandoc",
    srcs = ["bin/pandoc"],
    visibility = ["//visibility:public"],
)"""

def gapic_generator_python():

    _maybe(
        http_archive,
        name = "pandoc_linux_arm_64",
        build_file_content = _PANDOC_BUILD_FILE,
        strip_prefix = "pandoc-3.7.0.2",
        url = "https://github.com/jgm/pandoc/releases/download/3.7.0.2/pandoc-3.7.0.2-linux-arm64.tar.gz",
    )

    _maybe(
        http_archive,
        name = "pandoc_linux_x86_64",
        build_file_content = _PANDOC_BUILD_FILE,
        strip_prefix = "pandoc-3.7.0.2",
        url = "https://github.com/jgm/pandoc/releases/download/3.7.0.2/pandoc-3.7.0.2-linux-amd64.tar.gz",
    )

    _maybe(
        http_archive,
        name = "pandoc_macOS_arm_64",
        build_file_content = _PANDOC_BUILD_FILE,
        strip_prefix = "pandoc-3.7.0.2",
        url = "https://github.com/jgm/pandoc/releases/download/3.7.0.2/pandoc-3.7.0.2-arm64-macOS.zip",
    )

    _maybe(
        http_archive,
        name = "pandoc_macOS_x86_64",
        build_file_content = _PANDOC_BUILD_FILE,
        strip_prefix = "pandoc-3.7.0.2",
        url = "https://github.com/jgm/pandoc/releases/download/3.7.0.2/pandoc-3.7.0.2-x86_64-macOS.zip",
    )

    _maybe(
        http_archive,
        name = "pandoc_windows_x86_64",
        build_file_content = _PANDOC_BUILD_FILE,
        strip_prefix = "pandoc-3.7.0.2",
        url = "https://github.com/jgm/pandoc/releases/download/3.7.0.2/pandoc-3.7.0.2-windows-x86_64.zip",
    )


def gapic_generator_register_toolchains():
    native.register_toolchains(
        "@gapic_generator_python//:pandoc_toolchain_linux_arm_64",
        "@gapic_generator_python//:pandoc_toolchain_linux_x86_64",
        "@gapic_generator_python//:pandoc_toolchain_macOS_arm_64",
        "@gapic_generator_python//:pandoc_toolchain_macOS_x86_64",
        "@gapic_generator_python//:pandoc_toolchain_windows_x86_64",
    )

def _maybe(repo_rule, name, strip_repo_prefix = "", **kwargs):
    if not name.startswith(strip_repo_prefix):
        return
    repo_name = name[len(strip_repo_prefix):]
    if repo_name in native.existing_rules():
        return
    repo_rule(name = repo_name, **kwargs)
