
class DesktopIconFileAction():
    # https://specifications.freedesktop.org/desktop-entry-spec/latest/ar01s11.html
    def __init__(self, identifier, name='', exec='', icon=''):
        self.identifier = identifier
        self.name = name
        self.exec = exec
        self.icon = icon

class DesktopIconFile() :
    # https://specifications.freedesktop.org/desktop-entry-spec/latest/ar01s06.html
    def __init__(self, 
        name:str,
        type:str, 
        exec:str, 
        file_name:str='', 
        file_path:str='',
        terminal:bool='', 
        icon:str='', 
        comment:str='', 
        categories=[], 
        version:str=-1, 
        generic_name='', 
        no_display:bool='', 
        hidden:bool='',
        try_exec='',
        path:str='',
        actions=[],
        actions_ojb=[],
        url:str='',
        single_main_window:bool='',
        only_show_in=[],
        not_show_in=[],
        dbus_activatable:bool='',
        mime_type=[],
        implements=[],
        keywords=[],
        startup_notify:bool='',
        startup_wm_class:str='',
        prefers_non_default_gpu:bool='',
        other_entries=[]
        ):
        self.name = name
        self.type = type
        self.exec = exec
        self.file_name = file_name
        self.file_path = file_path
        self.terminal = terminal
        self.icon = icon
        self.comment = comment
        self.categories = list(categories)
        self.version = version
        self.generic_name = generic_name
        self.hidden = hidden
        self.no_display = no_display
        self.try_exec = try_exec
        self.path = path
        self.actions = list(actions)
        self.actions_ojb = list(actions_ojb)
        self.url = url
        self.single_main_window = single_main_window
        self.only_show_in = list(only_show_in)
        self.not_show_in = list(not_show_in)
        self.dbus_activatable = dbus_activatable
        self.mime_type = mime_type
        self.implements = list(implements)
        self.keywords = list(keywords)
        self.startup_notify = startup_notify
        self.startup_wm_class = startup_wm_class
        self.prefers_non_default_gpu = prefers_non_default_gpu
        self.other_entries = list(other_entries)
    
    def __str__(self):
        str_obj = '>>> Desktop Entry <<<'
        str_obj += '\nName : ' + self.name
        str_obj += '\nType : ' + self.type
        str_obj += '\nExec : ' + self.exec
        str_obj += '\nComment : ' + self.comment
        str_obj += '\nIcon : ' + self.icon
        str_obj += '\nTerminal : ' + str(self.terminal)
        if len(self.categories) > 0 : str_obj += '\nCategories : ' + str(self.categories)
        if self.version != -1 : str_obj += '\nVersion : ' + str(self.version)

        return str_obj

    # def __lt__(self, other):
    #     return self.name > other.name
