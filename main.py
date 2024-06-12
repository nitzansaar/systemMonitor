import psutil
import time
import threading
from tkinter import Tk, Label, StringVar

class SystemMonitorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("System Monitor")

        self.cpu_label = Label(root, text="CPU Usage: ", font=("Helvetica", 14))
        self.cpu_label.pack()
        self.cpu_var = StringVar()
        self.cpu_value = Label(root, textvariable=self.cpu_var, font=("Helvetica", 14))
        self.cpu_value.pack()

        self.memory_label = Label(root, text="Memory Usage: ", font=("Helvetica", 14))
        self.memory_label.pack()
        self.memory_var = StringVar()
        self.memory_value = Label(root, textvariable=self.memory_var, font=("Helvetica", 14))
        self.memory_value.pack()

        self.disk_label = Label(root, text="Disk Usage: ", font=("Helvetica", 14))
        self.disk_label.pack()
        self.disk_var = StringVar()
        self.disk_value = Label(root, textvariable=self.disk_var, font=("Helvetica", 14))
        self.disk_value.pack()

        self.network_label = Label(root, text="Network Usage: ", font=("Helvetica", 14))
        self.network_label.pack()
        self.network_var = StringVar()
        self.network_value = Label(root, textvariable=self.network_var, font=("Helvetica", 14))
        self.network_value.pack()

        self.update_metrics()
    
    def get_system_metrics(self):
        cpu_usage = psutil.cpu_percent(interval=1)
        memory_info = psutil.virtual_memory()
        disk_info = psutil.disk_usage('/')
        net_info = psutil.net_io_counters()

        return {
            'cpu_usage': cpu_usage,
            'memory_total': memory_info.total,
            'memory_used': memory_info.used,
            'memory_free': memory_info.free,
            'disk_total': disk_info.total,
            'disk_used': disk_info.used,
            'disk_free': disk_info.free,
            'bytes_sent': net_info.bytes_sent,
            'bytes_received': net_info.bytes_recv
        }

    def update_metrics(self):
        metrics = self.get_system_metrics()
        self.cpu_var.set(f"{metrics['cpu_usage']}%")
        self.memory_var.set(f"{metrics['memory_used'] / (1024**3):.2f}GB used / {metrics['memory_total'] / (1024**3):.2f}GB total / {metrics['memory_free'] / (1024**3):.2f}GB free")
        self.disk_var.set(f"{metrics['disk_used'] / (1024**3):.2f}GB used / {metrics['disk_total'] / (1024**3):.2f}GB total / {metrics['disk_free'] / (1024**3):.2f}GB free")
        self.network_var.set(f"{metrics['bytes_sent'] / (1024**2):.2f}MB sent / {metrics['bytes_received'] / (1024**2):.2f}MB received")

        self.root.after(5000, self.update_metrics)  # Update every 5 seconds

def run_gui():
    root = Tk()
    app = SystemMonitorApp(root)
    root.mainloop()

if __name__ == "__main__":
    run_gui()
