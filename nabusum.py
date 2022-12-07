#!/usr/bin/env python3
from pathlib import Path
from struct import pack, unpack
from binascii import hexlify as to_hex, unhexlify as from_hex
import argparse

def main() -> None:
    """
    Easy ROM checksum patcher
    """
    parser = argparse.ArgumentParser('NABU ROM Checksum Calculator')
    parser.add_argument('infile', type=argparse.FileType('rb'),
        help='Binary ROM image')
    parser.add_argument('outfile', type=argparse.FileType('wb'),
        help='Binary ROM image')
    args = parser.parse_args()

    eprom = args.infile.read()
    cksum = sum([i for i in eprom[:-2]]) & 0xFFFF

    args.outfile.write(eprom[:-2])
    args.outfile.write(pack('<H', cksum))

if __name__ == '__main__':
    main()
