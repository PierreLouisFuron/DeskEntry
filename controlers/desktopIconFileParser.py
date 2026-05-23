
from distutils.util import strtobool
from fileinput import filename
import os

from models.desktopIconFile import DesktopIconFile, DesktopIconFileAction

class DesktopIconFileParser:

    def __init__(self, path):
        self.path = path

    def retrieve_all_desktop_icon_files(self):
        dir_list = os.listdir(self.path)
        desktop_files = []
        for file in dir_list:
            if file.endswith('.desktop'):
                dif = DesktopIconFileParser.parse_desktop_file(self, file)
                desktop_files.append(dif)
        return desktop_files

    def parse_desktop_file(self, file_name):
        file = open(self.path + '/' + file_name, 'r')
        lines = file.readlines()
        dif = DesktopIconFile('', '', '', file_name=file_name, file_path=self.path)
        current_desktop_action = -1
        for line in lines:
            if '[Desktop Entry' in line:
                isDesktopEntry = True
                isDesktopAction = False
            if '[Desktop Action' in line:
                isDesktopEntry = False
                isDesktopAction = True
                current_desktop_action += 1
                dif.actions_ojb.append(DesktopIconFileAction(line.strip()[16:len(action_identifier)-1]))
                print('>>> action id : ' + action_identifier)
            if '=' in line:
                line = line.replace('\n', '')
                key = line.split('=')[0]
                value = line[line.find('=')+1:]
                if isDesktopEntry:
                    if key == 'Type': dif.type = value
                    elif key == 'Version': dif.version = value
                    elif key == 'Name':  #TODO: IMPROVE THIS PART WHEN ACTIONS ARE ENTRIES ARE HANDLE PROPERLY
                        if dif.name == '':
                            dif.name = value
                    elif key == 'GenericName': dif.generic_name = value
                    elif key == 'NoDisplay': dif.no_display = strtobool(value)
                    elif key == 'Comment': dif.comment = value
                    elif key == 'Icon': #TODO: IMPROVE THIS PART WHEN ACTIONS ARE ENTRIES ARE HANDLE PROPERLY
                        if dif.icon == '':
                            dif.icon = value
                    elif key == 'Hidden': dif.hidden = strtobool(value)
                    elif key == 'OnlyShowIn': dif.only_show_in = value.split(';')
                    elif key == 'NotShowIn': dif.not_show_in = value.split(';')
                    elif key == 'DBusActivatable': dif.dbus_activatable = value
                    elif key == 'TryExec': dif.try_exec = value
                    elif key == 'Exec': dif.exec = value
                    elif key == 'Path': dif.path = value
                    elif key == 'Terminal': dif.terminal = strtobool(value)
                    elif key == 'Actions': 
                        for action_identifier in value.split(';'):
                            if action_identifier != '':
                                dif.actions.append(action_identifier)
                    elif key == 'MimeType': dif.mime_type = value.split(';')
                    elif key == 'Categories': dif.categories = value.split(';')
                    elif key == 'Implements': dif.implements = value.split(';')
                    elif key == 'Keywords': dif.keywords = value.split(';')
                    elif key == 'StartupNotify': dif.startup_notify = strtobool(value)
                    elif key == 'StartupWMClass': dif.startup_wm_class = value
                    elif key == 'URL': dif.url = value
                    elif key == 'PrefersNonDefaultGPU': dif.prefers_non_default_gpu = strtobool(value)
                    elif key == 'SingleMainWindow': dif.single_main_window = strtobool(value)
                    else:
                        dif.other_entries.append([key, value])
                elif isDesktopAction:
                    print('dif action identifier : ' + dif.actions_ojb[current_desktop_action].identifier)
                    if key == 'Name': dif.actions_ojb[current_desktop_action].name = value
                    elif key == 'Icon': dif.actions_ojb[current_desktop_action].icon = value
                    elif key == 'Exec': dif.actions_ojb[current_desktop_action].exec = value
                    # else : 
                    #     print('There is an error somewhere - key : ' + key)
        return dif
    
    def parse_desktop_entry_line(self):
        return 0

    def parse_desktop_action_line(self):
        return 0

    def open_folder(self):
        os.system('xdg-open "%s"' % self.path)

    def create_desktop_file(self, dif):
        file = open(self.path + '/' + dif.file_name, 'w')
        file.write('[Desktop Entry]')
        file.write('\nName=' + dif.name)
        if dif.type: file.write('\nType=' + dif.type)
        if dif.url: file.write('\nURL=' + dif.url)
        if dif.exec: file.write(f"\nExec={dif.exec}")
        if dif.terminal: file.write(f"\nTerminal={dif.terminal}")
        file.close()