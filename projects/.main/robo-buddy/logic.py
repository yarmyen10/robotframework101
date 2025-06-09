import os
import configparser

class RoboBuddyLogic:
    def __init__(self, robo):
        self.robo = robo
        self.config = configparser.ConfigParser()
        self.working_directory = None
        self.ini_path = self.set_default_directory()
        self.read_current_directory()

    def process_command(self, command):
        if command == "greet":
            return self.robo.greet()
        elif command == "move":
            return self.robo.move()
        elif command == "stop":
            return self.robo.stop()
        else:
            return "Unknown command"

    def execute(self, command):
        """
        Execute a command on the robo.

        :param command: The command to execute.
        :return: The result of the command execution.
        """
        return self.process_command(command)

    def greet(self):
        """
        Make the robo greet.

        :return: A greeting message.
        """
        return "Hello! I am RoboBuddy, your friendly robo assistant."

    def set_default_directory(self):
        # Path ของ Documents ของ User
        documents_path = os.path.join(os.path.expanduser("~"), "Documents")
        robo_buddy_folder = os.path.join(documents_path, "Robo Buddy")

        # ถ้า folder Robo Buddy ยังไม่มี ให้สร้าง
        if not os.path.exists(robo_buddy_folder):
            os.makedirs(robo_buddy_folder)
            print(f"สร้างโฟลเดอร์ใหม่: {robo_buddy_folder}")

        # เตรียม path ของ robobuddy.ini
        ini_path = os.path.join(robo_buddy_folder, 'robobuddy.ini')
        self.working_directory = robo_buddy_folder

        # เช็คว่า robobuddy.ini มีอยู่ไหม
        if not os.path.exists(ini_path):
            print(f"ไม่พบ robobuddy.ini ที่ {ini_path} กำลังสร้างใหม่...")
            self.create_default_ini(ini_path)
        else:
            print(f"พบ robobuddy.ini แล้วที่ {ini_path}")

        self.set_default_folder_basic(robo_buddy_folder)

        return ini_path
    
    def set_default_folder_basic(self, working_directory: str):
        robo_buddy_folder_basic = os.path.join(working_directory, "cases")

        # ถ้า folder Robo Buddy ยังไม่มี ให้สร้าง
        if not os.path.exists(robo_buddy_folder_basic):
            os.makedirs(robo_buddy_folder_basic)
            print(f"สร้างโฟลเดอร์ใหม่: {robo_buddy_folder_basic}")

        return robo_buddy_folder_basic

    def read_current_directory(self):
        self.config.read(self.ini_path)

        # เช็ค Section: System
        if 'System' in self.config and 'current_directory' in self.config['System']:
            self.working_directory = self.config['System']['current_directory']
            print(f"ตั้งค่า path ปัจจุบันแล้ว เป็น: {self.working_directory}")
        else:
            print(f"ยังไม่ได้ตั้ง current_directory ใน robobuddy.ini")

    def set_directory(self, working_directory: str):
        self.working_directory = working_directory

        # เตรียม path ของ robobuddy.ini
        ini_path = os.path.join(self.working_directory, 'robobuddy.ini')

        # เช็คว่าไฟล์มีอยู่ไหม
        if not os.path.exists(ini_path):
            print(f"ไม่พบ robobuddy.ini ใน {self.working_directory} กำลังสร้างไฟล์ใหม่...")
            self.create_default_ini(ini_path)
            self.config['System'] = {'current_directory': self.working_directory}
            print(f"ตั้งค่า path ปัจจุบันเป็น: {self.working_directory}")
            with open(self.ini_path, 'w') as configfile:
                self.config.write(configfile)
        else:
            print(f"พบ robobuddy.ini แล้วที่ {self.working_directory}")

    def create_default_ini(self, ini_path):
        # สร้าง config object
        config = configparser.ConfigParser()

        # เพิ่มค่าตั้งต้น
        config['Settings'] = {
            'browser': 'Edge',
            'headless': 'True',
            'timeout': '30',
            'retry': '2',
        }

        config['Paths'] = {
            'testcase_dir': './tests/',
            'log_dir': './logs/',
            'output_dir': './output/',
        }

        config['Credentials'] = {
            'username': 'your_username',
            'password': 'your_password',
        }

        config['Environment'] = {
            'base_url': 'https://example.com',
            'env': 'dev',
        }

        config['RobotOptions'] = {
            'log_level': 'INFO',
            'run_mode': 'normal',
        }

        # เขียนไฟล์ ini
        with open(ini_path, 'w') as configfile:
            config.write(configfile)
        print(f"สร้าง robobuddy.ini เรียบร้อยที่ {ini_path}")


    def check_ini_file(self, ini_path):
        return os.path.exists(ini_path)

    def get_case_list(self, folder_name: str) -> list:
        print(f"กำลังดึงรายการเคสทดสอบ... {self.working_directory}")
        if not self.check_ini_file(self.ini_path):
            print(f"ไม่พบไฟล์ ini ที่ {self.ini_path}")
            return []
        else:
            files_case = self.list_files_in_folder(os.path.join(self.working_directory, folder_name))
            print(f"รายการเคสทดสอบในโฟลเดอร์ {folder_name} ถูกดึงเรียบร้อยแล้ว")
            print(f"พบ {len(files_case)} ไฟล์ในโฟลเดอร์ {folder_name}")
            if files_case:
                for filename, size in files_case:
                    print(f"ไฟล์: {filename}, ขนาด: {size} bytes")
            else:
                print(f"ไม่พบไฟล์ในโฟลเดอร์ {folder_name}")

            return []
        
    def list_files_in_folder(self, folder_path):
        files_case = []
        if not os.path.exists(folder_path):
            return files_case

        for filename in os.listdir(folder_path):
            filepath = os.path.join(folder_path, filename)
            if os.path.isfile(filepath):
                size = os.path.getsize(filepath)
                files_case.append((filename, size))
        return files_case