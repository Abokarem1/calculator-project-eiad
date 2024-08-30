import logging
import logger  # Anta att detta är en modul där du konfigurerar loggern

class CalculatorHelper:
    log_properties = {
        'custom_dimensions': {
            'userId': 'MohamadEyad_Abouselo'
        }
    }

    _instance = None
    _is_initialized = False

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(CalculatorHelper, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        if not self._is_initialized:
            # Setup logger
            self.logger = logging.getLogger(__name__)
            self.logger.setLevel(logging.DEBUG)
            # You might need to set up handlers and formatters depending on your logger configuration
            # Example:
            # handler = logging.StreamHandler()
            # formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
            # handler.setFormatter(formatter)
            # self.logger.addHandler(handler)
            
            self._user_list = []
            self._current_user = None
            admin = self.User('admin', 'test1234')
            self._user_list.append(admin)
            self._is_initialized = True

    class User:
        def __init__(self, username, password):
            self.username = username
            self.password = password

        def __repr__(self):
            return f"User(username={self.username}, password={self.password})"

    def add(self, a, b):
        self.logger.debug(f"add {a} + {b}", extra=self.log_properties)
        return a + b

    def subtract(self, a, b):
        self.logger.debug(f"subtract {a} - {b}", extra=self.log_properties)
        return a - b

    def multiply(self, a, b):
        self.logger.debug(f"multiply {a} * {b}", extra=self.log_properties)
        return a * b

    def divide(self, a, b):
        if b == 0:
            self.logger.error("Division by zero is not allowed.", extra=self.log_properties)
            raise ValueError("Cannot divide by zero")
        self.logger.debug(f"divide {a} / {b}", extra=self.log_properties)
        return a / b

    def register_user(self, username, password):
        for user in self._user_list:
            if user.username == username:
                self.logger.debug(f"Registreringsförsök misslyckades: Användarnamnet {username} är redan taget.", extra=self.log_properties)
                return None
        
        user = self.User(username, password)
        self._user_list.append(user)
        self.logger.debug(f"Ny användare registrerad: {username}.", extra=self.log_properties)
        return username

    def login(self, username, password):
        for user in self._user_list:
            if user.username == username and user.password == password:
                self._current_user = user
                self.logger.debug(f"username {username} har loggat in.", extra=self.log_properties)
                return username
        return None

    def logout(self):
        user = self._current_user
        if user:
            self.logger.debug(f"Användaren {user.username} har loggat ut.", extra=self.log_properties)
        self._current_user = None
        return user

    def get_current_user(self):
        return self._current_user
