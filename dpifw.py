#!/usr/bin/env python

"""
A stunningly shithouse DPI firewall
"""

import re
import sys

from netfilterqueue import NetfilterQueue

ARMED = True if len(sys.argv) > 1 and sys.argv[1].lower() == "arm" else False
BAD_PATTERNS ={
    "SSH": re.compile(b"SSH-2.0-OpenSSH_.+\r\n$"),
}

def filter(pkt):
    print(f"Analysing packet: {pkt}...", end="")
    for label, pattern in BAD_PATTERNS.items():
        if re.search(pattern, pkt.get_payload()):
            if ARMED:
                print(f"\t*** Detected {label}, blocking!")
                return pkt.drop()
            else:
                print(f"\t*** Detected {label}, but I am disarmed. Letting it through.")
                return pkt.accept()
    print("\tPacket looks clean, letting it through.")
    return pkt.accept()


if __name__ == "__main__":
    state = ARMED and "Armed" or "Disarmed"
    print(f"\n--==] The Stunningly Shithouse DPI Firewall ]==--")
    print(f"     State: {state}. Listening for traffic...\n")
    nfqueue = NetfilterQueue()
    nfqueue.bind(1, filter)
    try:
        nfqueue.run()
    except KeyboardInterrupt:
        print('')
    nfqueue.unbind()
