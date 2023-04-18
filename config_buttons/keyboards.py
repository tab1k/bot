from telebot.util import quick_markup
from config_buttons.menu_commands import *

welcome_text = {
    'is_valid_sign' : 'Здраствуй, {message.from_user.first_name}. \n \nМоя команда рада видеть тебя тут снова! Выбери одно из списка) ',
    'is_error_sign' : 'Здраствуй, {get_user_name}. \n \nМоя команда рада видеть тебя! \nИзвини, но ты не зарегистрирован у нас!( \n( Зарегистрируйся и получай знания) '
}



# ПРЕДЛАГАЕМЫЙ НАЧАЛЬНЫЙ СПИСОК

markup_general = quick_markup(SELECT_STEP, row_width=2)

markup_course_type = quick_markup(SELECT_COURSE_TYPE, row_width=1)

# СПИСОК УРОКОВ
markup_subjects_programming = quick_markup(SUBJECTS_PROGRAMMING, row_width=1)


# РЕГИСТРАЦИЯ

markup_register = quick_markup(REGISTER, row_width=1)



# КУРАТОРЫ

markup_coordinators = quick_markup(COORDINATORS, row_width=1)

markup_reguest_from_user = quick_markup(REQUEST_FROM_USER, row_width=2)

# YES OR NO

agree_or_not_agree = quick_markup(AGREE_OR_NOTAGREE, row_width=2)





