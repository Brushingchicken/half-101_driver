basic.showLeds(`
    # # # . .
    # . . . .
    . . . . .
    . . . . .
    # . . . .
    `)
basic.forever(function () {
    if (pins.digitalReadPin(DigitalPin.P5) == 0 && pins.digitalReadPin(DigitalPin.P6) == 0) {
        pins.analogWritePin(AnalogPin.P1, 0)
        pins.analogWritePin(AnalogPin.P8, 0)
    } else if (pins.digitalReadPin(DigitalPin.P5) == 0 && pins.digitalReadPin(DigitalPin.P6) == 1) {
        pins.analogWritePin(AnalogPin.P1, 0)
        pins.analogWritePin(AnalogPin.P8, 0)
    } else if (pins.digitalReadPin(DigitalPin.P5) == 1 && pins.digitalReadPin(DigitalPin.P6) == 0) {
        pins.analogWritePin(AnalogPin.P1, 0)
        pins.analogWritePin(AnalogPin.P8, 0)
    } else if (pins.digitalReadPin(DigitalPin.P5) == 1 && pins.digitalReadPin(DigitalPin.P6) == 1) {
        pins.analogWritePin(AnalogPin.P1, 0)
        pins.analogWritePin(AnalogPin.P8, 0)
    } else {
    	
    }
})
