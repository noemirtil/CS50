#!/usr/bin/env python


distances = {
    "Voyager 1": 163,
    "Voyager 2": 136,
    "Pioneer 10": 80,
    "New Horizons": 58,
    "Pioneer 11": 44,
}


def main():
    spacecraft = {"name": "James Webb Space Telescope"}
    spacecraft.update({"distance": 0.01, "orbit": "Sun"})
    print(create_report(spacecraft))

    print(distances)
    print(distances.keys())
    print(distances.values())
    for name in distances.keys():
        print(f"{name} is {distances[name]} AU from Earth")
    for distance in distances.values():
        print(f"This spacecraft is {distance} AU from Earth")


def create_report(spacecraft):
    return f"""
    ========= REPORT =========

    Name: {spacecraft.get("name", "Unknown")}
    Distance: {spacecraft.get("distance", "Unknown")} AU
    Orbit: {spacecraft.get("orbit", "Unknown")}

    ==========================
    """


main()
