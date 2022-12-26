# Realops Time Converter
Convert times for realops arrival flights into departure times

### Requirements
* Python 3
* [Requests](https://requests.readthedocs.io/en/latest/)

### Usage
1. Put the properly formatted file for realops in the base directory with the name `flights.csv`
  1. It is recommended to make a copy because the script will over-write the file and may corrupt the file if the program is interrupted
2. Run the script: `python3 convert_times.py`
3. The output (in the correct format with the new date and departure time) will be in `flights.csv`
