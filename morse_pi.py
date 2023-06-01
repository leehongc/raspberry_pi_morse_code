# tutorial on gpio: https://dev.to/halcolo/morse-code-in-raspberry-pi-1h9b

import RPi.GPIO as GPIO
import time

'''
1. The length of a dot is 1 unit
2. A dash is 3 units
3. The space between parts of the same letter is 1 unit
4. The space between letters is 3 units
5. The space between words is 7 units
'''
morse_dict = {
    'A':'.-',
    'B':'-...',
    'C':'-.-.',
    'D':'-..',
    'E':'.',
    'F':'..-.',
    'G':'--.',
    'H':'....',
    'I':'..',
    'J':'.---',
    'K':'-.-',
    'L':'.-..',
    'M':'--',
    'N':'-.',
    'O':'---',
    'P':'.--.',
    'Q':'--.-',
    'R':'.-.',
    'S':'...',
    'T':'-',
    'U':'..-',
    'V':'...-',
    'W':'.--',
    'X':'-..-',
    'Y':'-.--',
    'Z':'--..',
    '0':'-----',
    '1':'.----',
    '2':'..---',
    '3':'...--',
    '4':'....-',
    '5':'.....',
    '6':'-....',
    '7':'--...',
    '8':'---..',
    '9':'----.',
    ' ':'....'
}

def led_control(sleep_time):
    GPIO.output(PIN, GPIO.HIGH)
    time.sleep(sleep_time)
    GPIO.output(PIN, GPIO.LOW)

def word_to_morse():
    # GPIO settings
    PIN = 7
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(PIN, GPIO.OUT)

    # converting user_input to morse
    user_input = input('Enter a word or words').strip().upper()
    for letter in user_input:
        morse_code = morse_dict[letter]
        for character in morse_code:
            if character == '.':
                led_control(0.2)
                print('0.2')
            else:
                led_control(0.6)
                print('0.6')
        led_control(1.4)
        print('1.4')
        
    GPIO.cleanup()


if __name__ == '__main__':
    word_to_morse()