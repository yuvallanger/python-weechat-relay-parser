#!/usr/bin/env python3

from typing import (  # noqa: F401
    Sequence,
    Dict,
    NamedTuple,
    NewType,
    Any,
)

import bitstring


class SignedChar(NamedTuple):
    def __init__(self, data: bitstring.Bits) -> None:
        self.data = bitstring.Bits

    def __str__(self) -> str:
        return self.data.unpack('bytes:1').decode()

    def as_int(self) -> int:
        return self.data.unpack('int:8')


class SignedInt(NamedTuple):
    def __init__(self, data: bitstring.Bits) -> None:
        self.data = bitstring.Bits

    def __str__(self) -> str:
        return self.data.unpack('bytes:1').decode()

    def as_int(self) -> int:
        return self.data.unpack('int:8')
    pass


class SignedLongInt(NamedTuple):
    def __init__(self, data: int) -> None:
        self.data = data

    def __str__(self) -> str:
        return str(self.data)


class String(NamedTuple):
    def __init__(self, data: str) -> None:
        self.data = data

    def __str__(self) -> str:
        return self.data


class Buffer(NamedTuple):
    def __init__(self, data: bytes) -> None:
        self.data = data

    def __str__(self) -> str:
        return str(self.data)


class Pointer(NamedTuple):
    def __init__(self, data: int) -> None:
        self.data = data

    def __str__(self):
        return hex(self.data)


class Time(NamedTuple):
    def __init__(self, data: int) -> None:
        self.data = data

    def __str__(self):
        return hex(self.data)


class HashTable(NamedTuple):
    def __init__(self, data: Dict[Any, Any]) -> None:
        self.data = data


class HData(NamedTuple):
    def __init__(self, data: Dict[Any, Any]) -> None:
        self.data = data


class Info(NamedTuple):
    def __init__(self, data: Dict[Any, Any]) -> None:
        self.data = data


class InfoList(NamedTuple):
    def __init__(self, data: Dict[Any, Any]) -> None:
        self.data = data


class Array(NamedTuple):
    def __init__(self, data: Dict[Any, Any]) -> None:
        self.data = data


class Message(object):
    def __init__(self, id: str, objects: Sequence[Any]) -> None:
        self.id = id
        self.objects = objects
