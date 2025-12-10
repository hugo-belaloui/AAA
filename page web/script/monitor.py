import psutil # import de la bibiliotheque pour monitor le system
import platform 
import time #library for time mangement 
import socket #library for network management to retrieve ip
import pprint #library to display dicitionary in a pretty way
import pathlib

""" informations CPU """

print(psutil.cpu_count()) #fonction pour compter le nombre de coeurs
print(psutil.cpu_freq().current) #fonction pour recuperer la frequence CPU
print(psutil.cpu_percent(0)) #fonction pour recuperer le pourcentage d'utilisation CPU avec interval de temps en seconde

""" informations RAM """

print(psutil.virtual_memory()) #fonction qui retourne un tuple d'informations sur la memoire en byte ! 
memory = psutil.virtual_memory()
print(memory.used) #recupere du tuple uniquement la memoire utilisé 
print(memory.total) #recupere du tuple uniquement la memoire totale
print(memory.percent) #recupere du tuple uniquement le pourcentage de memoire utilisé

""" informations systeme """

print(platform.node()) #recupere le nom de la machine
print(platform.platform())
print(platform.system()) #recupere le nom system d'exploitation 
print(platform.version()) #recupere la version du system d'exploitation
print(psutil.boot_time()) #recupere l'heure de boot
print(time.time()-psutil.boot_time()) #recupere le temps écoulé depuis le démarage
print(psutil.users()) #tuple contenant infos sur les users
users = psutil.users()# Get the list of users
number_users = len(users) #get the length of the list of users in other words the amount of users
print(number_users)
host = socket.gethostname() #get the host's name (machine)
print(host)
ip_address = socket.gethostbyname(host) #get ip adress using the host's name
print (ip_address)

""" informations about processes """

dictionary_of_pid= {}
processes = list(psutil.process_iter())
cpu_count = psutil.cpu_count()

for p in processes:
        p.cpu_percent()

time.sleep(0)

for p in processes:
        cpu = p.cpu_percent() / cpu_count
        
        name = p.name()
        mem = p.memory_info().rss  
        
        dictionary_of_pid[p.pid] = {
            'name': name,
            'ram_bytes': mem,
            'cpu_percent': cpu
        }
pprint.pprint(dictionary_of_pid)


cpu_consumption_list = []

# 2. Loop through your complex dictionary
for pid, details in dictionary_of_pid.items():
    cpu = details['cpu_percent']
    name = details['name']
    
    # 3. Add a list to simple_list. 
    # IMPORTANT: Put 'cpu' first! Python sorts by the first item it sees.
    cpu_consumption_list.append([cpu, name, pid])
    

# 4. Sort the list. 
# Since 'cpu' is index 0, it sorts by CPU automatically.
cpu_consumption_list.sort(reverse=True)

# 5. Get the top 3
top_3 = cpu_consumption_list[:3]

# Print them out
for item in top_3:
    print(f"Process: {item[1]}, CPU: {item[0]}%")

""" informations about folder """

folder_to_analyze = pathlib.Path ("C:/Users/pc/Desktop/AAA")
extensions = ['.txt', '.py', '.pdf', '.jpg']
count_ext = {ext : 0 for ext in extensions}

for file in folder_to_analyze.rglob('*'):
    if file.suffix in count_ext:
        count_ext[file.suffix] += 1

pprint.pprint(count_ext)

total_files = sum(count_ext.values())
if total_files > 0:
    for ext, count in count_ext.items():
        percentile = (count / total_files) * 100
        print(f"{ext} : {percentile:.2f}%") # :.2f format decimal
else:
    print("Aucun fichier correspondant trouvé pour calculer des pourcentages.")

html = open("template.html").read()
print(html)


html = html.replace(f"RAM, {platform.node}")


with open("index.html", "w") as fp:
    fp.write(html)