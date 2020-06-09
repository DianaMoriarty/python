from io import StringIO


START = "Приветствую тебя, путник, в моей сувенирной лавке. \n Могу предложить тебе купить слона."
ARGUMENTS = ["Купи слона!", "Слону одиноко, купи слона!", "Я тебе скидку сделаю, купи слона!",
             "Ковер в подарок при покупке слона, купишь слона?", "Два слона по цене одного, купи слона!"]


def elephant():
    i = 0
    word = ''
    while word != 'yes' and i < 5:
        print(ARGUMENTS[i])
        word = input()
        i += 1
    if word == "yes":
        return "Поздравляю, теперь у вас есть слон!"
    else:
        return "Вы остались без слона."


def test_no(monkeypatch):
    number_inputs = StringIO('No\nNo\nNo\nNo\nNo')
    monkeypatch.setattr('sys.stdin', number_inputs)
    assert elephant() == "Вы остались без слона."


def test_yes(monkeypatch):
    number_inputs = StringIO('yes\n')
    monkeypatch.setattr('sys.stdin', number_inputs)
    assert elephant() == "Поздравляю, теперь у вас есть слон!"

if __name__ == '__main__':
    print(START)
    print(elephant())
