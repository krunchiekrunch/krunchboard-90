import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import MatrixScanner
from kmk.keys import KC
from kmk.modules.encoder import EncoderHandler
from kmk.scanners import DiodeOrientation
from kmk.extensions.RGB import RGB, AnimationModes
from kmk.extensions.LED import LED
from kmk.modules.macros import Macros, Press, Release, Tap
from kmk.modules.layers import Layers
from kmk.extensions.media_keys import MediaKeys

keyboard = KMKKeyboard()
macros = Macros()
keyboard.modules.append(macros)
keyboard.extensions.append(MediaKeys())
keyboard.modules.append(Layers())

# matrix
keyboard.row_pins = (
    board.GP22, # R0
    board.GP19,
    board.GP18,
    board.GP17,
    board.GP16,
    board.GP11, # R5
)

keyboard.col_pins = (
    board.GP12, # C0
    board.GP13,
    board.GP14,
    board.GP15,
    board.GP20,
    board.GP21,
    board.GP2,
    board.GP1,
    board.GP0,
    board.GP3,
    board.GP4,
    board.GP5,
    board.GP6,
    board.GP7,
    board.GP8,
    board.GP9,
    board.GP10, # C16
)

keyboard.diode_orientation = DiodeOrientation.COL2ROW

BASE = 0
FN = 1

keyboard.keymap = [
    # Base (Layer 0)
    [
        KC.ESC, KC.F1, KC.F2, KC.F3, KC.F4, KC.F5, KC.F6, KC.F7, KC.F8, KC.F9, KC.F10, KC.F11, KC.F12, KC.NUMLOCK, KC.SLCK, KC.INSERT, KC.MUTE,
        KC.GRAVE, KC.N1, KC.N2, KC.N3, KC.N4, KC.N5, KC.N6, KC.N7, KC.N8, KC.N9, KC.N0, KC.MINUS, KC.EQUAL, KC.NO, KC.BACKSPACE, KC.HOME, KC.NO,
        KC.TAB, KC.NO, KC.Q, KC.W, KC.E, KC.R, KC.T, KC.Y, KC.U, KC.I, KC.O, KC.P, KC.LBRACKET, KC.RBRACKET, KC.BSLASH, KC.PGUP, KC.NO,
        KC.CAPS, KC.NO, KC.A, KC.S, KC.D, KC.F, KC.G, KC.H, KC.J, KC.K, KC.L, KC.SCOLON, KC.QUOTE, KC.ENTER, KC.NO, KC.PGDN, KC.NO,
        KC.NO, KC.LSHIFT, KC.Z, KC.X, KC.C, KC.V, KC.B, KC.N, KC.M, KC.COMMA, KC.DOT, KC.SLASH, KC.NO, KC.RSHIFT, KC.UP, KC.END, KC.NO,
        KC.LCTRL, KC.LGUI, KC.NO, KC.LALT, KC.NO, KC.NO, KC.SPACE, KC.NO, KC.NO, KC.NO, KC.RALT, KC.MO(FN), KC.RCTRL, KC.LEFT, KC.DOWN, KC.RIGHT, KC.NO,
    ],

    # Fn (Layer 1)
    [
        KC.NO, KC.MUTE, KC.VOLD, KC.VOLU, KC.MPRV, KC.MPLY, KC.MNXT, KC.NO, KC.NO, KC.NO, KC.NO, KC.BRID, KC.BRIU, KC.PSCREEN, KC.PAUSE, KC.DELETE, KC.TRNS,
        KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS,
        KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS,
        KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS,
        KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS,
    ]
]

# volume knob
encoder = EncoderHandler()
encoder.pins = ((board.GP27, board.GP26),)
encoder.map = [((KC.VOLU, KC.VOLD))]  # cw = vol up, ccw = vol down
keyboard.modules.append(encoder)

if __name__ == '__main__':
    keyboard.go()