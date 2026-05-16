import sys
from reader import read_events, read_stats
from activity_engine import generate_activities
from analysis_engine import run_analysis
from alert_engine import run_alert_engine


def main():
    # Validate command line arguments
    if len(sys.argv) != 4:
        print("Usage: python main.py Events.txt Stats.txt <days>")
        sys.exit(1)

    events_file = sys.argv[1]
    stats_file = sys.argv[2]

    try:
        days = int(sys.argv[3])
        if days <= 0:
            raise ValueError
    except ValueError:
        print("ERROR: Days must be a positive integer.")
        sys.exit(1)

    # Phase 1: Read and validate input files
    print("=== Initial Input ===")
    events = read_events(events_file)
    events = read_stats(stats_file, events)

    print("\nEvents loaded:")
    for name, data in events.items():
        print(f"  {name}: type={data['type']}, min={data['min']}, max={data['max']}, "
              f"weight={data['weight']}, mean={data.get('mean', 'N/A')}, std={data.get('std', 'N/A')}")

    # Phase 2: Generate baseline activity logs
    print("\n=== Activity Engine ===")
    generate_activities(events, days, log_filename="activity_log.txt")

    # Phase 3: Analyse logs and compute baseline statistics
    baseline = run_analysis(log_filename="activity_log.txt", output_filename="baseline_stats.txt")

    # Phase 4: Run alert engine
    run_alert_engine(base_events=events, baseline=baseline)


if __name__ == "__main__":
    main()