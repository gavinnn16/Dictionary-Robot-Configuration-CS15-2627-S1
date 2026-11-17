robot = {
    "name": "Atlas",
    "model": "RX-7",
    "battery": 85,
    "speed": 6,
    "mode": "exploration"
}

print(robot["name"])
print(robot["model"])
robot["battery"] = 100
print(robot["battery"])
robot["color"] = "silver"
robot.pop("mode")
print(len(robot))

for key, value in robot.items():
    print(f"{key}: {value}")