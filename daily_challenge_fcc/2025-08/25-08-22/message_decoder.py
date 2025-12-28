def decode(message, shift):
    """Decode a Caesar cipher message by reversing the shift"""
    lower_alphabet = 'abcdefghijklmnopqrstuvwxyz'
    upper_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    
    # Create the shifted (encrypted) alphabet
    shifted_lower = lower_alphabet[shift:] + lower_alphabet[:shift]
    shifted_upper = upper_alphabet[shift:] + upper_alphabet[:shift]
    
    # For DECODING: map FROM shifted alphabet TO original alphabet
    table = str.maketrans(shifted_lower + shifted_upper, 
                         lower_alphabet + upper_alphabet)
    
    return message.translate(table)