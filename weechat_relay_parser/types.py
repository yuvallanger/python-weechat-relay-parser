#!/usr/bin/env python3

from typing import (
    Sequence,
    Dict,
)

import bitstring


class Object(object):
    pass


class SignedChar(Object):
    def __init__(self, data: bitstring.Bits) -> None:
        self.data = bitstring.Bits

    def __str__(self) -> str:
        return self.data.unpack('bytes:1').decode()

    def as_int(self) -> int:
        return self.data.unpack('int:8')


class SignedInt(Object):
    def __init__(self, data: bitstring.Bits) -> None:
        self.data = bitstring.Bits

    def __str__(self) -> str:
        return self.data.unpack('bytes:1').decode()

    def as_int(self) -> int:
        return self.data.unpack('int:8')
    pass


class SignedLongInt(Object):
    def __init__(self, data: int) -> None:
        self.data = data

    def __str__(self) -> str:
        return str(self.data)


class String(Object):
    def __init__(self, data: str) -> None:
        self.data = data

    def __str__(self) -> str:
        return self.data


class Buffer(Object):
    def __init__(self, data: bytes) -> None:
        self.data = data

    def __str__(self) -> str:
        return str(self.data)


class Pointer(Object):
    def __init__(self, data: int) -> None:
        self.data = data

    def __str__(self):
        return hex(self.data)


class Time(Object):
    def __init__(self, data: int) -> None:
        self.data = data

    def __str__(self):
        return hex(self.data)


class HashTable(Object):
    def __init__(self, data: Dict[Object, Object]) -> None:
        self.data = data

class HData(Object):
    def __init__(self, data: Dict[Object, Object]) -> None:
        self.data = data


class Info(Object):
    def __init__(self, data: Dict[Object, Object]) -> None:
        self.data = data


class InfoList(Object):
    def __init__(self, data: Dict[Object, Object]) -> None:
        self.data = data


class Array(Object):
    def __init__(self, data: Dict[Object, Object]) -> None:
        self.data = data


class Message(object):
    def __init__(self, id: str, objects: Sequence[Object]) -> None:
        self.id = id
        self.objects = objects
