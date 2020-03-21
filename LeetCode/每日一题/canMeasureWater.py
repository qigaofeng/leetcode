def canMeasureWater( x, y, z):
    """
    :type x: int
    :type y: int
    :type z: int
    :rtype: bool
    """
    import math
    if z == 0 or x == z or y == z or abs(x - y) == z or x + y == z:
        return True
    elif z % math.gcd(x, y) == 0:
        return True
    else:
        return False

if __name__ == '__main__':
    print(canMeasureWater(3,5,4))