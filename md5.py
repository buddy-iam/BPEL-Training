import struct

S = [
    7, 12, 17, 22,  7, 12, 17, 22,  
    7, 12, 17, 22,  7, 12, 17, 22,
    5,  9, 14, 20,  5,  9, 14, 20,  
    5,  9, 14, 20,  5,  9, 14, 20,
    4, 11, 16, 23,  4, 11, 16, 23,  
    4, 11, 16, 23,  4, 11, 16, 23,
    6, 10, 15, 21,  6, 10, 15, 21,  
    6, 10, 15, 21,  6, 10, 15, 21
]

K = [
    0xd76aa478, 0xe8c7b756, 0x242070db, 0xc1bdceee, 0xf57c0faf, 0x4787c62a, 0xa8304613, 0xfd469501,
    0x698098d8, 0x8b44f7af, 0xffff5bb1, 0x895cd7be, 0x6b901122, 0xfd987193, 0xa679438e, 0x49b40821,
    0xf61e2562, 0xc040b340, 0x265e5a51, 0xe9b6c7aa, 0xd62f105d, 0x02441453, 0xd8a1e681, 0xe7d3fbc8,
    0x21e1cde6, 0xc33707d6, 0xf4d50d87, 0x455a14ed, 0xa9e3e905, 0xfcefa3f8, 0x676f02d9, 0x8d2a4c8a,
    0xfffa3942, 0x8771f681, 0x6d9d6122, 0xfde5380c, 0xa4beea44, 0x4bdecfa9, 0xf6bb4b60, 0xbebfbc70,
    0x289b7ec6, 0xeaa127fa, 0xd4ef3085, 0x04881d05, 0xd9d4d039, 0xe6db99e5, 0x1fa27cf8, 0xc4ac5665,
    0xf4292244, 0x432aff97, 0xab9423a7, 0xfc93a039, 0x655b59c3, 0x8f0ccc92, 0xffeff47d, 0x85845dd1,
    0x6fa87e4f, 0xfe2ce6e0, 0xa3014314, 0x4e0811a1, 0xf7537e82, 0xbd3af235, 0x2ad7d2bb, 0xeb86d391
]

def left_rotate(x, amount):
   x &=0xFFFFFFFF
   return ((x<<amount) | (x >> (32 -  amount))) & 0xFFFFFFFF
def md5(message):
   message = bytearray(message)
   original_byte_len= len(message)
   original_bit_len= original_byte_len*8
   message.append(0x80)
   while len(message) % 64 != 56 :
      message.append(0)

   message += struct.pack('<Q', original_bit_len)

   A = 0x67452301
   B = 0xefcdab89
   C = 0x98badcfe
   D = 0x10325476

   for chunck_offset in range(0, len(message), 64):
      chunck = message[chunck_offset:chunck_offset + 64]
      M = list(struct.unpack('<16I', chunck))

      a,b,c,d= A, B, C, D

      for i in range(64):
         if 0 <= i <= 15:
            F = ( b & c ) | ( ~b & d )
            g = i
         elif 16 <= i <= 31:
            F = (d & b) | (~d & c)
            g = (5 * i + 1) % 16
         elif 32 <= i <= 47:
            F = b ^ c ^ d
            g = ( 3 * i + 5 ) % 16
         else:
            F = c ^ (b | ~d)
            g = ( 7 * i) % 16

         F = (F + a + K[i] + M[g] ) & 0xFFFFFFFF
         a = d
         d = c
         c = b
         b = (b + left_rotate(F, S[i])) & 0xFFFFFFFF
      
      A = (A + a) & 0xFFFFFFFF
      B = (B + b) & 0xFFFFFFFF
      C = (C + c) & 0xFFFFFFFF
      D = (D + d) & 0xFFFFFFFF
   return '{:08x}{:08x}{:08x}{:08x}'.format(A, B, C, D)

input_string = "QWENDBV45657"
hash_result = md5(input_string.encode())
print(f"MD5 hash of '{input_string}' : {hash_result}")