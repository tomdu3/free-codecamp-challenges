# Message Decoder

Given a secret message string, and an integer representing the number of letters that were used to shift the message to encode it, return the decoded string.

- A positive number means the message was shifted forward in the alphabet.
- A negative number means the message was shifted backward in the alphabet.
- Case matters, decoded characters should retain the case of their encoded counterparts.
- Non-alphabetical characters should not get decoded.

---

**N.B. This is a Caesar cipher.**
- The shift value will always be between -25 and 25. The elegant solution would be to use the modulo operator to wrap the shift value around, but that is not required for this challenge.
- One other elegant solution, implemented here, is to use the `str.maketrans()` method to create a translation table.