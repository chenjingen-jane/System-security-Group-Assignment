import copy
from reader import read_events, read_stats
from activity_engine import generate_activities
from analysis_engine import parse_log, compute_baseline


def read_new_stats(filename, events):
    # Load a new stats file into a fresh copy of events
    new_events = copy.deepcopy(events)
    try:
        new_events = read_stats(filename, new_events)
    except FileNotFoundError:
        print(f"ERROR: File '{filename}' not found.")
        return None
    return new_events


def compute_threshold(events):
    # Threshold = 2 x sum of all event weights
    total_weight = sum(stats["weight"] for stats in events.values())
    return 2 * total_weight


def detect_anomalies(baseline, daily_totals, events, threshold):
    # Compare each day's activity against baseline and flag anomalies
    num_days = max(len(v) for v in daily_totals.values()) if daily_totals else 0

    print(f"\n--- Alert Engine Report ---")
    print(f"Threshold: {threshold:.2f}\n")

    for day_idx in range(num_days):
        anomaly_counter = 0.0

        for event_name, baseline_stats in baseline.items():
            if event_name not in daily_totals:
                continue
            if day_idx >= len(daily_totals[event_name]):
                continue

            day_val = daily_totals[event_name][day_idx]
            b_mean = baseline_stats["mean"]
            b_std = baseline_stats["std"]

            deviation = 0.0 if b_std == 0 else abs(day_val - b_mean) / b_std

            weight = events.get(event_name, {}).get("weight", 0)
            anomaly_counter += deviation * weight

        status = "FLAGGED" if anomaly_counter >= threshold else "okay"
        print(f"  Day {day_idx + 1}: anomaly counter = {anomaly_counter:.4f} | {status}")


def run_alert_engine(base_events, baseline):
    # Main loop: load new stats, simulate days, detect anomalies, repeat until quit
    while True:
        print("\n=== Alert Engine ===")
        stats_file = input("Enter new stats file (or 'quit' to exit): ").strip()

        if stats_file.lower() == "quit":
            print("Exiting alert engine.")
            break

        new_events = read_new_stats(stats_file, base_events)
        if new_events is None:
            continue

        try:
            days = int(input("Enter number of days to simulate: ").strip())
            if days <= 0:
                print("ERROR: Days must be a positive integer.")
                continue
        except ValueError:
            print("ERROR: Invalid number of days.")
            continue

        generate_activities(new_events, days, log_filename="alert_activity_log.txt")

        daily_totals = parse_log("alert_activity_log.txt")
        if not daily_totals:
            print("ERROR: No activity data generated.")
            continue

        threshold = compute_threshold(base_events)
        detect_anomalies(baseline, daily_totals, base_events, threshold)