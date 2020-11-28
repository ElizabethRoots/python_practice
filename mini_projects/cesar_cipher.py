'''
1. Encrypt the string in 'test'
2. Decrypt the string in 'ttest'
--consider punctuation or characters not in the 'letters' list
'''
letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
cipher = {letters[i]: letters[(i-3) % len(letters)]
          for i in range(len(letters))}
decoder = {letters[i]: letters[(i+3) % len(letters)]
           for i in range(len(letters))}


def transform_message(message, cipher):
    tmsg = ''
    for c in message:
        if c in cipher:
            tmsg = tmsg + cipher[c]  # tmsg = tmsg + cipher.get(c, c)
        else:
            tmsg = tmsg + c
    return tmsg


test = "I come to bury Caesar, not to praise him."
ttest = "F Zljb ql Yrov zXbpXo, klq ql moXfpb efj."
print(transform_message(test, cipher))
print(transform_message(ttest, decoder))

# ------------------------------------------------


class ShiftCipher:
    """
    ShiftCipher objects that can encrypt and decode text messages based on a specific shift length.
    """

    def __init__(self, shift):
        """
        Constructs a ShiftCipher for the specified degree of shift (positive or negative),
        by building a cipher (dictionary mapping from letters to other letters), and 
        a decoder (the inverse of the cipher)
        """
        self.shift = shift
        self.letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
        self.cipher = {self.letters[i]: self.letters[(
            i + self.shift) % len(self.letters)] for i in range(len(self.letters))}
        self.decoder = {self.letters[i]: self.letters[(
            i + (self.shift - self.shift)) % len(self.letters)] for i in range(len(self.letters))}

    def transform_message(self, message, code_cipher):
        """
        Transforms a message using the specified cipher.  Is not called by users directly,
        and can be called with either the cipher (to encrypt) or the decoder (to decode).
        """
        result = ''
        for letter in message:
            if letter in code_cipher:
                result = result + code_cipher.get(letter, letter)
            else:
                result = result + letter
        return result

        tmsg = ''
        for c in message:
            tmsg = tmsg + cipher.get(c, c)
        return tmsg

    def encrypt(self, message):
        """
        Transforms a message using the cipher, by calling self.transform_message
        """
        return self.transform_message(test, self.cipher)

    def decode(self, message):
        """
        Transforms a message using the decoder, by calling self.transform_message
        """
        return self.transform_message(test, self.decoder)


# sample sentence
test = "I come to bury Caesar, not to praise him."

# code a message by no shift spaces
print("--c0--")
c0 = ShiftCipher(0)
c0_coded_message = c0.encrypt(test)
print("Coded c0", c0_coded_message)
c0_decoded_message = c0.decode(c0_coded_message)
print("Decoded c0", c0_decoded_message)
print(" ")

# code a message by 3 shift spaces
print("--m3--")
m3 = ShiftCipher(-3)
m3_coded_message = m3.encrypt(test)
print("Coded m3", m3_coded_message)
m3_decoded_message = m3.decode(m3_coded_message)
print("Decoded m3", m3_decoded_message)
print(" ")

# code a message by 13 shift spaces
print("--p13--")
p13 = ShiftCipher(13)
p13_coded_message = p13.encrypt(test)
print("Coded p13", p13_coded_message)
p13_decoded_message = p13.decode(p13_coded_message)
print("Decoded p13", p13_decoded_message)
print(" ")

# test that both encrypt and decode functions work
print("--sanity test--")
if test == p13.decode(p13.encrypt(test)):
    print("decoding worked")
