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
            tmsg = tmsg + cipher[c]
        else:
            tmsg = tmsg + c
    return tmsg


test = "I come to bury Caesar, not to praise him."
ttest = "F Zljb ql Yrov zXbpXo, klq ql moXfpb efj."
print(transform_message(test, cipher))
print(transform_message(ttest, decoder))
