import random

def generate_activities(event_data, days, log_filename="activity_log.txt"):
    """
    Generates fake user activities based on provided statistics and logs them.
    """
    print("Starting Event Generation...")
    
    with open(log_filename, 'w') as log_file:
        for day in range(1, days + 1):
            print(f"Generating Day {day}...")
            log_file.write(f"--- Day {day} ---\n")
            
            for event_name, stats in event_data.items():
                # 1. Generate base value using Gaussian distribution
                mean = stats['mean']
                std = stats['std']
                raw_value = random.gauss(mean, std)
                
                # Enforce minimum and maximum ranges defined in Events.txt
                min_val = stats.get('min')
                max_val = stats.get('max')
                
                if min_val is not None and min_val != '':
                    raw_value = max(float(min_val), raw_value)
                if max_val is not None and max_val != '':
                    raw_value = min(float(max_val), raw_value)
                    
                # 2. Format based on Continuous (C) or Discrete (D)
                if stats['type'] == 'D':
                    # Discrete must be integers
                    final_value = int(round(raw_value))
                else:
                    # Continuous in 2 decimal places
                    final_value = round(raw_value, 2)
                    
                # 3. Write to log
                log_file.write(f"{event_name}:{final_value}\n")
                
    print("Event Generation Complete. Logs saved to", log_filename)