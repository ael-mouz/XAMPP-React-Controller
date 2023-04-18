import sys
import subprocess
import tkinter as tk

def start_services():
    try:
        # Start Apache
        subprocess.Popen(['C:\\xampp\\apache\\bin\\httpd.exe'], startupinfo=subprocess.STARTUPINFO(dwFlags=subprocess.STARTF_USESHOWWINDOW), stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        
        # Start MySQL
        subprocess.Popen(['C:\\xampp\\mysql\\bin\\mysqld.exe'], startupinfo=subprocess.STARTUPINFO(dwFlags=subprocess.STARTF_USESHOWWINDOW), stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        
        # Start React server
        subprocess.Popen(['cmd', '/c', 'start', 'npm', 'start'], cwd='C:\\Users\\SPARROW\\Desktop\\Formation', startupinfo=subprocess.STARTUPINFO(dwFlags=subprocess.STARTF_USESHOWWINDOW), stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        
        status_label.config(text='XAMPP services and React server started successfully!', fg='green')
    except Exception as e:
        status_label.config(text=f'Failed to start services: {e}', fg='red')

def stop_services():
    try:
        # Stop Apache
        subprocess.run(['C:\\xampp\\apache\\bin\\httpd.exe', '-k', 'stop'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        
        # Stop MySQL with empty password
        subprocess.run(['C:\\xampp\\mysql\\bin\\mysqladmin.exe', '-u', 'root', '-p'], input=b'', stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        
        # Stop React server
        subprocess.run(['taskkill', '/IM', 'node.exe', '/F'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        
        status_label.config(text='XAMPP services and React server stopped successfully!', fg='green')
    except Exception as e:
        status_label.config(text=f'Failed to stop services: {e}', fg='red')

def exit_app():
    root.destroy()  # Destroy the main window to exit the application

# Create the main window
root = tk.Tk()
root.title('XAMPP Services and React Server')
root.geometry('300x200') # Set the window size to 300x200

# Create label for displaying status messages
status_label = tk.Label(root, text='', fg='black')
status_label.pack(pady=10)

# Create buttons for starting and stopping services
start_button = tk.Button(root, text='Start Services', command=start_services)
start_button.pack(pady=10)

stop_button = tk.Button(root, text='Stop Services', command=stop_services)
stop_button.pack(pady=10)

# Create exit button
exit_button = tk.Button(root, text='Exit', command=exit_app)
exit_button.pack(pady=10)

# Start the main event loop
root.mainloop()
