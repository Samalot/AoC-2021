import Reader


def run():
    tracking = { "depth": 0, "horizontal": 0 }

    trackingMap = {"up": "depth", "down": "depth", "forward": "horizontal"}
    mods = { "up": -1, "down": 1, "forward": 1 }

    for data in Reader.read("input"):
        direction, amount = data.split(" ")
        tracking[trackingMap[direction]] += mods[direction] * int(amount)

    return tracking['depth'] * tracking['horizontal']


print(f'Answer: {run()}')
