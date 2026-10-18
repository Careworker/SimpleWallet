from .base import Base
from .ripemd import Ripemd
from .sha256 import Sha256

class Hash160:

	@classmethod
	def hash(self, x: bytes) -> bytes:
		return Ripemd.hash(Sha256.hash(x))

	@classmethod
	def hash160_to_b58_address(self, h160: bytes, addrtype: int) -> str:
		s = bytes([addrtype]) + h160
		s = s + Sha256.hashd(s)[0:4]
		return Base.encode(s, base=58)
