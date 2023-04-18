# XAMPP-React-Controller

XAMPP-React-Controller is a Python script that provides a graphical user interface (GUI) for controlling XAMPP services (Apache and MySQL) and a React server.

## Prerequisites
- Python 3.x installed on your Windows machine
- tkinter library (which is usually included in Python standard library)

## Getting Started
1. Clone this repository to your local machine.
2. Open a command prompt or terminal window and navigate to the directory where you cloned the repository.
3. Run the following command to install the required dependencies:
```
pip install tk
```

4. Once the dependencies are installed, you can run the Python script using the following command:
```
python xampp_react_controller.py
```

This will open the GUI interface for controlling XAMPP services and the React server.

## Making the Python Script Executable
If you want to make the Python script executable without having to run it through the command prompt or terminal, you can create an executable (`.exe`) file. Here's how you can do it using the `pyinstaller` package:

1. Install `pyinstaller` by running the following command:
```
pip install pyinstaller
```

2. Once `pyinstaller` is installed, you can create an executable file using the following command:
```
pyinstaller --onefile xampp_react_controller.py
```
```
pyinstaller --onefile --noconsole my_script.py
```
This will create a standalone executable file in the `dist` directory within the cloned repository.

3. You can then distribute the executable file to other Windows machines without the need for Python or any dependencies. Users can simply double-click the executable file to run the XAMPP-React-Controller GUI.

## Exiting the Application
To exit the application, you can click the "Exit" button in the GUI interface, or simply close the window.

