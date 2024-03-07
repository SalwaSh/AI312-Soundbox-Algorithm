def soundex(name):
    # Step 1: Keep the first letter of the name
    soundex_code = name[0].upper()

    # Step 2: Replace letters with their corresponding numbers
    mapping = {
        'AEIOUHWY': '',
        'BFPV': '1',
        'CGJKQSXZ': '2',
        'DT': '3',
        'L': '4',
        'MN': '5',
        'R': '6'
    }
    for letter in name[1:]:
        letter = letter.upper()
        for key, value in mapping.items():
            if letter in key:
                soundex_code += value
                break

    # Step 3: Remove sequences of identical numbers
    cleaned_code = ''
    prev_digit = ''
    for digit in soundex_code:
        if digit != prev_digit:
            cleaned_code += digit
        prev_digit = digit

    # Step 4: Convert to the form Letter Digit Digit Digit
    soundex_code = cleaned_code.ljust(4, '0')[:4]

    return soundex_code
