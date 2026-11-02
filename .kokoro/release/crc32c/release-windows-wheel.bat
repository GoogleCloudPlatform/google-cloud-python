@rem Copyright 2019 Google LLC. All rights reserved.
@rem
@rem Licensed under the Apache License, Version 2.0 (the "License");
@rem you may not use this file except in compliance with the License.
@rem You may obtain a copy of the License at
@rem
@rem     http://www.apache.org/licenses/LICENSE-2.0
@rem
@rem Unless required by applicable law or agreed to in writing, software
@rem distributed under the License is distributed on an "AS IS" BASIS,
@rem WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
@rem See the License for the specific language governing permissions and
@rem limitations under the License.

@echo "Starting Windows release"

cd /d %~dp0..\..\..\packages\google-crc32c || goto :error

if "%PUBLISH_WHEELS%"=="" set PUBLISH_WHEELS=true

@echo "Build, Test, and Publish Wheels"
call scripts\windows\build.bat || goto :error

goto :EOF

:error
exit /b 1
