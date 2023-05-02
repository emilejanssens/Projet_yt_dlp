import subprocess
import random
import string

# Number of iterations
num_iter = 100

def generate_url(id_size, str_url):
    """Generate a random url
    Parameters
    ----------
    id_size : size of the id (int)
    str_url : url string (str)
    
    Returns
    -------
    an random url (str)
    """
    # Generate a random YouTube video ID
    video_id = ''.join(random.choice(string.ascii_lowercase + string.digits) for i in range(id_size))
    
    return str_url + video_id
    
    
def mutate_url(url):
    """Mutation of an url
    
    Parameters
    ----------
    url : url to mutate (str)
    
    Returns
    -------
    type_mutation : type of mutation (str)
    mutated_url : mutated url (str)
    """
    # Convertir l'URL en une liste de caractères pour pouvoir la modifier
    url_list = list(url)
    
    # Choisir aléatoirement le type de mutation à effectuer
    type_mutation = random.choice(["change", "delete", "add"])
    
    if type_mutation == "change":
        # Choisir un caractère aléatoire à remplacer
        index = random.randint(0, len(url_list) - 1)
        
        # Remplacer le caractère par un autre caractère aléatoire
        url_list[index] = random.choice(string.ascii_lowercase + string.digits)
        
    elif type_mutation == "delete":
        # Choisir un caractère aléatoire à supprimer
        index = random.randint(0, len(url_list) - 1)
        
        # Supprimer le caractère de la liste
        url_list.pop(index)
        
    else :
        # Choisir un caractère aléatoire à ajouter
        char = random.choice(string.ascii_lowercase + string.digits)
        
        # Choisir un index aléatoire pour ajouter le caractère
        index = random.randint(0, len(url_list))
        
        # Ajouter le caractère à la liste
        url_list.insert(index, char)
    
    # Rejoindre les caractères pour former une nouvelle URL mutée
    mutated_url = ''.join(url_list)
    
    return type_mutation, mutated_url


COMMAND = "yt-dlp {} -P ./trash"

with open('logs.txt', 'a') as f:
    for i in range(num_iter):
        
        # Generate a random URL
        url = random.choice([generate_url(11, "https://www.youtube.com/watch?v="),
                            generate_url(8, "https://player.vimeo.com/video/"),
                            generate_url(7, "https://www.dailymotion.com/video/"),
                            generate_url(9, "https://www.deezer.com/fr/album/"),
                            generate_url(11, "https://youtu.be/"),
                            generate_url(14, "https://www.amazon.com/gp/customer-reviews/"),
                            generate_url(20, "https://www.tiktok.com/@reussironly/video/"),
                            ])

        # Mutate the URL
        type_mutation, mutated_url = mutate_url(url)
        
        print(f"Iter : {i}")
        
        message = f"No mutated url : {url} [{type_mutation}]" 
        print(message) 
        f.write(message)
            
        try:
            output = subprocess.check_output(COMMAND.format(
                mutated_url), shell=True, stderr=subprocess.STDOUT)
            
            message = f"Command succeeded with input: {mutated_url}\n"
            print(message)
            # print(output)

        except subprocess.CalledProcessError as e:
            
            message = f"Command succeeded with input: {mutated_url}\n{e.output}\n"
            print(message)
            
        f.write(message + "\n")