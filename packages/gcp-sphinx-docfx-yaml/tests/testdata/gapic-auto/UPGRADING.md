# 2.0.0 Migration Guide

The 2.0 release of the `google-cloud-texttospeech` client is a significant upgrade based on a [next-gen code generator](https://github.com/googleapis/gapic-generator-python), and includes substantial interface changes. Existing code written for earlier versions of this library will likely require updates to use this version. This document describes the changes that have been made, and what you need to do to update your usage.

If you experience issues or have questions, please file an [issue](https://github.com/googleapis/python-texttospeech/issues).

## Supported Python Versions

> **WARNING**: Breaking change

The 2.0.0 release requires Python 3.6+.


## Method Calls

> **WARNING**: Breaking change

Methods expect request objects. We provide a script that will convert most common use cases.

* Install the library and `libcst`.

```py
python3 -m pip install google-cloud-texttospeech libcst
```

* The script `fixup_keywords.py` is shipped with the library. It expects
an input directory (with the code to convert) and an empty destination directory.

```sh
$ fixup_keywords.py --input-directory .samples/ --output-directory samples/
```

**Before:**
```py
from google.cloud import texttospeech

client = texttospeech.TextToSpeechClient()

voices = client.list_voices(language_code="no")
```


**After:**
```py
from google.cloud import texttospeech

client = texttospeech.TextToSpeechClient()

voices = client.list_voices(request={"language_code": "no"})
```

### More Details

In `google-cloud-texttospeech<2.0.0`, parameters required by the API were positional parameters and optional parameters were keyword parameters.

**Before:**
```py
    def synthesize_speech(
        self,
        input_,
        voice,
        audio_config,
        retry=google.api_core.gapic_v1.method.DEFAULT,
        timeout=google.api_core.gapic_v1.method.DEFAULT,
        metadata=None,
    ):
```

In the 2.0.0 release, all methods have a single positional parameter `request`. Method docstrings indicate whether a parameter is required or optional.

Some methods have additional keyword only parameters. The available parameters depend on the [`google.api.method_signature` annotation](https://github.com/googleapis/googleapis/blob/master/google/cloud/texttospeech/v1/cloud_tts.proto#L53) specified by the API producer.


**After:**
```py
    def synthesize_speech(
        self,
        request: cloud_tts.SynthesizeSpeechRequest = None,
        *,
        input: cloud_tts.SynthesisInput = None,
        voice: cloud_tts.VoiceSelectionParams = None,
        audio_config: cloud_tts.AudioConfig = None,
        retry: retries.Retry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> cloud_tts.SynthesizeSpeechResponse:
```

> **NOTE:** The `request` parameter and flattened keyword parameters for the API are mutually exclusive.
> Passing both will result in an error.


Both of these calls are valid:

```py
response = client.synthesize_speech(
    request={
        "input": input_text,
        "voice": voice,
        "audio_config": audio_config
    }
)
```

```py
response = client.synthesize_speech(
    input=input_text,
    voice=voice,
    audio_config=audio_config
)
```

This call is invalid because it mixes `request` with a keyword argument `audio_config`. Executing this code
will result in an error.

```py
response = client.synthesize_speech(
    request={
        "input": input_text,
        "voice": voice,
    },
    audio_config=audio_config
)
```



## Enums and Types


> **WARNING**: Breaking change

The submodules `enums` and `types` have been removed.

**Before:**
```py

from google.cloud import texttospeech

encoding = texttospeech.enums.AudioEncoding.MP3
voice = texttospeech.types.VoiceSelectionParams(language_code="en-US")
```


**After:**
```py
from google.cloud import texttospeech

encoding = texttospeech.AudioEncoding.MP3
voice = texttospeech.VoiceSelectionParams(language_code="en-US")
```
