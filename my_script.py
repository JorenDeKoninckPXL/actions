#!/usr/bin/env python3

print("Hello from Python!")
print("This script is running in a GitHub Actions workflow.")
print("Python version and environment details:")

import sys
import platform

print(f"Python version: {sys.version}")
print(f"Platform: {platform.platform()}")
print(f"Processor: {platform.processor()}")
