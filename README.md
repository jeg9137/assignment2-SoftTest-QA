Detailed setup and execution instructions:

Step 1 – Install Python:

• Go to https://www.python.org/downloads/

• Download the latest Python 3.x Windows installer

• Run the installer and check “Add Python to PATH” before clicking Install

• Verify by opening the PowerShell terminal and running python –version

Step 2 – Download the application:

•	Go to the GitHub repository, assignment2-SoftTest-QA, repository link:
    
    https://github.com/jeg9137/assignment2-SoftTest-QA

•	Download bmi_calculator.py and test_bmi_calculator.py

•	Place both files in the same folder

Step 3 – Install pytest:

•	Open the Powershell terinal in the folder containing your files

•	Run the command: py -m pip install pytest OR python -m pip install pytest

Step 4 – Run the application:

•	Run the command: py bmi_calculator.py or python bmi_calculator.py

Step 5 – Run the tests:

•	Run the command: python -m pytest test_bmi_calculator.py -v OR py -m pytest test_bmi_calculator.py -v
