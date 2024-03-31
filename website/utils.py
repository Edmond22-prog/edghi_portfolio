import uuid


def generate_uuid() -> str:
    return uuid.uuid4().hex


def build_enum_tuple(enum) -> tuple:
    return tuple((item.value, item.name) for item in enum)
