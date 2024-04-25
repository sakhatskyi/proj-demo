def process_int(some_int: int) -> int:
    return some_int ** 2

def process_str(some_str: str) -> str:
    return " ".join(some_str.strip().split())

def process_list(some_list: list) -> list:
    return [i for i in some_list if isinstance(i, int)]