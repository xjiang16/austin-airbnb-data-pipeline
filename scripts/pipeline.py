import subprocess
import sys
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

scripts = [
    "scripts/transform_data.py",
    "scripts/validate_data.py",
    "scripts/load_to_postgres.py",
]

for script in scripts:
    print(f"\nRunning {script}...\n")

    result = subprocess.run([sys.executable, script])

    if result.returncode != 0:
        logging.error(f"{script} failed.")
        sys.exit(1)

logging.info("Pipeline completed successfully.")