## Bitwise Operations

1. AND (&): Only true if both input bits are true
2. OR (|): True if either of the input bits is true
3. XOR (^): True iff one input bit is true. i.e., if bits are different then 1, same then 0.
4. NOT (~): One's complement operator: flips the input bit
- LEFT SHIFT (<<)
    
    Shifts the binary digits to the left by $n$and pads zeros on the right. Same as multiplying by 2. Does not wrap around. eg: 00010110 << 2 = 01011000
    
- RIGHT SHIFT (>>)
    
    Shifts the binary digits by n, pad 0s on the left. Same as dividing by 2 with round towards -infinity.
    

## Bit Manipulation Basics

- Set Bit (setting bit at a position to 1)
    
    ```jsx
    def set_bit(x, position):
        mask = 1 << position
        return x | mask
    
    ###
    eg: x = 00000110
    position = 00000101 (5)
    mask = 1 << 5 = 00100000
    x | mask = 00100110
    ###
    ```
    
- Clear bit(setting bit at a position to 0)
    
    ```jsx
    def clear_bit(x, position):
        mask = 1 << position
        return x & ~mask
    
    eg: x = 00000110
    position = 00000010
    mask = 00000100
    ~mask = 11111011
    x & ~mask = 00000010
    ```
    
- Flip bit (flipping bit at a position)
    
    ```jsx
    def flip_bit(x, position):
        mask = 1 << position
        return x ^ mask
    ```
    
- Checking if bit is set (if it has value 1)
    
    ```jsx
    def is_bit_set(x, position):
        shifted = x >> position
        return shifted & 1
    The right shift pushes the concerned bit to the rightmost edge, where
    we do & with 1 to see what its value is.
    eg: x = 01100110
    position = 00000101
    shifted = 00000011
    shifted & 1 = 00000001
    ```
    
- Modify bit (not very important)
    
    ```jsx
    def modify_bit(x, position, state):
        mask = 1 << position
        return (x & ~mask) | (-state & mask)
    ```
    

## Bit Tricks

- How to check if number is even?
    
    ```jsx
    def check_even(x):
        return x & 1
    ```
    
- How to check if number is power of 2?
    
    ```jsx
    def check_two(x):
    return x & x-1
    ```
    
- What is ones complement? Convert all 0 to 1 and 1 to 0
    
- What is twos complement?
    
    Convert all 0 to 1 and 1 to 0, then add 1
    
- How to count number of set bits?
    
    ```jsx
    unsigned int countSetBits(int n)
    {
        unsigned int count = 0;
        while (n) {
            n &= (n - 1);
            count++;
        }
        return count;
    }
    ```