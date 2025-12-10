import psutil # library to monitor the system
import platform 
import time #library for time mangement 
import socket #library for network management to retrieve ip
import pprint #library to display dicitionary in a pretty way
import pathlib

""" informations CPU """

amount_of_cores = psutil.cpu_count() #var that stores the amount of cores 
current_cpu_frequency = psutil.cpu_freq().current #var that stores the current CPU frequency
usage_cpu = psutil.cpu_percent(0) #var that stores pourcentage of CPU usage in an interval of X seconds

""" informations RAM """

memory = psutil.virtual_memory() #var that stores a tuple a tuple of informations about memory
used_memory = memory.used / (1024 ** 3)#var storing the used  memory in gb
total_memory = memory.total / (1024 ** 3) #var storing the total memory in gb
used_memory = memory.percent #var storing the percentage of used memory 
""" informations systeme """

machine_name = platform.node() #var storing the name of the machine
os_name_version =platform.platform() #var storing the name and version of OS
boot_time = psutil.boot_time() #var storing the boot time
time_since_boot = (time.time()-psutil.boot_time()) #var storing time since boot
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
pprint.pprint(dictionary_of_pid) #display the dictionary using pretty print 

#top three per CPU consumption usage
cpu_consumption_list = []
for pid, details in dictionary_of_pid.items(): #loop through the dictionary 
    cpu = details['cpu_percent']
    name = details['name']
    cpu_consumption_list.append([cpu, name, pid]) #list of CPU consumption with corresponding process'    
cpu_consumption_list.sort(reverse=True) #sort from the end
top_3 = cpu_consumption_list[:3] #sort the top three
for item in top_3:
    print(f"Process: {item[1]}, CPU: {item[0]:.2f}%")

#top three per RAM consumption usage
mem_consumption_list = []
for pid, details in dictionary_of_pid.items(): #loop through the dictionary 
    mem = details['ram_percent']
    name = details['name']
    mem_consumption_list.append([mem, name, pid]) #list of RAM consumption with corresponding process'    
mem_consumption_list.sort(reverse=True) #sort from the end
top_3 = mem_consumption_list[:3] #sort the top three
for item in top_3:
    print(f"Process: {item[1]}, RAM: {item[0]:.2f}%")



""" informations about folder """

folder_to_analyze = pathlib.Path ("C:/Users/pc/Desktop/AAA") #get the path of the folder to analyze (to change depending on the system)
extensions = ['.txt', '.py', '.pdf', '.jpg'] #list of extenstions to count
count_ext = {ext : 0 for ext in extensions} #dictionary of extensions and their amount

for file in folder_to_analyze.rglob('*'): #looping through the entirety of the folder (global)
    if file.suffix in count_ext:
        count_ext[file.suffix] += 1

pprint.pprint(count_ext)

total_files = sum(count_ext.values()) #sum of the amount of extensions 
if total_files > 0:
    for ext, count in count_ext.items(): #count the extensions 
        percentile = (count / total_files) * 100
        print(f"{ext} : {percentile:.2f}%") # :.2f format decimal
else:
    print("Aucun fichier correspondant trouvé pour calculer des pourcentages.")