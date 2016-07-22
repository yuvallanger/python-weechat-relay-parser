#!/usr/bin/env python3

from weechat_relay_parser import (
    Message,
    SignedChar,
    decode_message,
)


def test_decode_message_compression_off():
    message_correct = Message(
         id='poop',
         objects=[
             SignedChar(bytes.fromhex('41'))])
    message_bytes = open('weechat_test_compression_off.data', 'rb').read()
    message_parsed = decode_message(message_bytes)
    assert message_parsed == message_correct


def test_decode_message_compression_6():
    message_correct = Message(
         id='poop',
         objects=[
             SignedChar(bytes.fromhex('41'))])
    message_bytes = open('weechat_test_compression_6.data', 'rb').read()
    message_parsed = decode_message(message_bytes)
    assert message_parsed == message_correct
