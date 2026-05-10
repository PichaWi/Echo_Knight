import csv
import datetime
import os

class StatsManager:
    def __init__(self, filename="game_stats.csv"):
        self.filename = filename
        self.current_run_data = {
            "enemies_defeated": 0,
            "distance_traveled": 0,
            "start_time": None,
            "death_cause": "Unknown"
        }
        # Create file with headers if it doesn't exist
        if not os.path.exists(self.filename):
            with open(self.filename, mode='w', newline='') as f:
                writer = csv.writer(f)
                writer.writerow(["timestamp", "enemies_defeated", "distance_traveled", "survival_time", "death_cause"])

    def start_new_run(self):
        """Called by main.py when a new game starts."""
        self.current_run_data = {
            "enemies_defeated": 0,
            "distance_traveled": 0,
            "start_time": datetime.datetime.now(),
            "death_cause": "Survived" # Default until death occurs
        }

    def record_kill(self):
        """Called by entities.py or main.py when an enemy health reaches 0."""
        self.current_run_data["enemies_defeated"] += 1

    def update_distance(self, pixels):
        """Called by entities.py when the player moves."""
        self.current_run_data["distance_traveled"] += abs(pixels)

    def log_death(self, cause):
        """Called by entities.py when player health <= 0."""
        self.current_run_data["death_cause"] = cause
        self.save_run()

    def save_run(self):
        """Writes the current run statistics to the CSV file."""
        if self.current_run_data["start_time"] is None:
            return

        end_time = datetime.datetime.now()
        duration = (end_time - self.current_run_data["start_time"]).total_seconds()
        timestamp = self.current_run_data["start_time"].strftime("%a %b %d %H:%M:%S %Y")

        with open(self.filename, mode='a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([
                timestamp,
                self.current_run_data["enemies_defeated"],
                int(self.current_run_data["distance_traveled"]),
                round(duration, 2),
                self.current_run_data["death_cause"]
            ])
        
        # Reset start_time to prevent double-logging
        self.current_run_data["start_time"] = None