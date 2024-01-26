from aiogram.types import InlineKeyboardButton

from src.bot.keyboards import Keyboard
from src.bot.callbacks import PostsCallback


class PostsKeyboard(Keyboard):
    def __init__(self, amount_of_buttons: int, action: str):
        super().__init__(amount_of_buttons, action)

        self.add_buttons()
        self.adjust_buttons()

    def add_buttons(self):
        for i in range(1, self.amount_of_buttons + 1):
            self.builder.add(InlineKeyboardButton(text=f"{i}", callback_data=PostsCallback(action=self.action, index=i - 1).pack()))
        self.builder.add(InlineKeyboardButton(text="Все", callback_data=PostsCallback(action=self.action, index=self.amount_of_buttons + 1).pack()))

    def get_row_size(self) -> int:
        if self.amount_of_buttons <= 5:
            return self.amount_of_buttons
        elif self.amount_of_buttons % 2 == 0:
            return int(self.amount_of_buttons / 2)
        else:
            return int(self.amount_of_buttons / 2) + 1

    def adjust_buttons(self) -> None:
        row_size = self.get_row_size()

        if row_size < 10:
            self.builder.adjust(row_size, repeat=True)
        else:
            self.builder.adjust(9, repeat=True)
