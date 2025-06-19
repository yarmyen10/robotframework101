from datetime import datetime
import sys, os
from random import choices
from functools import partial
import ttkbootstrap as ttk
from ttkbootstrap.style import Bootstyle
from tkinter.filedialog import askdirectory, askopenfilename
from ttkbootstrap.dialogs import Messagebox
from ttkbootstrap.constants import *
from tkinter.scrolledtext import ScrolledText
from ttkbootstrap.tooltip import ToolTip
from pathlib import Path
from tkinter import Toplevel
import tkinter.font as tkFont
import logic
import subprocess
import threading
import utils
import logging

PATH = Path(__file__).parent / 'assets'
if getattr(sys, 'frozen', False):
    PROJECTS_PATH = Path(sys.executable).parent.parent.parent.parent
    logging.info(f'PROJECTS_PATH: {PROJECTS_PATH}', )
else:
    PROJECTS_PATH = Path(__file__).parent.parent.parent



class RoboBuddy(ttk.Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Messagebox.ok(message=f"sys.executable:\n{sys.executable}")
        self.robo_logic = logic.RoboBuddyLogic(self)
        self.robo_utils = utils.RoboBuddyUtils()
        self.pack(fill=BOTH, expand=YES)
        self.modal = {}
        # print('PROJECTS_PATH:', PROJECTS_PATH)
        

        image_files = {
            'properties-dark': 'icons8_settings_24px.png',
            'properties-light': 'icons8_settings_24px_2.png',
            # 'add-to-robo-dark': 'icons8_add_folder_24px.png',
            'add-to-robo-dark': 'add-robo-dark.png',
            'add-to-robo-light': 'icons8_add_book_24px.png',
            'stop-robo-dark': 'icons8_cancel_24px.png',
            'stop-robo-light': 'icons8_cancel_24px_1.png',
            'play': 'icons8_play_24px_1.png',
            'play16' : 'icons8_play_16px.png',
            'refresh': 'icons8_refresh_24px_1.png',
            'stop-dark': 'icons8_stop_24px.png',
            'stop-light': 'icons8_stop_24px_1.png',
            'opened-folder': 'icons8_opened_folder_24px.png',
            'logo': 'Robot-framework-logo.png',
            'edge_icon': 'microsoft.png',
            'firefox_icon': 'firefox.png',
        }

        self.photoimages = []
        imgpath = Path(__file__).parent / 'assets'
        for key, val in image_files.items():
            _path = self.robo_utils.resource_path(imgpath / val)
            self.photoimages.append(ttk.PhotoImage(name=key, file=_path))

        # buttonbar
        buttonbar = ttk.Frame(self, style='primary.TFrame')
        buttonbar.pack(fill=X, pady=1, side=TOP)

        ## new robo
        #_func = lambda: Messagebox.ok(message='Adding new robo')
        btn = ttk.Button(
            master=buttonbar, text='New robo set',
            image='add-to-robo-light',
            compound=LEFT,
            command=self.new_robo_modal
        )
        btn.pack(side=LEFT, ipadx=5, ipady=5, padx=(1, 0), pady=1)

        ## Robo
        # _func = lambda: Messagebox.ok(message='Play robo...')
        btn = ttk.Button(
            master=buttonbar,
            text='Robo',
            image='play',
            compound=LEFT,
            command=self.play_robo_modal
        )
        btn.pack(side=LEFT, ipadx=5, ipady=5, padx=0, pady=1)

        ## refresh
        _func = lambda: Messagebox.ok(message='Refreshing...')
        btn = ttk.Button(
            master=buttonbar,
            text='Refresh',
            image='refresh',
            compound=LEFT,
            command=_func
        )
        btn.pack(side=LEFT, ipadx=5, ipady=5, padx=0, pady=1)

        ## stop
        _func = lambda: Messagebox.ok(message='Stopping robo.')
        btn = ttk.Button(
            master=buttonbar,
            text='Stop',
            image='stop-light',
            compound=LEFT,
            command=_func
        )
        btn.pack(side=LEFT, ipadx=5, ipady=5, padx=0, pady=1)

        ## settings
        _func = lambda: Messagebox.ok(message='Changing settings')
        btn = ttk.Button(
            master=buttonbar,
            text='Settings',
            image='properties-light',
            compound=LEFT,
            command=_func
        )
        btn.pack(side=LEFT, ipadx=5, ipady=5, padx=0, pady=1)

        # left panel
        left_panel = ttk.Frame(self, style='bg.TFrame')
        left_panel.pack(side=LEFT, fill=Y)

        ## backup summary (collapsible)
        bus_cf = CollapsingFrame(left_panel)
        bus_cf.pack(fill=X, pady=1)

        ## container
        bus_frm = ttk.Frame(bus_cf, padding=5)
        bus_frm.columnconfigure(1, weight=1)
        bus_cf.add(
            child=bus_frm,
            title='Robo Summary',
            bootstyle=SECONDARY)

        ## destination
        lbl = ttk.Label(bus_frm, text='Destination:')
        lbl.grid(row=0, column=0, sticky=W, pady=2)
        lbl = ttk.Label(bus_frm, textvariable='destination')
        lbl.grid(row=0, column=1, sticky=EW, padx=5, pady=2)
        self.setvar('destination', 'd:/test/')

        ## last run
        lbl = ttk.Label(bus_frm, text='Last Run:')
        lbl.grid(row=1, column=0, sticky=W, pady=2)
        lbl = ttk.Label(bus_frm, textvariable='lastrun')
        lbl.grid(row=1, column=1, sticky=EW, padx=5, pady=2)
        self.setvar('lastrun', '14.06.2021 19:34:43')

        ## files Identical
        lbl = ttk.Label(bus_frm, text='Files Identical:')
        lbl.grid(row=2, column=0, sticky=W, pady=2)
        lbl = ttk.Label(bus_frm, textvariable='filesidentical')
        lbl.grid(row=2, column=1, sticky=EW, padx=5, pady=2)
        self.setvar('filesidentical', '15%')

        ## section separator
        sep = ttk.Separator(bus_frm, bootstyle=SECONDARY)
        sep.grid(row=3, column=0, columnspan=2, pady=10, sticky=EW)

        ## properties button
        _func = lambda: Messagebox.ok(message='Changing properties')
        bus_prop_btn = ttk.Button(
            master=bus_frm,
            text='Properties',
            image='properties-dark',
            compound=LEFT,
            command=_func,
            bootstyle=LINK
        )
        bus_prop_btn.grid(row=4, column=0, columnspan=2, sticky=W)

        ## add to backup button
        _func = lambda: Messagebox.ok(message='Adding to robo')
        add_btn = ttk.Button(
            master=bus_frm,
            text='Add to robo',
            image='add-to-robo-dark',
            compound=LEFT,
            command=_func,
            bootstyle=LINK
        )
        add_btn.grid(row=5, column=0, columnspan=2, sticky=W)

        # backup status (collapsible)
        status_cf = CollapsingFrame(left_panel)
        status_cf.pack(fill=BOTH, pady=1)

        ## container
        status_frm = ttk.Frame(status_cf, padding=10)
        status_frm.columnconfigure(1, weight=1)
        status_cf.add(
            child=status_frm,
            title='Robo Status',
            bootstyle=SECONDARY
        )
        ## progress message
        lbl = ttk.Label(
            master=status_frm,
            textvariable='prog-message',
            font='Helvetica 10 bold'
        )
        lbl.grid(row=0, column=0, columnspan=2, sticky=W)
        self.setvar('prog-message', 'Running Robo Script...')

        ## progress bar
        pb = ttk.Progressbar(
            master=status_frm,
            variable='prog-value',
            bootstyle=SUCCESS
        )
        pb.grid(row=1, column=0, columnspan=2, sticky=EW, pady=(10, 5))
        self.setvar('prog-value', 71)

        ## time started
        lbl = ttk.Label(status_frm, textvariable='prog-time-started')
        lbl.grid(row=2, column=0, columnspan=2, sticky=EW, pady=2)
        self.setvar('prog-time-started', 'Started at: 14.06.2021 19:34:56')

        ## time elapsed
        lbl = ttk.Label(status_frm, textvariable='prog-time-elapsed')
        lbl.grid(row=3, column=0, columnspan=2, sticky=EW, pady=2)
        self.setvar('prog-time-elapsed', 'Elapsed: 1 sec')

        ## time remaining
        lbl = ttk.Label(status_frm, textvariable='prog-time-left')
        lbl.grid(row=4, column=0, columnspan=2, sticky=EW, pady=2)
        self.setvar('prog-time-left', 'Left: 0 sec')

        ## section separator
        sep = ttk.Separator(status_frm, bootstyle=SECONDARY)
        sep.grid(row=5, column=0, columnspan=2, pady=10, sticky=EW)

        ## stop button
        _func = lambda: Messagebox.ok(message='Stopping robo')
        btn = ttk.Button(
            master=status_frm,
            text='Stop',
            image='stop-robo-dark',
            compound=LEFT,
            command=_func,
            bootstyle=LINK
        )
        btn.grid(row=6, column=0, columnspan=2, sticky=W)

        ## section separator
        sep = ttk.Separator(status_frm, bootstyle=SECONDARY)
        sep.grid(row=7, column=0, columnspan=2, pady=10, sticky=EW)

        # current file message
        lbl = ttk.Label(status_frm, textvariable='current-file-msg')
        lbl.grid(row=8, column=0, columnspan=2, pady=2, sticky=EW)
        self.setvar('current-file-msg', 'Uploading: d:/test/settings.txt')

        # logo
        lbl = ttk.Label(left_panel, image='logo', style='bg.TLabel')
        lbl.pack(side='bottom')

        # right panel
        right_panel = ttk.Frame(self, padding=(2, 1))
        right_panel.pack(side=RIGHT, fill=BOTH, expand=YES)

        ## file input
        browse_frm = ttk.Frame(right_panel)
        browse_frm.pack(side=TOP, fill=X, padx=2, pady=1)

        file_entry = ttk.Entry(browse_frm, textvariable='folder-path')
        file_entry.pack(side=LEFT, fill=X, expand=YES)

        btn = ttk.Button(
            master=browse_frm,
            image='opened-folder',
            bootstyle=(LINK, SECONDARY),
            command=self.get_directory
        )
        btn.pack(side=RIGHT)

        ## Treeview
        tv = ttk.Treeview(right_panel, show='headings', height=5)
        tv.configure(columns=(
            'name', 'state', 'last-modified',
            'last-run-time', 'size'
        ))
        tv.column('name', width=150, stretch=True)

        for col in ['last-modified', 'last-run-time', 'size']:
            tv.column(col, stretch=False)

        for col in tv['columns']:
            tv.heading(col, text=col.title(), anchor=W)

        tv.pack(fill=X, pady=1)
        tv.bind('<<TreeviewSelect>>', partial(self.on_tree_select, tv=tv))
        tv.bind("<Double-1>", self.on_treeview_double_click)

        ## scrolling text output
        scroll_cf = CollapsingFrame(right_panel)
        scroll_cf.pack(fill=BOTH, expand=YES)

        output_container = ttk.Frame(scroll_cf, padding=1)
        _value = 'Log: Robo Script...'
        self.setvar('scroll-message', _value)
        self.setvar('scroll-message-tooltip', _value)
        self.scroll_display = ScrolledText(output_container)
        self.scroll_display.pack(fill=BOTH, expand=YES)
        self.scroll_display.bind("<Key>", self.robo_utils.ignore_typing)
        scroll_cf.add(output_container, textvariable='scroll-message', texttooltip='scroll-message-tooltip')

        # seed with some sample data

        ## starting sample directory
        file_entry.insert(END, self.robo_logic.working_directory)

        self.setvar('case-directory', os.path.join(self.robo_logic.working_directory, 'Cases'))

        files_case = self.robo_logic.get_case_list('Cases', ('.csv', '.json'))
        ## treeview and backup logs
        if files_case:
            for filename, size in files_case:
                size_type = 'MB'
                if (self.bytes_to_mb(size) < 0.1):
                    size_type = 'Bytes'
                else:
                    size = self.bytes_to_mb(size)

                item_id = tv.insert('', END, filename,
                    values=(filename, 'Ready',
                            datetime.now().strftime('%d.%m.%Y %H:%M:%S'),
                            datetime.now().strftime('%d.%m.%Y %H:%M:%S'),
                            f'{size} {size_type}')
                )
            if len(files_case) > 0:
                items = tv.get_children()
                if items:
                    tv.selection_set(items[0])
                    tv.focus(items[0])
                    tv.see(items[0])

            self.autofit_columns(tv)

    def bytes_to_mb(self, num_bytes):
        return round(int(num_bytes) / (1024 * 1024), 2)

    def autofit_columns(self, treeview):
        font = tkFont.Font()
        for col in treeview['columns']:
            max_width = font.measure(col)
            for item in treeview.get_children():
                cell_value = str(treeview.set(item, col))
                cell_width = font.measure(cell_value)
                if cell_width > max_width:
                    max_width = cell_width
            # เพิ่ม padding เล็กน้อย
            treeview.column(col, width=max_width + 20)

    def on_tree_select(self, event, tv=None):
        selected_item = tv.selection()  # คืนค่า tuple ของ item id ที่เลือก
        if selected_item:
            item = selected_item[0]  # เอา item ตัวแรก
            values = tv.item(item, 'values')  # ดึงข้อมูลในแถวนั้น
            self.setvar('selected-test-name', os.path.splitext(values[0])[0])  # เก็บชื่อไฟล์ในตัวแปร
            self.setvar('selected-file-name', values[0])  # เก็บชื่อไฟล์ในตัวแปร
            self.setvar('selected-file-size', values[4])  # เก็บขนาดไฟล์ในตัวแปร
            # print(f"Selected Filename: {values[0]}, Size: {values[4]}")

    def on_treeview_double_click(self, event):
        tree = event.widget
        item_id = tree.identify_row(event.y)
        if item_id:
            values = tree.item(item_id, "values")
            # แสดง Messagebox พร้อมข้อมูลในแถว
            Messagebox.ok(message=f"ข้อมูลแถว:\n{values}")

    def get_directory(self):
        """Open dialogue to get directory and update variable"""
        self.update_idletasks()
        d = askdirectory()
        # print(f'Selected directory: {d}')
        if d:
            self.robo_logic.set_directory(d)
            self.setvar('folder-path', d)

    def get_file_robo(self):
        """Open dialogue to get file and update variable"""
        self.update_idletasks()
        f = askopenfilename(
            title="เลือกไฟล์",
            filetypes=[
                ("CSV Files", "*.csv"),
                ("Excel Files", "*.xlsx *.xls")
            ]
        )
        # print(f'Selected file: {f}')
        if f:
            self.setvar('file-path', f)

    def new_robo_modal(self):
        # ขนาด modal
        modal_width = 600
        modal_height = 300

        # คำนวณตำแหน่งให้อยู่กลาง
        x = self.winfo_x() + (self.winfo_screenwidth() // 2) - (modal_width // 2)
        y = self.winfo_y() + (self.winfo_screenheight() // 2) - (modal_height // 2)

        # เปิด Toplevel (Modal)
        modal = Toplevel(self)
        modal.title("New robo set")
        modal.geometry(f"{modal_width}x{modal_height}+{x}+{y}")
        modal.transient(self)
        modal.grab_set()


        modal_container = ttk.Frame(modal, padding=10)
        modal_container.pack(side=TOP, fill=BOTH, expand=True)

        top_frame = ttk.Frame(modal_container)
        top_frame.pack(side=TOP, fill=X, pady=(0, 10))

        # Entry
        # new_file_case = ttk.Entry(modal_container, textvariable='file-path')
        # new_file_case.pack(side=LEFT, fill=X, expand=True, padx=(0, 0), pady=5)
        # self.setvar('file-path', 'D:/text/myfiles/top-secret/samples/')

        # Button
        # btn = ttk.Button(
        #     master=top_frame,
        #     image='add-to-robo-dark',
        #     bootstyle=(LINK, SECONDARY),
        #     command=self.get_file_robo
        # )
        # btn.pack(side=RIGHT)

        # --- ใส่ Separator เส้นคั่น ---
        separator = ttk.Separator(modal, orient='horizontal')
        separator.pack(fill=X)  # เว้นระยะนิดนึง

        bottom_frame = ttk.Frame(modal, padding=(5, 5))
        bottom_frame.pack(fill=X, padx=2)

        self.buttons = []
        self.buttons.append(
            ttk.Button(
                master=bottom_frame,
                text="Cancel",
                width=10,
                bootstyle=DANGER,
                command=modal.destroy,
            )
        )

        for button in self.buttons:
            button.pack(side=RIGHT, fill=X, padx=5, pady=5)

    def play_robo_modal(self):
        modal = Toplevel()
        modal.title("Play Robo")
        modal.resizable(False, False)
        modal.minsize(600, 300)
        # modal.iconphoto(True, ttk.PhotoImage(name='logo', file=PATH / 'Robot-framework-logo.png'))

        modal_container = ttk.Frame(modal, padding=10)
        modal_container.pack(side=TOP, fill=BOTH, expand=True)

        top_frame = ttk.Frame(modal_container)
        top_frame.pack(side=TOP, fill=X, pady=(0, 10))

        # lbl = ttk.Label(top_frame, text="Select Browser to run Robo Script:")
        # lbl.configure(font='Helvetica 12 bold')
        # lbl.pack(pady=10)

        browser_labelframe = ttk.Labelframe(
            master=top_frame,
            text='Browser Selection',
            padding=(5, 5)
        )
        browser_labelframe.pack(fill=BOTH, expand=YES, padx=5, pady=(5, 5))

        # open_browser = ttk.StringVar(value='Edge')
        self.setvar('open_browser', 'Edge')
        ttk.Radiobutton(
            browser_labelframe,
            text="Microsoft Edge",
            image='edge_icon',
            compound="left",    # icon อยู่ซ้ายข้อความ
            variable='open_browser',
            value="Edge",
            command=self.on_set_command
        ).pack(side=LEFT, padx=15, pady=10, anchor="w")

        ttk.Radiobutton(
            browser_labelframe,
            text="Firefox",
            image='firefox_icon',
            compound="left",    # icon อยู่ซ้ายข้อความ
            variable='open_browser',
            value="Firefox",
            command=self.on_set_command
        ).pack(side=LEFT, padx=15, pady=10, anchor="w")

        info_labelframe = ttk.Labelframe(
            master=top_frame,
            text='Command Execution Details',
            bootstyle=INFO,
            padding=(5, 5)
        )
        info_labelframe.pack(fill=BOTH, expand=YES, padx=5, pady=(5, 5))
        # Label: Folder
        lbl_folder = ttk.Label(info_labelframe, text="Folder:", bootstyle="inverse-dark")
        lbl_folder.grid(row=0, column=0, sticky='e', padx=(10, 5), pady=(5, 5))

        # Entry: case-directory
        entry_folder = ttk.Entry(info_labelframe, textvariable='case-directory', state='readonly')
        entry_folder.grid(row=0, column=1, sticky='we', padx=(5, 10), pady=(5, 5))

        # Label: File Case
        lbl_filecase = ttk.Label(info_labelframe, text="File Case:", bootstyle="inverse-dark")
        lbl_filecase.grid(row=1, column=0, sticky='e', padx=(10, 5), pady=(5, 5))

        # Entry: selected-file-name
        entry_case = ttk.Entry(info_labelframe, textvariable='selected-file-name', state='readonly')
        entry_case.grid(row=1, column=1, sticky='we', padx=(5, 10), pady=(5, 5))

        # Label: Test Name
        lbl_testname = ttk.Label(info_labelframe, text="Test Name:", bootstyle="inverse-dark")
        lbl_testname.grid(row=2, column=0, sticky='e', padx=(10, 5), pady=(5, 5))

        # Entry: selected-test-name
        entry_testname = ttk.Entry(info_labelframe, textvariable='selected-test-name', state='normal')
        entry_testname.grid(row=2, column=1, sticky='we', padx=(5, 10), pady=(5, 5))
        entry_testname.bind("<KeyRelease>", self.on_set_command)

        # Label: Robo Script
        lbl_script = ttk.Label(info_labelframe, text="Robot Script:", bootstyle="inverse-dark")
        lbl_script.grid(row=3, column=0, sticky='e', padx=(10, 5), pady=(5, 5))

        # ComboBox: robot-script
        key_to_path, key_to_label  = self.robo_logic.load_robot_script_from_ini(self.robo_logic.ini_path)
        robo_scripts = list(key_to_label.values())
        # robo_scripts = ['Robo Script 1', 'Robo Script 2', 'Robo Script 3']  # ตัวอย่างชื่อสคริปต์
        robo_script_combobox = ttk.Combobox(
            info_labelframe,
            values=robo_scripts,
            state='readonly',
            textvariable='robot-script'
        )
        robo_script_combobox.grid(row=3, column=1, sticky='we', padx=(5, 10), pady=(5, 5))
        if robo_scripts:
            robo_script_combobox.current(0)
            self.setvar('robot-script', robo_scripts[0])  # ตั้งค่าเริ่มต้นเป็นสคริปต์แรก
        else:
            self.setvar('robot-script', NONE)  # ถ้าไม่มีสคริปต์ ให้เป็น None

        self.cmd_box = ScrolledText(info_labelframe, font=("Consolas", 11), wrap='word', height=6)
        self.on_set_command()  # เรียกใช้เพื่อใส่คำสั่งเริ่มต้น
        self.cmd_box.tag_configure("bold", font=("Consolas", 11, "bold"))
        #self.cmd_box.configure(state='disabled')  # ไม่ให้แก้ไข
        self.cmd_box.grid(row=4, column=0, columnspan=2, sticky='nsew', padx=(10, 10), pady=(5, 5))

        # ทำให้ column 1 (Entry) ขยายเต็มที่
        info_labelframe.columnconfigure(1, weight=1)

        # --- ใส่ Separator เส้นคั่น ---
        separator = ttk.Separator(modal, orient='horizontal')
        separator.pack(fill=X)  # เว้นระยะนิดนึง

        container = ttk.Frame(modal, padding=(5, 5))
        container.pack(fill=X, padx=2)

        buttons = []
        buttons.append(
            ttk.Button(
                master=container,
                text="Cancel",
                width=10,
                bootstyle=DANGER,
                command=modal.destroy,
            )
        )
        buttons.append(
            ttk.Button(
                master=container,
                text="Robo",
                image='play16',
                compound=LEFT,  # icon อยู่ซ้ายข้อความ
                width=8,
                bootstyle=SUCCESS,
                command=self.on_run_command,
            )
        )
        for button in buttons:
            button.pack(side=RIGHT, fill=X, padx=5, pady=5)

        # btn = ttk.Button(modal, text="OK", command=modal.destroy)
        # btn.pack(side=BOTTOM, padx=30, pady=10)
        # อัปเดต geometry ก่อนคำนวณ
        modal.withdraw()
        modal.update_idletasks()

        modal_width = modal.winfo_width()
        modal_height = modal.winfo_height()

        x = self.winfo_x() + (self.winfo_screenwidth() // 2) - (modal_width // 2)
        y = self.winfo_y() + (self.winfo_screenheight() // 2) - (modal_height // 2)

        modal.geometry(f"+{x}+{y}")
        modal.transient(self)
        modal.deiconify()
        modal.grab_set() # ทำให้ popup เป็น modal
        self.modal['play_robo_modal'] = modal

    def on_set_command(self, *args):
        """Set command to run Robo Script"""
        # print(f"Browser selected: {self.getvar('open_browser')}")
        key_to_path, key_to_label  = self.robo_logic.load_robot_script_from_ini(self.robo_logic.ini_path)
        # print(f'key_to_path= {key_to_path}')
        # print(f'key_to_label= {key_to_label}')
        key_robot_script = next((k for k, v in key_to_label.items() if v == self.getvar('robot-script')), None)
        path = Path(self.getvar('case-directory')) / self.getvar('selected-file-name')
        path_case = str(path.resolve())
        path = Path(PROJECTS_PATH) / key_to_path.get(key_robot_script)
        path_robot_script = str(path.resolve())
        path = Path(self.getvar('case-directory')).parent / 'results'
        outputdir = str(path.resolve())
        # Create a list of command parts
        python_path = os.path.join(os.getcwd(), '.venv', 'Scripts', 'python.exe')
        command_parts = [
            f"\"{python_path}\"", 
            "-m",
            #sys.executable, "-m",
            f"robot",
            f"--name \"{self.getvar('selected-test-name')}\"",
            f"--variable \"OPEN_BROWSER:{self.getvar('open_browser')}\"",
            f"--variable \"PATH_CASE:{path_case}\"",
            f"--outputdir \"{outputdir}\"",
            "--loglevel DEBUG",
            #"--consolewidth 120",
            # "--listener my_listener.py",
            f"\"{path_robot_script}\""

        ]

        # Join the list into a single string with a space separator
        command = " ".join(command_parts)
        self.cmd_box.configure(state='normal')
        self.cmd_box.delete('1.0', 'end')
        self.cmd_box.insert('1.0', command)
        self.setvar('robot-command', command)

    def on_run_command(self, command=None):
        """Run the command in a separate thread and display output in scrollable text area."""
        if command is None:
            command = self.getvar('robot-command')
            if not command:
                Messagebox.show_error("No command set to run.")
                return
        # print(f"Running command: {command}")
        self.modal['play_robo_modal'].destroy()
        # หลัง self.scroll_display = ScrolledText(output_container)
        self.scroll_display.tag_configure("red", foreground="red")
        self.scroll_display.tag_configure("green", foreground="green")
        def task():
            max_length = 80
            short_command = command if len(command) <= max_length else command[:max_length] + "..."
            self.setvar('scroll-message', f'Log: Running command: {short_command}')
            self.setvar('scroll-message-tooltip', command)
            process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True, text=True)
            print(f"Process started with PID: {process.pid}")
            self.scroll_display.configure(state='normal')
            self.scroll_display.delete('1.0', 'end')  # ล้างข้อความเก่า
            for line in process.stdout:
                self.insert_log_with_pass_highlight(line)
                # self.scroll_display.insert(END, line)
                # self.scroll_display.see(END)  # Scroll ตามข้อความล่าสุด
            process.stdout.close()
            process.wait()

        threading.Thread(target=task).start()

    def insert_log_with_pass_highlight(self, text):
        """
        Insert log text into the scroll_display widget, highlighting specific keywords.
        """
        self.scroll_display.configure(state='normal')
        keywords = {
            'PASS': 'green',
            'FAIL': 'red',
            'ERROR': 'red',
            'SKIP': 'orange',
            'WARN': 'orange',
            'WARNING': 'orange',
        }
        idx = 0
        text_len = len(text)
        while idx < text_len:
            # Find the next keyword occurrence
            next_pos = text_len
            next_key = None
            for key in keywords:
                pos = text.find(key, idx)
                if pos != -1 and pos < next_pos:
                    next_pos = pos
                    next_key = key
            if next_key is None:
                # No more keywords, insert the rest
                self.scroll_display.insert('end', text[idx:])
                break
            # Insert text before the keyword
            if next_pos > idx:
                self.scroll_display.insert('end', text[idx:next_pos])
            # Insert the keyword with tag
            self.scroll_display.insert('end', next_key, keywords[next_key])
            idx = next_pos + len(next_key)
        self.scroll_display.see('end')
        # self.scroll_display.configure(state='disabled')

class CollapsingFrame(ttk.Frame):
    """A collapsible frame widget that opens and closes with a click."""

    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.columnconfigure(0, weight=1)
        self.cumulative_rows = 0

        # widget images
        self.images = [
            ttk.PhotoImage(file=PATH/'icons8_double_up_24px.png'),
            ttk.PhotoImage(file=PATH/'icons8_double_right_24px.png')
        ]

    def add(self, child, title="", bootstyle=PRIMARY, **kwargs):
        """Add a child to the collapsible frame

        Parameters:

            child (Frame):
                The child frame to add to the widget.

            title (str):
                The title appearing on the collapsible section header.

            bootstyle (str):
                The style to apply to the collapsible section header.

            **kwargs (Dict):
                Other optional keyword arguments.
        """
        if child.winfo_class() != 'TFrame':
            return

        style_color = Bootstyle.ttkstyle_widget_color(bootstyle)
        frm = ttk.Frame(self, bootstyle=style_color)
        frm.grid(row=self.cumulative_rows, column=0, sticky=EW)

        # header title
        header = ttk.Label(
            master=frm,
            text=title,
            bootstyle=(style_color, INVERSE)
        )
        if kwargs.get('texttooltip') is None and kwargs.get('textvariable') is not None:
            header.configure(textvariable=kwargs.get('textvariable'))
        if kwargs.get('texttooltip') is not None and kwargs.get('textvariable') is not None:
            header.configure(textvariable=kwargs.get('textvariable'))
            # print(f"Text tooltip: {kwargs.get('texttooltip')}")
            # ดึงชื่อของ tooltip variable
            tooltip_var_name = kwargs.get('texttooltip')

            # ดึงค่าเริ่มต้นมาแสดง tooltip
            tooltip_var = ttk.StringVar(name=tooltip_var_name)
            tooltip = ToolTip(header, text=tooltip_var.get())

            # ผูก trace เพื่ออัปเดต tooltip ทุกครั้งที่ตัวแปรเปลี่ยน
            def update_tooltip(*_):
                tooltip.text = tooltip_var.get()
            tooltip_var.trace_add('write', update_tooltip)

        header.pack(side=LEFT, fill=BOTH, padx=10)

        # header toggle button
        def _func(c=child): return self._toggle_open_close(c)
        btn = ttk.Button(
            master=frm,
            image=self.images[0],
            bootstyle=style_color,
            command=_func
        )
        btn.pack(side=RIGHT)

        # assign toggle button to child so that it can be toggled
        child.btn = btn
        child.grid(row=self.cumulative_rows + 1, column=0, sticky=NSEW)

        # increment the row assignment
        self.cumulative_rows += 2

    def _toggle_open_close(self, child):
        """Open or close the section and change the toggle button
        image accordingly.

        Parameters:

            child (Frame):
                The child element to add or remove from grid manager.
        """
        if child.winfo_viewable():
            child.grid_remove()
            child.btn.configure(image=self.images[1])
        else:
            child.grid()
            child.btn.configure(image=self.images[0])


if __name__ == '__main__':
    logging.basicConfig(filename="robo_buddy.log", level=logging. DEBUG)
    app = ttk.Window("Robo Buddy", themename='darkly')
    RoboBuddy(app)
    # --- Center window on screen ---
    app.withdraw()
    app.update_idletasks()
    width = app.winfo_width()
    height = app.winfo_height()
    screen_width = app.winfo_screenwidth()
    screen_height = app.winfo_screenheight()
    x = (screen_width // 2) - (width // 2)
    y = (screen_height // 2) - (height // 2)
    app.geometry(f'+{x}+{y}')
    app.deiconify()
    # --- End center window ---

    app.mainloop()
