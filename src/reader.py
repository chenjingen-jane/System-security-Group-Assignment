def clean_name(name):
    return name.strip().lower().replace(" ", "")

def read_events(filename):
    events = {}

    with open(filename, "r") as file:
        lines = file.readlines()
        
    numbers_of_events = int(lines[0].strip())
    

    valid_count = 0

    for line in lines[1:]:
        parts = line.strip().split(":")
        while parts and parts[-1] == "":
            parts.pop()

        if len(parts) != 5:
            print(f"ERROR: Invalid line format for {line.strip()}")
            continue

        name = clean_name(parts[0])
        event_type = parts[1]

        if event_type not in ["D", "C"]:
            print(f"ERROR: Invalid type for {name}")
            continue

        try:
           minimum = float(parts[2]) if parts[2] != "" else 0.0
           maximum = float(parts[3]) if parts[3] != "" else float('inf')
           weight = float(parts[4]) if parts[4] != "" else 0.0
        except ValueError:
            print(f"ERROR: Invalid numeric value for {name}")
            continue

        events[name] = {
            "type": event_type,
            "min": minimum,
            "max": maximum,
            "weight": weight
        }

        valid_count += 1

    if numbers_of_events != valid_count:
        print("ERROR: Event count mismatch")

    return events

def read_stats(filename, events):

    with open(filename, "r") as file:
        lines = file.readlines()

    number_of_stats = int(lines[0].strip())

    valid_stats = 0

    for line in lines[1:]:
        parts = line.strip().split(":")
        while parts and parts[-1] == "":
            parts.pop()

        if len(parts) != 3:
            print(f"ERROR: Invalid line format for {line.strip()}")
            continue

        name = clean_name(parts[0])
        try:
            mean = float(parts[1])
            std = float(parts[2])
        except ValueError:
            print(f"ERROR: Invalid numeric value in stats for {name}")
            continue

        if name in events:
               events[name]["mean"] = float(parts[1]) if parts[1] != "" else 0.0
               events[name]["std"] = float(parts[2]) if parts[2] != "" else 0.0
        else:
            print(f"ERROR: {name} not found in Events.txt")
        
        valid_stats += 1
        
    if number_of_stats != valid_stats:
        print("ERROR: Stats count mismatch")

    return events