# Akai Pro MIDI Mix MIDI code layout

All values are in hexademical.

## Control IDs as they appear on the controller

```text
10 14 18 1C 2E 32 36 3A
11 15 19 1D 2F 33 37 3B   19
12 16 1A 1E 30 34 38 3C   1A

01 04 07 0A 0D 10 13 16   1B
03 06 09 0C 0F 12 15 18

13 17 1B 1F 31 35 39 3D   3E
```

### "SOLO" buttons

If a MUTE button is pressed while the SOLO button is held down, the code changes (increased by one):

```text
02 05 08 0B 0E 11 14 17
```

## Events

### Knobs and faders

Fader changes are reported as: `B0 <knob> <value>`

### Buttons

"SEND ALL" sends all the values to the MIDI output and does not send a MIDI message.

- `90 <button> 7F` is for pressing the button
- `80 <button> 7F` is for releasing the button

## Controlling the LEDs

Button LEDs are controlled with:

- Send `90 <button> 7F` to turn it on
- Send `90 <button> 00` to turn it off
