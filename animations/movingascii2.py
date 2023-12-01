import os
import time

# ASCII Art Frames
art_frames = [
    """
            )           )                  (    (     
        ( /(        ( /(           (      )\ ) )\ )  
        )\())    )  )\())          )\    (()/((()/(  
        ((_)\  ( /( ((_)\   ___  ((((_)(   /(_))/(_)) 
        _((_) )(_)) _((_)  |___|  )\ _ )\ (_)) (_))   
        | \| |((_)_ | \| |        (_)_\(_)|_ _|| _ \  
        | .` |/ _` || .` |         / _ \   | | |   /  
        |_|\_|\__,_||_|\_|        /_/ \_\ |___||_|_\ 
    """,
    """
            ()           ()                  ()    )     
         ) \ )        ) \)           (      )\ ) )\ )  
        (/ ())    )  )\())          )\    (()/((()/(  
         ((_)\  ( /( ((_)\  ___   ((((_)(   /(_))/(_)) 
         _(_(_\ )/_))(_(_\)|___|   (/ _ )/ (_)( (_))   
        | \| |((_)_ | \| |        (_)_\(_)|_ _|| _ \ 
        | .` |/ _` || .` |         / _ \   | | |   /  
        |_|\_|\__,_||_|\_|        /_/ \_\ |___||_|_\ 
    """,
]

# Animation Loop
frame_count = len(art_frames)
for i in range(100):  # Loop for 100 iterations
    os.system("cls" if os.name == "nt" else "clear")  # Clear screen
    print(art_frames[i % frame_count])  # Print current frame
    time.sleep(0.2)  # Adjust speed as needed
