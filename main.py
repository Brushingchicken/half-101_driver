basic.show_leds("""
    # # # . .
    # . . . .
    . . . . .
    . . . . .
    # . . . .
    """)

def on_forever():
    if pins.digital_read_pin(DigitalPin.P5) == 0 and pins.digital_read_pin(DigitalPin.P6) == 0:
        pins.analog_write_pin(AnalogPin.P1, 0)
        pins.analog_write_pin(AnalogPin.P8, 0)
    elif pins.digital_read_pin(DigitalPin.P5) == 0 and pins.digital_read_pin(DigitalPin.P6) == 1:
        pins.analog_write_pin(AnalogPin.P1, 0)
        pins.analog_write_pin(AnalogPin.P8, 0)
    elif pins.digital_read_pin(DigitalPin.P5) == 1 and pins.digital_read_pin(DigitalPin.P6) == 0:
        pins.analog_write_pin(AnalogPin.P1, 0)
        pins.analog_write_pin(AnalogPin.P8, 0)
    elif pins.digital_read_pin(DigitalPin.P5) == 1 and pins.digital_read_pin(DigitalPin.P6) == 1:
        pins.analog_write_pin(AnalogPin.P1, 0)
        pins.analog_write_pin(AnalogPin.P8, 0)
    else:
        pins.analog_write_pin(AnalogPin.P1, 0)
        pins.analog_write_pin(AnalogPin.P8, 0)
basic.forever(on_forever)
