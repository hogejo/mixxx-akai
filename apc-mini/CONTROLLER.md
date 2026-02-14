# Akai Pro APC Mini MK2 MIDI code layout

All values are in hexadecimal. See also the official
[Akai documentation](https://cdn.inmusicbrands.com/akai/attachments/APC%20mini%20mk2%20-%20Communication%20Protocol%20-%20v1.0.pdf).

## Control IDs as they appear on the controller

There are 64 pads, numbered from the bottom left. The track and scene lunch buttons are numbered after those. The faders
are numbered from left to right.

```text
38 39 3A 3B 3C 3D 3E 3F   70
30 31 32 33 34 35 36 37   71
28 29 2A 2B 2C 2D 2E 2F   72
20 21 22 23 24 25 26 27   73
18 19 1A 1B 1C 1D 1E 1F   74
10 11 12 13 14 15 16 17   75
08 09 0A 0B 0C 0D 0E 0F   76
00 01 02 03 04 05 06 07   77

64 65 66 67 68 69 6A 6B   7A

30 31 32 33 34 35 36 37   38
```

## Events

### Pads and buttons

- `90 <button> 7F` is for pressing the button
- `80 <button> 00` is for releasing the button

### Faders

Fader changes are reported as: `B0 <fader> <value>`

## Controlling the LEDs

### Buttons

Buttons support their own single colour only, but they support blinking.

```text
90 <button> <mode>
```

Mode can be:

- `00` for LED off
- `01` and `03-7F` for LED on
- `02` for LED blinking

The SHIFT button has no LED.

### Pads

#### Single pad control

`<mode> <pad> <colour>` sets a pad's colour.

Available modes:

- `90` for On 10% brightness
- `91` for On 25% brightness
- `92` for On 50% brightness
- `93` for On 65% brightness
- `94` for On 75% brightness
- `95` for On 90% brightness
- `96` for On 100% brightness
- `97` for Pulsing 1/16
- `98` for Pulsing 1/8
- `99` for Pulsing 1/4
- `9A` for Pulsing 1/2
- `9B` for Blinking 1/24
- `9C` for Blinking 1/16
- `9D` for Blinking 1/8
- `9E` for Blinking 1/4
- `9F` for Blinking 1/2

NOTE: Pulsing (any speed) or fast blinking *more than ~40 pads* will cause artifacts and will cause the device to stop
accepting MIDI messages.

See above for pad numbering. See below for built-in colours.
See below for custom colour mode, that supports setting multiple pads at once.

## Built-in colours

Akai has provided the following built-in colours:

- `0x00` (0) for `#000000`
- `0x01` (1) for `#1E1E1E`
- `0x02` (2) for `#7F7F7F`
- `0x03` (3) for `#FFFFFF`
- `0x04` (4) for `#FF4C4C`
- `0x05` (5) for `#FF0000`
- `0x06` (6) for `#590000`
- `0x07` (7) for `#190000`
- `0x08` (8) for `#FFBD6C`
- `0x09` (9) for `#FF5400`
- `0x0A` (10) for `#591D00`
- `0x0B` (11) for `#271B00`
- `0x0C` (12) for `#FFFF4C`
- `0x0D` (13) for `#FFFF00`
- `0x0E` (14) for `#595900`
- `0x0F` (15) for `#191900`
- `0x10` (16) for `#88FF4C`
- `0x11` (17) for `#54FF00`
- `0x12` (18) for `#1D5900`
- `0x13` (19) for `#142B00`
- `0x14` (20) for `#4CFF4C`
- `0x15` (21) for `#00FF00`
- `0x16` (22) for `#005900`
- `0x17` (23) for `#001900`
- `0x18` (24) for `#4CFF5E`
- `0x19` (25) for `#00FF19`
- `0x1A` (26) for `#00590D`
- `0x1B` (27) for `#001902`
- `0x1C` (28) for `#4CFF88`
- `0x1D` (29) for `#00FF55`
- `0x1E` (30) for `#00591D`
- `0x1F` (31) for `#001F12`
- `0x20` (32) for `#4CFFB7`
- `0x21` (33) for `#00FF99`
- `0x22` (34) for `#005935`
- `0x23` (35) for `#001912`
- `0x24` (36) for `#4CC3FF`
- `0x25` (37) for `#00A9FF`
- `0x26` (38) for `#004152`
- `0x27` (39) for `#001019`
- `0x28` (40) for `#4C88FF`
- `0x29` (41) for `#0055FF`
- `0x2A` (42) for `#001D59`
- `0x2B` (43) for `#000819`
- `0x2C` (44) for `#4C4CFF`
- `0x2D` (45) for `#0000FF`
- `0x2E` (46) for `#000059`
- `0x2F` (47) for `#000019`
- `0x30` (48) for `#874CFF`
- `0x31` (49) for `#5400FF`
- `0x32` (50) for `#190064`
- `0x33` (51) for `#0F0030`
- `0x34` (52) for `#FF4CFF`
- `0x35` (53) for `#FF00FF`
- `0x36` (54) for `#590059`
- `0x37` (55) for `#190019`
- `0x38` (56) for `#FF4C87`
- `0x39` (57) for `#FF0054`
- `0x3A` (58) for `#59001D`
- `0x3B` (59) for `#220013`
- `0x3C` (60) for `#FF1500`
- `0x3D` (61) for `#993500`
- `0x3E` (62) for `#795100`
- `0x3F` (63) for `#436400`
- `0x40` (64) for `#033900`
- `0x41` (65) for `#005735`
- `0x42` (66) for `#00547F`
- `0x43` (67) for `#0000FF`
- `0x44` (68) for `#00454F`
- `0x45` (69) for `#2500CC`
- `0x46` (70) for `#7F7F7F`
- `0x47` (71) for `#202020`
- `0x48` (72) for `#FF0000`
- `0x49` (73) for `#BDFF2D`
- `0x4A` (74) for `#AFED06`
- `0x4B` (75) for `#64FF09`
- `0x4C` (76) for `#108B00`
- `0x4D` (77) for `#00FF87`
- `0x4E` (78) for `#00A9FF`
- `0x4F` (79) for `#002AFF`
- `0x50` (80) for `#3F00FF`
- `0x51` (81) for `#7A00FF`
- `0x52` (82) for `#B21A7D`
- `0x53` (83) for `#402100`
- `0x54` (84) for `#FF4A00`
- `0x55` (85) for `#88E106`
- `0x56` (86) for `#72FF15`
- `0x57` (87) for `#00FF00`
- `0x58` (88) for `#3BFF26`
- `0x59` (89) for `#59FF71`
- `0x5A` (90) for `#38FFCC`
- `0x5B` (91) for `#5B8AFF`
- `0x5C` (92) for `#3151C6`
- `0x5D` (93) for `#877FE9`
- `0x5E` (94) for `#D31DFF`
- `0x5F` (95) for `#FF005D`
- `0x60` (96) for `#FF7F00`
- `0x61` (97) for `#B9B000`
- `0x62` (98) for `#90FF00`
- `0x63` (99) for `#835D07`
- `0x64` (100) for `#392b00`
- `0x65` (101) for `#144C10`
- `0x66` (102) for `#0D5038`
- `0x67` (103) for `#15152A`
- `0x68` (104) for `#16205A`
- `0x69` (105) for `#693C1C`
- `0x6A` (106) for `#A8000A`
- `0x6B` (107) for `#DE513D`
- `0x6C` (108) for `#D86A1C`
- `0x6D` (109) for `#FFE126`
- `0x6E` (110) for `#9EE12F`
- `0x6F` (111) for `#67B50F`
- `0x70` (112) for `#1E1E30`
- `0x71` (113) for `#DCFF6B`
- `0x72` (114) for `#80FFBD`
- `0x73` (115) for `#9A99FF`
- `0x74` (116) for `#8E66FF`
- `0x75` (117) for `#404040`
- `0x76` (118) for `#757575`
- `0x77` (119) for `#E0FFFF`
- `0x78` (120) for `#A00000`
- `0x79` (121) for `#350000`
- `0x7A` (122) for `#1AD000`
- `0x7B` (123) for `#074200`
- `0x7C` (124) for `#B9B000`
- `0x7D` (125) for `#3F3100`
- `0x7E` (126) for `#B35F00`
- `0x7F` (127) for `#4B1502`

Several basic combinations are missing, like `#00FFFF` for cyan.
Several colours are repeated. I assume you can use different ranges as different palettes.
The duplicates are commented out in [apc-colours.js](apc-colours.js) for reference.

See the [HTML version](colours.html) of this list.

Use the [colours.sh](colours.sh) script to show all the colours on the device.

## Custom colours

Pad colours can be set with customized using SysEx commands:

| Byte |           |                                              |
|------|-----------|----------------------------------------------|
| 1    | `F0`      | MIDI System exclusive message start          |
| 2    | `47`      | Manufacturer's ID Byte                       |
| 3    | `7F`      | System Exclusive Device ID                   |
| 4    | `4F`      | Product model ID                             |
| 5    | `24`      | Message type identifier                      |
| 6    |           | Total following bytes MSB                    |
| 7    |           | Total following bytes LSB                    |
| 8    | `00`-`3F` | First pad to apply to                        |
| 9    | `00`-`3F` | Last pad to apply to                         |
| 10   | `00`-`7F` | Red brigthness MSB                           |
| 11   | `00`-`7F` | Red brigthness LSB                           |
| 12   | `00`-`7F` | Green brigthness MSB                         |
| 13   | `00`-`7F` | Green brigthness LSB                         |
| 14   | `00`-`7F` | Blue brigthness MSB                          |
| 15   | `00`-`7F` | Blue brigthness LSB                          |
|      |           | Repeat bytes 8-15 for each additional colour |
| last | F7        | MIDI System exclusive message terminator     |

### Examples

Set all the pads to cyan (`#00FFFF` not available in built-in colours): `F0477F4F24 0008 00 3F 0000 7F7F 7F7F F7`
