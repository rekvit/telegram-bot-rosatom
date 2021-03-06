from aiogram.dispatcher.filters.state import StatesGroup, State
# API_KEY = "1707362497:AAFSyW_HreeIUZ-5DSdk5xFDe_DCWyIUB8M"
API_KEY = "1787274187:AAFKOJPLmdbrIKVRRCi7LMAcL49Su042b74"
admin_id = 1011677109
calendar_id = "bbottelegram@gmail.com"  # календарь в общем доступе
# client_secret_calendar = "deadlines\\client_secret.json"  # Google API Calendar
client_secret_calendar = "..\\deadlines\\client_secret.json"  # Google API Calendar
# путь для тех кто запускает через venv
CALENDAR_TOKEN_PATH = "..\\token.pkl"
documents_directory = "..\\documentation\\documentation_files"
database_path = "../Case_in_bot.db"
ROSATOM_SITE = "https://www.rosatom.ru/"


class States(StatesGroup):
    """
    Машина конечных состояний:
    у нас два сотстояния ввод текста и ввод команд
    также есть нулевое состояние, при запуске
    состояния переключатся при функциях вроде "задать вопрос"
    """
    # NON_AUTHORISED_STATE = State()
    COMMAND_STATE = State()
    ENTER_QUESTION_STATE = State()
    ENTER_EMAIL_STATE = State()
    ENTER_POST_STATE = State()
    SELECT_WORKER_STATE = State()
    ENTER_SUMMARY_STATE = State()
    ENTER_DATESTART_STATE = State()
    ENTER_DATEEND_STATE = State()
    ENTER_TIMESTART_STATE = State()
    ENTER_TIMEEND_STATE = State()
    ENTER_DESCRIPTION_STATE = State()


Authorized_states = [
    None,
    States.COMMAND_STATE,
    States.ENTER_QUESTION_STATE,
    States.SELECT_WORKER_STATE,
    States.ENTER_SUMMARY_STATE,
    States.ENTER_DATESTART_STATE,
    States.ENTER_DATEEND_STATE,
    States.ENTER_TIMESTART_STATE,
    States.ENTER_TIMEEND_STATE,
    States.ENTER_DESCRIPTION_STATE,
]
