import pyautogui
import time


class DragonValeHack():
    """
    This class is designed to automate interactions with the Game Guardian overlay in DragonVale using Nox simulator.
    """
    def __init__(self):
        """
        Initializes the DragonValeHack class.
        """
        pass


    def move_and_click(self, x: int, y: int, sleep: float = 0) -> None:
        """
        Moves the mouse to the specified coordinates and clicks.

        Args:
            x (int): The x-coordinate to move the mouse to.
            y (int): The y-coordinate to move the mouse to.
            sleep (float, optional): Time in seconds to wait after clicking. Default is 0.
        """
        pyautogui.moveTo(x, y)
        pyautogui.click()
        time.sleep(sleep)


    def enter_qword_value(self, value: int, interval: float = 0.5) -> None:
        """
        Enters Q-Word value into the input field by simulating mouse clicks.

        Args:
            value (int): The 64-bit integer value to enter.
            interval (float, optional): Time in seconds to wait between set keystrokes. Default is 0.5.
        """
        # Specify the coordinates for each digit on the screen
        COLS = (1380, 1475, 1570)
        ROWS = (270, 360, 450, 540, 630, 720)
        number_mapping = {1: (COLS[0], ROWS[0]), 2: (COLS[1], ROWS[0]), 3: (COLS[2], ROWS[0]),
                        4: (COLS[0], ROWS[1]), 5: (COLS[1], ROWS[1]), 6: (COLS[2], ROWS[1]),
                        7: (COLS[0], ROWS[2]), 8: (COLS[1], ROWS[2]), 9: (COLS[2], ROWS[2]),
                        0: (COLS[0], ROWS[3]), "-": (COLS[0], ROWS[5]),}

        for digit in str(value):
            try:
                digit = int(digit)
            except ValueError:
                pass
            x, y = number_mapping[digit]
            self.move_and_click(x, y, sleep=interval)


    def open_game_guardian(self) -> None:
        """
        Opens the Game Guardian overlay.
        """
        self.move_and_click(70, 80, sleep=0.5)

    
    def close_game_guardian(self) -> None:
        """
        Closes the Game Guardian overlay.
        """
        self.move_and_click(1800, 80, sleep=0.3)


    def select_process(self) -> None:
        """
        Selects the DragonVale process in the Game Guardian overlay.
        """
        self.move_and_click(615, 182, sleep=0.7)

    
    def select_search_tab(self) -> None:
        """
        Selects the search tab in the Game Guardian overlay.
        """
        self.move_and_click(650, 90, sleep=0.5)


    def select_qword_search_type(self) -> None:
        """
        Selects the Q-Word search option in the Game Guardian overlay.
        """
        # Open type menu
        self.move_and_click(700, 450, sleep=0.5)

        # Select Q-Word data type
        pyautogui.moveTo(800, 700)
        [pyautogui.scroll(100) for _ in range(3)]
        time.sleep(0.5)
        pyautogui.click()


    def click_search_button(self) -> None:
        """
        Clicks the search button in the Game Guardian overlay.
        """
        self.move_and_click(1730, 230, sleep=0.5)


    def click_change_all_values_button(self) -> None:
        """
        Clicks the 'Change All Values' button in the Game Guardian overlay.
        """
        self.move_and_click(1650, 230, sleep=0.5)


    def click_yes_button(self) -> None:
        """
        Clicks the yes button in the Game Guardian overlay.
        """
        self.move_and_click(1650, 830, sleep=0.2)


    def click_first_result(self) -> None:
        """
        Clicks the first result in the Game Guardian overlay.
        """
        self.move_and_click(450, 320, sleep=0.5)


    def search(self) -> None:
        """
        Click the 'New Search' button in both possible locations in the Game Guardian overlay.
        """
        # Click the new search button if it appears
        self.move_and_click(260, 830)

        # Click the search button if it appears
        self.move_and_click(1600, 830, sleep=2)

    
    def goto(self) -> None:
        """
        Clicks the 'Goto' button in the Game Guardian overlay.
        """
        self.move_and_click(260, 830, sleep=1)

    
    def type(self, value: str, interval: float = 0.1) -> None:
        """
        Types out a string value into an input field by simulating keystrokes in the Game Guardian overlay.
        """
        pyautogui.typewrite(value, interval=interval)


    def arrow_down(self, count: int = 1, interval: float = 0.3) -> None: 
        """
        Simulates pressing the down arrow key to scroll through the list of results in the Game Guardian overlay.
        """
        for _ in range(count):
            pyautogui.press('down')
            time.sleep(interval)


    def press_key(self, key: str, sleep: float = 0.3) -> None:
        """
        Simulates pressing a specific key.

        Args:
            key (str): The key to press.
            interval (float, optional): Time in seconds to wait after pressing the key. Default is 0.3.
        """
        pyautogui.press(key)
        time.sleep(sleep)