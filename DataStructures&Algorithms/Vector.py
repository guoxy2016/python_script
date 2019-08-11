class Vector:
    """Represent a vector in a multidimensional space."""

    def __init__(self, d):
        """Create d-dimensional vector of zeros.
        :param d: dimensional
        """

        if isinstance(d, int):
            self._coords = [0] * d
        elif isinstance(d, (list, tuple)):
            self._coords = list(d)

    def __len__(self):
        """Return the dimension of the vector."""
        return len(self._coords)

    def __getitem__(self, item):
        """Return item-th coordinate of vector."""
        return self._coords[item]

    def __setitem__(self, key, value):
        """Set key-th coordinate of vector to given value."""
        self._coords[key] = value

    def __add__(self, other):
        """Return sum of two vectors."""
        if len(self) != len(other):
            raise ValueError('dimensions must agree')
        result = Vector(len(self))
        for j in range(len(self)):
            result[j] = self[j] + other[j]
        return result

    def __eq__(self, other):
        """Return True if vector has same coordinates as other."""
        return self._coords == other._coords

    def __ne__(self, other):
        """Return True if vector differs from other."""
        return not self == other

    def __str__(self):
        """Produce string representation of vector."""
        return '<' + str(self._coords)[1:-1] + '>'

    def __sub__(self, other):
        if len(self) != len(other):
            raise ValueError('dimensions must agree')
        result = Vector(len(self))
        for j in range(len(self)):
            result[j] = self[j] - other[j]
        return result

    def __neg__(self):
        for i in range(len(self)):
            self[i] *= -1
        return self

    def __mul__(self, other):
        if len(self) != len(other):
            raise ValueError('dimensions must agree')
        result = 0
        for j in range(len(self)):
            result += self[j] * other[j]
        return result

    def __rmul__(self, other):
        return self.__mul__(other)


if __name__ == '__main__':
    v = Vector(5)
    v[1] = 23
    v[-1] = 45
    print(v[4])
    u = v + v
    print(u)
    total = 0
    for entry in v:
        total += entry
    print(v)
    print(-v)

