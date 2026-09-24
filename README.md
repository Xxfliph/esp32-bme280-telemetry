# ESP32 BME280 Environmental Data Logger

A simple environmental data logging project using an **ESP32** and **BME280 sensor**. The ESP32 continuously measures temperature, humidity, and atmospheric pressure, sends the readings over serial communication, and a Python program records the data with timestamps. A separate Python script is used to visualize the collected data.

## Features

* Measures:

  * Temperature
  * Relative humidity
  * Atmospheric pressure
* Sends sensor data from the ESP32 over serial at **115200 baud**
* Logs measurements to a timestamped data file
* Visualizes collected data using Matplotlib
* Uses the BME280's I2C interface

## Hardware

* ESP32 development board
* BME280 environmental sensor
* USB cable
* Jumper wires / breadboard

## Software

* Arduino IDE
* Python 3
* `pyserial`
* `matplotlib`

## How It Works

The project has three main parts:

```text
BME280 Sensor
     │
     │ I2C
     ▼
   ESP32
     │
     │ Serial @ 115200 baud
     ▼
 Python Data Logger
     │
     │
     ▼
  data.txt
     │
     ▼
 Python Plotting Script
     │
     ▼
 Temperature / Humidity / Pressure Graphs
```

### 1. ESP32 Sensor Program

The ESP32 reads the BME280 once every second and sends the measurements over serial in the following format:

```text
temperature,humidity,pressure
```

For example:

```text
23.45,48.21,1012.36
```

The BME280 is initialized using I2C address `0x76`.

### 2. Python Data Logger

The Python logging script connects to the ESP32 through a serial port at **115200 baud**.

Each received measurement is given a timestamp and appended to `data.txt`.

The resulting file follows this format:

```text
2026-09-24 15:32:01.123456,23.45,48.21,1012.36
2026-09-24 15:32:02.123456,23.46,48.19,1012.34
```

### 3. Python Visualization

The plotting script reads the recorded data and uses Matplotlib to create three plots:

* Temperature vs. Time
* Humidity vs. Time
* Pressure vs. Time

This makes it possible to observe how the environmental conditions change over the course of a measurement session.

## Setup

### ESP32

1. Connect the BME280 to the ESP32 using I2C.
2. Install the required Arduino libraries:

   * `Adafruit BME280 Library`
   * `Adafruit Unified Sensor`
3. Upload the ESP32 code.
4. Open the Serial Monitor to verify that sensor readings are being transmitted.

### Python

Install the required packages:

```bash
pip install pyserial matplotlib
```

Update the serial port in the Python logger if necessary:

```python
ser = serial.Serial("COM3", 115200)
```

For example, your ESP32 may appear as `COM4` or another port depending on your computer.

### Running the Project

First, run the Python data logging script:

```bash
python data_logger.py
```

Leave it running while measurements are being collected.

Stop the logger when enough data has been recorded.

Then run the plotting script:

```bash
python plot_data.py
```

The recorded sensor data will be displayed as three graphs.

## File Structure

```text
BME280-Data-Logger/
│
├── esp32_bme280.ino      # ESP32 sensor code
├── data_logger.py         # Reads serial data and records measurements
├── plot_data.py           # Loads and plots recorded measurements
├── data.txt               # Recorded sensor data
└── README.md
```

## Example Output

The ESP32 outputs readings in this format:

```text
22.91,51.34,1014.27
22.93,51.29,1014.31
22.94,51.25,1014.28
```

The Python logger adds a timestamp:

```text
2026-09-24 15:32:01.123456,22.91,51.34,1014.27
2026-09-24 15:32:02.123456,22.93,51.29,1014.31
```

The plotting script then produces temperature, humidity, and pressure graphs against time.

## Future Improvements

Some possible improvements to the project include:

* Automatically detect the ESP32 serial port
* Save measurements as a proper `.csv` file
* Add configurable sampling intervals
* Add error handling for malformed serial data
* Display live sensor graphs while data is being collected
* Add additional sensors
* Calculate statistics such as minimum, maximum, and average values
* Add a real-time dashboard
* Store data in a database for longer-term monitoring

## What I Learned

This project provided hands-on experience with:

* ESP32 microcontrollers
* I2C communication
* Environmental sensors
* Serial communication
* Python file I/O
* Parsing sensor data
* Timestamping measurements
* Data visualization with Matplotlib
* Connecting embedded hardware with Python software
