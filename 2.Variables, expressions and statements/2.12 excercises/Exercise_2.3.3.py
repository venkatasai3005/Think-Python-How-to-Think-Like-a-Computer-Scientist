# Define the starting time
start_time_hours = 6
start_time_minutes = 52
start_time_seconds=0

# Define the time it takes to run 1 mile at an easy pace (8:15 per mile)
easy_pace_minutes = 8
easy_pace_seconds = 15

# Define the time it takes to run 3 miles at tempo (7:12 per mile)
tempo_pace_minutes = 7
tempo_pace_seconds = 12

# Calculate the total time for the run
total_run_time_minutes = 2 * easy_pace_minutes + 3 * tempo_pace_minutes
total_run_time_seconds = 2 * easy_pace_seconds + 3 * tempo_pace_seconds

# Add the total run time to the starting time
end_time_minutes = start_time_minutes + total_run_time_minutes
end_time_seconds = start_time_seconds + total_run_time_seconds

# Adjust the time if it goes over 60 minutes
if end_time_seconds >= 60:
    end_time_minutes += 1
    end_time_seconds -= 60

# Format the end time
end_time_hours = start_time_hours + (end_time_minutes // 60)
end_time_minutes %= 60

# Display the time you get home for breakfast
print(f'You get home for breakfast at {end_time_hours:02}:{end_time_minutes:02}')

# You get home for breakfast at 07:30
