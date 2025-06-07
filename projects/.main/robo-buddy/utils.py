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
