def solovay_strassen(n, k=10):
	if n == 2:
		return True
	if not n & 1:
		return False

	def legendre(a, p):
		if p < 2:
			raise ValueError('p must not be < 2')
		if (a == 0) or (a == 1):
			return a
		if a % 2 == 0:
			r = legendre(a / 2, p)
			if p * p - 1 & 8 != 0:
				r *= -1
		else:
			r = legendre(p % a, a)
			if (a - 1) * (p - 1) & 4 != 0:
				r *= -1
		return r

	for i in range(k):
		a = randrange(2, n - 1)
		x = legendre(a, n)
		y = pow(a, (n - 1) / 2, n)
		if (x == 0) or (y != x % n):
			return False

	return True
