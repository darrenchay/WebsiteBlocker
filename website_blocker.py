#!/usr/bin/env python
import time
from win10toast import ToastNotifier
import atexit

host_path = r"C:/Windows/System32/drivers/etc/hosts"
local_host = "127.0.0.1"

websites = ["www.facebook.com", "www.youtube.com", "facebook.com", "youtube.com", "www.github.com", "github.com"]


def exit_handler():
    with open(host_path, "r+") as curr_file:
        file_content = curr_file.readlines()
        curr_file.seek(0)
        for line in file_content:
            if not any(curr_website in line for curr_website in websites):
                curr_file.write(line)

            curr_file.truncate()

    toast = ToastNotifier()
    toast.show_toast("Website Blocker", "Terminating Website Blocker...", duration=2)


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

finally:
    exit_handler()

