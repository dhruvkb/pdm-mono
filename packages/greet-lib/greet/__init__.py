def get_hello_msg(name: str | None = None) -> str:
    if name is None:
        name = "World"
    return f"Hello, {name}!"
