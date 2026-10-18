def inv_dict(d):
	return {v: k for k, v in d.items()}

def assert_bytes(*args):
	try:
		for x in args:
			assert isinstance(x, (bytes, bytearray))
	except:
		raise TypeError("Failed to determine type")

def to_bytes(obj, encoding='utf8') -> bytes:
	if isinstance(obj, bytes):
		return obj
	if isinstance(obj, str):
		return obj.encode(encoding)
	elif isinstance(obj, bytearray):
		return bytes(obj)
	else:
		raise TypeError("Not a string or bytes like object")

def powbase2(data, frombits, tobits, pad=True):
	# General power-of-2 base conversion.
	acc = 0
	bits = 0
	ret = []
	maxv = (1 << tobits) - 1
	max_acc = (1 << (frombits + tobits - 1)) - 1
	for value in data:
		if value < 0 or (value >> frombits):
			return None
		acc = ((acc << frombits) | value) & max_acc
		bits += frombits
		while bits >= tobits:
			bits -= tobits
			ret.append((acc >> bits) & maxv)
	if pad:
		if bits:
			ret.append((acc << (tobits - bits)) & maxv)
	elif bits >= frombits or ((acc << (tobits - bits)) & maxv):
		return None
	return ret
