# CSCI262 Assignment 3 – Fast Group Work Division (1.5 Week Plan)

## Project Overview

This assignment is to build an Email System Intrusion Detection System (IDS).

The system should:

1. Read event and statistics files
2. Generate user activity logs
3. Analyze generated logs
4. Detect abnormal behaviour
5. Produce a report

Since the deadline is very short (1.5 weeks), the group should focus on:
- Finishing core functions first
- Keeping the program simple
- Working in parallel
- Integrating early

---

# Recommended Fast Work Division (4 Members)

| Member | Responsibility |
|---|---|
| Member 1 | File reading + validation |
| Member 2 | Activity generation + logs |
| Member 3 | Analysis + statistics |
| Member 4 | Alert engine + integration + testing |

---

# Member 1 – File Reader & Validation

## Main Responsibility

Handle:
- Reading `Events.txt`
- Reading `Stats.txt`
- Validating data
- Storing data internally

---

## Tasks

### 1. Read Events.txt

Need to:
- Read event names
- Read event type (`C` or `D`)
- Read minimum/maximum values
- Read weights

Example:

```txt
Logins:D:0::2:
```

---

### 2. Read Stats.txt

Need to:
- Read mean values
- Read standard deviation values
- Match statistics with events

Example:

```txt
Logins:4:1.5:
```

---

### 3. Detect Errors

Need to check:
- Missing events
- Wrong event names
- Invalid types
- Invalid ranges

---

### 4. Create Internal Storage

Example in Python:

```python
{
  "Logins": {
      "type": "D",
      "weight": 2,
      "mean": 4,
      "std": 1.5
  }
}
```

---

## Report Section

This member writes:
- Input handling explanation
- Validation explanation
- Data structure explanation

---

## Deadline

Finish within:
- 1–2 days

This is important because other members depend on this structure.

---

# Member 2 – Activity Generator

## Main Responsibility

Generate fake user activities and save logs.

---

## Tasks

### 1. Generate Random Activities

Generate:
- Logins
- Emails sent
- Emails opened
- Time online

---

### 2. Follow Statistics

Generated values should approximately follow:
- Mean
- Standard deviation

Use:

```python
random.gauss(mean, std)
```

---

### 3. Handle Event Types

Discrete:
- Integer values only

Continuous:
- Decimal values allowed

---

### 4. Save Log Files

Example:

```txt
Day 1
Logins:5
Emails sent:8
Time online:120.5
```

---

### 5. Show Progress

Example:

```txt
Generating Day 1...
Generating Day 2...
```

---

## Report Section

This member writes:
- Activity engine explanation
- Random generation explanation
- Log structure explanation

---

## Deadline

Finish within:
- 2–3 days

---

# Member 3 – Analysis Engine

## Main Responsibility

Analyze logs and calculate statistics.

---

## Tasks

### 1. Read Log Files

Need to:
- Open generated logs
- Read event values

---

### 2. Calculate Daily Totals

Example:

```txt
Day 1:
Logins = 5
Emails sent = 10
```

---

### 3. Calculate Mean

Formula:

Mean = Sum of values / Number of values

---

### 4. Calculate Standard Deviation

Formula:

Standard deviation = sqrt(sum((x - mean)^2) / n)

---

### 5. Save Analysis Results

Example:

```txt
Logins Mean = 4.2
Logins Std = 1.1
```

---

### 6. Handle Missing Data

Program should not crash if data is incomplete.

---

## Simplification Advice

Use Python built-in functions:

```python
statistics.mean()
statistics.stdev()
```

No need to build complicated calculations manually.

---

## Report Section

This member writes:
- Analysis engine explanation
- Statistics explanation
- Analysis output explanation

---

## Deadline

Finish within:
- 2 days

---

# Member 4 – Alert Engine & Final Integration

## Main Responsibility

Detect anomalies and combine all modules together.

---

## Tasks

### 1. Load New Statistics File

Need to:
- Accept another `Stats.txt`
- Generate new activity data

---

### 2. Calculate Anomaly Score

Deviation formula:

```txt
z = (x - mean) / std
```

Weighted anomaly formula:

```txt
Anomaly = sum(|z| × weight)
```

---

### 3. Calculate Threshold

Formula:

```txt
Threshold = 2 × sum(weights)
```

---

### 4. Detect Alerts

If:

```txt
Anomaly Counter >= Threshold
```

Then:

```txt
FLAGGED
```

Else:

```txt
OKAY
```

---

### 5. Integrate All Modules

Connect:
1. File reader
2. Activity generator
3. Analysis engine
4. Alert engine

---

### 6. Testing

Need to test:
- Different statistics files
- Different day counts
- Error handling

---

## Report Section

This member writes:
- Alert engine explanation
- Anomaly calculation explanation
- Testing and integration explanation

---

## Deadline

Finish within:
- 2–3 days

---

# IMPORTANT – Daily Integration

Do NOT wait until the final day.

Every day:
- Push code to GitHub
- Test together
- Merge together

Otherwise integration problems will become very serious later.

---

# Recommended Simple File Structure

```txt
main.py
reader.py
generator.py
analysis.py
alert.py
```

Keep the project simple.

---

# Recommended 1.5 Week Timeline

## Day 1–2
- Member 1 completes file reader
- Other members prepare module structure

---

## Day 3–5
- Member 2 completes activity generator
- Member 3 completes analysis engine

---

## Day 6–8
- Member 4 completes alert engine
- Group integration
- Debugging
- Testing

---

## Final 2–3 Days
- Complete report
- Prepare screenshots
- Final testing
- Prepare presentation

---

# Final Advice

## Do NOT aim for perfection

Focus on:
- Working program
- No crashes
- Basic anomaly detection

A simple working system is better than an unfinished advanced system.

---

# Recommended Technologies

| Task | Recommendation |
|---|---|
| Language | Python |
| Random generation | `random.gauss()` |
| Statistics | `statistics` module |
| File storage | `.txt` files |
| Collaboration | GitHub |
