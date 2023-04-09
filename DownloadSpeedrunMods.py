import os
import shutil
import urllib.request
import time
# get the username of the current user
username = os.getlogin()

# specify the folder to download the files to
folder_path = f"C:/Users/{username}/AppData/Roaming/.minecraft/mods"

# create the folder if it does not exist
if not os.path.exists(folder_path):
    os.makedirs(folder_path)

# specify the links to the files
links = [
    "https://cdn.modrinth.com/data/PNEi3GLK/versions/TilzJg8a/atum-1.1.3%2B1.16.5.jar",
    "https://cdn.modrinth.com/data/hvFnDODi/versions/0.1.2/lazydfu-0.1.2.jar",
    "https://cdn.modrinth.com/data/gvQqBUqZ/versions/mc1.16.5-0.6.6/lithium-fabric-mc1.16.5-0.6.6.jar",
    "https://cdn.modrinth.com/data/AANobbMI/versions/mc1.16.5-0.2.0/sodium-fabric-mc1.16.5-0.2.0%2Bbuild.4.jar",
    "https://cdn.modrinth.com/data/tKUU4TXD/versions/vBgg8ZKY/worldpreview-2.3.3%2B1.16.5.jar"
    "https://cdn.modrinth.com/data/jnkd7LkJ/versions/XsXpngi5/SpeedRunIGT-13.3%2B1.16.5.jar"
]

# download each file and save it to the specified folder
for link in links:
    file_name = link.split("/")[-1]
    file_path = os.path.join(folder_path, file_name)

    # Create a request object with URL and User-Agent headers
    req = urllib.request.Request(url=link, headers={'User-Agent': 'Mozilla/5.0'})

# Open the request and save the response to a file
    with urllib.request.urlopen(req) as response, open(file_path, "wb") as out_file:
        shutil.copyfileobj(response, out_file)

    print(f"[i] Sucsessfully Downloaded {file_name} to mods folder")
time.sleep(0.5)
print("[!] 𝗬𝗼𝘂 𝗡𝗼𝘄 𝗰𝗮𝗻 𝗹𝗮𝘂𝗻𝗰𝗵 𝗠𝗶𝗻𝗲𝗰𝗿𝗮𝗳𝘁 𝗙𝗮𝗯𝗿𝗶𝗰 𝟭.𝟭𝟲.𝟱")
