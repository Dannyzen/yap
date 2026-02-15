
import os

path = "src/fast_voice/whisper_live/server.py"

with open(path, "r") as f:
    lines = f.readlines()

# Indicies are 0-based, so line 63 is index 62.
# Range 63-79 means indices 62 to 78 (inclusive).
# Range 492-508 means indices 491 to 507 (inclusive).

# We must delete from bottom up to avoid shifting indices.

# Check context before deleting
print(f"Line 492: {lines[491]}")
print(f"Line 508: {lines[507]}")
print(f"Line 63: {lines[62]}")
print(f"Line 79: {lines[78]}")

# Delete 492-508
del lines[491:508]

# Delete 63-79
del lines[62:79]

with open(path, "w") as f:
    f.writelines(lines)

print("Fixed duplicates.")
