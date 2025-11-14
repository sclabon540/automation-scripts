import os
import logging

logging.basicConfig(
    filename="automation.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def run_automation():
    try:
        logging.info("Automation started")

        # Example task 1: Read a file
        input_file = "data.txt"
        if not os.path.exists(input_file):
            raise FileNotFoundError(f"{input_file} not found!")

        with open(input_file, "r") as file:
            content = file.read()
            logging.info(f"Read {input_file} successfully")

        # Example Task 2: Write backup file
        backup_file = "backup.txt"
        with open(backup_file, "w") as backup:
            backup.write(content)
            logging.info(f"{backup_file} created successfully")

        # Validation check
        if os.path.exists(backup_file):
            print("Automation completed: all tasks succeeded")
            logging.info("Automation completed: all tasks succeeded")
        else:
            raise Exception("Backup file not created!")

    except Exception as e:
        logging.exception("Automation failed")
        print("Error:", e)
        logging.error("Automation Failed")
        logging.error(str(e))

        #-------------------------
        # Run automation
        #-------------------------
if __name__ == "__main__":
    run_automation()


    