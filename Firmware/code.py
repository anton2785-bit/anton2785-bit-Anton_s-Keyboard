import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.extensions.RGB import RGB
from kmk.modules.encoder import Encoder
from kmk.modules.layers import Layers

keyboard = KMKKeyboard()
keyboard.modules.append(Layers())

# 1. 11 Rows x 9 Columns Matrix Configuration
keyboard.row_pins = (
    board.GP11, board.GP12, board.GP13, board.GP14, board.GP15, 
    board.GP16, board.GP17, board.GP18, board.GP19, board.GP20, board.GP21
)
keyboard.col_pins = (
    board.GP0, board.GP1, board.GP2, board.GP3, board.GP4, 
    board.GP5, board.GP6, board.GP7, board.GP8
)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

# 2. RGB LED Configuration (50% Power Safety)
# val_limit=128 prevents the LEDs from drawing too much current
rgb = RGB(
    pixel_pin=board.GP22, 
    num_pixels=96, 
    val_limit=128, 
    hue_default=0, 
    sat_default=0, 
    val_default=100
)
keyboard.extensions.append(rgb)

# 3. Rotary Encoder (A & B Pins)
encoder = Encoder()
encoder.pins = (
    (board.GP26, board.GP27, None), # Rotation Pins (A, B). Push is in Matrix.
)
# Layer 0: Volume | Layer 1: LED Brightness
encoder.map = [
    ((KC.VOLU, KC.VOLD),),        # Standard Mode
    ((KC.RGB_VAI, KC.RGB_VAD),),  # FN Mode (Brightness Up/Down)
]
keyboard.modules.append(encoder)

# 4. 1800 Layout Matrix (11x9)
# Note: 'KC.MO(1)' is your Function key. Hold it to use the 2nd encoder mode.
# I've mapped the Encoder Push to KC.MUTE.
keyboard.keymap = [
    # LAYER 0: Standard
    [
        KC.ESC,  KC.F1,   KC.F2,   KC.F3,   KC.F4,   KC.F5,   KC.F6,   KC.F7,   KC.F8,
        KC.F9,   KC.F10,  KC.F11,  KC.F12,  KC.PSCR, KC.SLCK, KC.PAUS, KC.GRV,  KC.1,
        KC.2,    KC.3,    KC.4,    KC.5,    KC.6,    KC.7,    KC.8,    KC.9,    KC.0,
        KC.MINS, KC.EQL,  KC.BSPC, KC.INS,  KC.HOME, KC.PGUP, KC.TAB,  KC.Q,    KC.W,
        KC.E,    KC.R,    KC.T,    KC.Y,    KC.U,    KC.I,    KC.O,    KC.P,    KC.LBRC,
        KC.RBRC, KC.BSLS, KC.DEL,  KC.END,  KC.PGDN, KC.CAPS, KC.A,    KC.S,    KC.D,
        KC.F,    KC.G,    KC.H,    KC.J,    KC.K,    KC.L,    KC.SCLN, KC.QUOT, KC.ENT,
        KC.P7,   KC.P8,   KC.P9,   KC.LSFT, KC.Z,    KC.X,    KC.C,    KC.V,    KC.B,
        KC.N,    KC.M,    KC.COMM, KC.DOT,  KC.SLSH, KC.RSFT, KC.UP,   KC.P4,   KC.P5,
        KC.P6,   KC.LCTL, KC.LGUI, KC.LALT, KC.SPC,  KC.RALT, KC.MO(1),KC.RCTL, KC.LEFT,
        KC.DOWN, KC.RGHT, KC.P1,   KC.P2,   KC.P3,   KC.PENT, KC.P0,   KC.PDOT, KC.MUTE
    ],
    # LAYER 1: Function (Add specific FN keys here if needed)
    [
        KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS,
        KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS,
        KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS,
        KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS,
        KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS,
        KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS,
        KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS,
        KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS,
        KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS,
        KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS,
        KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS
    ]
]

if __name__ == '__main__':
    keyboard.go()