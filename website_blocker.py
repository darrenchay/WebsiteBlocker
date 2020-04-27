#!/usr/bin/env python
import time
from win10toast import ToastNotifier
host_path = r"C:/Windows/System32/drivers/etc/hosts"
local_host = "127.0.0.1"

websites = ["www.facebook.com", "www.youtube.com", "facebook.com", "youtube.com", "www.github.com", "github.com"]

try:
    while True:
        with open(host_path, 'r+') as file:
            content = file.read()
            for website in websites:
                if website in content:
                    pass
                else:
                    # map hostname to localhost IP
                    file.write(local_host + " " + website + "\n")
        time.sleep(5)

except KeyboardInterrupt:
    with open(host_path, "r+") as file:
        content = file.readlines()
        file.seek(0)
        for line in content:
            if not any(website in line for website in websites):
                file.write(line)

            file.truncate()

    toast = ToastNotifier()
    toast.show_toast("Website Blocker", "Terminating Website Blocker...", duration=2)