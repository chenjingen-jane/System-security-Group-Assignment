import statistics


def read_activity_log(filename="activity_log.txt"):
    event_values = {}

    try:
        with open(filename, "r") as file:
            for line in file:
                line = line.strip()

                if not line:
                    continue

                if line.startswith("--- Day"):
                    continue

                if ":" not in line:
                    continue

                event_name, value = line.split(":", 1)
                event_name = event_name.strip()

                try:
                    value = float(value.strip())
                except ValueError:
                    print(f"Skipping invalid value: {line}")
                    continue

                if event_name not in event_values:
                    event_values[event_name] = []

                event_values[event_name].append(value)

    except FileNotFoundError:
        print(f"Error: {filename} not found.")
        return {}

    return event_values


def calculate_analysis(event_values):
    analysis_results = {}

    for event_name, values in event_values.items():
        if not values:
            continue

        mean_value = statistics.mean(values)

        if len(values) > 1:
            std_value = statistics.stdev(values)
        else:
            std_value = 0

        analysis_results[event_name] = {
            "mean": mean_value,
            "std": std_value
        }

    return analysis_results


def save_analysis_results(results, filename="Analysis.txt"):
    with open(filename, "w") as file:
        for event_name, stats in results.items():
            file.write(f"{event_name}:{stats['mean']:.2f}:{stats['std']:.2f}:\n")


def run_analysis(log_filename="activity_log.txt", output_filename="Analysis.txt"):
    event_values = read_activity_log(log_filename)

    if not event_values:
        print("No activity data found. Analysis stopped.")
        return {}

    results = calculate_analysis(event_values)
    save_analysis_results(results, output_filename)

    print("Analysis completed successfully.")
    print(f"Results saved to {output_filename}")

    return results


if __name__ == "__main__":
    run_analysis()