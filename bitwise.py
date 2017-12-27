#OR turns on third bit
a = 0b10111011

mask = 0b0100
desired = a | mask
print bin(desired)

#XOR flips bits. note that mask is all set to on & is same length as a
a = 0b11101110
mask = 0b11111111
desired = a ^ mask

print bin(desired)

#bit flipper. flips n number of bits & returns bin string result
def flip_bit(number, n):
    mask = (0b1 << n-1)
    result = mask ^ number
    return bin(result)
