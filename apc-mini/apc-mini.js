// noinspection ES6ConvertVarToLetConst
var APCMini = {};

//
// Constants
//

const decks = [1, 2];
const eqs = [1, 2, 3];
// hotcue -> hotcue offset
const hotcues = {
    1: 8, 2: 9, 3: 10, 4: 11,
    5: 0, 6: 1, 7: 2, 8: 3
}
const padRows = {
    beatjump: 0x20,
    beatloop: 0x30,
    hotcue: 0x10,
    intro: 0x08,
    play: 0x00,
    sync: 0x28,
}
const padColours = {
    back: 0x06,
    back_press: 0x05,
    beatloop: 0x54,
    cue: 0x09,
    cue_set: 0x3C,
    forward: 0x16,
    forward_press: 0x57,
    hotcue: 0x2D,
    intro: 0x25,
    outro: 0x4F,
    play: 0x15,
    press: 0x02,
    reverse: 0x05,
    sync: 0x60,
    sync_leader: 0x54,
}

//
// Colours
//

var APCColours = {
    0x000000: 0x00,
    0x1E1E1E: 0x01,
    0x7F7F7F: 0x02,
    0xFFFFFF: 0x03,
    0xFF4C4C: 0x04,
    0xFF0000: 0x05,
    0x590000: 0x06,
    0x190000: 0x07,
    0xFFBD6C: 0x08,
    0xFF5400: 0x09,
    0x591D00: 0x0A,
    0x271B00: 0x0B,
    0xFFFF4C: 0x0C,
    0xFFFF00: 0x0D,
    0x595900: 0x0E,
    0x191900: 0x0F,
    0x88FF4C: 0x10,
    0x54FF00: 0x11,
    0x1D5900: 0x12,
    0x142B00: 0x13,
    0x4CFF4C: 0x14,
    0x00FF00: 0x15,
    0x005900: 0x16,
    0x001900: 0x17,
    0x4CFF5E: 0x18,
    0x00FF19: 0x19,
    0x00590D: 0x1A,
    0x001902: 0x1B,
    0x4CFF88: 0x1C,
    0x00FF55: 0x1D,
    0x00591D: 0x1E,
    0x001F12: 0x1F,
    0x4CFFB7: 0x20,
    0x00FF99: 0x21,
    0x005935: 0x22,
    0x001912: 0x23,
    0x4CC3FF: 0x24,
    0x00A9FF: 0x25,
    0x004152: 0x26,
    0x001019: 0x27,
    0x4C88FF: 0x28,
    0x0055FF: 0x29,
    0x001D59: 0x2A,
    0x000819: 0x2B,
    0x4C4CFF: 0x2C,
    0x0000FF: 0x2D,
    0x000059: 0x2E,
    0x000019: 0x2F,
    0x874CFF: 0x30,
    0x5400FF: 0x31,
    0x190064: 0x32,
    0x0F0030: 0x33,
    0xFF4CFF: 0x34,
    0xFF00FF: 0x35,
    0x590059: 0x36,
    0x190019: 0x37,
    0xFF4C87: 0x38,
    0xFF0054: 0x39,
    0x59001D: 0x3A,
    0x220013: 0x3B,
    0xFF1500: 0x3C,
    0x993500: 0x3D,
    0x795100: 0x3E,
    0x436400: 0x3F,
    0x033900: 0x40,
    0x005735: 0x41,
    0x00547F: 0x42,
    // 0x0000FF: 0x43,
    0x00454F: 0x44,
    0x2500CC: 0x45,
    // 0x7F7F7F: 0x46,
    0x202020: 0x47,
    // 0xFF0000: 0x48,
    0xBDFF2D: 0x49,
    0xAFED06: 0x4A,
    0x64FF09: 0x4B,
    0x108B00: 0x4C,
    0x00FF87: 0x4D,
    // 0x00A9FF: 0x4E,
    0x002AFF: 0x4F,
    0x3F00FF: 0x50,
    0x7A00FF: 0x51,
    0xB21A7D: 0x52,
    0x402100: 0x53,
    0xFF4A00: 0x54,
    0x88E106: 0x55,
    0x72FF15: 0x56,
    // 0x00FF00: 0x57,
    0x3BFF26: 0x58,
    0x59FF71: 0x59,
    0x38FFCC: 0x5A,
    0x5B8AFF: 0x5B,
    0x3151C6: 0x5C,
    0x877FE9: 0x5D,
    0xD31DFF: 0x5E,
    0xFF005D: 0x5F,
    0xFF7F00: 0x60,
    0xB9B000: 0x61,
    0x90FF00: 0x62,
    0x835D07: 0x63,
    0x392b00: 0x64,
    0x144C10: 0x65,
    0x0D5038: 0x66,
    0x15152A: 0x67,
    0x16205A: 0x68,
    0x693C1C: 0x69,
    0xA8000A: 0x6A,
    0xDE513D: 0x6B,
    0xD86A1C: 0x6C,
    0xFFE126: 0x6D,
    0x9EE12F: 0x6E,
    0x67B50F: 0x6F,
    0x1E1E30: 0x70,
    0xDCFF6B: 0x71,
    0x80FFBD: 0x72,
    0x9A99FF: 0x73,
    0x8E66FF: 0x74,
    0x404040: 0x75,
    0x757575: 0x76,
    0xE0FFFF: 0x77,
    0xA00000: 0x78,
    0x350000: 0x79,
    0x1AD000: 0x7A,
    0x074200: 0x7B,
    // 0xB9B000: 0x7C,
    0x3F3100: 0x7D,
    0xB35F00: 0x7E,
    0x4B1502: 0x7F,
}
// noinspection ES6ConvertVarToLetConst
APCMini.ColorMapper = new ColorMapper(APCColours);

//
// Helper functions
//

APCMini.padOff = function () {
    midi.sendSysexMsg([
        0xF0, 0x47, 0x7F, 0x4F, 0x24,
        0x00, 0x08,
        0x00, 0x3F,
        0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
        0xF7
    ])
}

APCMini.ledOff = function (led) {
    midi.sendShortMsg(0x90, led, 0x00);
}
APCMini.ledOn = function (led, colorByte) {
    midi.sendShortMsg(0x96, led, colorByte)
}

APCMini.clear = function () {
    // Turn off pads
    for (let led = 0x00; led <= 0x3F; led++) {
        APCMini.ledOff(led);
    }
    // Turn off buttons
    for (let led = 0x64; led <= 0x6B; led++) {
        APCMini.ledOff(led);
    }
    for (let led = 0x70; led <= 0x77; led++) {
        APCMini.ledOff(led);
    }
}

//
// Init and shutdown
//

APCMini.init = function (_id, _debugging) {
    APCMini.clear()
}

APCMini.shutdown = function () {
    APCMini.clear()
}

//
// EQs and their clamping
//

const eqClampingEnabled = engine.getSetting('eqClampingEnabled');
const eqMaximum = eqClampingEnabled ? 0.5 : 1.0

APCMini.clampEQ = {}
for (let deck of decks) {
    APCMini.clampEQ[`deck${deck}`] = {};
    for (let eq of eqs) {
        APCMini.clampEQ[`deck${deck}`][`eq${eq}`] = function (channel, control, value, status, group) {
            APCMini.clampEQ.set(deck, eq, value);
        };
    }
}
APCMini.clampEQ.set = function (deck, eq, value) {
    let newValue = script.absoluteLin(value, 0, eqMaximum)
    engine.setParameter(`[EqualizerRack1_[Channel${deck}]_Effect1]`, `parameter${eq}`, newValue);
}

//
// Hotcue colors
//
for (let deck of decks) {
    let deckOffset = deck - 1
    for (let hotcue in hotcues) {
        let hotcueOffset = hotcues[hotcue];
        engine.makeConnection(`[Channel${deck}]`, `hotcue_${hotcue}_color`, (value, _group, _control) => {
            let led = padRows.hotcue + hotcueOffset + (4 * deckOffset)
            if (value === -1) {
                APCMini.ledOff(led)
            } else {
                APCMini.ledOn(led, APCMini.ColorMapper.getValueForNearestColor(value));
            }
        })
    }
    engine.makeConnection(`[Channel${deck}]`, `track_loaded`, (value, _group, _control) => {
        if (value === 1) {
            let beatloopEnabled = engine.getParameter(`[Channel${deck}]`, `loop_enabled`);
            if (beatloopEnabled === 1) {
                APCMini.ledOn(padRows.beatloop + 8 + (4 * deckOffset), padColours.beatloop);
            }
            let loopAnchor = engine.getParameter(`[Channel${deck}]`, `loop_anchor`);
            if (loopAnchor === 0) {
                APCMini.ledOn(padRows.beatloop + 3 + (4 * deckOffset), padColours.forward);
            } else {
                APCMini.ledOn(padRows.beatloop + 3 + (4 * deckOffset), padColours.back);
            }
            APCMini.ledOn(padRows.sync + (4 * deckOffset), padColours.back);
            APCMini.ledOn(padRows.sync + 1 + (4 * deckOffset), padColours.forward);
            APCMini.ledOn(padRows.beatjump + (4 * deckOffset), padColours.back);
            APCMini.ledOn(padRows.beatjump + 1 + (4 * deckOffset), padColours.forward);
        } else {
            for (let hotcue in hotcues) {
                let hotcueOffset = hotcues[hotcue];
                let led = padRows.hotcue + hotcueOffset + (4 * deckOffset)
                APCMini.ledOff(led)
            }
            APCMini.ledOff(padRows.beatloop + 8 + (4 * deckOffset));
            APCMini.ledOff(padRows.beatloop + 3 + (4 * deckOffset));
            APCMini.ledOff(padRows.sync + (4 * deckOffset));
            APCMini.ledOff(padRows.sync + 1 + (4 * deckOffset));
            APCMini.ledOff(padRows.beatjump + (4 * deckOffset));
            APCMini.ledOff(padRows.beatjump + 1 + (4 * deckOffset));
        }
    })
}
