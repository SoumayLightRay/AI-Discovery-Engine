import os
import sys

# Make `src.*` importable no matter where pytest is launched from.
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# Tests must never call the real LLM.
os.environ.pop("GROQ_API_KEY", None)
