def reverse(text: str) -> str:
    return "".join(text[-idx] for idx in range(1, len(text) + 1))
