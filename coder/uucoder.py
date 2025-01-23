class UUCoder:
    @staticmethod
    def encode(barr):
        rtn = []
        len_barr = len(barr)
        read = 0
        stop = False
        offset = 0

        while not stop:
            left = len_barr - read
            if left == 0:
                stop = True

            b = left if left <= 45 else 45

            rtn.append(UUCoder._enc(b))
            for i in range(0, b, 3):
                if len_barr - offset < 3:
                    padding = bytearray(3)
                    for z in range(len_barr - offset):
                        padding[z] = barr[offset + z]
                    UUCoder.encode_bytes(padding, 0, rtn)
                else:
                    UUCoder.encode_bytes(barr, offset, rtn)
                offset += 3

            rtn.append('\n')
            read += b
            if b < 45:
                stop = True

        return ''.join(rtn)

    @staticmethod
    def decode(str):
        out = bytearray(len(str))
        len_out = 0
        offset = 0
        stop = False
        it = iter(str)

        while not stop:
            b = UUCoder._dec(next(it))
            b1 = next(it)
            if b > 45:
                raise ValueError(f"can't decode string [{str}]")
            if b < 45:
                stop = True
            len_out += b

            while b > 0:
                UUCoder.decode_chars(it, out, offset, b1)
                b1 = next(it, None)
                offset += 3
                b -= 3
        return bytes(out[:len_out])

    @staticmethod
    def encode_bytes(in_bytes, off, out):
        out.append(UUCoder._enc(in_bytes[off] >> 2))
        out.append(UUCoder._enc((in_bytes[off] << 4 & 0x30) | (in_bytes[off + 1] >> 4 & 0xf)))
        out.append(UUCoder._enc((in_bytes[off + 1] << 2 & 0x3c) | (in_bytes[off + 2] >> 6 & 3)))
        out.append(UUCoder._enc(in_bytes[off + 2] & 0x3f))

    @staticmethod
    def decode_chars(it, out, off, b1):
        b1 = UUCoder._dec(b1)
        b2 = UUCoder._dec(next(it))
        b3 = UUCoder._dec(next(it))
        b4 = UUCoder._dec(next(it))
        out[off] = (b1 << 2 | b2 >> 4) & 0xff
        out[off + 1] = (b2 << 4 | b3 >> 2) & 0xff
        out[off + 2] = (b3 << 6 | b4) & 0xff

    @staticmethod
    def _enc(c):
        return chr((c & 0x3f) + 32)

    @staticmethod
    def _dec(c):
        return (ord(c) - 32) & 0x3f
