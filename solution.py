import pandas as pd
import numpy as np


chat_id = 586939927 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array) -> float:
    a = (x.mean()-1)/128
    return a # Ваш ответ
