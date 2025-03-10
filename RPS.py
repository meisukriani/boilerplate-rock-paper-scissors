import random

def player(prev_play, opponent_history=[], play_order={}, loss_streak=[0]):
    if prev_play:
        opponent_history.append(prev_play)

    counter_moves = {"R": "P", "P": "S", "S": "R"}
    possible_moves = ["R", "P", "S"]

    # Jika data masih sedikit, main random
    if len(opponent_history) < 5:
        return random.choice(possible_moves)

    # **Gunakan pola Markov dengan 5 langkah terakhir**
    last_five = "".join(opponent_history[-5:])
    if len(last_five) == 5:
        play_order[last_five] = play_order.get(last_five, 0) + 1

    # Prediksi langkah lawan berdasarkan 3 langkah terakhir
    prediction = max(possible_moves, key=lambda move: play_order.get(last_five[-4:] + move, 0))

    # Gunakan counter move
    guess = counter_moves[prediction]

    # **Hitung streak kekalahan**
    if len(opponent_history) > 10:
        last_10 = opponent_history[-10:]
        most_common = max(set(last_10), key=last_10.count)
        if most_common == prev_play:  # Jika lawan terus menang
            loss_streak[0] += 1
        else:
            loss_streak[0] = 0  # Reset jika menang

    # **Jika kalah 5x berturut-turut, ubah strategi jadi random**
    if loss_streak[0] >= 5:
        guess = random.choice(possible_moves)
        loss_streak[0] = 0  # Reset streak setelah mengganti strategi

    return guess
