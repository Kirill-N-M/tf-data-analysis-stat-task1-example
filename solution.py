import pandas as pd
import numpy as np


chat_id = 586939927 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array) -> float:
    a = 2*(x.mean()-1)/256
    return a # Ваш ответ
