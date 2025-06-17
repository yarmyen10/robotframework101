class RoboBuddyUtils:
    @staticmethod
    def get_project_root() -> str:
        import os
        return os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))

    @staticmethod
    def get_project_name() -> str:
        return "robo-buddy"

    @staticmethod
    def get_project_version() -> str:
        return "0.1.0"

    @staticmethod
    def ignore_typing(event):
        # อนุญาตให้ Ctrl+C หรือ Command+C ทำงานได้
        if (event.state & 0x4) and event.keysym.lower() == 'c':  # Windows/Linux
            return None
        if (event.state & 0x10000) and event.keysym.lower() == 'c':  # macOS
            return None
        return "break"  # บล็อก key อื่น
