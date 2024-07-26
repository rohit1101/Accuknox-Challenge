import psutil
import logging
from datetime import datetime
import time

# Set up logging
logging.basicConfig(filename='system_health.log', level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

# default thresholds
CPU_THRESHOLD = 80  
MEMORY_THRESHOLD = 80 
DISK_THRESHOLD = 80 
PROCESS_THRESHOLD = 300

def cpu_health_check():
    cpu_usage = psutil.cpu_percent(interval=1)
    if cpu_usage > CPU_THRESHOLD:
        logging.warning(f'CPU usage exceeded: {cpu_usage}%')
    return cpu_usage

def memory_health_check():
    memory = psutil.virtual_memory()
    memory_usage = memory.percent
    if memory_usage > MEMORY_THRESHOLD:
        logging.warning(f'memory usage exceeded: {memory_usage}%')
    return memory_usage

def disk_health_check():
    disk = psutil.disk_usage('/')
    disk_usage = disk.percent
    if disk_usage > DISK_THRESHOLD:
        logging.warning(f'disk usage exceeded: {DISK_THRESHOLD-disk_usage}%')
    return disk_usage

def processes_health_check():
    process_count = len(psutil.pids())
    if process_count > PROCESS_THRESHOLD:
        logging.warning(f'Number of processes exceeded: {PROCESS_THRESHOLD-process_count}')
    return process_count

def main():
    # log system metrics every 30 seconds
    while True:
        cpu_usage = cpu_health_check() 
        memory_usage = memory_health_check()
        disk_usage = disk_health_check()
        process_count = processes_health_check()
        
        print(f'{datetime.now()} - CPU: {cpu_usage}%, Memory: {memory_usage}%, Disk: {disk_usage}%, Processes: {process_count}')
        time.sleep(30)

if __name__ == '__main__':
    main()
