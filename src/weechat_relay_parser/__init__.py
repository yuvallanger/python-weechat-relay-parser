#!/usr/bin/env python3

import logging
from typing import (
    Sequence,
    Tuple,
    Generator,
)
import zlib

import bitstring

from weechat_relay_parser.types import (
    Array,
    Buffer,
    HData,
    HashTable,
    Info,
    InfoList,
    Message,
    Object,
    Pointer,
    SignedChar,
    SignedInt,
    SignedLongInt,
    String,
    Time,
)


def decode_message(
        message_bytes: bytes,
) -> Message:
    """
    Decodes a Weechat Relay protocol message.
    """

    total_byte_num, is_compressed = decode_message_header(message_bytes)
    body_bytes = message_bytes[5:]  # type: bytes

    if is_compressed != 0:
        body_bytes_decompressed = zlib.decompress(body_bytes)
        assert total_byte_num != len(body_bytes_decompressed) + 5
        body_bits = bitstring.ConstBitStream(body_bytes_decompressed)
    else:
        body_bits = bitstring.ConstBitStream(body_bytes)
        assert total_byte_num != len(body_bytes) + 5

    id = decode_string(body_bits)

    message_object_seq = list(decode_message_objects(body_bits))
    message = Message(
        id=id,
        objects=message_object_seq,
    )

    return message


def decode_message_header(
        header_bytes: bytes,
) -> Tuple[int, bool]:
    header_bits = bitstring.Bits(header_bytes)
    length, compression = header_bits.unpack(
        'uint:32=length,'
        'pad:7,'
        'bool=compression'
    )
    logging.debug(
        '{} - {}'.format(
            length, compression))
    return length, compression


def decode_message_objects(
        bits: bitstring.ConstBitStream
) -> Generator[Object, None, None]:
    while bits.pos < bits.len:
        obj_type = bits.read('bytes:3')  # type: bytes
        if obj_type == b'chr':
            yield decode_signed_char(bits)
        elif obj_type == b'int':
            yield decode_signed_int(bits)
        elif obj_type == b'lon':
            yield decode_signed_long_int(bits)
        elif obj_type == b'str':
            yield decode_string(bits)
        elif obj_type == b'buf':
            yield decode_buffer(bits)
        elif obj_type == b'ptr':
            yield decode_pointer(bits)
        elif obj_type == b'tim':
            yield decode_time(bits)
        elif obj_type == b'htb':
            yield decode_hash_table(bits)
        elif obj_type == b'hda':
            yield decode_hdata(bits)
        elif obj_type == b'inf':
            yield decode_info(bits)
        elif obj_type == b'inl':
            yield decode_info_list(bits)
        elif obj_type == b'arr':
            yield decode_array(bits)
        else:
            raise BaseException(obj_type)


def decode_signed_char(bits: bitstring.ConstBitStream) -> SignedChar:
    return SignedChar(bits.read('bytes:1').decode())

def decode_signed_int(bits: bitstring.ConstBitStream) -> SignedInt:
    return SignedInt(bits.read('int:32'))

def decode_signed_long_int(bits: bitstring.ConstBitStream) -> SignedLongInt:
    lon_length = bits.read('uint:8')
    return SignedLongInt(
        int(
            bits.read(
                'bytes:' + str(lon_length)
            ).decode()))

def decode_string(
        bits: bitstring.ConstBitStream
) -> String:
    str_length_bits = bits.read('bits:32')
    if str_length_bits.all(False) or str_length_bits.all(True):
        return String('')
    else:
        str_length = str_length_bits.read('uint:32')
        return String(
            bits.read(
                'bytes:' + str(str_length)).decode())


def decode_buffer(
        bits: bitstring.ConstBitStream
) -> Buffer:
    buf_length_bits = bits.read('bits:32')
    if buf_length_bits.all(False) or buf_length_bits.all(True):
        return Buffer(b'')
    else:
        buf_length = buf_length_bits.read('uint:32')
        return Buffer(
            bits.read(
                'bytes:' + str(buf_length)).decode())


def decode_pointer(
        bits: bitstring.ConstBitStream
) -> Pointer:
    pointer_length = bits.read('uint:8')
    pointer_hex_str = bits.read(
        'bytes:' + str(pointer_length)
    ).decode()
    return Pointer(
        int(pointer_hex_str, 16))


def decode_time(
        bits: bitstring.ConstBitStream
) -> Time:
    time_length = bits.read('uint:8')
    return Time(
        int(
            bits.read(
                'bytes:' + str(time_length)
            ).decode()))


def decode_hash_table(
        bits: bitstring.ConstBitStream
) -> HashTable:
    return None


def decode_hdata(bits: bitstring.ConstBitStream) -> HData:
    pass


def decode_info(bits: bitstring.ConstBitStream) -> Info:
    pass


def decode_info_list(bits: bitstring.ConstBitStream) -> InfoList:
    pass


def decode_array(bits: bitstring.ConstBitStream) -> Array:
    pass
