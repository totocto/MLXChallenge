from codecarbon import EmissionsTracker

tracker = EmissionsTracker()

tracker.start()

### YOUR FIT SHOULD BE HERE

emissions: float = tracker.stop()

print(f"Emissions: {emissions} kg")