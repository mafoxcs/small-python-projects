"""sPoNgEcAsE, by Al Sweigart al@inventwithpython.com
Translates English messages into sPOnGEtExT.
View this code at https://nostarch.com/big-book-small-python-projects
Tags: tiny, beginner, word"""

import random

try:
    import pyperclip  # pyperclip copies text to the clipboard.
except ImportError:
    pass  # If pyperclip is not installed, do nothing. It's no big deal.


def main():
    """Run the Spongetext program."""
    print('''sPoNgEcAsE, bY aL sWeIGaRt Al@iNvEnTwItHpYtHoN.cOm

eNtEr YoUr MeSsAgE:''')
    spongetext = englishToSpongecase(input('> '))
    print()
    print(spongetext)

    try:
        pyperclip.copy(spongetext)
        print('(cOpIed SpOnGeTexT to ClIpbOaRd.)')
    except:
        pass  # Do nothing if pyperclip wasn't installed.


def englishToSpongecase(message):
    """Return the spongetext form of the given string."""
    spongetext = ''
    useUpper = False

    for character in message:
        if not character.isalpha():
            spongetext += character
            continue

        if useUpper:
            spongetext += character.upper()
        else:
            spongetext += character.lower()

        # Flip the case, 90% of the time.
        if random.randint(1, 100) <= 90:
            useUpper = not useUpper  # Flip the case.
    return spongetext


# If this program was run (instead of imported), run the game:
if __name__ == '__main__':
    main()
