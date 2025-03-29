import random

def guess_number_game():
    print("欢迎宝宝来到猜数字游戏！(*^▽^*)")
    print("我已经想好了一个 1 到 100 之间的数字，你能猜到它吗？(^_−)☆")

    # 生成一个 1 到 100 的随机数
    secret_number = random.randint(1, 100)
    attempts = 0

    while True:
        try:
            # 提示用户输入数字
            guess = int(input("٩( 'ω' )و 请输入你的猜测："))
            attempts += 1

            if guess < secret_number:
                print("宝宝你猜小了！〒▽〒")
            elif guess > secret_number:
                print("宝宝你猜大了！(Θ３Θ)")
            else:
                print(f"恭喜宝宝猜对啦！٩(๑>◡<๑)۶ 这个数字是 {secret_number}。")
                print(f"宝宝总共猜了 {attempts} 次ヾ(ﾟ∀ﾟゞ)")
                break
        except ValueError:
            print("宝宝请输入一个有效的数字！(；д；)")

# 启动游戏
guess_number_game()