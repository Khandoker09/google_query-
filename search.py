import webbrowser
import pandas as pd

lib=str(input(("Enter what you want to search for:")))
ur=("https://www.google.com/search?q="+lib+"&rlz=1C1CHBF_deDE982DE982&oq=funke+media&aqs=chrome..69i57j0i512l2j0i22i30l7.1927j0j7&sourceid=chrome&ie=UTF-8")
webbrowser.open_new(ur+lib)
