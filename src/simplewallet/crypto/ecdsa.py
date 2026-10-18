from typing import Union

class Ecdsa:

	CURVE_ORDER = 0xFFFFFFFF_FFFFFFFF_FFFFFFFF_FFFFFFFE_BAAEDCE6_AF48A03B_BFD25E8C_D0364141
	GENERATOR_POINT = bytes.fromhex('0479be667ef9dcbbac55a06295ce870b07029bfcdb2dce28d959f2815b16f81798'
						'483ada7726a3c4655da4fbfc0e1108a8fd17b448a68554199c47d08ffb10d4b8')
	GENERATOR_POINT_COMPRESSED = bytes.fromhex('0279be667ef9dcbbac55a06295ce870b07029bfcdb2dce28d959f2815b16f81798')

	@classmethod
	def isValid(self, secretbytes: Union[int, bytes]) -> bool:
		if isinstance(secretbytes, bytes):
			secret = int.from_bytes(secretbytes, byteorder='big', signed=False)
		else:
			secret = secretbytes
		return 0 < secret < self.CURVE_ORDER

	@classmethod
	def normalize(self, secretbytes: bytes) -> bytes:
		string_to_number = int.from_bytes(secretbytes, byteorder='big', signed=False)
		scalar = string_to_number % self.CURVE_ORDER
		if scalar == 0:
			raise Exception('invalid EC private key scalar: zero')
		privkey_32bytes = int.to_bytes(scalar, length=32, byteorder='big', signed=False)
		return privkey_32bytes
