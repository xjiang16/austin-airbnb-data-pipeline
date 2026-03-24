import subprocess
import sys

scripts = [
    "scripts/transform_data.py",
    "scripts/load_to_postgres.py",
]

for script in scripts:
    print(f"\nRunning {script}...\n")

    result = subprocess.run([sys.executable, script])

    if result.returncode != 0:
        print(f"\nRunning {script}...\n")
        sys.exit(1)

print("\nPipeline completed successfully.\n")