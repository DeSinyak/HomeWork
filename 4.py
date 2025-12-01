class Money:
    def __init__(self, amount):
        self.amount = amount

    def spend(self, cost):
        if self.amount >= cost:
            self.amount -= cost
            print(f"(Баронесса потратила {cost}€. Остаток: {self.amount}€)")
            return True
        else:
            print(f"(Денег недостаточно: {self.amount}€)")
            return False

    def is_empty(self):
        return self.amount <= 0


def ask_choice(prompt, options):
    while True:
        choice = input(prompt)
        if choice in options:
            return choice
        else:
            print("Ошибка: выберите один из предложенных вариантов!")

purse = Money(5000)
HERMES_PRICE = 3000


def home():
    print("Баронесса решила остаться дома — расслабиться в роскошной тишине.")

    choice = ask_choice("Чем она займётся? (обзор/образы) ", ["обзор", "образы"])

    if choice == "обзор":
        print("Видео стало вирусным — лёгкий доход, но не сегодня. Настроение отличное.")
    elif choice == "образы":
        print("Новые образы придуманы. Стильно, эффектно, дорого.")


def progulka():
    print("Баронесса решила выйти в свет — Париж манит роскошью.")
    choice = ask_choice("Куда направится Баронесса? (гермес/подружка) ", ["гермес", "подружка"])
    if choice == "гермес":
        print("Баронесса направилась в Hermès…")

        while True:
            answer = input("Сережа, купить мне новую сумочку??? (купить/закончить): ")

            if answer == "закончить":
                print("Игореша решил пойти домой, мудрое решение для кошелька")
                break

            if answer == "купить":
                if purse.spend(HERMES_PRICE):
                    print("Игореша купил новую сумочку Гермес, Сережа, посмотри какая !!!")
                else:
                    print("Игореша потратил все деньги на сумочки, какой ужас!")
                    exit()
            else:
                print("Введите 'купить' или 'закончить'!")


    elif choice == "подружка":
        print("Прогулка с подружкой Анкорской наполнила утро светом и лёгкостью.")


def start_story():
    print("\nПарижская дива, Баронесса Де Синяк, проснулась ранним утром…")
    print(f"(У Баронессы сейчас {purse.amount}€)")

    choice = ask_choice("Что выберет Баронесса? (остаться/улица) ", ["остаться", "улица"])
    if choice == "остаться":
        home()
    elif choice == "улица":
        progulka()


def main():
    while True:
        start_story()

        again = input("\nХотите сыграть ещё раз? (y/n): ").strip().lower()
        if again != "y":
            print("До новых встреч! Баронесса уезжает на вечерний раут.")
            break


main()
