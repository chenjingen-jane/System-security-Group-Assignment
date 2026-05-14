from reader import read_events, read_stats

events = read_events("Events.txt")

events = read_stats("Stats.txt", events)

print(events)
