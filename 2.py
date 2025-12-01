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

purse = Money(15000)
HERMES_PRICE = 3000


def ask_choice(prompt, options):
    while True:
        choice = input(prompt)
        if choice in options:
            return choice
        else:
            print("Ошибка: выберите один из предложенных вариантов!")

def home():
    print("Баронесса решила остаться дома — расслабиться и провести утро в роскошной тишине своих апартаментов.")

    choice = ask_choice("Чем она займётся? (обзор/образы) ", ["обзор", "образы"])

    if choice == "обзор":
        print("Баронесса записала утончённый обзор на капсульную коллекцию именитого бренда. Видео сразу стало вирусным.")
    elif choice == "образы":
        print("Баронесса придумала новые образы для будущих клипов и заказала платье ручной работы из Дубая. Съёмка обещает быть грандиозной.")

def progulka():
    print("Баронесса решила выйти в свет — Париж манит роскошью.")

    choice = ask_choice("Куда направится Баронесса? (гермес/подружка) ", ["гермес", "подружка"])

    if choice == "гермес":
        print("Баронесса направилась в Hermès…")
        while True:
            answer = input("Купить новую сумочку Hermes или всё? (купить/закончить): ")
            if answer == "закончить":
                print("Баронесса приняла мудрое решение перестать тратить все свои деньги на сумочки......пока что")
                break

            if answer == "купить":
                if purse.spend(HERMES_PRICE):
                    print("Серёжааа, посмотри на мою сумочку из кожи в стиле леопардовый шик!")
                else:
                    print("Игорёша, ты потратил все деньги! А ну ка пойдем домой")
                    exit()
            else:
                print("Введите 'купить' или 'закончить'!")


    elif choice == "подружка":
        print("Баронесса поехала на шоппинг со своей подругой Анкорской. Впереди — прогулки, покупки и бесконечные разговоры о моде.")

def start_story():
    print("\nПарижская дива, Баронесса Де Синяк, проснулась ранним утром и задумалась... "
          "Выйти ли сегодня в свет или остаться дома?")

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