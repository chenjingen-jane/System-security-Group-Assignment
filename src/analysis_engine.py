import math

def parse_log(log_filename="activity_log.txt"):
    # Read log file and return daily totals per event
    daily_totals = {}
    current_day_data = {}
    in_day = False

    with open(log_filename, "r") as f:
        for line in f:
            line = line.strip()

            if line.startswith("--- Day"):
                # Save previous day before moving to next
                if in_day:
                    for name, val in current_day_data.items():
                        if name not in daily_totals:
                            daily_totals[name] = []
                        daily_totals[name].append(val)
                current_day_data = {}
                in_day = True

            elif ":" in line and in_day:
                parts = line.split(":")
                if len(parts) == 2:
                    name = parts[0].strip()
                    try:
                        val = float(parts[1].strip())
                        current_day_data[name] = current_day_data.get(name, 0) + val
                    except ValueError:
                        pass

        # Save the last day
        if in_day and current_day_data:
            for name, val in current_day_data.items():
                if name not in daily_totals:
                    daily_totals[name] = []
                daily_totals[name].append(val)

    return daily_totals


def compute_baseline(daily_totals):
    # Calculate mean and std for each event across all days
    baseline = {}

    for event_name, totals in daily_totals.items():
        n = len(totals)
        if n == 0:
            continue
        mean = sum(totals) / n
        variance = sum((x - mean) ** 2 for x in totals) / n
        std = math.sqrt(variance)
        baseline[event_name] = {
            "mean": mean,
            "std": std,
            "totals": totals
        }

    return baseline


def save_baseline(baseline, output_filename="baseline_stats.txt"):
    # Write baseline mean and std to file
    with open(output_filename, "w") as f:
        f.write(f"{len(baseline)}\n")
        for event_name, stats in baseline.items():
            f.write(f"{event_name}:{stats['mean']:.4f}:{stats['std']:.4f}:\n")
    print(f"Baseline stats saved to {output_filename}")


def run_analysis(log_filename="activity_log.txt", output_filename="baseline_stats.txt"):
    # Run full analysis: parse log, compute baseline, save to file
    print("\nStarting Analysis Engine...")
    daily_totals = parse_log(log_filename)

    if not daily_totals:
        print("ERROR: No data found in log file.")
        return {}

    baseline = compute_baseline(daily_totals)

    print("\n--- Baseline Statistics ---")
    for event_name, stats in baseline.items():
        print(f"  {event_name}: mean={stats['mean']:.4f}, std={stats['std']:.4f}")

    save_baseline(baseline, output_filename)
    print("Analysis Engine complete.\n")
    return baseline