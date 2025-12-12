import psutil # library to monitor the system
import platform 
import time #library for time mangement 
import socket #library for network management to retrieve ip
import pprint #library to display dicitionary in a pretty way
import pathlib
import jinja2

""" Jinja2 setup"""

env = jinja2.Environment(loader=jinja2.FileSystemLoader('web_pages'))
template = env.get_template('template.html')
output_folder = pathlib.Path("C:/Users/sofia/Downloads/AAA/web_pages")
output_file_path = output_folder / "index.html"

""" informations CPU """

amount_of_cores = psutil.cpu_count() #var that stores the amount of cores 
current_cpu_frequency = round(psutil.cpu_freq().current / 1024, 2) #var that stores the current CPU frequency
usage_cpu = psutil.cpu_percent(0) #var that stores pourcentage of CPU usage in an interval of X seconds

""" informations RAM """

memory = psutil.virtual_memory() #var that stores a tuple a tuple of informations about memory
used_memory = round(memory.used / (1024 ** 3), 2)#var storing the used  memory in gb round() to get only two decimals
total_memory = round(memory.total / (1024 ** 3), 2) #var storing the total memory in gb
used_memory_percent = memory.percent #var storing the percentage of used memory 

""" informations systeme """

machine_name = platform.node() #var storing the name of the machine
os_name_version =platform.platform() #var storing the name and version of OS
boot_time = psutil.boot_time() #var storing the boot time
time_since_boot = round((time.time()-psutil.boot_time()) / 3600 , 2) #var storing time since boot
users = psutil.users()# Get the list of users
number_users = len(users) #get the length of the list of users in other words the amount of users
host = socket.gethostname() #get the host's name (machine)
ip_address = socket.gethostbyname(host) #get ip adress using the host's name

""" informations about processes """

dictionary_of_pid= {} #dictionary containing the processes 
processes = list(psutil.process_iter())


for p in processes: #go through all the processes 
        p.cpu_percent() # get the interval

time.sleep(0)

for p in processes:
        cpu = p.cpu_percent() / amount_of_cores #CPU usage per core of process
        name = p.name() #process' name
        mem = p.memory_percent() #memory usage of process
        
        dictionary_of_pid[p.pid] = { #fill the dictionary with corresponding items
            'name': name,
            'ram_percent': mem,
            'cpu_percent': cpu
        }
#pprint.pprint(dictionary_of_pid) #display the dictionary using pretty print 

#top three per CPU consumption usage
cpu_consumption_list = []
for pid, details in dictionary_of_pid.items(): #loop through the dictionary 
    cpu = details['cpu_percent']
    name = details['name']
    cpu_consumption_list.append([round(cpu,2), name]) #list of CPU consumption with corresponding process'    
cpu_consumption_list.sort(reverse=True) #sort from the end
top_3_cpu = cpu_consumption_list[:3] #sort the top three
for item in top_3_cpu:
    print(f"Process: {item[1]}, CPU: {item[0]:.2f}%")

#top three per RAM consumption usage
mem_consumption_list = []
for pid, details in dictionary_of_pid.items(): #loop through the dictionary 
    mem = details['ram_percent']
    name = details['name']
    mem_consumption_list.append([round(mem,2), name]) #list of RAM consumption with corresponding process'    
mem_consumption_list.sort(reverse=True) #sort from the end
top_3_ram = mem_consumption_list[:3] #sort the top three
for item in top_3_ram:
    print(f"Process: {item[1]}, RAM: {item[0]:.2f}%")



""" informations about folder """

folder_to_analyze = pathlib.Path ("C:/Users/yaour/Desktop/AAA/AAA") #get the path of the folder to analyze (to change depending on the system)
extensions = ['.txt', '.py', '.pdf', '.jpg'] #list of extenstions to count
count_ext = {ext : 0 for ext in extensions} #dictionary of extensions and their amount

for file in folder_to_analyze.rglob('*'): #looping through the entirety of the folder (global) recursive
    if file.suffix in count_ext:
        count_ext[file.suffix] += 1

percent_ext = {}
pprint.pprint(count_ext)

total_files = sum(count_ext.values()) #sum of the amount of extensions 
if total_files > 0:
    for exten, count in count_ext.items(): #count the extensions 
        pct = (count / total_files) * 100
        percent_ext[exten] = pct 
        print(f"{exten} : {pct:.2f}%") # :.2f format decimal
else:
    print("Aucun fichier correspondant trouvé pour calculer des pourcentages.")

""" index generation"""

output = template.render(
    # System Info
    machine=machine_name, #var storing the name of the machine
    os=os_name_version, #var storing the name and version of OS
    boot_time_sec=boot_time, #var storing the boot time
    boot_time_since_boot_sec=time_since_boot,
    amount_of_users = #var storing time since boot
    number_users, #get the amount of users
    ip_addr = ip_address, #get ip adress using the host's name
    
    # CPU Data
    cores = amount_of_cores,#var that stores the amount of cores 
    freq = current_cpu_frequency,#var that stores the current CPU frequency
    cpu_usage = usage_cpu,#var that stores pourcentage of CPU usage
    
    # RAM Data
    total_ram=total_memory, #var storing the total memory
    used_ram_gb=used_memory, #var storing the used memory
    percentage_memory = used_memory_percent, #var storing the percentage of used memory
    
    # Process Lists (The Top 3 lists)
    top_cpu_processes=top_3_cpu, #var storing the top 3 process in cpu usage
    top_ram_processes=top_3_ram, #var storing the top 3 process in cpu usage

    # File Data
    amount_files_per_extensions=count_ext, #list of extenstions to count
    percentage_files = percent_ext
)

with open(output_file_path, "w") as file:
    file.write(output)
