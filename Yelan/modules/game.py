import html
import random
import time

from telegram import ParseMode, Update, ChatPermissions
from telegram.ext import CallbackContext, run_async
from telegram.error import BadRequest

import YorForger.modules.game_strings as game_strings
from YorForger import dispatcher
from YorForger.modules.disable import DisableAbleCommandHandler
from YorForger.modules.helper_funcs.chat_status import (is_user_admin)
from YorForger.modules.helper_funcs.extraction import extract_user



def truth(update: Update, context: CallbackContext):
    update.effective_message.reply_text(random.choice(game_strings.TRUTH_STRINGS))



def dare(update: Update, context: CallbackContext):
    update.effective_message.reply_text(random.choice(game_strings.DARE_STRINGS))



def tord(update: Update, context: CallbackContext):
    update.effective_message.reply_text(random.choice(game_strings.TORD_STRINGS))


def wyr(update: Update, context: CallbackContext):
    update.effective_message.reply_text(random.choice(game_strings.WYR_STRINGS))


__help__ = """
 • `/truth`*:* asks you a question
 • `/dare`*:* gives you a dare
 • `/tord`*:* can be a truth or a dare
 • `/rather`*:* would you rather
  """

TRUTH_HANDLER = DisableAbleCommandHandler("truth", truth, run_async = True)
DARE_HANDLER = DisableAbleCommandHandler("dare", dare, run_async = True)
TORD_HANDLER = DisableAbleCommandHandler("tord", tord, run_async = True)
WYR_HANDLER = DisableAbleCommandHandler("rather", wyr, run_async = True)

dispatcher.add_handler(TRUTH_HANDLER)
dispatcher.add_handler(DARE_HANDLER)
dispatcher.add_handler(TORD_HANDLER)
dispatcher.add_handler(WYR_HANDLER)

__mod_name__ = "Games"
__command_list__ = [
   "truth", "dare", "tord", "rather",
]

__handlers__ = [
    TRUTH_HANDLER, DARE_HANDLER, TORD_HANDLER, WYR_HANDLER,
]
