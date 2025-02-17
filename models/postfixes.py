# list of suffixes for roll modifications
postfixes = {
    "exp": {
        "name": "Explode",
        "aliases": ["explode", "exp"],
        "default_value": -1,
        "description": "Modifying dice to become exploding dice: roll again when equal or higher than value.",
        "shorty": "modify dice to become explode dice",
        "example": "roll 2d20/exp",
        "enabled": True
    },
    "pen": {
        "name": "Penetrate",
        "aliases": ["penetrate", "pen"],
        "default_value": -1,
        "description": "Modifying dice to become penetrating dice: roll again when equal or higher than value. "
                       "But 1 will be subtracted from the result of that additional roll.",
        "shorty": "modify dice to become penetration dice",
        "example": "roll 2d20/pen",
        "enabled": True
    },
    "sts": {
        "name": "Stress",
        "aliases": ["stress", "sts"],
        "default_value": 1,
        "description": "Roll additional part of dice if no maximum on first roll.",
        "shorty": "modify dice to become stress dice",
        "example": "roll 4d6/s",
        "enabled": False
    },
    "dl": {
        "name": "Drop Lowest",
        "aliases": ["droplowest", "dl", "dlow"],
        "default_value": 1,
        "description": "Drop specified number of dice with lowest number",
        "shorty": "drop dice with lowest result",
        "example": "roll 10d20/dl:3",
        "enabled": True
    },
    "dh": {
        "name": "Drop Highest",
        "aliases": ["drophighest", "dh", "dhigh"],
        "default_value": 1,
        "description": "Drop specified number of dice with highest number",
        "shorty": "drop dice with highest result",
        "example": "roll 5d10/dh:2",
        "enabled": True
    },
    "kl": {
        "name": "Keep Lowest",
        "aliases": ["keeplowest", "kl", "klow"],
        "default_value": 1,
        "description": "Keep specified number of dice with lowest number",
        "shorty": "keep dice with lowest result",
        "example": "roll 4d100/kl:1",
        "enabled": True
    },
    "kh": {
        "name": "Keep Highest",
        "aliases": ["keephighest", "kh", "khigh"],
        "default_value": 1,
        "description": "Keep specified number of dice with highest number",
        "shorty": "keep dice with highest result",
        "example": "roll 3d4/kh:1",
        "enabled": True
    },
    "rr": {
        "name": "ReRoll",
        "aliases": ["reroll", "rr"],
        "default_value": 1,
        "description": "Reroll dice with result on value or lower",
        "shorty": "reroll dice",
        "example": "roll 2d20/rr:2",
        "enabled": True
    },
    "x": {
        "name": "Multiplier",
        "aliases": ["multiplier", "x"],
        "default_value": 2,
        "description": "Multiply the number of dice rolls by the value",
        "shorty": "multiply dice amount",
        "example": "roll 2d20/x:3",
        "enabled": True
    },
    "fate": {
        "name": "Fate",
        "aliases": ["f", "fate"],
        "default_value": 6,
        "description": "Roll dice in the Fate system (+ - .)",
        "shorty": "Roll Fate dice",
        "example": "roll 4d6/fate",
        "type": 3,
        "enabled": True
    },
    "cod": {
        "name": "CoD",
        "aliases": ["cod"],
        "default_value": 10,
        "description": "Roll dice in the Chronicles of Darkness System. ",
        "shorty": "Roll Chronicles of Darkness dice",
        "example": "roll 5d10/cod. 5d10/cod:9 for 9-again, and 5d10/cod:8 for 8-again",
        "type": 4,
        "enabled": True
    },
    "wod": {
        "name": "WoD",
        "aliases": ["wod"],
        "default_value": 6,
        "description": "Roll dice in the World of Darkness System. ",
        "shorty": "Roll World of Darkness dice",
        "example": "roll 5d10/wod to roll standard difficulty (6). 5d10/wod:N to roll with difficulty \"N\"",
        "type": 5,
        "enabled": True
    }
}

aliases = {
    "dl": "dl",
    "dlow": "dl",
    "droplowest": "dl",
    "dh": "dh",
    "dhigh": "dh",
    "drophighest": "dh",
    "kl": "kl",
    "klow": "kl",
    "keeplowest": "kl",
    "kh": "kh",
    "khigh": "kh",
    "keephighest": "kh",
    "exp": "exp",
    "explode": "exp",
    "pen": "pen",
    "penetrate": "pen",
    "rr": "rr",
    "reroll": "rr",
    "x": "x",
    "multiplier": "x",
    "f": "fate",
    "fate": "fate",
    "cod": "cod",
    "wod": "wod"
}
