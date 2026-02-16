# QA Report
## Unit Tests
.Connecting to ws://localhost:9090...
Server is ready! Recording for 0.1 seconds...
....Cannot connect to server socket err = No such file or directory
Cannot connect to server request channel
jack server is not running or cannot be started
JackShmReadWritePtr::~JackShmReadWritePtr - Init not done for -1, skipping unlock
JackShmReadWritePtr::~JackShmReadWritePtr - Init not done for -1, skipping unlock
Cannot connect to server socket err = No such file or directory
Cannot connect to server request channel
jack server is not running or cannot be started
JackShmReadWritePtr::~JackShmReadWritePtr - Init not done for -1, skipping unlock
JackShmReadWritePtr::~JackShmReadWritePtr - Init not done for -1, skipping unlock
Cannot connect to server socket err = No such file or directory
Cannot connect to server request channel
jack server is not running or cannot be started
JackShmReadWritePtr::~JackShmReadWritePtr - Init not done for -1, skipping unlock
JackShmReadWritePtr::~JackShmReadWritePtr - Init not done for -1, skipping unlock
INFO:Config:Config reloaded from app.yaml
Connecting to ws://localhost:9090...
Server is ready! Recording for 5 seconds...
.INFO:root:Single model mode currently only works with custom models.
INFO:Config:Config reloaded from app.yaml
Connecting to ws://localhost:9091...
ERROR:websockets.server:opening handshake failed
Traceback (most recent call last):
  File "/home/danny/testing/fast-voice/.venv/lib/python3.11/site-packages/websockets/http11.py", line 138, in parse
    request_line = yield from parse_line(read_line)
                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/danny/testing/fast-voice/.venv/lib/python3.11/site-packages/websockets/http11.py", line 320, in parse_line
    line = yield from read_line(MAX_LINE_LENGTH)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/danny/testing/fast-voice/.venv/lib/python3.11/site-packages/websockets/streams.py", line 46, in read_line
    raise EOFError(f"stream ends after {p} bytes, before end of line")
EOFError: stream ends after 0 bytes, before end of line

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "/home/danny/testing/fast-voice/.venv/lib/python3.11/site-packages/websockets/server.py", line 547, in parse
    request = yield from Request.parse(
              ^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/danny/testing/fast-voice/.venv/lib/python3.11/site-packages/websockets/http11.py", line 140, in parse
    raise EOFError("connection closed while reading HTTP request line") from exc
EOFError: connection closed while reading HTTP request line

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "/home/danny/testing/fast-voice/.venv/lib/python3.11/site-packages/websockets/sync/server.py", line 592, in conn_handler
    connection.handshake(
  File "/home/danny/testing/fast-voice/.venv/lib/python3.11/site-packages/websockets/sync/server.py", line 189, in handshake
    raise self.protocol.handshake_exc
websockets.exceptions.InvalidMessage: did not receive a valid HTTP request
INFO:websockets.server:connection open
INFO:websockets.server:connection open
INFO:root:New monitor connected
INFO:root:New client connected
INFO:root:Using Device=cuda with precision float16
INFO:root:Loading model: small
INFO:httpx:HTTP Request: GET https://huggingface.co/api/models/Systran/faster-whisper-small/revision/main "HTTP/1.1 200 OK"
INFO:root:Running faster_whisper backend.
Server is ready! Recording for 5 seconds...
INFO:faster_whisper:Processing audio with duration 00:01.000
INFO:faster_whisper:VAD filter removed 00:01.000 of audio
INFO:faster_whisper:Processing audio with duration 00:01.000
INFO:faster_whisper:VAD filter removed 00:01.000 of audio
INFO:faster_whisper:Processing audio with duration 00:01.000
INFO:faster_whisper:VAD filter removed 00:00.496 of audio
INFO:faster_whisper:Processing audio with duration 00:01.300
INFO:faster_whisper:VAD filter removed 00:00.496 of audio
INFO:faster_whisper:Processing audio with duration 00:01.400
INFO:faster_whisper:VAD filter removed 00:00.496 of audio
INFO:faster_whisper:Processing audio with duration 00:01.500
INFO:faster_whisper:VAD filter removed 00:00.496 of audio
INFO:faster_whisper:Processing audio with duration 00:01.600
INFO:faster_whisper:VAD filter removed 00:00.496 of audio
INFO:faster_whisper:Processing audio with duration 00:01.700
INFO:faster_whisper:VAD filter removed 00:00.496 of audio
INFO:faster_whisper:Processing audio with duration 00:01.800
INFO:faster_whisper:VAD filter removed 00:00.496 of audio
INFO:faster_whisper:Processing audio with duration 00:01.900
INFO:faster_whisper:VAD filter removed 00:00.496 of audio
INFO:faster_whisper:Processing audio with duration 00:02.000
INFO:faster_whisper:VAD filter removed 00:00.496 of audio
INFO:faster_whisper:Processing audio with duration 00:02.100
INFO:faster_whisper:VAD filter removed 00:00.496 of audio
INFO:faster_whisper:Processing audio with duration 00:02.200
INFO:faster_whisper:VAD filter removed 00:00.496 of audio
INFO:faster_whisper:Processing audio with duration 00:02.300
INFO:faster_whisper:VAD filter removed 00:00.496 of audio
INFO:faster_whisper:Processing audio with duration 00:02.400
INFO:faster_whisper:VAD filter removed 00:00.496 of audio
INFO:faster_whisper:Processing audio with duration 00:02.400
INFO:faster_whisper:VAD filter removed 00:00.496 of audio
INFO:faster_whisper:Processing audio with duration 00:02.500
INFO:faster_whisper:VAD filter removed 00:00.496 of audio
INFO:faster_whisper:Processing audio with duration 00:02.500
INFO:faster_whisper:VAD filter removed 00:00.496 of audio
INFO:faster_whisper:Processing audio with duration 00:02.500
INFO:faster_whisper:VAD filter removed 00:00.496 of audio
INFO:faster_whisper:Processing audio with duration 00:02.500
INFO:faster_whisper:VAD filter removed 00:00.496 of audio
INFO:faster_whisper:Processing audio with duration 00:02.500
INFO:faster_whisper:VAD filter removed 00:00.496 of audio
INFO:faster_whisper:Processing audio with duration 00:02.500
INFO:faster_whisper:VAD filter removed 00:00.496 of audio
INFO:faster_whisper:Processing audio with duration 00:02.500
INFO:faster_whisper:VAD filter removed 00:00.496 of audio
INFO:faster_whisper:Processing audio with duration 00:02.500
INFO:faster_whisper:VAD filter removed 00:00.496 of audio
INFO:faster_whisper:Processing audio with duration 00:02.500
INFO:faster_whisper:VAD filter removed 00:00.496 of audio
INFO:faster_whisper:Processing audio with duration 00:02.500
INFO:faster_whisper:VAD filter removed 00:00.496 of audio
INFO:faster_whisper:Processing audio with duration 00:02.500
INFO:faster_whisper:VAD filter removed 00:00.496 of audio
INFO:root:Connection closed by client
INFO:root:Cleaning up.
INFO:root:Exiting speech to text thread
## Pylint Report
************* Module fast_voice.config
src/fast_voice/config.py:12:0: C0303: Trailing whitespace (trailing-whitespace)
src/fast_voice/config.py:24:0: C0303: Trailing whitespace (trailing-whitespace)
src/fast_voice/config.py:30:0: C0303: Trailing whitespace (trailing-whitespace)
src/fast_voice/config.py:33:0: C0303: Trailing whitespace (trailing-whitespace)
src/fast_voice/config.py:37:0: C0303: Trailing whitespace (trailing-whitespace)
src/fast_voice/config.py:49:0: C0303: Trailing whitespace (trailing-whitespace)
src/fast_voice/config.py:55:0: C0303: Trailing whitespace (trailing-whitespace)
src/fast_voice/config.py:57:0: C0301: Line too long (111/100) (line-too-long)
src/fast_voice/config.py:59:0: C0303: Trailing whitespace (trailing-whitespace)
src/fast_voice/config.py:62:0: C0303: Trailing whitespace (trailing-whitespace)
src/fast_voice/config.py:73:0: C0301: Line too long (107/100) (line-too-long)
src/fast_voice/config.py:1:0: C0114: Missing module docstring (missing-module-docstring)
src/fast_voice/config.py:8:0: C0115: Missing class docstring (missing-class-docstring)
src/fast_voice/config.py:65:15: W0718: Catching too general exception Exception (broad-exception-caught)
src/fast_voice/config.py:57:16: W1203: Use lazy % formatting in logging functions (logging-fstring-interpolation)
src/fast_voice/config.py:63:17: W1514: Using open without explicitly specifying an encoding (unspecified-encoding)
src/fast_voice/config.py:66:12: W1203: Use lazy % formatting in logging functions (logging-fstring-interpolation)
src/fast_voice/config.py:69:4: C0116: Missing function or method docstring (missing-function-docstring)
src/fast_voice/config.py:75:12: W1203: Use lazy % formatting in logging functions (logging-fstring-interpolation)
src/fast_voice/config.py:86:19: W0718: Catching too general exception Exception (broad-exception-caught)
src/fast_voice/config.py:87:16: W1203: Use lazy % formatting in logging functions (logging-fstring-interpolation)
src/fast_voice/config.py:97:19: W0718: Catching too general exception Exception (broad-exception-caught)
src/fast_voice/config.py:98:16: W1203: Use lazy % formatting in logging functions (logging-fstring-interpolation)
src/fast_voice/config.py:114:4: C0116: Missing function or method docstring (missing-function-docstring)
src/fast_voice/config.py:22:11: E0203: Access to member '_initialized' before its definition line 38 (access-member-before-definition)
src/fast_voice/config.py:2:0: C0411: standard import "time" should be placed before third party import "yaml" (wrong-import-order)
src/fast_voice/config.py:3:0: C0411: standard import "threading" should be placed before third party import "yaml" (wrong-import-order)
src/fast_voice/config.py:4:0: C0411: standard import "os" should be placed before third party import "yaml" (wrong-import-order)
src/fast_voice/config.py:5:0: C0411: standard import "logging" should be placed before third party import "yaml" (wrong-import-order)
src/fast_voice/config.py:6:0: C0411: standard import "typing.Any" should be placed before third party import "yaml" (wrong-import-order)
************* Module fast_voice.client
src/fast_voice/client/__init__.py:1:0: C0114: Missing module docstring (missing-module-docstring)
************* Module fast_voice.client.utils
src/fast_voice/client/utils.py:27:0: C0303: Trailing whitespace (trailing-whitespace)
src/fast_voice/client/utils.py:46:0: C0303: Trailing whitespace (trailing-whitespace)
src/fast_voice/client/utils.py:57:0: C0303: Trailing whitespace (trailing-whitespace)
src/fast_voice/client/utils.py:74:61: C0303: Trailing whitespace (trailing-whitespace)
src/fast_voice/client/utils.py:75:0: C0303: Trailing whitespace (trailing-whitespace)
src/fast_voice/client/utils.py:126:0: C0303: Trailing whitespace (trailing-whitespace)
src/fast_voice/client/utils.py:149:0: C0303: Trailing whitespace (trailing-whitespace)
src/fast_voice/client/utils.py:1:0: C0114: Missing module docstring (missing-module-docstring)
src/fast_voice/client/utils.py:59:11: W0718: Catching too general exception Exception (broad-exception-caught)
src/fast_voice/client/utils.py:40:8: R1732: Consider using 'with' for resource-allocating operations (consider-using-with)
src/fast_voice/client/utils.py:64:0: C0115: Missing class docstring (missing-class-docstring)
src/fast_voice/client/utils.py:96:0: C0115: Missing class docstring (missing-class-docstring)
src/fast_voice/client/utils.py:152:8: W0233: __init__ method from a non direct base class 'TranscriptionTeeClient' is called (non-parent-init-called)
src/fast_voice/client/utils.py:97:4: W0231: __init__ method from base class 'TranscriptionClient' is not called (super-init-not-called)
src/fast_voice/client/utils.py:97:4: R0913: Too many arguments (25/5) (too-many-arguments)
src/fast_voice/client/utils.py:97:4: R0917: Too many positional arguments (25/5) (too-many-positional-arguments)
src/fast_voice/client/utils.py:97:4: R0914: Too many local variables (26/15) (too-many-locals)
src/fast_voice/client/utils.py:151:8: C0415: Import outside toplevel (fast_voice.whisper_live.client.TranscriptionTeeClient) (import-outside-toplevel)
************* Module fast_voice.client.daemon
src/fast_voice/client/daemon.py:24:0: C0303: Trailing whitespace (trailing-whitespace)
src/fast_voice/client/daemon.py:39:0: C0303: Trailing whitespace (trailing-whitespace)
src/fast_voice/client/daemon.py:50:0: C0303: Trailing whitespace (trailing-whitespace)
src/fast_voice/client/daemon.py:1:0: C0114: Missing module docstring (missing-module-docstring)
src/fast_voice/client/daemon.py:52:11: W0718: Catching too general exception Exception (broad-exception-caught)
src/fast_voice/client/daemon.py:33:8: R1732: Consider using 'with' for resource-allocating operations (consider-using-with)
************* Module fast_voice.client.core
src/fast_voice/client/core.py:29:0: C0303: Trailing whitespace (trailing-whitespace)
src/fast_voice/client/core.py:32:0: C0303: Trailing whitespace (trailing-whitespace)
src/fast_voice/client/core.py:35:0: C0303: Trailing whitespace (trailing-whitespace)
src/fast_voice/client/core.py:38:0: C0303: Trailing whitespace (trailing-whitespace)
src/fast_voice/client/core.py:41:0: C0303: Trailing whitespace (trailing-whitespace)
src/fast_voice/client/core.py:47:0: C0303: Trailing whitespace (trailing-whitespace)
src/fast_voice/client/core.py:53:0: C0303: Trailing whitespace (trailing-whitespace)
src/fast_voice/client/core.py:57:0: C0303: Trailing whitespace (trailing-whitespace)
src/fast_voice/client/core.py:61:0: W0311: Bad indentation. Found 13 spaces, expected 12 (bad-indentation)
src/fast_voice/client/core.py:85:0: C0303: Trailing whitespace (trailing-whitespace)
src/fast_voice/client/core.py:93:0: C0303: Trailing whitespace (trailing-whitespace)
src/fast_voice/client/core.py:96:0: C0303: Trailing whitespace (trailing-whitespace)
src/fast_voice/client/core.py:98:0: C0301: Line too long (120/100) (line-too-long)
src/fast_voice/client/core.py:99:0: C0303: Trailing whitespace (trailing-whitespace)
src/fast_voice/client/core.py:102:0: C0303: Trailing whitespace (trailing-whitespace)
src/fast_voice/client/core.py:106:0: C0303: Trailing whitespace (trailing-whitespace)
src/fast_voice/client/core.py:143:0: C0303: Trailing whitespace (trailing-whitespace)
src/fast_voice/client/core.py:146:46: C0303: Trailing whitespace (trailing-whitespace)
src/fast_voice/client/core.py:148:0: C0303: Trailing whitespace (trailing-whitespace)
src/fast_voice/client/core.py:151:0: W0311: Bad indentation. Found 19 spaces, expected 20 (bad-indentation)
src/fast_voice/client/core.py:152:0: W0311: Bad indentation. Found 19 spaces, expected 20 (bad-indentation)
src/fast_voice/client/core.py:154:0: W0311: Bad indentation. Found 19 spaces, expected 20 (bad-indentation)
src/fast_voice/client/core.py:159:0: W0311: Bad indentation. Found 21 spaces, expected 20 (bad-indentation)
src/fast_voice/client/core.py:162:0: W0311: Bad indentation. Found 21 spaces, expected 20 (bad-indentation)
src/fast_voice/client/core.py:164:0: W0311: Bad indentation. Found 21 spaces, expected 20 (bad-indentation)
src/fast_voice/client/core.py:165:0: C0303: Trailing whitespace (trailing-whitespace)
src/fast_voice/client/core.py:173:0: W0311: Bad indentation. Found 13 spaces, expected 12 (bad-indentation)
src/fast_voice/client/core.py:179:25: C0303: Trailing whitespace (trailing-whitespace)
src/fast_voice/client/core.py:188:0: C0303: Trailing whitespace (trailing-whitespace)
src/fast_voice/client/core.py:205:0: C0303: Trailing whitespace (trailing-whitespace)
src/fast_voice/client/core.py:213:0: C0303: Trailing whitespace (trailing-whitespace)
src/fast_voice/client/core.py:1:0: C0114: Missing module docstring (missing-module-docstring)
src/fast_voice/client/core.py:12:0: R0902: Too many instance attributes (9/7) (too-many-instance-attributes)
src/fast_voice/client/core.py:34:8: C0415: Import outside toplevel (ctypes.CFUNCTYPE, ctypes.c_char_p, ctypes.c_int, ctypes.cdll) (import-outside-toplevel)
src/fast_voice/client/core.py:36:29: W0613: Unused argument 'filename' (unused-argument)
src/fast_voice/client/core.py:36:39: W0613: Unused argument 'line' (unused-argument)
src/fast_voice/client/core.py:36:45: W0613: Unused argument 'function' (unused-argument)
src/fast_voice/client/core.py:36:55: W0613: Unused argument 'err' (unused-argument)
src/fast_voice/client/core.py:36:60: W0613: Unused argument 'fmt' (unused-argument)
src/fast_voice/client/core.py:39:8: C0103: Variable name "ERROR_HANDLER_FUNC" doesn't conform to snake_case naming style (invalid-name)
src/fast_voice/client/core.py:172:15: W0718: Catching too general exception Exception (broad-exception-caught)
src/fast_voice/client/core.py:178:4: C0116: Missing function or method docstring (missing-function-docstring)
src/fast_voice/client/core.py:195:15: W0718: Catching too general exception Exception (broad-exception-caught)
src/fast_voice/client/core.py:5:0: C0411: standard import "uuid" should be placed before third party imports "pyaudio", "websockets" (wrong-import-order)
src/fast_voice/client/core.py:6:0: C0411: standard import "sys" should be placed before third party imports "pyaudio", "websockets" (wrong-import-order)
************* Module fast_voice.client.tui
src/fast_voice/client/tui.py:44:0: C0303: Trailing whitespace (trailing-whitespace)
src/fast_voice/client/tui.py:56:71: C0303: Trailing whitespace (trailing-whitespace)
src/fast_voice/client/tui.py:58:0: C0303: Trailing whitespace (trailing-whitespace)
src/fast_voice/client/tui.py:69:0: C0303: Trailing whitespace (trailing-whitespace)
src/fast_voice/client/tui.py:72:0: C0303: Trailing whitespace (trailing-whitespace)
src/fast_voice/client/tui.py:77:0: C0301: Line too long (104/100) (line-too-long)
src/fast_voice/client/tui.py:101:0: C0303: Trailing whitespace (trailing-whitespace)
src/fast_voice/client/tui.py:104:0: C0303: Trailing whitespace (trailing-whitespace)
src/fast_voice/client/tui.py:137:0: C0303: Trailing whitespace (trailing-whitespace)
src/fast_voice/client/tui.py:153:0: C0303: Trailing whitespace (trailing-whitespace)
src/fast_voice/client/tui.py:159:0: C0303: Trailing whitespace (trailing-whitespace)
src/fast_voice/client/tui.py:161:0: C0303: Trailing whitespace (trailing-whitespace)
src/fast_voice/client/tui.py:1:0: C0114: Missing module docstring (missing-module-docstring)
src/fast_voice/client/tui.py:21:0: C0115: Missing class docstring (missing-class-docstring)
src/fast_voice/client/tui.py:21:0: R0902: Too many instance attributes (8/7) (too-many-instance-attributes)
src/fast_voice/client/tui.py:32:4: C0116: Missing function or method docstring (missing-function-docstring)
src/fast_voice/client/tui.py:41:4: C0116: Missing function or method docstring (missing-function-docstring)
src/fast_voice/client/tui.py:51:4: C0116: Missing function or method docstring (missing-function-docstring)
src/fast_voice/client/tui.py:75:4: C0116: Missing function or method docstring (missing-function-docstring)
src/fast_voice/client/tui.py:88:4: C0116: Missing function or method docstring (missing-function-docstring)
src/fast_voice/client/tui.py:90:12: C0415: Import outside toplevel (pyperclip) (import-outside-toplevel)
src/fast_voice/client/tui.py:99:4: C0116: Missing function or method docstring (missing-function-docstring)
src/fast_voice/client/tui.py:116:8: C0415: Import outside toplevel (tty, termios) (import-outside-toplevel)
src/fast_voice/client/tui.py:116:8: C0410: Multiple imports on one line (tty, termios) (multiple-imports)
src/fast_voice/client/tui.py:123:15: W0718: Catching too general exception Exception (broad-exception-caught)
src/fast_voice/client/tui.py:140:20: C0415: Import outside toplevel (select) (import-outside-toplevel)
src/fast_voice/client/tui.py:126:87: W0612: Unused variable 'live' (unused-variable)
src/fast_voice/client/tui.py:173:0: C0116: Missing function or method docstring (missing-function-docstring)
src/fast_voice/client/tui.py:179:21: W0212: Access to a protected member _last_text of a client class (protected-access)
src/fast_voice/client/tui.py:4:0: W0611: Unused datetime imported from datetime (unused-import)
************* Module fast_voice.server.main
src/fast_voice/server/main.py:25:0: C0303: Trailing whitespace (trailing-whitespace)
src/fast_voice/server/main.py:31:0: C0303: Trailing whitespace (trailing-whitespace)
src/fast_voice/server/main.py:43:0: C0303: Trailing whitespace (trailing-whitespace)
src/fast_voice/server/main.py:35:11: W0718: Catching too general exception Exception (broad-exception-caught)
************* Module fast_voice.whisper_live.__version__
src/fast_voice/whisper_live/__version__.py:1:0: C0114: Missing module docstring (missing-module-docstring)
************* Module fast_voice.whisper_live.client
src/fast_voice/whisper_live/client.py:57:0: C0301: Line too long (115/100) (line-too-long)
src/fast_voice/whisper_live/client.py:58:0: C0301: Line too long (110/100) (line-too-long)
src/fast_voice/whisper_live/client.py:60:0: C0301: Line too long (116/100) (line-too-long)
src/fast_voice/whisper_live/client.py:61:0: C0301: Line too long (119/100) (line-too-long)
src/fast_voice/whisper_live/client.py:62:0: C0301: Line too long (141/100) (line-too-long)
src/fast_voice/whisper_live/client.py:63:0: C0301: Line too long (105/100) (line-too-long)
src/fast_voice/whisper_live/client.py:64:0: C0301: Line too long (135/100) (line-too-long)
src/fast_voice/whisper_live/client.py:65:0: C0301: Line too long (126/100) (line-too-long)
src/fast_voice/whisper_live/client.py:66:0: C0301: Line too long (124/100) (line-too-long)
src/fast_voice/whisper_live/client.py:68:0: C0301: Line too long (122/100) (line-too-long)
src/fast_voice/whisper_live/client.py:69:0: C0301: Line too long (144/100) (line-too-long)
src/fast_voice/whisper_live/client.py:136:0: C0301: Line too long (107/100) (line-too-long)
src/fast_voice/whisper_live/client.py:153:0: C0301: Line too long (131/100) (line-too-long)
src/fast_voice/whisper_live/client.py:156:0: C0301: Line too long (109/100) (line-too-long)
src/fast_voice/whisper_live/client.py:160:0: C0301: Line too long (104/100) (line-too-long)
src/fast_voice/whisper_live/client.py:212:0: C0301: Line too long (117/100) (line-too-long)
src/fast_voice/whisper_live/client.py:259:0: C0303: Trailing whitespace (trailing-whitespace)
src/fast_voice/whisper_live/client.py:373:0: C0301: Line too long (106/100) (line-too-long)
src/fast_voice/whisper_live/client.py:374:0: C0301: Line too long (103/100) (line-too-long)
src/fast_voice/whisper_live/client.py:379:0: C0301: Line too long (103/100) (line-too-long)
src/fast_voice/whisper_live/client.py:381:0: C0301: Line too long (165/100) (line-too-long)
src/fast_voice/whisper_live/client.py:412:0: C0301: Line too long (112/100) (line-too-long)
src/fast_voice/whisper_live/client.py:413:0: C0301: Line too long (114/100) (line-too-long)
src/fast_voice/whisper_live/client.py:417:0: C0301: Line too long (123/100) (line-too-long)
src/fast_voice/whisper_live/client.py:458:0: C0301: Line too long (121/100) (line-too-long)
src/fast_voice/whisper_live/client.py:506:0: C0303: Trailing whitespace (trailing-whitespace)
src/fast_voice/whisper_live/client.py:626:0: C0301: Line too long (102/100) (line-too-long)
src/fast_voice/whisper_live/client.py:646:0: C0301: Line too long (101/100) (line-too-long)
src/fast_voice/whisper_live/client.py:647:0: C0301: Line too long (104/100) (line-too-long)
src/fast_voice/whisper_live/client.py:650:0: C0301: Line too long (108/100) (line-too-long)
src/fast_voice/whisper_live/client.py:651:0: C0301: Line too long (124/100) (line-too-long)
src/fast_voice/whisper_live/client.py:652:0: C0301: Line too long (121/100) (line-too-long)
src/fast_voice/whisper_live/client.py:705:0: C0301: Line too long (111/100) (line-too-long)
src/fast_voice/whisper_live/client.py:706:0: C0301: Line too long (109/100) (line-too-long)
src/fast_voice/whisper_live/client.py:751:0: C0301: Line too long (108/100) (line-too-long)
src/fast_voice/whisper_live/client.py:761:0: C0301: Line too long (131/100) (line-too-long)
src/fast_voice/whisper_live/client.py:767:0: C0301: Line too long (120/100) (line-too-long)
src/fast_voice/whisper_live/client.py:768:0: C0301: Line too long (117/100) (line-too-long)
src/fast_voice/whisper_live/client.py:771:0: C0301: Line too long (107/100) (line-too-long)
src/fast_voice/whisper_live/client.py:772:0: C0301: Line too long (131/100) (line-too-long)
src/fast_voice/whisper_live/client.py:773:0: C0301: Line too long (132/100) (line-too-long)
src/fast_voice/whisper_live/client.py:774:0: C0301: Line too long (112/100) (line-too-long)
src/fast_voice/whisper_live/client.py:775:0: C0301: Line too long (115/100) (line-too-long)
src/fast_voice/whisper_live/client.py:776:0: C0301: Line too long (115/100) (line-too-long)
src/fast_voice/whisper_live/client.py:777:0: C0301: Line too long (137/100) (line-too-long)
src/fast_voice/whisper_live/client.py:778:0: C0301: Line too long (101/100) (line-too-long)
src/fast_voice/whisper_live/client.py:779:0: C0301: Line too long (131/100) (line-too-long)
src/fast_voice/whisper_live/client.py:780:0: C0301: Line too long (122/100) (line-too-long)
src/fast_voice/whisper_live/client.py:781:0: C0301: Line too long (120/100) (line-too-long)
src/fast_voice/whisper_live/client.py:783:0: C0301: Line too long (118/100) (line-too-long)
src/fast_voice/whisper_live/client.py:784:0: C0301: Line too long (140/100) (line-too-long)
src/fast_voice/whisper_live/client.py:787:0: C0301: Line too long (118/100) (line-too-long)
src/fast_voice/whisper_live/client.py:845:0: C0301: Line too long (112/100) (line-too-long)
src/fast_voice/whisper_live/client.py:847:0: C0301: Line too long (150/100) (line-too-long)
src/fast_voice/whisper_live/client.py:849:0: C0301: Line too long (150/100) (line-too-long)
src/fast_voice/whisper_live/client.py:1:0: C0114: Missing module docstring (missing-module-docstring)
src/fast_voice/whisper_live/client.py:13:0: R0402: Use 'from whisper_live import utils' instead (consider-using-from-import)
src/fast_voice/whisper_live/client.py:13:0: E0401: Unable to import 'whisper_live.utils' (import-error)
src/fast_voice/whisper_live/client.py:16:0: R0902: Too many instance attributes (33/7) (too-many-instance-attributes)
src/fast_voice/whisper_live/client.py:23:4: R0913: Too many arguments (20/5) (too-many-arguments)
src/fast_voice/whisper_live/client.py:23:4: R0917: Too many positional arguments (20/5) (too-many-positional-arguments)
src/fast_voice/whisper_live/client.py:23:4: R0914: Too many local variables (22/15) (too-many-locals)
src/fast_voice/whisper_live/client.py:109:24: W0108: Lambda may not be necessary (unnecessary-lambda)
src/fast_voice/whisper_live/client.py:110:27: W0108: Lambda may not be necessary (unnecessary-lambda)
src/fast_voice/whisper_live/client.py:111:25: W0108: Lambda may not be necessary (unnecessary-lambda)
src/fast_voice/whisper_live/client.py:112:25: W0108: Lambda may not be necessary (unnecessary-lambda)
src/fast_voice/whisper_live/client.py:169:23: W0718: Catching too general exception Exception (broad-exception-caught)
src/fast_voice/whisper_live/client.py:176:23: W0718: Catching too general exception Exception (broad-exception-caught)
src/fast_voice/whisper_live/client.py:143:4: R0912: Too many branches (21/12) (too-many-branches)
src/fast_voice/whisper_live/client.py:215:25: W0613: Unused argument 'ws' (unused-argument)
src/fast_voice/whisper_live/client.py:263:4: C0116: Missing function or method docstring (missing-function-docstring)
src/fast_voice/whisper_live/client.py:263:23: W0613: Unused argument 'ws' (unused-argument)
src/fast_voice/whisper_live/client.py:268:4: C0116: Missing function or method docstring (missing-function-docstring)
src/fast_voice/whisper_live/client.py:268:23: W0613: Unused argument 'ws' (unused-argument)
src/fast_voice/whisper_live/client.py:313:15: W0718: Catching too general exception Exception (broad-exception-caught)
src/fast_voice/whisper_live/client.py:326:15: W0718: Catching too general exception Exception (broad-exception-caught)
src/fast_voice/whisper_live/client.py:331:15: W0718: Catching too general exception Exception (broad-exception-caught)
src/fast_voice/whisper_live/client.py:368:0: R0902: Too many instance attributes (12/7) (too-many-instance-attributes)
src/fast_voice/whisper_live/client.py:381:4: R0913: Too many arguments (6/5) (too-many-arguments)
src/fast_voice/whisper_live/client.py:381:4: R0917: Too many positional arguments (6/5) (too-many-positional-arguments)
src/fast_voice/whisper_live/client.py:384:12: W0719: Raising too general exception: Exception (broad-exception-raised)
src/fast_voice/whisper_live/client.py:537:15: W0718: Catching too general exception Exception (broad-exception-caught)
src/fast_voice/whisper_live/client.py:559:15: W0718: Catching too general exception Exception (broad-exception-caught)
src/fast_voice/whisper_live/client.py:596:15: W0718: Catching too general exception Exception (broad-exception-caught)
src/fast_voice/whisper_live/client.py:796:4: R0913: Too many arguments (24/5) (too-many-arguments)
src/fast_voice/whisper_live/client.py:796:4: R0917: Too many positional arguments (24/5) (too-many-positional-arguments)
src/fast_voice/whisper_live/client.py:796:4: R0914: Too many local variables (24/15) (too-many-locals)
src/fast_voice/whisper_live/client.py:7:0: C0411: standard import "threading" should be placed before third party imports "numpy", "pyaudio" (wrong-import-order)
src/fast_voice/whisper_live/client.py:8:0: C0411: standard import "json" should be placed before third party imports "numpy", "pyaudio" (wrong-import-order)
src/fast_voice/whisper_live/client.py:10:0: C0411: standard import "uuid" should be placed before third party imports "numpy", "pyaudio", "websocket" (wrong-import-order)
src/fast_voice/whisper_live/client.py:11:0: C0411: standard import "time" should be placed before third party imports "numpy", "pyaudio", "websocket" (wrong-import-order)
************* Module fast_voice.whisper_live.server
src/fast_voice/whisper_live/server.py:30:0: C0301: Line too long (107/100) (line-too-long)
src/fast_voice/whisper_live/server.py:33:0: C0301: Line too long (118/100) (line-too-long)
src/fast_voice/whisper_live/server.py:34:0: C0301: Line too long (120/100) (line-too-long)
src/fast_voice/whisper_live/server.py:58:0: C0303: Trailing whitespace (trailing-whitespace)
src/fast_voice/whisper_live/server.py:89:0: C0301: Line too long (112/100) (line-too-long)
src/fast_voice/whisper_live/server.py:102:0: C0301: Line too long (118/100) (line-too-long)
src/fast_voice/whisper_live/server.py:105:0: C0301: Line too long (114/100) (line-too-long)
src/fast_voice/whisper_live/server.py:116:0: C0301: Line too long (115/100) (line-too-long)
src/fast_voice/whisper_live/server.py:134:0: C0301: Line too long (122/100) (line-too-long)
src/fast_voice/whisper_live/server.py:145:0: C0301: Line too long (116/100) (line-too-long)
src/fast_voice/whisper_live/server.py:168:0: C0303: Trailing whitespace (trailing-whitespace)
src/fast_voice/whisper_live/server.py:190:0: C0303: Trailing whitespace (trailing-whitespace)
src/fast_voice/whisper_live/server.py:195:0: C0303: Trailing whitespace (trailing-whitespace)
src/fast_voice/whisper_live/server.py:207:0: C0303: Trailing whitespace (trailing-whitespace)
src/fast_voice/whisper_live/server.py:214:0: C0303: Trailing whitespace (trailing-whitespace)
src/fast_voice/whisper_live/server.py:215:0: C0301: Line too long (116/100) (line-too-long)
src/fast_voice/whisper_live/server.py:245:0: C0303: Trailing whitespace (trailing-whitespace)
src/fast_voice/whisper_live/server.py:275:0: C0301: Line too long (107/100) (line-too-long)
src/fast_voice/whisper_live/server.py:347:0: C0301: Line too long (106/100) (line-too-long)
src/fast_voice/whisper_live/server.py:379:29: C0303: Trailing whitespace (trailing-whitespace)
src/fast_voice/whisper_live/server.py:410:0: C0303: Trailing whitespace (trailing-whitespace)
src/fast_voice/whisper_live/server.py:414:0: C0301: Line too long (103/100) (line-too-long)
src/fast_voice/whisper_live/server.py:418:0: W0311: Bad indentation. Found 13 spaces, expected 12 (bad-indentation)
src/fast_voice/whisper_live/server.py:423:0: C0303: Trailing whitespace (trailing-whitespace)
src/fast_voice/whisper_live/server.py:426:0: C0301: Line too long (113/100) (line-too-long)
src/fast_voice/whisper_live/server.py:485:0: C0301: Line too long (113/100) (line-too-long)
src/fast_voice/whisper_live/server.py:487:0: C0301: Line too long (143/100) (line-too-long)
src/fast_voice/whisper_live/server.py:498:0: C0301: Line too long (119/100) (line-too-long)
src/fast_voice/whisper_live/server.py:530:0: C0301: Line too long (111/100) (line-too-long)
src/fast_voice/whisper_live/server.py:536:0: C0301: Line too long (131/100) (line-too-long)
src/fast_voice/whisper_live/server.py:558:0: C0301: Line too long (103/100) (line-too-long)
src/fast_voice/whisper_live/server.py:590:0: C0301: Line too long (151/100) (line-too-long)
src/fast_voice/whisper_live/server.py:596:0: C0301: Line too long (124/100) (line-too-long)
src/fast_voice/whisper_live/server.py:597:0: C0301: Line too long (116/100) (line-too-long)
src/fast_voice/whisper_live/server.py:599:0: C0301: Line too long (130/100) (line-too-long)
src/fast_voice/whisper_live/server.py:631:0: C0301: Line too long (110/100) (line-too-long)
src/fast_voice/whisper_live/server.py:633:0: C0301: Line too long (116/100) (line-too-long)
src/fast_voice/whisper_live/server.py:634:0: C0301: Line too long (107/100) (line-too-long)
src/fast_voice/whisper_live/server.py:635:0: C0301: Line too long (109/100) (line-too-long)
src/fast_voice/whisper_live/server.py:639:0: C0301: Line too long (107/100) (line-too-long)
src/fast_voice/whisper_live/server.py:641:0: C0301: Line too long (109/100) (line-too-long)
src/fast_voice/whisper_live/server.py:645:0: C0301: Line too long (112/100) (line-too-long)
src/fast_voice/whisper_live/server.py:646:0: C0301: Line too long (110/100) (line-too-long)
src/fast_voice/whisper_live/server.py:670:0: C0303: Trailing whitespace (trailing-whitespace)
src/fast_voice/whisper_live/server.py:674:0: C0304: Final newline missing (missing-final-newline)
src/fast_voice/whisper_live/server.py:1:0: C0114: Missing module docstring (missing-module-docstring)
src/fast_voice/whisper_live/server.py:27:0: C0115: Missing class docstring (missing-class-docstring)
src/fast_voice/whisper_live/server.py:43:4: C0116: Missing function or method docstring (missing-function-docstring)
src/fast_voice/whisper_live/server.py:46:4: C0116: Missing function or method docstring (missing-function-docstring)
src/fast_voice/whisper_live/server.py:56:19: W0718: Catching too general exception Exception (broad-exception-caught)
src/fast_voice/whisper_live/server.py:145:12: W1203: Use lazy % formatting in logging functions (logging-fstring-interpolation)
src/fast_voice/whisper_live/server.py:150:0: C0115: Missing class docstring (missing-class-docstring)
src/fast_voice/whisper_live/server.py:156:4: C0116: Missing function or method docstring (missing-function-docstring)
src/fast_voice/whisper_live/server.py:160:4: C0116: Missing function or method docstring (missing-function-docstring)
src/fast_voice/whisper_live/server.py:163:4: C0116: Missing function or method docstring (missing-function-docstring)
src/fast_voice/whisper_live/server.py:166:4: C0116: Missing function or method docstring (missing-function-docstring)
src/fast_voice/whisper_live/server.py:169:4: C0116: Missing function or method docstring (missing-function-docstring)
src/fast_voice/whisper_live/server.py:173:0: C0115: Missing class docstring (missing-class-docstring)
src/fast_voice/whisper_live/server.py:173:0: R0902: Too many instance attributes (8/7) (too-many-instance-attributes)
src/fast_voice/whisper_live/server.py:182:4: C0116: Missing function or method docstring (missing-function-docstring)
src/fast_voice/whisper_live/server.py:182:4: R0913: Too many arguments (7/5) (too-many-arguments)
src/fast_voice/whisper_live/server.py:182:4: R0917: Too many positional arguments (7/5) (too-many-positional-arguments)
src/fast_voice/whisper_live/server.py:182:4: R0914: Too many local variables (18/15) (too-many-locals)
src/fast_voice/whisper_live/server.py:199:12: C0415: Import outside toplevel (fast_voice.whisper_live.backend.translation_backend.ServeClientTranslation) (import-outside-toplevel)
src/fast_voice/whisper_live/server.py:215:12: W1203: Use lazy % formatting in logging functions (logging-fstring-interpolation)
src/fast_voice/whisper_live/server.py:235:19: W0718: Catching too general exception Exception (broad-exception-caught)
src/fast_voice/whisper_live/server.py:219:16: C0415: Import outside toplevel (fast_voice.whisper_live.backend.trt_backend.ServeClientTensorRT) (import-outside-toplevel)
src/fast_voice/whisper_live/server.py:236:16: W1203: Use lazy % formatting in logging functions (logging-fstring-interpolation)
src/fast_voice/whisper_live/server.py:262:19: W0718: Catching too general exception Exception (broad-exception-caught)
src/fast_voice/whisper_live/server.py:248:16: C0415: Import outside toplevel (fast_voice.whisper_live.backend.openvino_backend.ServeClientOpenVINO) (import-outside-toplevel)
src/fast_voice/whisper_live/server.py:263:16: W1203: Use lazy % formatting in logging functions (logging-fstring-interpolation)
src/fast_voice/whisper_live/server.py:300:15: W0718: Catching too general exception Exception (broad-exception-caught)
src/fast_voice/whisper_live/server.py:275:16: C0415: Import outside toplevel (fast_voice.whisper_live.backend.faster_whisper_backend.ServeClientFasterWhisper) (import-outside-toplevel)
src/fast_voice/whisper_live/server.py:278:20: W1203: Use lazy % formatting in logging functions (logging-fstring-interpolation)
src/fast_voice/whisper_live/server.py:296:37: W0108: Lambda may not be necessary (unnecessary-lambda)
src/fast_voice/whisper_live/server.py:328:4: C0116: Missing function or method docstring (missing-function-docstring)
src/fast_voice/whisper_live/server.py:328:4: R0913: Too many arguments (7/5) (too-many-arguments)
src/fast_voice/whisper_live/server.py:328:4: R0917: Too many positional arguments (7/5) (too-many-positional-arguments)
src/fast_voice/whisper_live/server.py:355:15: W0718: Catching too general exception Exception (broad-exception-caught)
src/fast_voice/whisper_live/server.py:356:12: W1203: Use lazy % formatting in logging functions (logging-fstring-interpolation)
src/fast_voice/whisper_live/server.py:359:4: C0116: Missing function or method docstring (missing-function-docstring)
src/fast_voice/whisper_live/server.py:378:4: R0913: Too many arguments (7/5) (too-many-arguments)
src/fast_voice/whisper_live/server.py:378:4: R0917: Too many positional arguments (7/5) (too-many-positional-arguments)
src/fast_voice/whisper_live/server.py:417:15: W0718: Catching too general exception Exception (broad-exception-caught)
src/fast_voice/whisper_live/server.py:436:15: W0718: Catching too general exception Exception (broad-exception-caught)
src/fast_voice/whisper_live/server.py:437:12: W1203: Use lazy % formatting in logging functions (logging-fstring-interpolation)
src/fast_voice/whisper_live/server.py:444:4: C0116: Missing function or method docstring (missing-function-docstring)
src/fast_voice/whisper_live/server.py:455:23: W0718: Catching too general exception Exception (broad-exception-caught)
src/fast_voice/whisper_live/server.py:461:4: R0913: Too many arguments (15/5) (too-many-arguments)
src/fast_voice/whisper_live/server.py:461:4: R0917: Too many positional arguments (15/5) (too-many-positional-arguments)
src/fast_voice/whisper_live/server.py:461:4: R0914: Too many local variables (19/15) (too-many-locals)
src/fast_voice/whisper_live/server.py:514:12: R0913: Too many arguments (12/5) (too-many-arguments)
src/fast_voice/whisper_live/server.py:514:12: R0917: Too many positional arguments (12/5) (too-many-positional-arguments)
src/fast_voice/whisper_live/server.py:514:12: R0914: Too many local variables (31/15) (too-many-locals)
src/fast_voice/whisper_live/server.py:539:20: W1203: Use lazy % formatting in logging functions (logging-fstring-interpolation)
src/fast_voice/whisper_live/server.py:603:23: W0718: Catching too general exception Exception (broad-exception-caught)
src/fast_voice/whisper_live/server.py:564:20: R1705: Unnecessary "elif" after "return", remove the leading "el" from "elif" (no-else-return)
src/fast_voice/whisper_live/server.py:514:12: R0911: Too many return statements (7/6) (too-many-return-statements)
src/fast_voice/whisper_live/server.py:514:12: R0912: Too many branches (14/12) (too-many-branches)
src/fast_voice/whisper_live/server.py:524:16: W0613: Unused argument 'include' (unused-argument)
src/fast_voice/whisper_live/server.py:612:12: W1203: Use lazy % formatting in logging functions (logging-fstring-interpolation)
src/fast_voice/whisper_live/server.py:461:4: R0915: Too many statements (60/50) (too-many-statements)
src/fast_voice/whisper_live/server.py:237:16: W0201: Attribute 'client_uid' defined outside __init__ (attribute-defined-outside-init)
src/fast_voice/whisper_live/server.py:265:16: W0201: Attribute 'client_uid' defined outside __init__ (attribute-defined-outside-init)
src/fast_voice/whisper_live/server.py:244:16: W0201: Attribute 'backend' defined outside __init__ (attribute-defined-outside-init)
src/fast_voice/whisper_live/server.py:264:16: W0201: Attribute 'backend' defined outside __init__ (attribute-defined-outside-init)
src/fast_voice/whisper_live/server.py:409:8: W0201: Attribute 'backend' defined outside __init__ (attribute-defined-outside-init)
src/fast_voice/whisper_live/server.py:345:16: W0201: Attribute 'vad_detector' defined outside __init__ (attribute-defined-outside-init)
src/fast_voice/whisper_live/server.py:483:8: W0201: Attribute 'cache_path' defined outside __init__ (attribute-defined-outside-init)
src/fast_voice/whisper_live/server.py:18:0: C0411: standard import "enum.Enum" should be placed before third party imports "fastapi.FastAPI", "fastapi.middleware.cors.CORSMiddleware", "starlette.responses.PlainTextResponse", "uvicorn", "faster_whisper.WhisperModel", "torch" (wrong-import-order)
************* Module fast_voice.whisper_live.utils
src/fast_voice/whisper_live/utils.py:1:0: C0114: Missing module docstring (missing-module-docstring)
src/fast_voice/whisper_live/utils.py:33:0: C0116: Missing function or method docstring (missing-function-docstring)
src/fast_voice/whisper_live/utils.py:4:0: C0411: standard import "pathlib.Path" should be placed before third party import "av" (wrong-import-order)
************* Module fast_voice.whisper_live.vad
src/fast_voice/whisper_live/vad.py:21:0: C0301: Line too long (116/100) (line-too-long)
src/fast_voice/whisper_live/vad.py:23:0: C0301: Line too long (117/100) (line-too-long)
src/fast_voice/whisper_live/vad.py:44:0: C0301: Line too long (101/100) (line-too-long)
src/fast_voice/whisper_live/vad.py:62:0: C0301: Line too long (136/100) (line-too-long)
src/fast_voice/whisper_live/vad.py:79:0: C0301: Line too long (110/100) (line-too-long)
src/fast_voice/whisper_live/vad.py:137:0: C0301: Line too long (113/100) (line-too-long)
src/fast_voice/whisper_live/vad.py:145:0: C0301: Line too long (112/100) (line-too-long)
src/fast_voice/whisper_live/vad.py:149:0: C0301: Line too long (111/100) (line-too-long)
src/fast_voice/whisper_live/vad.py:153:0: C0301: Line too long (114/100) (line-too-long)
src/fast_voice/whisper_live/vad.py:156:0: C0301: Line too long (105/100) (line-too-long)
src/fast_voice/whisper_live/vad.py:1:0: C0114: Missing module docstring (missing-module-docstring)
src/fast_voice/whisper_live/vad.py:9:0: C0115: Missing class docstring (missing-class-docstring)
src/fast_voice/whisper_live/vad.py:50:4: C0116: Missing function or method docstring (missing-function-docstring)
src/fast_voice/whisper_live/vad.py:74:11: C1802: Do not use `len(SEQUENCE)` without comparison to determine if a sequence is empty (use-implicit-booleaness-not-len)
src/fast_voice/whisper_live/vad.py:93:4: C0116: Missing function or method docstring (missing-function-docstring)
src/fast_voice/whisper_live/vad.py:105:24: C2801: Unnecessarily calls dunder method __call__. Invoke instance directly. (unnecessary-dunder-call)
src/fast_voice/whisper_live/vad.py:112:4: C0116: Missing function or method docstring (missing-function-docstring)
src/fast_voice/whisper_live/vad.py:82:12: W0201: Attribute '_state' defined outside __init__ (attribute-defined-outside-init)
src/fast_voice/whisper_live/vad.py:75:12: W0201: Attribute '_context' defined outside __init__ (attribute-defined-outside-init)
src/fast_voice/whisper_live/vad.py:86:8: W0201: Attribute '_context' defined outside __init__ (attribute-defined-outside-init)
src/fast_voice/whisper_live/vad.py:87:8: W0201: Attribute '_last_sr' defined outside __init__ (attribute-defined-outside-init)
src/fast_voice/whisper_live/vad.py:88:8: W0201: Attribute '_last_batch_size' defined outside __init__ (attribute-defined-outside-init)
src/fast_voice/whisper_live/vad.py:131:0: C0115: Missing class docstring (missing-class-docstring)
src/fast_voice/whisper_live/vad.py:131:0: R0903: Too few public methods (1/2) (too-few-public-methods)
src/fast_voice/whisper_live/vad.py:6:0: C0411: standard import "warnings" should be placed before third party imports "torch", "numpy", "onnxruntime" (wrong-import-order)
************* Module fast_voice.whisper_live.backend.base
src/fast_voice/whisper_live/backend/base.py:69:0: C0301: Line too long (119/100) (line-too-long)
src/fast_voice/whisper_live/backend/base.py:70:0: C0301: Line too long (122/100) (line-too-long)
src/fast_voice/whisper_live/backend/base.py:71:0: C0301: Line too long (104/100) (line-too-long)
src/fast_voice/whisper_live/backend/base.py:98:0: C0301: Line too long (104/100) (line-too-long)
src/fast_voice/whisper_live/backend/base.py:111:0: C0303: Trailing whitespace (trailing-whitespace)
src/fast_voice/whisper_live/backend/base.py:114:0: C0301: Line too long (104/100) (line-too-long)
src/fast_voice/whisper_live/backend/base.py:137:0: C0301: Line too long (108/100) (line-too-long)
src/fast_voice/whisper_live/backend/base.py:138:0: C0301: Line too long (110/100) (line-too-long)
src/fast_voice/whisper_live/backend/base.py:141:0: C0301: Line too long (108/100) (line-too-long)
src/fast_voice/whisper_live/backend/base.py:142:0: C0301: Line too long (119/100) (line-too-long)
src/fast_voice/whisper_live/backend/base.py:143:0: C0301: Line too long (110/100) (line-too-long)
src/fast_voice/whisper_live/backend/base.py:171:0: C0301: Line too long (118/100) (line-too-long)
src/fast_voice/whisper_live/backend/base.py:201:0: C0301: Line too long (101/100) (line-too-long)
src/fast_voice/whisper_live/backend/base.py:251:0: C0303: Trailing whitespace (trailing-whitespace)
src/fast_voice/whisper_live/backend/base.py:265:0: C0301: Line too long (104/100) (line-too-long)
src/fast_voice/whisper_live/backend/base.py:278:0: C0301: Line too long (106/100) (line-too-long)
src/fast_voice/whisper_live/backend/base.py:279:0: C0301: Line too long (107/100) (line-too-long)
src/fast_voice/whisper_live/backend/base.py:285:0: C0303: Trailing whitespace (trailing-whitespace)
src/fast_voice/whisper_live/backend/base.py:313:0: C0301: Line too long (104/100) (line-too-long)
src/fast_voice/whisper_live/backend/base.py:349:100: C0303: Trailing whitespace (trailing-whitespace)
src/fast_voice/whisper_live/backend/base.py:350:0: C0301: Line too long (108/100) (line-too-long)
src/fast_voice/whisper_live/backend/base.py:1:0: C0114: Missing module docstring (missing-module-docstring)
src/fast_voice/whisper_live/backend/base.py:9:0: C0115: Missing class docstring (missing-class-docstring)
src/fast_voice/whisper_live/backend/base.py:9:0: R0205: Class 'ServeClientBase' inherits from object, can be safely removed from bases in python3 (useless-object-inheritance)
src/fast_voice/whisper_live/backend/base.py:9:0: R0902: Too many instance attributes (20/7) (too-many-instance-attributes)
src/fast_voice/whisper_live/backend/base.py:27:4: R0913: Too many arguments (9/5) (too-many-arguments)
src/fast_voice/whisper_live/backend/base.py:27:4: R0917: Too many positional arguments (9/5) (too-many-positional-arguments)
src/fast_voice/whisper_live/backend/base.py:102:19: W0718: Catching too general exception Exception (broad-exception-caught)
src/fast_voice/whisper_live/backend/base.py:94:25: E1121: Too many positional arguments for method call (too-many-function-args)
src/fast_voice/whisper_live/backend/base.py:96:37: E1101: Instance of 'ServeClientBase' has no 'language' member (no-member)
src/fast_voice/whisper_live/backend/base.py:103:16: W1203: Use lazy % formatting in logging functions (logging-fstring-interpolation)
src/fast_voice/whisper_live/backend/base.py:106:4: C0116: Missing function or method docstring (missing-function-docstring)
src/fast_voice/whisper_live/backend/base.py:109:4: C0116: Missing function or method docstring (missing-function-docstring)
src/fast_voice/whisper_live/backend/base.py:127:21: C0209: Formatting a regular string which could be an f-string (consider-using-f-string)
src/fast_voice/whisper_live/backend/base.py:128:19: C0209: Formatting a regular string which could be an f-string (consider-using-f-string)
src/fast_voice/whisper_live/backend/base.py:149:8: R1732: Consider using 'with' for resource-allocating operations (consider-using-with)
src/fast_voice/whisper_live/backend/base.py:156:12: R1731: Consider using 'self.timestamp_offset = max(self.timestamp_offset, self.frames_offset)' instead of unnecessary if block (consider-using-max-builtin)
src/fast_voice/whisper_live/backend/base.py:249:15: W0718: Catching too general exception Exception (broad-exception-caught)
src/fast_voice/whisper_live/backend/base.py:250:12: W1203: Use lazy % formatting in logging functions (logging-fstring-interpolation)
src/fast_voice/whisper_live/backend/base.py:258:19: W0718: Catching too general exception Exception (broad-exception-caught)
src/fast_voice/whisper_live/backend/base.py:259:16: W1203: Use lazy % formatting in logging functions (logging-fstring-interpolation)
src/fast_voice/whisper_live/backend/base.py:286:4: C0116: Missing function or method docstring (missing-function-docstring)
src/fast_voice/whisper_live/backend/base.py:289:4: C0116: Missing function or method docstring (missing-function-docstring)
src/fast_voice/whisper_live/backend/base.py:292:4: C0116: Missing function or method docstring (missing-function-docstring)
src/fast_voice/whisper_live/backend/base.py:295:4: R0912: Too many branches (16/12) (too-many-branches)
src/fast_voice/whisper_live/backend/base.py:295:4: R0915: Too many statements (55/50) (too-many-statements)
************* Module fast_voice.whisper_live.backend.faster_whisper_backend
src/fast_voice/whisper_live/backend/faster_whisper_backend.py:36:0: C0303: Trailing whitespace (trailing-whitespace)
src/fast_voice/whisper_live/backend/faster_whisper_backend.py:95:0: C0301: Line too long (124/100) (line-too-long)
src/fast_voice/whisper_live/backend/faster_whisper_backend.py:96:0: C0301: Line too long (119/100) (line-too-long)
src/fast_voice/whisper_live/backend/faster_whisper_backend.py:97:0: C0301: Line too long (141/100) (line-too-long)
src/fast_voice/whisper_live/backend/faster_whisper_backend.py:98:0: C0301: Line too long (105/100) (line-too-long)
src/fast_voice/whisper_live/backend/faster_whisper_backend.py:99:0: C0301: Line too long (135/100) (line-too-long)
src/fast_voice/whisper_live/backend/faster_whisper_backend.py:136:0: C0303: Trailing whitespace (trailing-whitespace)
src/fast_voice/whisper_live/backend/faster_whisper_backend.py:192:0: C0301: Line too long (105/100) (line-too-long)
src/fast_voice/whisper_live/backend/faster_whisper_backend.py:200:43: C0303: Trailing whitespace (trailing-whitespace)
src/fast_voice/whisper_live/backend/faster_whisper_backend.py:223:0: C0301: Line too long (102/100) (line-too-long)
src/fast_voice/whisper_live/backend/faster_whisper_backend.py:224:0: C0301: Line too long (103/100) (line-too-long)
src/fast_voice/whisper_live/backend/faster_whisper_backend.py:225:0: C0301: Line too long (103/100) (line-too-long)
src/fast_voice/whisper_live/backend/faster_whisper_backend.py:230:0: C0301: Line too long (107/100) (line-too-long)
src/fast_voice/whisper_live/backend/faster_whisper_backend.py:232:0: C0301: Line too long (113/100) (line-too-long)
src/fast_voice/whisper_live/backend/faster_whisper_backend.py:238:0: C0301: Line too long (102/100) (line-too-long)
src/fast_voice/whisper_live/backend/faster_whisper_backend.py:1:0: C0114: Missing module docstring (missing-module-docstring)
src/fast_voice/whisper_live/backend/faster_whisper_backend.py:13:0: C0115: Missing class docstring (missing-class-docstring)
src/fast_voice/whisper_live/backend/faster_whisper_backend.py:13:0: R0902: Too many instance attributes (12/7) (too-many-instance-attributes)
src/fast_voice/whisper_live/backend/faster_whisper_backend.py:49:12: W1203: Use lazy % formatting in logging functions (logging-fstring-interpolation)
src/fast_voice/whisper_live/backend/faster_whisper_backend.py:58:16: W1203: Use lazy % formatting in logging functions (logging-fstring-interpolation)
src/fast_voice/whisper_live/backend/faster_whisper_backend.py:61:4: R0913: Too many arguments (18/5) (too-many-arguments)
src/fast_voice/whisper_live/backend/faster_whisper_backend.py:61:4: R0917: Too many positional arguments (18/5) (too-many-positional-arguments)
src/fast_voice/whisper_live/backend/faster_whisper_backend.py:61:4: R0914: Too many local variables (20/15) (too-many-locals)
src/fast_voice/whisper_live/backend/faster_whisper_backend.py:135:8: W1203: Use lazy % formatting in logging functions (logging-fstring-interpolation)
src/fast_voice/whisper_live/backend/faster_whisper_backend.py:146:15: W0718: Catching too general exception Exception (broad-exception-caught)
src/fast_voice/whisper_live/backend/faster_whisper_backend.py:147:12: W1203: Use lazy % formatting in logging functions (logging-fstring-interpolation)
src/fast_voice/whisper_live/backend/faster_whisper_backend.py:198:24: W1203: Use lazy % formatting in logging functions (logging-fstring-interpolation)
src/fast_voice/whisper_live/backend/faster_whisper_backend.py:210:8: W1203: Use lazy % formatting in logging functions (logging-fstring-interpolation)
src/fast_voice/whisper_live/backend/faster_whisper_backend.py:230:12: W1203: Use lazy % formatting in logging functions (logging-fstring-interpolation)
src/fast_voice/whisper_live/backend/faster_whisper_backend.py:234:4: W0221: Number of parameters was 1 in 'ServeClientBase.transcribe_audio' and is now 2 in overriding 'ServeClientFasterWhisper.transcribe_audio' method (arguments-differ)
src/fast_voice/whisper_live/backend/faster_whisper_backend.py:251:12: R1732: Consider using 'with' for resource-allocating operations (consider-using-with)
src/fast_voice/whisper_live/backend/faster_whisper_backend.py:280:11: C1802: Do not use `len(SEQUENCE)` without comparison to determine if a sequence is empty (use-implicit-booleaness-not-len)
src/fast_voice/whisper_live/backend/faster_whisper_backend.py:276:12: W0201: Attribute 't_start' defined outside __init__ (attribute-defined-outside-init)
************* Module fast_voice.whisper_live.backend.openvino_backend
src/fast_voice/whisper_live/backend/openvino_backend.py:45:0: C0301: Line too long (124/100) (line-too-long)
src/fast_voice/whisper_live/backend/openvino_backend.py:46:0: C0301: Line too long (119/100) (line-too-long)
src/fast_voice/whisper_live/backend/openvino_backend.py:47:0: C0301: Line too long (141/100) (line-too-long)
src/fast_voice/whisper_live/backend/openvino_backend.py:48:0: C0301: Line too long (105/100) (line-too-long)
src/fast_voice/whisper_live/backend/openvino_backend.py:49:0: C0301: Line too long (135/100) (line-too-long)
src/fast_voice/whisper_live/backend/openvino_backend.py:96:0: C0301: Line too long (102/100) (line-too-long)
src/fast_voice/whisper_live/backend/openvino_backend.py:113:0: C0301: Line too long (102/100) (line-too-long)
src/fast_voice/whisper_live/backend/openvino_backend.py:1:0: C0114: Missing module docstring (missing-module-docstring)
src/fast_voice/whisper_live/backend/openvino_backend.py:5:0: E0401: Unable to import 'openvino' (import-error)
src/fast_voice/whisper_live/backend/openvino_backend.py:10:0: C0115: Missing class docstring (missing-class-docstring)
src/fast_voice/whisper_live/backend/openvino_backend.py:14:4: R0913: Too many arguments (15/5) (too-many-arguments)
src/fast_voice/whisper_live/backend/openvino_backend.py:14:4: R0917: Too many positional arguments (15/5) (too-many-positional-arguments)
src/fast_voice/whisper_live/backend/openvino_backend.py:14:4: R0914: Too many local variables (19/15) (too-many-locals)
src/fast_voice/whisper_live/backend/openvino_backend.py:95:8: W1203: Use lazy % formatting in logging functions (logging-fstring-interpolation)
src/fast_voice/whisper_live/backend/openvino_backend.py:96:8: W1203: Use lazy % formatting in logging functions (logging-fstring-interpolation)
src/fast_voice/whisper_live/backend/openvino_backend.py:18:8: W0613: Unused argument 'device' (unused-argument)
src/fast_voice/whisper_live/backend/openvino_backend.py:22:8: W0613: Unused argument 'initial_prompt' (unused-argument)
src/fast_voice/whisper_live/backend/openvino_backend.py:23:8: W0613: Unused argument 'vad_parameters' (unused-argument)
src/fast_voice/whisper_live/backend/openvino_backend.py:24:8: W0613: Unused argument 'use_vad' (unused-argument)
src/fast_voice/whisper_live/backend/openvino_backend.py:109:4: W0221: Number of parameters was 1 in 'ServeClientBase.transcribe_audio' and is now 2 in overriding 'ServeClientOpenVINO.transcribe_audio' method (arguments-differ)
src/fast_voice/whisper_live/backend/openvino_backend.py:126:12: R1732: Consider using 'with' for resource-allocating operations (consider-using-with)
src/fast_voice/whisper_live/backend/openvino_backend.py:146:11: C1802: Do not use `len(SEQUENCE)` without comparison to determine if a sequence is empty (use-implicit-booleaness-not-len)
src/fast_voice/whisper_live/backend/openvino_backend.py:142:12: W0201: Attribute 't_start' defined outside __init__ (attribute-defined-outside-init)
************* Module fast_voice.whisper_live.backend.tokenization_small100
src/fast_voice/whisper_live/backend/tokenization_small100.py:3:141: C0303: Trailing whitespace (trailing-whitespace)
src/fast_voice/whisper_live/backend/tokenization_small100.py:3:0: C0301: Line too long (141/100) (line-too-long)
src/fast_voice/whisper_live/backend/tokenization_small100.py:46:0: C0301: Line too long (113/100) (line-too-long)
src/fast_voice/whisper_live/backend/tokenization_small100.py:49:0: C0301: Line too long (111/100) (line-too-long)
src/fast_voice/whisper_live/backend/tokenization_small100.py:59:0: C0301: Line too long (617/100) (line-too-long)
src/fast_voice/whisper_live/backend/tokenization_small100.py:66:0: C0301: Line too long (103/100) (line-too-long)
src/fast_voice/whisper_live/backend/tokenization_small100.py:67:0: C0301: Line too long (119/100) (line-too-long)
src/fast_voice/whisper_live/backend/tokenization_small100.py:73:0: C0301: Line too long (119/100) (line-too-long)
src/fast_voice/whisper_live/backend/tokenization_small100.py:80:0: C0301: Line too long (119/100) (line-too-long)
src/fast_voice/whisper_live/backend/tokenization_small100.py:81:0: C0301: Line too long (116/100) (line-too-long)
src/fast_voice/whisper_live/backend/tokenization_small100.py:84:0: C0301: Line too long (119/100) (line-too-long)
src/fast_voice/whisper_live/backend/tokenization_small100.py:91:0: C0301: Line too long (101/100) (line-too-long)
src/fast_voice/whisper_live/backend/tokenization_small100.py:92:0: C0301: Line too long (119/100) (line-too-long)
src/fast_voice/whisper_live/backend/tokenization_small100.py:98:0: C0301: Line too long (116/100) (line-too-long)
src/fast_voice/whisper_live/backend/tokenization_small100.py:100:0: C0301: Line too long (112/100) (line-too-long)
src/fast_voice/whisper_live/backend/tokenization_small100.py:139:0: C0301: Line too long (104/100) (line-too-long)
src/fast_voice/whisper_live/backend/tokenization_small100.py:157:0: C0301: Line too long (118/100) (line-too-long)
src/fast_voice/whisper_live/backend/tokenization_small100.py:159:0: C0301: Line too long (118/100) (line-too-long)
src/fast_voice/whisper_live/backend/tokenization_small100.py:165:0: C0303: Trailing whitespace (trailing-whitespace)
src/fast_voice/whisper_live/backend/tokenization_small100.py:178:0: C0303: Trailing whitespace (trailing-whitespace)
src/fast_voice/whisper_live/backend/tokenization_small100.py:214:0: C0301: Line too long (119/100) (line-too-long)
src/fast_voice/whisper_live/backend/tokenization_small100.py:217:0: C0301: Line too long (115/100) (line-too-long)
src/fast_voice/whisper_live/backend/tokenization_small100.py:225:0: C0301: Line too long (101/100) (line-too-long)
src/fast_voice/whisper_live/backend/tokenization_small100.py:227:0: C0301: Line too long (111/100) (line-too-long)
src/fast_voice/whisper_live/backend/tokenization_small100.py:245:0: C0301: Line too long (119/100) (line-too-long)
src/fast_voice/whisper_live/backend/tokenization_small100.py:246:0: C0301: Line too long (109/100) (line-too-long)
src/fast_voice/whisper_live/backend/tokenization_small100.py:249:0: C0301: Line too long (111/100) (line-too-long)
src/fast_voice/whisper_live/backend/tokenization_small100.py:257:0: C0301: Line too long (104/100) (line-too-long)
src/fast_voice/whisper_live/backend/tokenization_small100.py:289:0: C0301: Line too long (104/100) (line-too-long)
src/fast_voice/whisper_live/backend/tokenization_small100.py:294:0: C0301: Line too long (101/100) (line-too-long)
src/fast_voice/whisper_live/backend/tokenization_small100.py:302:0: C0301: Line too long (110/100) (line-too-long)
src/fast_voice/whisper_live/backend/tokenization_small100.py:335:48: C0303: Trailing whitespace (trailing-whitespace)
src/fast_voice/whisper_live/backend/tokenization_small100.py:338:0: C0301: Line too long (106/100) (line-too-long)
src/fast_voice/whisper_live/backend/tokenization_small100.py:365:0: C0304: Final newline missing (missing-final-newline)
src/fast_voice/whisper_live/backend/tokenization_small100.py:25:0: E0401: Unable to import 'sentencepiece' (import-error)
src/fast_voice/whisper_live/backend/tokenization_small100.py:27:0: E0401: Unable to import 'transformers.tokenization_utils' (import-error)
src/fast_voice/whisper_live/backend/tokenization_small100.py:28:0: E0401: Unable to import 'transformers.utils' (import-error)
src/fast_voice/whisper_live/backend/tokenization_small100.py:64:0: R0902: Too many instance attributes (19/7) (too-many-instance-attributes)
src/fast_voice/whisper_live/backend/tokenization_small100.py:120:4: R0913: Too many arguments (12/5) (too-many-arguments)
src/fast_voice/whisper_live/backend/tokenization_small100.py:120:4: R0917: Too many positional arguments (12/5) (too-many-positional-arguments)
src/fast_voice/whisper_live/backend/tokenization_small100.py:183:4: C0116: Missing function or method docstring (missing-function-docstring)
src/fast_voice/whisper_live/backend/tokenization_small100.py:187:4: C0116: Missing function or method docstring (missing-function-docstring)
src/fast_voice/whisper_live/backend/tokenization_small100.py:260:12: R1705: Unnecessary "else" after "return", remove the "else" and de-indent the code inside it (no-else-return)
src/fast_voice/whisper_live/backend/tokenization_small100.py:265:8: R1705: Unnecessary "else" after "return", remove the "else" and de-indent the code inside it (no-else-return)
src/fast_voice/whisper_live/backend/tokenization_small100.py:270:4: C0116: Missing function or method docstring (missing-function-docstring)
src/fast_voice/whisper_live/backend/tokenization_small100.py:289:4: C0116: Missing function or method docstring (missing-function-docstring)
src/fast_voice/whisper_live/backend/tokenization_small100.py:311:4: C0116: Missing function or method docstring (missing-function-docstring)
src/fast_voice/whisper_live/backend/tokenization_small100.py:344:4: C0116: Missing function or method docstring (missing-function-docstring)
src/fast_voice/whisper_live/backend/tokenization_small100.py:347:4: C0116: Missing function or method docstring (missing-function-docstring)
src/fast_voice/whisper_live/backend/tokenization_small100.py:352:0: C0116: Missing function or method docstring (missing-function-docstring)
src/fast_voice/whisper_live/backend/tokenization_small100.py:358:0: C0116: Missing function or method docstring (missing-function-docstring)
src/fast_voice/whisper_live/backend/tokenization_small100.py:359:9: W1514: Using open without explicitly specifying an encoding (unspecified-encoding)
src/fast_voice/whisper_live/backend/tokenization_small100.py:363:0: C0116: Missing function or method docstring (missing-function-docstring)
src/fast_voice/whisper_live/backend/tokenization_small100.py:364:9: W1514: Using open without explicitly specifying an encoding (unspecified-encoding)
************* Module fast_voice.whisper_live.backend.translation_backend
src/fast_voice/whisper_live/backend/translation_backend.py:17:0: C0303: Trailing whitespace (trailing-whitespace)
src/fast_voice/whisper_live/backend/translation_backend.py:23:29: C0303: Trailing whitespace (trailing-whitespace)
src/fast_voice/whisper_live/backend/translation_backend.py:48:0: C0303: Trailing whitespace (trailing-whitespace)
src/fast_voice/whisper_live/backend/translation_backend.py:54:0: C0303: Trailing whitespace (trailing-whitespace)
src/fast_voice/whisper_live/backend/translation_backend.py:60:0: C0303: Trailing whitespace (trailing-whitespace)
src/fast_voice/whisper_live/backend/translation_backend.py:62:0: C0301: Line too long (107/100) (line-too-long)
src/fast_voice/whisper_live/backend/translation_backend.py:68:0: C0303: Trailing whitespace (trailing-whitespace)
src/fast_voice/whisper_live/backend/translation_backend.py:81:0: C0303: Trailing whitespace (trailing-whitespace)
src/fast_voice/whisper_live/backend/translation_backend.py:85:0: C0303: Trailing whitespace (trailing-whitespace)
src/fast_voice/whisper_live/backend/translation_backend.py:89:0: C0303: Trailing whitespace (trailing-whitespace)
src/fast_voice/whisper_live/backend/translation_backend.py:93:0: C0303: Trailing whitespace (trailing-whitespace)
src/fast_voice/whisper_live/backend/translation_backend.py:97:0: C0303: Trailing whitespace (trailing-whitespace)
src/fast_voice/whisper_live/backend/translation_backend.py:104:0: C0303: Trailing whitespace (trailing-whitespace)
src/fast_voice/whisper_live/backend/translation_backend.py:109:0: C0303: Trailing whitespace (trailing-whitespace)
src/fast_voice/whisper_live/backend/translation_backend.py:114:0: C0303: Trailing whitespace (trailing-whitespace)
src/fast_voice/whisper_live/backend/translation_backend.py:119:0: C0303: Trailing whitespace (trailing-whitespace)
src/fast_voice/whisper_live/backend/translation_backend.py:123:0: C0303: Trailing whitespace (trailing-whitespace)
src/fast_voice/whisper_live/backend/translation_backend.py:132:0: C0303: Trailing whitespace (trailing-whitespace)
src/fast_voice/whisper_live/backend/translation_backend.py:136:0: C0303: Trailing whitespace (trailing-whitespace)
src/fast_voice/whisper_live/backend/translation_backend.py:138:0: C0303: Trailing whitespace (trailing-whitespace)
src/fast_voice/whisper_live/backend/translation_backend.py:144:0: C0303: Trailing whitespace (trailing-whitespace)
src/fast_voice/whisper_live/backend/translation_backend.py:146:0: C0303: Trailing whitespace (trailing-whitespace)
src/fast_voice/whisper_live/backend/translation_backend.py:157:0: C0303: Trailing whitespace (trailing-whitespace)
src/fast_voice/whisper_live/backend/translation_backend.py:174:0: C0303: Trailing whitespace (trailing-whitespace)
src/fast_voice/whisper_live/backend/translation_backend.py:181:0: C0303: Trailing whitespace (trailing-whitespace)
src/fast_voice/whisper_live/backend/translation_backend.py:193:0: C0303: Trailing whitespace (trailing-whitespace)
src/fast_voice/whisper_live/backend/translation_backend.py:198:0: C0303: Trailing whitespace (trailing-whitespace)
src/fast_voice/whisper_live/backend/translation_backend.py:203:0: C0303: Trailing whitespace (trailing-whitespace)
src/fast_voice/whisper_live/backend/translation_backend.py:205:0: C0303: Trailing whitespace (trailing-whitespace)
src/fast_voice/whisper_live/backend/translation_backend.py:212:0: C0303: Trailing whitespace (trailing-whitespace)
src/fast_voice/whisper_live/backend/translation_backend.py:1:0: C0114: Missing module docstring (missing-module-docstring)
src/fast_voice/whisper_live/backend/translation_backend.py:5:0: E0401: Unable to import 'transformers' (import-error)
src/fast_voice/whisper_live/backend/translation_backend.py:11:0: W0223: Method 'handle_transcription_output' is abstract in class 'ServeClientBase' but is not overridden in child class 'ServeClientTranslation' (abstract-method)
src/fast_voice/whisper_live/backend/translation_backend.py:11:0: W0223: Method 'transcribe_audio' is abstract in class 'ServeClientBase' but is not overridden in child class 'ServeClientTranslation' (abstract-method)
src/fast_voice/whisper_live/backend/translation_backend.py:11:0: R0902: Too many instance attributes (9/7) (too-many-instance-attributes)
src/fast_voice/whisper_live/backend/translation_backend.py:18:4: R0913: Too many arguments (7/5) (too-many-arguments)
src/fast_voice/whisper_live/backend/translation_backend.py:18:4: R0917: Too many positional arguments (7/5) (too-many-positional-arguments)
src/fast_voice/whisper_live/backend/translation_backend.py:63:15: W0718: Catching too general exception Exception (broad-exception-caught)
src/fast_voice/whisper_live/backend/translation_backend.py:53:12: W1203: Use lazy % formatting in logging functions (logging-fstring-interpolation)
src/fast_voice/whisper_live/backend/translation_backend.py:62:12: W1203: Use lazy % formatting in logging functions (logging-fstring-interpolation)
src/fast_voice/whisper_live/backend/translation_backend.py:64:12: W1203: Use lazy % formatting in logging functions (logging-fstring-interpolation)
src/fast_voice/whisper_live/backend/translation_backend.py:94:15: W0718: Catching too general exception Exception (broad-exception-caught)
src/fast_voice/whisper_live/backend/translation_backend.py:95:12: W1203: Use lazy % formatting in logging functions (logging-fstring-interpolation)
src/fast_voice/whisper_live/backend/translation_backend.py:103:8: W1203: Use lazy % formatting in logging functions (logging-fstring-interpolation)
src/fast_voice/whisper_live/backend/translation_backend.py:141:19: W0718: Catching too general exception Exception (broad-exception-caught)
src/fast_voice/whisper_live/backend/translation_backend.py:112:20: W1203: Use lazy % formatting in logging functions (logging-fstring-interpolation)
src/fast_voice/whisper_live/backend/translation_backend.py:142:16: W1203: Use lazy % formatting in logging functions (logging-fstring-interpolation)
src/fast_voice/whisper_live/backend/translation_backend.py:145:8: W1203: Use lazy % formatting in logging functions (logging-fstring-interpolation)
src/fast_voice/whisper_live/backend/translation_backend.py:172:15: W0718: Catching too general exception Exception (broad-exception-caught)
src/fast_voice/whisper_live/backend/translation_backend.py:173:12: W1203: Use lazy % formatting in logging functions (logging-fstring-interpolation)
src/fast_voice/whisper_live/backend/translation_backend.py:192:12: W1203: Use lazy % formatting in logging functions (logging-fstring-interpolation)
src/fast_voice/whisper_live/backend/translation_backend.py:196:8: W1203: Use lazy % formatting in logging functions (logging-fstring-interpolation)
src/fast_voice/whisper_live/backend/translation_backend.py:201:15: W0718: Catching too general exception Exception (broad-exception-caught)
************* Module fast_voice.whisper_live.backend.trt_backend
src/fast_voice/whisper_live/backend/trt_backend.py:40:0: C0301: Line too long (117/100) (line-too-long)
src/fast_voice/whisper_live/backend/trt_backend.py:43:0: C0301: Line too long (124/100) (line-too-long)
src/fast_voice/whisper_live/backend/trt_backend.py:44:0: C0301: Line too long (104/100) (line-too-long)
src/fast_voice/whisper_live/backend/trt_backend.py:46:0: C0301: Line too long (119/100) (line-too-long)
src/fast_voice/whisper_live/backend/trt_backend.py:47:0: C0301: Line too long (141/100) (line-too-long)
src/fast_voice/whisper_live/backend/trt_backend.py:48:0: C0301: Line too long (105/100) (line-too-long)
src/fast_voice/whisper_live/backend/trt_backend.py:49:0: C0301: Line too long (135/100) (line-too-long)
src/fast_voice/whisper_live/backend/trt_backend.py:129:0: C0301: Line too long (117/100) (line-too-long)
src/fast_voice/whisper_live/backend/trt_backend.py:147:0: C0301: Line too long (110/100) (line-too-long)
src/fast_voice/whisper_live/backend/trt_backend.py:170:0: C0303: Trailing whitespace (trailing-whitespace)
src/fast_voice/whisper_live/backend/trt_backend.py:181:0: C0301: Line too long (119/100) (line-too-long)
src/fast_voice/whisper_live/backend/trt_backend.py:182:0: C0301: Line too long (122/100) (line-too-long)
src/fast_voice/whisper_live/backend/trt_backend.py:183:0: C0301: Line too long (104/100) (line-too-long)
src/fast_voice/whisper_live/backend/trt_backend.py:1:0: C0114: Missing module docstring (missing-module-docstring)
src/fast_voice/whisper_live/backend/trt_backend.py:10:0: C0115: Missing class docstring (missing-class-docstring)
src/fast_voice/whisper_live/backend/trt_backend.py:14:4: R0913: Too many arguments (14/5) (too-many-arguments)
src/fast_voice/whisper_live/backend/trt_backend.py:14:4: R0917: Too many positional arguments (14/5) (too-many-positional-arguments)
src/fast_voice/whisper_live/backend/trt_backend.py:110:12: W0612: Unused variable 'i' (unused-variable)
src/fast_voice/whisper_live/backend/trt_backend.py:120:8: R1732: Consider using 'with' for resource-allocating operations (consider-using-with)
src/fast_voice/whisper_live/backend/trt_backend.py:124:4: W0237: Parameter 'result' has been renamed to 'last_segment' in overriding 'ServeClientTensorRT.handle_transcription_output' method (arguments-renamed)
src/fast_voice/whisper_live/backend/trt_backend.py:138:4: W0221: Number of parameters was 1 in 'ServeClientBase.transcribe_audio' and is now 2 in overriding 'ServeClientTensorRT.transcribe_audio' method (arguments-differ)
src/fast_voice/whisper_live/backend/trt_backend.py:146:12: R1732: Consider using 'with' for resource-allocating operations (consider-using-with)
src/fast_voice/whisper_live/backend/trt_backend.py:147:8: W1203: Use lazy % formatting in logging functions (logging-fstring-interpolation)
src/fast_voice/whisper_live/backend/trt_backend.py:166:11: C1802: Do not use `len(SEQUENCE)` without comparison to determine if a sequence is empty (use-implicit-booleaness-not-len)
src/fast_voice/whisper_live/backend/trt_backend.py:209:19: W0718: Catching too general exception Exception (broad-exception-caught)
src/fast_voice/whisper_live/backend/trt_backend.py:206:16: W1203: Use lazy % formatting in logging functions (logging-fstring-interpolation)
src/fast_voice/whisper_live/backend/trt_backend.py:210:16: W1203: Use lazy % formatting in logging functions (logging-fstring-interpolation)
************* Module fast_voice.whisper_live.transcriber.tensorrt_utils
src/fast_voice/whisper_live/transcriber/tensorrt_utils.py:1:0: C0301: Line too long (103/100) (line-too-long)
src/fast_voice/whisper_live/transcriber/tensorrt_utils.py:1:0: C0114: Missing module docstring (missing-module-docstring)
src/fast_voice/whisper_live/transcriber/tensorrt_utils.py:22:0: E0401: Unable to import 'kaldialign' (import-error)
src/fast_voice/whisper_live/transcriber/tensorrt_utils.py:69:0: C0116: Missing function or method docstring (missing-function-docstring)
src/fast_voice/whisper_live/transcriber/tensorrt_utils.py:128:0: R0913: Too many arguments (6/5) (too-many-arguments)
src/fast_voice/whisper_live/transcriber/tensorrt_utils.py:128:0: R0917: Too many positional arguments (6/5) (too-many-positional-arguments)
src/fast_voice/whisper_live/transcriber/tensorrt_utils.py:189:4: R1705: Unnecessary "else" after "return", remove the "else" and de-indent the code inside it (no-else-return)
src/fast_voice/whisper_live/transcriber/tensorrt_utils.py:190:25: E0606: Possibly using variable 'duration' before assignment (possibly-used-before-assignment)
src/fast_voice/whisper_live/transcriber/tensorrt_utils.py:208:9: W1514: Using open without explicitly specifying an encoding (unspecified-encoding)
src/fast_voice/whisper_live/transcriber/tensorrt_utils.py:214:0: R0914: Too many local variables (32/15) (too-many-locals)
src/fast_voice/whisper_live/transcriber/tensorrt_utils.py:262:4: C0103: Variable name "ERR" doesn't conform to snake_case naming style (invalid-name)
src/fast_voice/whisper_live/transcriber/tensorrt_utils.py:279:14: R1728: Consider using a generator instead 'sum(len(r) for (_, r, _) in results)' (consider-using-generator)
src/fast_voice/whisper_live/transcriber/tensorrt_utils.py:284:19: C0209: Formatting a regular string which could be an f-string (consider-using-f-string)
src/fast_voice/whisper_live/transcriber/tensorrt_utils.py:287:8: W1203: Use lazy % formatting in logging functions (logging-fstring-interpolation)
src/fast_voice/whisper_live/transcriber/tensorrt_utils.py:214:0: R0912: Too many branches (15/12) (too-many-branches)
src/fast_voice/whisper_live/transcriber/tensorrt_utils.py:214:0: R0915: Too many statements (62/50) (too-many-statements)
src/fast_voice/whisper_live/transcriber/tensorrt_utils.py:25:0: C0411: standard import "wave" should be placed before third party imports "kaldialign", "numpy", "soundfile" (wrong-import-order)
************* Module fast_voice.whisper_live.transcriber.transcriber_faster_whisper
src/fast_voice/whisper_live/transcriber/transcriber_faster_whisper.py:1887:0: C0304: Final newline missing (missing-final-newline)
src/fast_voice/whisper_live/transcriber/transcriber_faster_whisper.py:1:0: C0302: Too many lines in module (1887/1000) (too-many-lines)
src/fast_voice/whisper_live/transcriber/transcriber_faster_whisper.py:1:0: C0114: Missing module docstring (missing-module-docstring)
src/fast_voice/whisper_live/transcriber/transcriber_faster_whisper.py:34:0: C0115: Missing class docstring (missing-class-docstring)
src/fast_voice/whisper_live/transcriber/transcriber_faster_whisper.py:50:0: C0115: Missing class docstring (missing-class-docstring)
src/fast_voice/whisper_live/transcriber/transcriber_faster_whisper.py:50:0: R0902: Too many instance attributes (11/7) (too-many-instance-attributes)
src/fast_voice/whisper_live/transcriber/transcriber_faster_whisper.py:73:0: C0115: Missing class docstring (missing-class-docstring)
src/fast_voice/whisper_live/transcriber/transcriber_faster_whisper.py:73:0: R0902: Too many instance attributes (26/7) (too-many-instance-attributes)
src/fast_voice/whisper_live/transcriber/transcriber_faster_whisper.py:103:0: C0115: Missing class docstring (missing-class-docstring)
src/fast_voice/whisper_live/transcriber/transcriber_faster_whisper.py:113:0: C0115: Missing class docstring (missing-class-docstring)
src/fast_voice/whisper_live/transcriber/transcriber_faster_whisper.py:121:4: C0116: Missing function or method docstring (missing-function-docstring)
src/fast_voice/whisper_live/transcriber/transcriber_faster_whisper.py:121:4: R0914: Too many local variables (16/15) (too-many-locals)
src/fast_voice/whisper_live/transcriber/transcriber_faster_whisper.py:136:16: W0212: Access to a protected member _split_segments_by_timestamps of a client class (protected-access)
src/fast_voice/whisper_live/transcriber/transcriber_faster_whisper.py:146:20: R1735: Consider using '{"text": tokenizer.decode(subsegment['tokens']), "avg_logprob": output['avg_logprob'], ... }' instead of a call to 'dict'. (use-dict-literal)
src/fast_voice/whisper_live/transcriber/transcriber_faster_whisper.py:134:16: W0612: Unused variable 'seek' (unused-variable)
src/fast_voice/whisper_live/transcriber/transcriber_faster_whisper.py:135:16: W0612: Unused variable 'single_timestamp_ending' (unused-variable)
src/fast_voice/whisper_live/transcriber/transcriber_faster_whisper.py:176:4: C0116: Missing function or method docstring (missing-function-docstring)
src/fast_voice/whisper_live/transcriber/transcriber_faster_whisper.py:176:4: R0914: Too many local variables (18/15) (too-many-locals)
src/fast_voice/whisper_live/transcriber/transcriber_faster_whisper.py:247:16: R1735: Consider using '{"avg_logprob": cum_logprob / (seq_len + 1), "no_speech_prob": result.no_speech_prob, ... }' instead of a call to 'dict'. (use-dict-literal)
src/fast_voice/whisper_live/transcriber/transcriber_faster_whisper.py:256:4: W0102: Dangerous default value [] as argument (dangerous-default-value)
src/fast_voice/whisper_live/transcriber/transcriber_faster_whisper.py:256:4: W0102: Dangerous default value [] as argument (dangerous-default-value)
src/fast_voice/whisper_live/transcriber/transcriber_faster_whisper.py:256:4: R0913: Too many arguments (37/5) (too-many-arguments)
src/fast_voice/whisper_live/transcriber/transcriber_faster_whisper.py:256:4: R0917: Too many positional arguments (37/5) (too-many-positional-arguments)
src/fast_voice/whisper_live/transcriber/transcriber_faster_whisper.py:256:4: R0914: Too many local variables (49/15) (too-many-locals)
src/fast_voice/whisper_live/transcriber/transcriber_faster_whisper.py:462:20: C0209: Formatting a regular string which could be an f-string (consider-using-f-string)
src/fast_voice/whisper_live/transcriber/transcriber_faster_whisper.py:256:4: R0912: Too many branches (14/12) (too-many-branches)
src/fast_voice/whisper_live/transcriber/transcriber_faster_whisper.py:279:8: W0613: Unused argument 'condition_on_previous_text' (unused-argument)
src/fast_voice/whisper_live/transcriber/transcriber_faster_whisper.py:280:8: W0613: Unused argument 'prompt_reset_on_temperature' (unused-argument)
src/fast_voice/whisper_live/transcriber/transcriber_faster_whisper.py:286:8: W0613: Unused argument 'max_initial_timestamp' (unused-argument)
src/fast_voice/whisper_live/transcriber/transcriber_faster_whisper.py:296:8: W0613: Unused argument 'hallucination_silence_threshold' (unused-argument)
src/fast_voice/whisper_live/transcriber/transcriber_faster_whisper.py:534:4: R0913: Too many arguments (7/5) (too-many-arguments)
src/fast_voice/whisper_live/transcriber/transcriber_faster_whisper.py:534:4: R0917: Too many positional arguments (7/5) (too-many-positional-arguments)
src/fast_voice/whisper_live/transcriber/transcriber_faster_whisper.py:574:0: C0115: Missing class docstring (missing-class-docstring)
src/fast_voice/whisper_live/transcriber/transcriber_faster_whisper.py:574:0: R0902: Too many instance attributes (11/7) (too-many-instance-attributes)
src/fast_voice/whisper_live/transcriber/transcriber_faster_whisper.py:575:4: R0913: Too many arguments (10/5) (too-many-arguments)
src/fast_voice/whisper_live/transcriber/transcriber_faster_whisper.py:575:4: R0917: Too many positional arguments (10/5) (too-many-positional-arguments)
src/fast_voice/whisper_live/transcriber/transcriber_faster_whisper.py:692:4: W0102: Dangerous default value [] as argument (dangerous-default-value)
src/fast_voice/whisper_live/transcriber/transcriber_faster_whisper.py:692:4: W0102: Dangerous default value [] as argument (dangerous-default-value)
src/fast_voice/whisper_live/transcriber/transcriber_faster_whisper.py:692:4: R0913: Too many arguments (36/5) (too-many-arguments)
src/fast_voice/whisper_live/transcriber/transcriber_faster_whisper.py:692:4: R0917: Too many positional arguments (36/5) (too-many-positional-arguments)
src/fast_voice/whisper_live/transcriber/transcriber_faster_whisper.py:692:4: R0914: Too many local variables (53/15) (too-many-locals)
src/fast_voice/whisper_live/transcriber/transcriber_faster_whisper.py:849:24: C0209: Formatting a regular string which could be an f-string (consider-using-f-string)
src/fast_voice/whisper_live/transcriber/transcriber_faster_whisper.py:901:16: W1201: Use lazy % formatting in logging functions (logging-not-lazy)
src/fast_voice/whisper_live/transcriber/transcriber_faster_whisper.py:902:20: C0209: Formatting a regular string which could be an f-string (consider-using-f-string)
src/fast_voice/whisper_live/transcriber/transcriber_faster_whisper.py:692:4: R0912: Too many branches (14/12) (too-many-branches)
src/fast_voice/whisper_live/transcriber/transcriber_faster_whisper.py:836:26: W0612: Unused variable 'chunks_metadata' (unused-variable)
src/fast_voice/whisper_live/transcriber/transcriber_faster_whisper.py:970:4: R0913: Too many arguments (7/5) (too-many-arguments)
src/fast_voice/whisper_live/transcriber/transcriber_faster_whisper.py:970:4: R0917: Too many positional arguments (7/5) (too-many-positional-arguments)
src/fast_voice/whisper_live/transcriber/transcriber_faster_whisper.py:970:4: R0914: Too many local variables (21/15) (too-many-locals)
src/fast_voice/whisper_live/transcriber/transcriber_faster_whisper.py:1008:20: R1735: Consider using '{"seek": seek, "start": start_time, "end": end_time, "tokens": sliced_tokens, ... }' instead of a call to 'dict'. (use-dict-literal)
src/fast_voice/whisper_live/transcriber/transcriber_faster_whisper.py:1037:16: R1735: Consider using '{"seek": seek, "start": time_offset, "end": time_offset + duration, ... }' instead of a call to 'dict'. (use-dict-literal)
src/fast_voice/whisper_live/transcriber/transcriber_faster_whisper.py:1049:4: C0116: Missing function or method docstring (missing-function-docstring)
src/fast_voice/whisper_live/transcriber/transcriber_faster_whisper.py:1049:4: R0913: Too many arguments (6/5) (too-many-arguments)
src/fast_voice/whisper_live/transcriber/transcriber_faster_whisper.py:1049:4: R0917: Too many positional arguments (6/5) (too-many-positional-arguments)
src/fast_voice/whisper_live/transcriber/transcriber_faster_whisper.py:1049:4: R0914: Too many local variables (57/15) (too-many-locals)
src/fast_voice/whisper_live/transcriber/transcriber_faster_whisper.py:1106:12: R1730: Consider using 'seek_clip_end = min(seek_clip_end, content_frames)' instead of unnecessary if block (consider-using-min-builtin)
src/fast_voice/whisper_live/transcriber/transcriber_faster_whisper.py:1108:12: R1731: Consider using 'seek = max(seek, seek_clip_start)' instead of unnecessary if block (consider-using-max-builtin)
src/fast_voice/whisper_live/transcriber/transcriber_faster_whisper.py:1255:20: C0200: Consider using enumerate instead of iterating with range and len (consider-using-enumerate)
src/fast_voice/whisper_live/transcriber/transcriber_faster_whisper.py:1225:12: R1702: Too many nested blocks (6/5) (too-many-nested-blocks)
src/fast_voice/whisper_live/transcriber/transcriber_faster_whisper.py:1049:4: R0912: Too many branches (35/12) (too-many-branches)
src/fast_voice/whisper_live/transcriber/transcriber_faster_whisper.py:1049:4: R0915: Too many statements (129/50) (too-many-statements)
src/fast_voice/whisper_live/transcriber/transcriber_faster_whisper.py:1141:32: W0612: Unused variable 'language_probability' (unused-variable)
src/fast_voice/whisper_live/transcriber/transcriber_faster_whisper.py:1339:4: C0116: Missing function or method docstring (missing-function-docstring)
src/fast_voice/whisper_live/transcriber/transcriber_faster_whisper.py:1350:4: C0116: Missing function or method docstring (missing-function-docstring)
src/fast_voice/whisper_live/transcriber/transcriber_faster_whisper.py:1350:4: R0914: Too many local variables (20/15) (too-many-locals)
src/fast_voice/whisper_live/transcriber/transcriber_faster_whisper.py:1350:4: R0912: Too many branches (13/12) (too-many-branches)
src/fast_voice/whisper_live/transcriber/transcriber_faster_whisper.py:1480:4: C0116: Missing function or method docstring (missing-function-docstring)
src/fast_voice/whisper_live/transcriber/transcriber_faster_whisper.py:1480:4: R0913: Too many arguments (6/5) (too-many-arguments)
src/fast_voice/whisper_live/transcriber/transcriber_faster_whisper.py:1480:4: R0917: Too many positional arguments (6/5) (too-many-positional-arguments)
src/fast_voice/whisper_live/transcriber/transcriber_faster_whisper.py:1515:4: C0116: Missing function or method docstring (missing-function-docstring)
src/fast_voice/whisper_live/transcriber/transcriber_faster_whisper.py:1515:4: R0913: Too many arguments (8/5) (too-many-arguments)
src/fast_voice/whisper_live/transcriber/transcriber_faster_whisper.py:1515:4: R0917: Too many positional arguments (8/5) (too-many-positional-arguments)
src/fast_voice/whisper_live/transcriber/transcriber_faster_whisper.py:1515:4: R0914: Too many local variables (29/15) (too-many-locals)
src/fast_voice/whisper_live/transcriber/transcriber_faster_whisper.py:1584:28: R1735: Consider using '{"word": timing['word'], "start": round(time_offset + timing['start'], 2), ... }' instead of a call to 'dict'. (use-dict-literal)
src/fast_voice/whisper_live/transcriber/transcriber_faster_whisper.py:1515:4: R0912: Too many branches (19/12) (too-many-branches)
src/fast_voice/whisper_live/transcriber/transcriber_faster_whisper.py:1515:4: R1710: Either all return statements in a function should return an expression, or none of them should. (inconsistent-return-statements)
src/fast_voice/whisper_live/transcriber/transcriber_faster_whisper.py:1646:4: C0116: Missing function or method docstring (missing-function-docstring)
src/fast_voice/whisper_live/transcriber/transcriber_faster_whisper.py:1646:4: R0913: Too many arguments (6/5) (too-many-arguments)
src/fast_voice/whisper_live/transcriber/transcriber_faster_whisper.py:1646:4: R0917: Too many positional arguments (6/5) (too-many-positional-arguments)
src/fast_voice/whisper_live/transcriber/transcriber_faster_whisper.py:1646:4: R0914: Too many local variables (22/15) (too-many-locals)
src/fast_voice/whisper_live/transcriber/transcriber_faster_whisper.py:1702:20: R1735: Consider using '{"word": word, "tokens": tokens, "start": start, "end": end, "probability": probability, ... }' instead of a call to 'dict'. (use-dict-literal)
src/fast_voice/whisper_live/transcriber/transcriber_faster_whisper.py:1716:4: R0913: Too many arguments (7/5) (too-many-arguments)
src/fast_voice/whisper_live/transcriber/transcriber_faster_whisper.py:1716:4: R0917: Too many positional arguments (7/5) (too-many-positional-arguments)
src/fast_voice/whisper_live/transcriber/transcriber_faster_whisper.py:1716:4: R0914: Too many local variables (17/15) (too-many-locals)
src/fast_voice/whisper_live/transcriber/transcriber_faster_whisper.py:1753:30: W0612: Unused variable 'chunks_metadata' (unused-variable)
src/fast_voice/whisper_live/transcriber/transcriber_faster_whisper.py:1792:0: C0116: Missing function or method docstring (missing-function-docstring)
src/fast_voice/whisper_live/transcriber/transcriber_faster_whisper.py:1820:0: C0116: Missing function or method docstring (missing-function-docstring)
src/fast_voice/whisper_live/transcriber/transcriber_faster_whisper.py:1826:0: C0116: Missing function or method docstring (missing-function-docstring)
src/fast_voice/whisper_live/transcriber/transcriber_faster_whisper.py:1831:0: C0116: Missing function or method docstring (missing-function-docstring)
src/fast_voice/whisper_live/transcriber/transcriber_faster_whisper.py:1856:0: C0116: Missing function or method docstring (missing-function-docstring)
************* Module fast_voice.whisper_live.transcriber.transcriber_openvino
src/fast_voice/whisper_live/transcriber/transcriber_openvino.py:8:0: C0301: Line too long (113/100) (line-too-long)
src/fast_voice/whisper_live/transcriber/transcriber_openvino.py:20:0: C0301: Line too long (114/100) (line-too-long)
src/fast_voice/whisper_live/transcriber/transcriber_openvino.py:1:0: C0114: Missing module docstring (missing-module-docstring)
src/fast_voice/whisper_live/transcriber/transcriber_openvino.py:3:0: E0401: Unable to import 'openvino_genai' (import-error)
src/fast_voice/whisper_live/transcriber/transcriber_openvino.py:7:0: C0115: Missing class docstring (missing-class-docstring)
src/fast_voice/whisper_live/transcriber/transcriber_openvino.py:7:0: R0205: Class 'WhisperOpenVINO' inherits from object, can be safely removed from bases in python3 (useless-object-inheritance)
src/fast_voice/whisper_live/transcriber/transcriber_openvino.py:19:4: C0116: Missing function or method docstring (missing-function-docstring)
src/fast_voice/whisper_live/transcriber/transcriber_openvino.py:21:18: R1721: Unnecessary use of a comprehension, use list(outputs.chunks) instead. (unnecessary-comprehension)
src/fast_voice/whisper_live/transcriber/transcriber_openvino.py:7:0: R0903: Too few public methods (1/2) (too-few-public-methods)
************* Module fast_voice.whisper_live.transcriber.transcriber_tensorrt
src/fast_voice/whisper_live/transcriber/transcriber_tensorrt.py:13:16: C0303: Trailing whitespace (trailing-whitespace)
src/fast_voice/whisper_live/transcriber/transcriber_tensorrt.py:14:26: C0303: Trailing whitespace (trailing-whitespace)
src/fast_voice/whisper_live/transcriber/transcriber_tensorrt.py:15:16: C0303: Trailing whitespace (trailing-whitespace)
src/fast_voice/whisper_live/transcriber/transcriber_tensorrt.py:49:0: C0301: Line too long (109/100) (line-too-long)
src/fast_voice/whisper_live/transcriber/transcriber_tensorrt.py:65:0: C0301: Line too long (108/100) (line-too-long)
src/fast_voice/whisper_live/transcriber/transcriber_tensorrt.py:259:22: C0303: Trailing whitespace (trailing-whitespace)
src/fast_voice/whisper_live/transcriber/transcriber_tensorrt.py:279:0: C0325: Unnecessary parens after '=' keyword (superfluous-parens)
src/fast_voice/whisper_live/transcriber/transcriber_tensorrt.py:323:0: C0301: Line too long (103/100) (line-too-long)
src/fast_voice/whisper_live/transcriber/transcriber_tensorrt.py:383:0: C0301: Line too long (108/100) (line-too-long)
src/fast_voice/whisper_live/transcriber/transcriber_tensorrt.py:1:0: C0114: Missing module docstring (missing-module-docstring)
src/fast_voice/whisper_live/transcriber/transcriber_tensorrt.py:11:0: E0401: Unable to import 'whisper.tokenizer' (import-error)
src/fast_voice/whisper_live/transcriber/transcriber_tensorrt.py:19:0: E0401: Unable to import 'tensorrt_llm' (import-error)
src/fast_voice/whisper_live/transcriber/transcriber_tensorrt.py:20:0: R0402: Use 'from tensorrt_llm import logger' instead (consider-using-from-import)
src/fast_voice/whisper_live/transcriber/transcriber_tensorrt.py:20:0: E0401: Unable to import 'tensorrt_llm.logger' (import-error)
src/fast_voice/whisper_live/transcriber/transcriber_tensorrt.py:21:0: E0401: Unable to import 'tensorrt_llm._utils' (import-error)
src/fast_voice/whisper_live/transcriber/transcriber_tensorrt.py:23:0: E0401: Unable to import 'tensorrt_llm.bindings' (import-error)
src/fast_voice/whisper_live/transcriber/transcriber_tensorrt.py:24:0: E0401: Unable to import 'tensorrt_llm.runtime' (import-error)
src/fast_voice/whisper_live/transcriber/transcriber_tensorrt.py:25:0: E0401: Unable to import 'tensorrt_llm.runtime.session' (import-error)
src/fast_voice/whisper_live/transcriber/transcriber_tensorrt.py:27:4: E0401: Unable to import 'tensorrt_llm.runtime' (import-error)
src/fast_voice/whisper_live/transcriber/transcriber_tensorrt.py:35:0: C0116: Missing function or method docstring (missing-function-docstring)
src/fast_voice/whisper_live/transcriber/transcriber_tensorrt.py:37:9: W1514: Using open without explicitly specifying an encoding (unspecified-encoding)
src/fast_voice/whisper_live/transcriber/transcriber_tensorrt.py:45:0: C0116: Missing function or method docstring (missing-function-docstring)
src/fast_voice/whisper_live/transcriber/transcriber_tensorrt.py:79:0: C0115: Missing class docstring (missing-class-docstring)
src/fast_voice/whisper_live/transcriber/transcriber_tensorrt.py:89:4: C0116: Missing function or method docstring (missing-function-docstring)
src/fast_voice/whisper_live/transcriber/transcriber_tensorrt.py:95:4: C0116: Missing function or method docstring (missing-function-docstring)
src/fast_voice/whisper_live/transcriber/transcriber_tensorrt.py:95:4: R0914: Too many local variables (16/15) (too-many-locals)
src/fast_voice/whisper_live/transcriber/transcriber_tensorrt.py:100:26: R1728: Consider using a generator instead 'max(f.shape[-1] for f in mel)' (consider-using-generator)
src/fast_voice/whisper_live/transcriber/transcriber_tensorrt.py:152:0: C0115: Missing class docstring (missing-class-docstring)
src/fast_voice/whisper_live/transcriber/transcriber_tensorrt.py:160:4: C0116: Missing function or method docstring (missing-function-docstring)
src/fast_voice/whisper_live/transcriber/transcriber_tensorrt.py:194:4: C0116: Missing function or method docstring (missing-function-docstring)
src/fast_voice/whisper_live/transcriber/transcriber_tensorrt.py:194:4: R0913: Too many arguments (8/5) (too-many-arguments)
src/fast_voice/whisper_live/transcriber/transcriber_tensorrt.py:194:4: R0917: Too many positional arguments (8/5) (too-many-positional-arguments)
src/fast_voice/whisper_live/transcriber/transcriber_tensorrt.py:194:4: R0914: Too many local variables (16/15) (too-many-locals)
src/fast_voice/whisper_live/transcriber/transcriber_tensorrt.py:231:12: C0103: Variable name "WHISPER_PAD_TOKEN_ID" doesn't conform to snake_case naming style (invalid-name)
src/fast_voice/whisper_live/transcriber/transcriber_tensorrt.py:257:0: C0115: Missing class docstring (missing-class-docstring)
src/fast_voice/whisper_live/transcriber/transcriber_tensorrt.py:257:0: R0205: Class 'WhisperTRTLLM' inherits from object, can be safely removed from bases in python3 (useless-object-inheritance)
src/fast_voice/whisper_live/transcriber/transcriber_tensorrt.py:257:0: R0902: Too many instance attributes (9/7) (too-many-instance-attributes)
src/fast_voice/whisper_live/transcriber/transcriber_tensorrt.py:259:4: R0913: Too many arguments (11/5) (too-many-arguments)
src/fast_voice/whisper_live/transcriber/transcriber_tensorrt.py:259:4: R0917: Too many positional arguments (11/5) (too-many-positional-arguments)
src/fast_voice/whisper_live/transcriber/transcriber_tensorrt.py:259:4: R0914: Too many local variables (18/15) (too-many-locals)
src/fast_voice/whisper_live/transcriber/transcriber_tensorrt.py:298:28: R1735: Consider using '{"engine_dir": engine_dir, "is_enc_dec": True, "max_batch_size": 1, ... }' instead of a call to 'dict'. (use-dict-literal)
src/fast_voice/whisper_live/transcriber/transcriber_tensorrt.py:307:36: E0606: Possibly using variable 'ModelRunnerCpp' before assignment (possibly-used-before-assignment)
src/fast_voice/whisper_live/transcriber/transcriber_tensorrt.py:364:8: R1705: Unnecessary "else" after "return", remove the "else" and de-indent the code inside it (no-else-return)
src/fast_voice/whisper_live/transcriber/transcriber_tensorrt.py:365:29: E0606: Possibly using variable 'duration' before assignment (possibly-used-before-assignment)
src/fast_voice/whisper_live/transcriber/transcriber_tensorrt.py:369:4: C0116: Missing function or method docstring (missing-function-docstring)
src/fast_voice/whisper_live/transcriber/transcriber_tensorrt.py:369:4: R0913: Too many arguments (6/5) (too-many-arguments)
src/fast_voice/whisper_live/transcriber/transcriber_tensorrt.py:369:4: R0917: Too many positional arguments (6/5) (too-many-positional-arguments)
src/fast_voice/whisper_live/transcriber/transcriber_tensorrt.py:369:4: R0914: Too many local variables (17/15) (too-many-locals)
src/fast_voice/whisper_live/transcriber/transcriber_tensorrt.py:415:8: C0200: Consider using enumerate instead of iterating with range and len (consider-using-enumerate)
src/fast_voice/whisper_live/transcriber/transcriber_tensorrt.py:420:4: C0116: Missing function or method docstring (missing-function-docstring)
src/fast_voice/whisper_live/transcriber/transcriber_tensorrt.py:420:4: R0913: Too many arguments (8/5) (too-many-arguments)
src/fast_voice/whisper_live/transcriber/transcriber_tensorrt.py:420:4: R0917: Too many positional arguments (8/5) (too-many-positional-arguments)
src/fast_voice/whisper_live/transcriber/transcriber_tensorrt.py:457:0: C0116: Missing function or method docstring (missing-function-docstring)
src/fast_voice/whisper_live/transcriber/transcriber_tensorrt.py:457:0: R0913: Too many arguments (8/5) (too-many-arguments)
src/fast_voice/whisper_live/transcriber/transcriber_tensorrt.py:457:0: R0917: Too many positional arguments (8/5) (too-many-positional-arguments)
src/fast_voice/whisper_live/transcriber/transcriber_tensorrt.py:465:8: W0613: Unused argument 'mel_filters_dir' (unused-argument)
src/fast_voice/whisper_live/transcriber/transcriber_tensorrt.py:19:0: C0411: third party import "tensorrt_llm" should be placed before first party import "fast_voice.whisper_live.transcriber.tensorrt_utils.mel_filters"  (wrong-import-order)
src/fast_voice/whisper_live/transcriber/transcriber_tensorrt.py:20:0: C0411: third party import "tensorrt_llm.logger" should be placed before first party import "fast_voice.whisper_live.transcriber.tensorrt_utils.mel_filters"  (wrong-import-order)
src/fast_voice/whisper_live/transcriber/transcriber_tensorrt.py:21:0: C0411: third party import "tensorrt_llm._utils.str_dtype_to_torch" should be placed before first party import "fast_voice.whisper_live.transcriber.tensorrt_utils.mel_filters"  (wrong-import-order)
src/fast_voice/whisper_live/transcriber/transcriber_tensorrt.py:23:0: C0411: third party import "tensorrt_llm.bindings.GptJsonConfig" should be placed before first party import "fast_voice.whisper_live.transcriber.tensorrt_utils.mel_filters"  (wrong-import-order)
src/fast_voice/whisper_live/transcriber/transcriber_tensorrt.py:24:0: C0411: third party import "tensorrt_llm.runtime.PYTHON_BINDINGS" should be placed before first party import "fast_voice.whisper_live.transcriber.tensorrt_utils.mel_filters"  (wrong-import-order)
src/fast_voice/whisper_live/transcriber/transcriber_tensorrt.py:25:0: C0411: third party import "tensorrt_llm.runtime.session.Session" should be placed before first party import "fast_voice.whisper_live.transcriber.tensorrt_utils.mel_filters"  (wrong-import-order)
src/fast_voice/whisper_live/transcriber/transcriber_tensorrt.py:10:0: C0412: Imports from package torch are not grouped (ungrouped-imports)
************* Module fast_voice.testing.client
src/fast_voice/testing/client.py:40:0: C0303: Trailing whitespace (trailing-whitespace)
src/fast_voice/testing/client.py:47:0: C0303: Trailing whitespace (trailing-whitespace)
src/fast_voice/testing/client.py:56:0: C0303: Trailing whitespace (trailing-whitespace)
src/fast_voice/testing/client.py:68:0: C0303: Trailing whitespace (trailing-whitespace)
src/fast_voice/testing/client.py:71:0: C0303: Trailing whitespace (trailing-whitespace)
src/fast_voice/testing/client.py:73:0: C0301: Line too long (104/100) (line-too-long)
src/fast_voice/testing/client.py:81:0: C0303: Trailing whitespace (trailing-whitespace)
src/fast_voice/testing/client.py:85:0: C0303: Trailing whitespace (trailing-whitespace)
src/fast_voice/testing/client.py:89:0: C0303: Trailing whitespace (trailing-whitespace)
src/fast_voice/testing/client.py:95:0: C0303: Trailing whitespace (trailing-whitespace)
src/fast_voice/testing/client.py:100:0: C0303: Trailing whitespace (trailing-whitespace)
src/fast_voice/testing/client.py:105:0: C0303: Trailing whitespace (trailing-whitespace)
src/fast_voice/testing/client.py:108:0: C0303: Trailing whitespace (trailing-whitespace)
src/fast_voice/testing/client.py:111:0: C0303: Trailing whitespace (trailing-whitespace)
src/fast_voice/testing/client.py:1:0: C0114: Missing module docstring (missing-module-docstring)
src/fast_voice/testing/client.py:32:4: R0914: Too many local variables (19/15) (too-many-locals)
src/fast_voice/testing/client.py:74:15: W0718: Catching too general exception Exception (broad-exception-caught)
src/fast_voice/testing/client.py:72:20: W0612: Unused variable 'duration' (unused-variable)
src/fast_voice/testing/client.py:4:0: C0411: standard import "sys" should be placed before third party import "numpy" (wrong-import-order)
src/fast_voice/testing/client.py:5:0: C0411: standard import "os" should be placed before third party import "numpy" (wrong-import-order)
src/fast_voice/testing/client.py:6:0: C0411: standard import "wave" should be placed before third party import "numpy" (wrong-import-order)
************* Module fast_voice.testing
src/fast_voice/testing/__init__.py:1:0: C0114: Missing module docstring (missing-module-docstring)
************* Module test_client
tests/test_client.py:11:0: C0303: Trailing whitespace (trailing-whitespace)
tests/test_client.py:15:0: C0303: Trailing whitespace (trailing-whitespace)
tests/test_client.py:35:0: C0303: Trailing whitespace (trailing-whitespace)
tests/test_client.py:39:0: C0303: Trailing whitespace (trailing-whitespace)
tests/test_client.py:47:0: C0303: Trailing whitespace (trailing-whitespace)
tests/test_client.py:50:0: C0303: Trailing whitespace (trailing-whitespace)
tests/test_client.py:56:0: C0303: Trailing whitespace (trailing-whitespace)
tests/test_client.py:1:0: C0114: Missing module docstring (missing-module-docstring)
tests/test_client.py:6:0: C0115: Missing class docstring (missing-class-docstring)
tests/test_client.py:26:4: C0116: Missing function or method docstring (missing-function-docstring)
tests/test_client.py:32:4: C0116: Missing function or method docstring (missing-function-docstring)
tests/test_client.py:54:19: W0718: Catching too general exception Exception (broad-exception-caught)
tests/test_client.py:59:12: C0415: Import outside toplevel (json) (import-outside-toplevel)
************* Module test_e2e
tests/test_e2e.py:15:0: C0303: Trailing whitespace (trailing-whitespace)
tests/test_e2e.py:18:0: C0303: Trailing whitespace (trailing-whitespace)
tests/test_e2e.py:21:0: C0303: Trailing whitespace (trailing-whitespace)
tests/test_e2e.py:35:0: C0303: Trailing whitespace (trailing-whitespace)
tests/test_e2e.py:37:0: C0301: Line too long (112/100) (line-too-long)
tests/test_e2e.py:39:0: C0301: Line too long (121/100) (line-too-long)
tests/test_e2e.py:40:0: C0303: Trailing whitespace (trailing-whitespace)
tests/test_e2e.py:42:0: C0301: Line too long (103/100) (line-too-long)
tests/test_e2e.py:45:0: C0303: Trailing whitespace (trailing-whitespace)
tests/test_e2e.py:1:0: C0114: Missing module docstring (missing-module-docstring)
tests/test_e2e.py:7:0: C0115: Missing class docstring (missing-class-docstring)
tests/test_e2e.py:13:8: C0103: Variable name "HOST" doesn't conform to snake_case naming style (invalid-name)
tests/test_e2e.py:14:8: C0103: Variable name "PORT" doesn't conform to snake_case naming style (invalid-name)
tests/test_e2e.py:46:8: W1503: Redundant use of assertTrue with constant value True (redundant-unittest-assert)
tests/test_e2e.py:3:0: W0611: Unused import threading (unused-import)
************* Module test_monitor_e2e
tests/test_monitor_e2e.py:20:0: C0301: Line too long (103/100) (line-too-long)
tests/test_monitor_e2e.py:22:0: C0303: Trailing whitespace (trailing-whitespace)
tests/test_monitor_e2e.py:31:0: C0301: Line too long (116/100) (line-too-long)
tests/test_monitor_e2e.py:34:0: C0303: Trailing whitespace (trailing-whitespace)
tests/test_monitor_e2e.py:39:0: C0301: Line too long (104/100) (line-too-long)
tests/test_monitor_e2e.py:43:0: C0303: Trailing whitespace (trailing-whitespace)
tests/test_monitor_e2e.py:46:0: C0303: Trailing whitespace (trailing-whitespace)
tests/test_monitor_e2e.py:50:0: C0303: Trailing whitespace (trailing-whitespace)
tests/test_monitor_e2e.py:65:0: C0303: Trailing whitespace (trailing-whitespace)
tests/test_monitor_e2e.py:71:0: C0303: Trailing whitespace (trailing-whitespace)
tests/test_monitor_e2e.py:75:0: C0303: Trailing whitespace (trailing-whitespace)
tests/test_monitor_e2e.py:79:0: C0303: Trailing whitespace (trailing-whitespace)
tests/test_monitor_e2e.py:82:0: C0303: Trailing whitespace (trailing-whitespace)
tests/test_monitor_e2e.py:89:0: C0303: Trailing whitespace (trailing-whitespace)
tests/test_monitor_e2e.py:94:0: C0303: Trailing whitespace (trailing-whitespace)
tests/test_monitor_e2e.py:95:70: C0303: Trailing whitespace (trailing-whitespace)
tests/test_monitor_e2e.py:98:0: C0303: Trailing whitespace (trailing-whitespace)
tests/test_monitor_e2e.py:100:29: C0303: Trailing whitespace (trailing-whitespace)
tests/test_monitor_e2e.py:1:0: C0114: Missing module docstring (missing-module-docstring)
tests/test_monitor_e2e.py:11:0: C0115: Missing class docstring (missing-class-docstring)
tests/test_monitor_e2e.py:17:8: W0212: Access to a protected member _instance of a client class (protected-access)
tests/test_monitor_e2e.py:24:8: W0107: Unnecessary pass statement (unnecessary-pass)
tests/test_monitor_e2e.py:26:4: C0116: Missing function or method docstring (missing-function-docstring)
tests/test_monitor_e2e.py:35:8: C0415: Import outside toplevel (fast_voice.whisper_live.server.TranscriptionServer) (import-outside-toplevel)
tests/test_monitor_e2e.py:61:19: W0718: Catching too general exception Exception (broad-exception-caught)
tests/test_monitor_e2e.py:100:8: W1503: Redundant use of assertTrue with constant value True (redundant-unittest-assert)
tests/test_monitor_e2e.py:7:0: W0611: Unused start imported from fast_voice.server.main as start_server (unused-import)
************* Module test_tui
tests/test_tui.py:15:0: C0303: Trailing whitespace (trailing-whitespace)
tests/test_tui.py:20:0: C0303: Trailing whitespace (trailing-whitespace)
tests/test_tui.py:1:0: C0114: Missing module docstring (missing-module-docstring)
tests/test_tui.py:6:0: C0115: Missing class docstring (missing-class-docstring)
tests/test_tui.py:32:4: C0116: Missing function or method docstring (missing-function-docstring)
tests/test_tui.py:35:25: W0212: Access to a protected member _last_text of a client class (protected-access)
tests/test_tui.py:36:25: W0212: Access to a protected member _show_help of a client class (protected-access)
tests/test_tui.py:38:4: C0116: Missing function or method docstring (missing-function-docstring)
tests/test_tui.py:43:25: W0212: Access to a protected member _last_text of a client class (protected-access)
tests/test_tui.py:45:4: C0116: Missing function or method docstring (missing-function-docstring)
tests/test_tui.py:49:4: C0116: Missing function or method docstring (missing-function-docstring)
tests/test_tui.py:55:4: C0116: Missing function or method docstring (missing-function-docstring)
tests/test_tui.py:56:25: W0212: Access to a protected member _show_help of a client class (protected-access)
tests/test_tui.py:57:8: W0212: Access to a protected member _show_help of a client class (protected-access)
************* Module test_client_flow
tests/test_client_flow.py:12:0: C0303: Trailing whitespace (trailing-whitespace)
tests/test_client_flow.py:18:0: C0303: Trailing whitespace (trailing-whitespace)
tests/test_client_flow.py:39:0: C0303: Trailing whitespace (trailing-whitespace)
tests/test_client_flow.py:42:0: C0303: Trailing whitespace (trailing-whitespace)
tests/test_client_flow.py:47:0: C0301: Line too long (105/100) (line-too-long)
tests/test_client_flow.py:50:0: C0303: Trailing whitespace (trailing-whitespace)
tests/test_client_flow.py:56:0: C0303: Trailing whitespace (trailing-whitespace)
tests/test_client_flow.py:58:0: C0303: Trailing whitespace (trailing-whitespace)
tests/test_client_flow.py:61:0: C0303: Trailing whitespace (trailing-whitespace)
tests/test_client_flow.py:63:42: C0303: Trailing whitespace (trailing-whitespace)
tests/test_client_flow.py:70:0: C0303: Trailing whitespace (trailing-whitespace)
tests/test_client_flow.py:71:100: C0303: Trailing whitespace (trailing-whitespace)
tests/test_client_flow.py:74:0: C0303: Trailing whitespace (trailing-whitespace)
tests/test_client_flow.py:78:0: C0303: Trailing whitespace (trailing-whitespace)
tests/test_client_flow.py:80:63: C0303: Trailing whitespace (trailing-whitespace)
tests/test_client_flow.py:83:0: C0303: Trailing whitespace (trailing-whitespace)
tests/test_client_flow.py:88:0: C0303: Trailing whitespace (trailing-whitespace)
tests/test_client_flow.py:89:12: C0303: Trailing whitespace (trailing-whitespace)
tests/test_client_flow.py:93:0: C0301: Line too long (101/100) (line-too-long)
tests/test_client_flow.py:93:0: W0311: Bad indentation. Found 13 spaces, expected 12 (bad-indentation)
tests/test_client_flow.py:94:0: C0303: Trailing whitespace (trailing-whitespace)
tests/test_client_flow.py:96:0: C0303: Trailing whitespace (trailing-whitespace)
tests/test_client_flow.py:100:0: C0303: Trailing whitespace (trailing-whitespace)
tests/test_client_flow.py:104:0: C0303: Trailing whitespace (trailing-whitespace)
tests/test_client_flow.py:1:0: C0114: Missing module docstring (missing-module-docstring)
tests/test_client_flow.py:8:0: C0115: Missing class docstring (missing-class-docstring)
tests/test_client_flow.py:25:8: C0103: Attribute name "VoiceClient" doesn't conform to snake_case naming style (invalid-name)
tests/test_client_flow.py:24:8: C0415: Import outside toplevel (fast_voice.client.core.VoiceClient) (import-outside-toplevel)
tests/test_client_flow.py:89:8: W0107: Unnecessary pass statement (unnecessary-pass)
************* Module test_cowsay
tests/test_cowsay.py:14:0: C0303: Trailing whitespace (trailing-whitespace)
tests/test_cowsay.py:19:0: C0303: Trailing whitespace (trailing-whitespace)
tests/test_cowsay.py:23:0: C0303: Trailing whitespace (trailing-whitespace)
tests/test_cowsay.py:29:0: C0303: Trailing whitespace (trailing-whitespace)
tests/test_cowsay.py:34:0: C0303: Trailing whitespace (trailing-whitespace)
tests/test_cowsay.py:37:0: C0303: Trailing whitespace (trailing-whitespace)
tests/test_cowsay.py:43:0: C0303: Trailing whitespace (trailing-whitespace)
tests/test_cowsay.py:46:0: C0303: Trailing whitespace (trailing-whitespace)
tests/test_cowsay.py:54:0: C0303: Trailing whitespace (trailing-whitespace)
tests/test_cowsay.py:1:0: C0114: Missing module docstring (missing-module-docstring)
tests/test_cowsay.py:7:0: E0401: Unable to import 'examples.cowsay_app' (import-error)
tests/test_cowsay.py:7:0: C0413: Import "from examples.cowsay_app import cowsay, main" should be placed at the top of the module (wrong-import-position)
tests/test_cowsay.py:9:0: C0115: Missing class docstring (missing-class-docstring)
tests/test_cowsay.py:10:4: C0116: Missing function or method docstring (missing-function-docstring)
tests/test_cowsay.py:25:4: C0116: Missing function or method docstring (missing-function-docstring)
tests/test_cowsay.py:25:29: C0103: Argument name "MockVoiceClient" doesn't conform to snake_case naming style (invalid-name)
tests/test_cowsay.py:35:8: C0415: Import outside toplevel (asyncio) (import-outside-toplevel)
tests/test_cowsay.py:2:0: W0611: Unused MagicMock imported from unittest.mock (unused-import)
tests/test_cowsay.py:1:0: R0801: Similar lines in 2 files
==fast_voice.client.utils:[127:146]
==fast_voice.whisper_live.client:[822:841]
            host,
            port,
            lang,
            translate,
            model,
            srt_file_path=output_transcription_path,
            use_vad=use_vad,
            use_wss=use_wss,
            log_transcription=log_transcription,
            send_last_n_segments=send_last_n_segments,
            no_speech_thresh=no_speech_thresh,
            clip_audio=clip_audio,
            same_output_threshold=same_output_threshold,
            transcription_callback=transcription_callback,
            enable_translation=enable_translation,
            target_language=target_language,
            translation_callback=translation_callback,
            translation_srt_file_path=translation_srt_file_path,
            enable_timestamps=enable_timestamps, (duplicate-code)
tests/test_cowsay.py:1:0: R0801: Similar lines in 2 files
==fast_voice.client.utils:[75:89]
==fast_voice.whisper_live.client:[284:298]
        ws.send(
            json.dumps(
                {
                    "uid": self.uid,
                    "language": self.language,
                    "task": self.task,
                    "model": self.model,
                    "use_vad": self.use_vad,
                    "send_last_n_segments": self.send_last_n_segments,
                    "no_speech_thresh": self.no_speech_thresh,
                    "clip_audio": self.clip_audio,
                    "same_output_threshold": self.same_output_threshold,
                    "enable_translation": self.enable_translation,
                    "target_language": self.target_language, (duplicate-code)
tests/test_cowsay.py:1:0: R0801: Similar lines in 2 files
==fast_voice.client.daemon:[29:46]
==fast_voice.client.utils:[36:52]
    try:
        # Launch independent subprocess
        # stdout/stderr to DEVNULL to avoid cluttering client
        subprocess.Popen(
            cmd,
            start_new_session=True, # Detach so it survives client exit
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )

        # Wait for port to open
        print("[INFO] Waiting for daemon to initialize...", file=sys.stderr)
        start_time = time.time()
        while time.time() - start_time < 20: # 20s timeout (model load can be slow)
            try:
                with socket.create_connection((host, port), timeout=1):
                    # print("[INFO] Daemon started successfully.", file=sys.stderr) (duplicate-code)
tests/test_cowsay.py:1:0: R0801: Similar lines in 2 files
==fast_voice.client.daemon:[11:27]
==fast_voice.client.utils:[14:30]
    try:
        with socket.create_connection((host, port), timeout=1):
            return # Daemon is running
    except (socket.timeout, ConnectionRefusedError, OSError):
        pass # Daemon not running

    # Daemon not running, check config
    config = Config()
    if not config.get("daemon.auto_start", True):
        return # Auto-start disabled or not configured

    print(f"[INFO] Daemon not found on {host}:{port}. Auto-starting...", file=sys.stderr)

    cmd = config.get("daemon.command")
    if not cmd:
        # Default to running the module (duplicate-code)
tests/test_cowsay.py:1:0: R0801: Similar lines in 2 files
==fast_voice.whisper_live.backend.openvino_backend:[10:58]
==fast_voice.whisper_live.backend.trt_backend:[10:59]
    SINGLE_MODEL = None
    SINGLE_MODEL_LOCK = threading.Lock()

    def __init__(
        self,
        websocket,
        task="transcribe",
        multilingual=False,
        language=None,
        client_uid=None,
        model=None,
        single_model=False,
        use_py_session=False,
        max_new_tokens=225,
        send_last_n_segments=10,
        no_speech_thresh=0.45,
        clip_audio=False,
        same_output_threshold=10,
    ):
        """
        Initialize a ServeClient instance.
        The Whisper model is initialized based on the client's language and device availability.
        The transcription thread is started upon initialization. A "SERVER_READY" message is sent
        to the client to indicate that the server is ready.

        Args:
            websocket (WebSocket): The WebSocket connection for the client.
            task (str, optional): The task type, e.g., "transcribe." Defaults to "transcribe".
            device (str, optional): The device type for Whisper, "cuda" or "cpu". Defaults to None.
            multilingual (bool, optional): Whether the client supports multilingual transcription. Defaults to False.
            language (str, optional): The language for transcription. Defaults to None.
            client_uid (str, optional): A unique identifier for the client. Defaults to None.
            single_model (bool, optional): Whether to instantiate a new model for each client connection. Defaults to False.
            use_py_session (bool, optional): Use python session or cpp session. Defaults to Cpp Session.
            max_new_tokens (int, optional): Max number of tokens to generate.
            send_last_n_segments (int, optional): Number of most recent segments to send to the client. Defaults to 10.
            no_speech_thresh (float, optional): Segments with no speech probability above this threshold will be discarded. Defaults to 0.45.
            clip_audio (bool, optional): Whether to clip audio with no valid segments. Defaults to False.
            same_output_threshold (int, optional): Number of repeated outputs before considering it as a valid segment. Defaults to 10.
        """
        super().__init__(
            client_uid,
            websocket,
            send_last_n_segments,
            no_speech_thresh,
            clip_audio,
            same_output_threshold,
        )
 (duplicate-code)
tests/test_cowsay.py:1:0: R0801: Similar lines in 2 files
==fast_voice.client.utils:[151:159]
==fast_voice.whisper_live.client:[849:857]
        TranscriptionTeeClient.__init__(
            self,
            [self.client],
            save_output_recording=save_output_recording,
            output_recording_filename=output_recording_filename,
            mute_audio_playback=mute_audio_playback,
            input_device_index=input_device_index
        ) (duplicate-code)
tests/test_cowsay.py:1:0: R0801: Similar lines in 2 files
==fast_voice.whisper_live.backend.faster_whisper_backend:[263:281]
==fast_voice.whisper_live.backend.openvino_backend:[129:147]
        return result

    def handle_transcription_output(self, result, duration):
        """
        Handle the transcription output, updating the transcript and sending data to the client.

        Args:
            result (str): The result from whisper inference i.e. the list of segments.
            duration (float): Duration of the transcribed audio chunk.
        """
        segments = []
        if len(result):
            self.t_start = None
            last_segment = self.update_segments(result, duration)
            segments = self.prepare_segments(last_segment)

        if len(segments):
            self.send_transcription_to_client(segments) (duplicate-code)
tests/test_cowsay.py:1:0: R0801: Similar lines in 2 files
==fast_voice.whisper_live.backend.faster_whisper_backend:[101:108]
==fast_voice.whisper_live.backend.openvino_backend:[50:57]
        super().__init__(
            client_uid,
            websocket,
            send_last_n_segments,
            no_speech_thresh,
            clip_audio,
            same_output_threshold, (duplicate-code)
tests/test_cowsay.py:1:0: R0801: Similar lines in 2 files
==fast_voice.whisper_live.transcriber.tensorrt_utils:[185:207]
==fast_voice.whisper_live.transcriber.transcriber_tensorrt:[360:375]
    log_spec = torch.clamp(mel_spec, min=1e-10).log10()
    log_spec = torch.maximum(log_spec, log_spec.max() - 8.0)
    log_spec = (log_spec + 4.0) / 4.0
    if return_duration:
        return log_spec, duration
    else:
        return log_spec


def store_transcripts(filename: Pathlike, texts: Iterable[Tuple[str, str,
                                                                str]]) -> None:
    """Save predicted results and reference transcripts to a file.
    https://github.com/k2-fsa/icefall/blob/master/icefall/utils.py
    Args:
      filename:
        File to save the results to.
      texts:
        An iterable of tuples. The first element is the cur_id, the second is
        the reference transcript and the third element is the predicted result.
    Returns:
      Return None.
    """ (duplicate-code)
tests/test_cowsay.py:1:0: R0801: Similar lines in 2 files
==fast_voice.client.daemon:[46:53]
==fast_voice.client.utils:[53:63]
                    return
            except (socket.timeout, ConnectionRefusedError, OSError):
                time.sleep(0.5)

        print("[ERROR] Timeout waiting for daemon to start.", file=sys.stderr)
    except Exception as e:
        print(f"[ERROR] Failed to auto-start daemon: {e}", file=sys.stderr)


# Subclass Client to inject initial_prompt (duplicate-code)
tests/test_cowsay.py:1:0: R0801: Similar lines in 2 files
==fast_voice.whisper_live.transcriber.tensorrt_utils:[157:163]
==fast_voice.whisper_live.transcriber.transcriber_tensorrt:[338:344]
    if not torch.is_tensor(audio):
        if isinstance(audio, str):
            if audio.endswith('.wav'):
                audio, _ = load_audio_wav_format(audio)
            else:
                audio = load_audio(audio) (duplicate-code)
tests/test_cowsay.py:1:0: R0801: Similar lines in 2 files
==fast_voice.whisper_live.backend.base:[76:82]
==fast_voice.whisper_live.backend.trt_backend:[188:194]
        while True:
            if self.exit:
                logging.info("Exiting speech to text thread")
                break

            if self.frames_np is None: (duplicate-code)
tests/test_cowsay.py:1:0: R0801: Similar lines in 2 files
==fast_voice.whisper_live.backend.openvino_backend:[86:92]
==fast_voice.whisper_live.backend.trt_backend:[74:80]
        self.trans_thread = threading.Thread(target=self.speech_to_text)
        self.trans_thread.start()

        self.websocket.send(json.dumps({
            "uid": self.client_uid,
            "message": self.SERVER_READY, (duplicate-code)
tests/test_cowsay.py:1:0: R0801: Similar lines in 2 files
==fast_voice.whisper_live.transcriber.tensorrt_utils:[32:55]
==fast_voice.whisper_live.transcriber.transcriber_tensorrt:[28:35]
SAMPLE_RATE = 16000
N_FFT = 400
HOP_LENGTH = 160
CHUNK_LENGTH = 30
N_SAMPLES = CHUNK_LENGTH * SAMPLE_RATE  # 480000 samples in a 30-second chunk


def load_audio(file: str, sr: int = 16000):
    """
    Open an audio file, resample it, and read as a mono waveform.

    Parameters
    ----------
    file: str
        The audio file to open.

    sr: int
        The sample rate to resample the audio if necessary.

    Returns
    -------
    A NumPy array containing the audio waveform, in float32 dtype.
    """ (duplicate-code)

------------------------------------------------------------------
Your code has been rated at 6.87/10 (previous run: 6.87/10, +0.00)

