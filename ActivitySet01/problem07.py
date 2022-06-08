# Strings


text = "X-DSPAM-Confidence:0.8475"
n=text.find(':')
a=text[n+1:]
b=float(a)
print(b)
