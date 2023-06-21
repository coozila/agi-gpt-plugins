import os
from typing import Any

from memory import Memory


def get_memory_backend() -> Any:
    memory_backend = os.getenv("MEMORY_BACKEND", "json_file")
    if memory_backend == "json_file":
        return Memory()
    elif memory_backend == "redis":
        # Configure and return Redis memory backend
        pass  # Replace with your Redis memory backend setup
    else:
        raise ValueError(f"Invalid memory backend: {memory_backend}")


def audit_and_test_plan():
    memory_backend = get_memory_backend()
    memory_backend.store("key", "value")

    value = memory_backend.retrieve("key")
    print(value)


if __name__ == "__main__":
    audit_and_test_plan()


