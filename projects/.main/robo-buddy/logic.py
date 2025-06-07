class RoboBuddyLogic:
    def __init__(self, robot):
        self.robot = robot

    def process_command(self, command):
        if command == "greet":
            return self.robot.greet()
        elif command == "move":
            return self.robot.move()
        elif command == "stop":
            return self.robot.stop()
        else:
            return "Unknown command"

    def execute(self, command):
        """
        Execute a command on the robot.

        :param command: The command to execute.
        :return: The result of the command execution.
        """
        return self.process_command(command)

    def greet(self):
        """
        Make the robot greet.

        :return: A greeting message.
        """
        return "Hello! I am RoboBuddy, your friendly robot assistant."
