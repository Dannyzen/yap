import pyaudio
import sys

p = pyaudio.PyAudio()
device_index = 6 # C920
rates = [8000, 16000, 32000, 44100, 48000]

print(f"Probing Device {device_index}...", file=sys.stderr)
try:
    info = p.get_device_info_by_index(device_index)
    print(f"Device Name: {info.get('name')}", file=sys.stderr)
    print(f"Max Input Channels: {info.get('maxInputChannels')}", file=sys.stderr)
    print(f"Default Sample Rate: {info.get('defaultSampleRate')}", file=sys.stderr)
except Exception as e:
    print(f"Error getting info: {e}", file=sys.stderr)

print("\nTesting Rates:", file=sys.stderr)
for rate in rates:
    try:
        if p.is_format_supported(rate, input_device=device_index, input_channels=1, input_format=pyaudio.paInt16):
            print(f"  {rate} Hz: SUPPORTED", file=sys.stderr)
        else:
            print(f"  {rate} Hz: No", file=sys.stderr)
    except Exception as e:
        print(f"  {rate} Hz: Error ({e})", file=sys.stderr)

p.terminate()
