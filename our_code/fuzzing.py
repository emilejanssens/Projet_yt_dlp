import subprocess

# Entrées valides 
inputs = ["https://www.youtube.com/watch?v=F_mqShCzlAY","http://www.youtube.com/watch?v=pRpeEdMmmQ0"]

COMMAND = "yt-dlp {} -P ./trash"

for input_str in inputs:
    try:
        output = subprocess.check_output(COMMAND.format(input_str), shell=True, stderr=subprocess.STDOUT)
        print(f"Command succeeded with input: {input_str}")
        print(output.decode())
        
    except subprocess.CalledProcessError as e:
        
        print(f"Command failed with input: {input_str}")
        print(e.output.decode())

