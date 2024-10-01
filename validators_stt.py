import math
from config_stt import MAX_USER_STT_BLOCKS
def count_tokens(user_id):
    return 2
# проверяем не превысил ли пользователь лимиты на преобразование аудио в текст
def is_stt_block_limit(user_id, duration):
    if duration > 30:
        return None, "blin slyshkom dolgo"

    cur_blocks = math.ceil(duration / 15)

    user_blocks = count_tokens(user_id)

    all_blocks = user_blocks + cur_blocks

    # сравниваем all_blocks с количеством доступных пользователю аудиоблоков
    if all_blocks >= MAX_USER_STT_BLOCKS:
        return None, "tokenov nema"
    return all_blocks, ""