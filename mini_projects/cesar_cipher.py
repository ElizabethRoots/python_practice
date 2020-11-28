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
        self.shift = -3
        self.letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
        self.cipher = {self.letters[i]: self.letters[(
            i-self.shift) % len(self.letters)] for i in range(len(self.letters))}
        self.decoder = {self.letters[i]: self.letters[(
            i+3) % len(self.letters)] for i in range(len(self.letters))}

    def transform_message(self, message, cipher):
        """
        Transforms a message using the specified cipher.  Is not called by users directly,
        and can be called with either the cipher (to encrypt) or the decoder (to decode).
        """
        result = ''
        for letter in message:
            if letter in cipher:
                result = result + cipher[letter]
            else:
                result = result + letter
        return result

    def encrypt(self, message):
        """
        Transforms a message using the cipher, by calling self.transform_message
        """
        return self.transformMessage(message, cipher)

    def decode(self, message):
        """
        Transforms a message using the decoder, by calling self.transform_message
        """
        return self.transformMessage(message, decoder)


test = "I come to bury Caesar, not to praise him."

encShift = shift = -3

c0 = ShiftCipher(0)
print("--c0--")
print(c0.cipher)

m3 = ShiftCipher(-3)
print("--m3--")
print(m3.cipher)

p13 = ShiftCipher(13)
print("--p13--")
print(p13.cipher)
