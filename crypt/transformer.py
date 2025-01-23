class Transformer:
    def __init__(self):
        self.m_Key = ""
        self.m_LFSR_A = 0x13579bdf
        self.m_LFSR_B = 0x2468ace0
        self.m_LFSR_C = 0xfdb97531
        self.m_Mask_A = 0x80000062
        self.m_Mask_B = 0x40000020
        self.m_Mask_C = 0x10000002
        self.m_Rot0_A = 0x7fffffff
        self.m_Rot0_B = 0x3fffffff
        self.m_Rot0_C = 0xfffffff
        self.m_Rot1_A = 0x80000000
        self.m_Rot1_B = 0xc0000000
        self.m_Rot1_C = 0xf0000000

    def transform_string(self, key, in_bytes):
        self.set_key(key)
        length = len(in_bytes)
        out_bytes = bytearray(length)
        for i in range(length):
            out_bytes[i] = self.transform_byte(in_bytes[i])
        return out_bytes

    def transform_byte(self, target):
        crypto = 0
        b = self.m_LFSR_B & 1
        c = self.m_LFSR_C & 1
        for _ in range(8):
            if self.m_LFSR_A & 1 != 0:
                self.m_LFSR_A = (self.m_LFSR_A ^ (self.m_Mask_A >> 1)) | self.m_Rot1_A
                if self.m_LFSR_B & 1 != 0:
                    self.m_LFSR_B = (self.m_LFSR_B ^ (self.m_Mask_B >> 1)) | self.m_Rot1_B
                    b = 1
                else:
                    self.m_LFSR_B = (self.m_LFSR_B >> 1) & self.m_Rot0_B
                    b = 0
            else:
                self.m_LFSR_A = (self.m_LFSR_A >> 1) & self.m_Rot0_A
                if self.m_LFSR_C & 1 != 0:
                    self.m_LFSR_C = (self.m_LFSR_C ^ (self.m_Mask_C >> 1)) | self.m_Rot1_C
                    c = 1
                else:
                    self.m_LFSR_C = (self.m_LFSR_C >> 1) & self.m_Rot0_C
                    c = 0
            crypto = (crypto << 1) | (b ^ c)
        out = target
        out ^= crypto
        return out

    def set_key(self, key):
        self.m_Key = key
        local_key = key if key else "Default Seed"
        seed = list(local_key) + [local_key[i % len(local_key)] for i in range(12 - len(local_key))]
        for i in range(4):
            self.m_LFSR_A = (self.m_LFSR_A << 8) | ord(seed[i + 4])
            self.m_LFSR_B = (self.m_LFSR_B << 8) | ord(seed[i + 4])
            self.m_LFSR_C = (self.m_LFSR_C << 8) | ord(seed[i + 4])
        if self.m_LFSR_A == 0:
            self.m_LFSR_A = 0x13579bdf
        if self.m_LFSR_B == 0:
            self.m_LFSR_B = 0x2468ace0
        if self.m_LFSR_C == 0:
            self.m_LFSR_C = 0xfdb97531
