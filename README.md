# Лабораторная работа №1 - Отчет

## Выполненные задания

### 1. Настройка Git конфигурации
**Команды:**
```bash
git config --global user.name "timoonnovi"
git config --global user.email "pasko.id@phystech.su"
git config --global core.editor "vim"
git config --global core.autocrlf input
git config --global credential.helper cache
git config --global help.autocorrect prompt
git config --global commit.gpgsign true
git config --global tag.gpgsign true
```

**Результат:** Git настроен на глобальном уровне (`~/.gitconfig`)

### 2. Генерация SSH ключа
**Команды:**
```bash
ssh-keygen -t rsa -b 4096 -C "pasko.id@phystech.su"
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_rsa
```

**Результат:** SSH ключ создан и добавлен в GitHub как Authentication key

### 3. Personal Token с правами gist
**Команды:**
```bash
echo *** > ~/.github_token
chmod 600 ~/.github_token
```

**Результат:** Токен сохранен в `~/.github_token` с правами доступа 600

### 4. GnuPG для подписания коммитов
**Команды:**
```bash
gpg --full-generate-key # Создание ключа с выбором его типа
gpg --list-secret-keys --keyid-format=long # Вывод всех ключей в длинной форме
gpg --armor --export AD97B7D35E5FC681  # Экспорт публичного ключа в ASCII формате
git config --global user.signingkey # Внесение вложенного ключа (обоих)
git config --global commit.gpgsign true # Подпись всех фиксаций
git config --global tag.gpgSign true # Подпись всех тегов
```

**Результат:** GPG ключ создан (ID: AD97B7D35E5FC681), все коммиты автоматически подписываются

**Что такое smimesign:**
`smimesign` - инструмент для подписания коммитов Git с использованием X.509 сертификатов (S/MIME). Альтернатива GnuPG для подписания коммитов, использует сертификаты вместо GPG ключей.

### 5. Создание hello.py
**Первая версия (грязный код):**
```python
print("Enter your name")
a = input()
print("enter if you want the dialog to be formal y/n")
b = input()
if b == 'y':
    formal = True
    print("The pleasure is mine, %name%")
else:
    formal = False
    print("Hi, "+a+"!")
```

**Команды:**
```bash
git add hello.py
git commit -m "added hello.py"
```
Дальше код немного модифицирован и снова закоммичен + закинут в удалённый репозиторий:
```bash
git add hello.py
git commit -m "modified hello.py"
git push
```

**Проверка с интерпретаторами:**
- Python3: работает

### 6. Работа с ветками и PR

**Создание ветки patch1:**
```bash
git branch patch1
git switch patch1
```

**Модификация кода:**
```python
import typer

def main(
    name: str,
    lastname: str = typer.Option("", help="Фамилия пользователя."),
    formal: bool = typer.Option(False, "--formal", "-f", help="Использовать формальное приветствие."),
):
    """
    Говорит "Привет" пользователю, опционально используя фамилию и формальный стиль.
    """
    if formal:
        print(f"Добрый день, {name} {lastname}!")
    else:
        print(f"Привет, {name}!")

if __name__ == "__main__":
    typer.run(main)
```

**Код залит на гитхаб**
```bash
git add .
git commit -m "modified hello.py"
git push
```

**Создание pull-request:**
- PR #1: patch1 -> main (создан через web)
- Внесение комментариев в hello.py ветки patch1 на github через web
- Комментарии видны в pull-request
- Принятие pull-реквеста, успешное слияние веток
- Удаление ветки patch1

```bash
git pull
git log --oneline --graph --all main
git branch -d patch1
```

### 7. Работа с конфликтами (patch2)

**Создание ветки patch2:**
```bash
git branch patch2
git switch patch2
```

**Изменение code style:**
- Изменено написание имён
- Исправлены ошибки форматирования

**Создание конфликта:**
```bash
git add .
git commit -m "codestyle changed"
git push
```

- Создание pull-request #2: patch2 -> main через api
- Изменение комменатрия в hello.py ветки main через web
- Конфликт pull-request

```bash
git pull --rebase origin
git commit
git push
```

- Расхождения исправлены
- pull-request #2: patch2 -> main принят
- Слияние успешно


## История коммитов

### Локальный репозиторий:
```
* 9b7546d (HEAD -> patch2, origin/patch2) 123
*   6925c25 Merge branch 'main' into patch2
|\  
| * b4472c1 (origin/main, main) Changed comment
* | 1ae6834 changed comment to resolve conflict
* | 078b4c3 codestyle changed
|/  
*   c73c1f9 Merge pull request #1 from timoonnovi/patch1
|\  
| * 28c778c Update hello.py
| * 37d8673 (origin/patch1) modified hello.py
|/  
* d15e3ae modified hello.py
* 7b10d96 added hello.py
* 0ba94a2 Initial commit
```

### Удаленный репозиторий:
Все коммиты синхронизированы с `origin/main`

## Использованные инструменты

- Git 2.34.1
- GnuPG 2.2.27
- GitHub CLI 2.4.0
- Python 3.14
- SSH (rsa 4096)

## Выводы

Выполнены все задания лабораторной работы:
- Настроен Git с подписанием коммитов
- Создан и настроен SSH ключ
- Создан GPG ключ для подписания
- Выполнена работа с ветками, PR и конфликтами
- Освоены команды rebase для разрешения конфликтов
