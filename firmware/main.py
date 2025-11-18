import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import MatrixScanner
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.extensions.display import Display, TextEntry
from kmk.extensions.display.ssd1306 import SSD1306
from kmk.extensions.RGB import RGB, AnimationModes
from kmk.modules.macros import Macros, Press, Release, Tap
from kmk.modules.mouse_keys import MouseKeys
from kmk.extensions.media_keys import MediaKeys
from kmk.modules.encoder import EncoderHandler

keyboard = KMKKeyboard()

macros = Macros()
keyboard.modules.append(macros)
mouse = MouseKeys()
keyboard.modules.append(MouseKeys())
keyboard.extensions.append(MediaKeys())
encoder_handler = EncoderHandler()
keyboard.modules.append(encoder_handler)

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

_______ = KC.TRNS
xxxxxxx = KC.NO
xxxx = KC.NO
Fn = KC.MO(1)


keyboard.keymap = [
    # Base (Layer 0)
    [
        KC.ESC,   KC.F1,   KC.F2, KC.F3,   KC.F4, KC.F5, KC.F6,    KC.F7, KC.F8, KC.F9,    KC.F10,  KC.F11,    KC.F12,   KC.NLCK,  KC.SLCK, KC.INS,   KC.MUTE,
        KC.GRAVE, KC.N1,   KC.N2, KC.N3,   KC.N4, KC.N5, KC.N6,    KC.N7, KC.N8, KC.N9,    KC.N0,   KC.MINUS,  KC.EQUAL, xxxxxxx,  KC.BSPC, KC.HOME,  xxxxxxx,
        KC.TAB,   xxxxxxx, KC.Q,  KC.W,    KC.E,  KC.R,  KC.T,     KC.Y,  KC.U,  KC.I,     KC.O,    KC.P,      KC.LBRC,  KC.RBRC,  KC.BSLS, KC.PGUP,  xxxxxxx,
        KC.CAPS,  xxxxxxx, KC.A,  KC.S,    KC.D,  KC.F,  KC.G,     KC.H,  KC.J,  KC.K,     KC.L,    KC.SCOLON, KC.QUOTE, KC.ENTER, KC.NO,   KC.PGDN,  xxxxxxx,
        xxxxxxx,  KC.LSFT, KC.Z,  KC.X,    KC.C,  KC.V,  KC.B,     KC.N,  KC.M,  KC.COMMA, KC.DOT,  KC.SLASH,  xxxxxxx,  KC.RSFT,  KC.UP,   KC.END,   xxxxxxx,
        KC.LCTRL, KC.LGUI, KC.NO, KC.LALT, xxxx,  xxxx,  KC.SPACE, xxxx,  xxxx,  xxxxxxx,  KC.RALT, Fn,        KC.RCTRL, KC.LEFT,  KC.DOWN, KC.RIGHT, xxxxxxx,
    ],

    # Fn (Layer 1)
    [
        xxxxxxx, KC.MUTE, KC.VOLD, KC.VOLU, KC.MPRV, KC.MPLY, KC.MNXT, xxxxxxx, xxxxxxx, xxxxxxx, xxxxxxx, KC.BRID, KC.BRIU, KC.PSCR, KC.PAUS, KC.DEL,  _______,
        _______, _______, _______, _______, _______, _______, _______, _______, _______, _______, _______, _______, _______, _______, _______, _______, _______,
        _______, _______, _______, _______, _______, _______, _______, _______, _______, _______, _______, _______, _______, _______, _______, _______, _______,
        _______, _______, _______, _______, _______, _______, _______, _______, _______, _______, _______, _______, _______, _______, _______, _______, _______,
        _______, _______, _______, _______, _______, _______, _______, _______, _______, _______, _______, _______, _______, _______, _______, _______, _______,
    ]
]

# volume knob
encoder_handler.pins = ((board.GP27, board.GP26),)
encoder_handler.map = [
    ((KC.VOLD, KC.VOLU),), # Volume
    ((KC.BRID, KC.BRIU),), # Brightness (Fn)
    ]

if __name__ == '__main__':
    keyboard.go()
