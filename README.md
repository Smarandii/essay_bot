## This bot will help you to check basic mistakes in english essay from English Unified state examination:
- /countwords - calculate words quantity (takes first 275 symbols if the text is longer than 275 symbols)
- /countmistakes - counts all mistakes in the essay
- /checkwords - checks all words for typos and etc.
- /checkcomma - checks all basic comma rules
- /checkshortcuts - checks is there is any shortcuts used
- /findmistakes - firstly counting words, after finds all mistakes 


## Usage:
1. ![image](https://user-images.githubusercontent.com/48328325/200233828-a9f2a56e-cd53-497b-846a-06d9d1bce097.png)
2. ![image](https://user-images.githubusercontent.com/48328325/200233879-811fbe06-41c2-4a18-aa98-a4ddafb4de51.png)
3. ![image](https://user-images.githubusercontent.com/48328325/200233915-adc759f9-236a-4f21-8635-ff2dcce38730.png)
4. ![image](https://user-images.githubusercontent.com/48328325/200234073-c24894c0-0b46-4ef6-bcab-2fe1e958a843.png)


## Run this bot localy on your computer:
1. run **cmd**
1. change working directory to repository directory (`cd` command)

**Pro-tip: To change drive in Windows use (D: - change drive to drive D | C: - change drive to drive C)**
1. run `python -m venv env` with **cmd** in repository directory
1. run virtual environment "env" (`.\env\Scripts\activate` for Windows)
1. run `pip install -r requirements.txt`
2. [get telegram bot token](t.me/BotFather)
3. add token in `bot.py` in `token` variable
4. run `python bot.py`
5. go to your bot in telegram and start using (BotFather gave you link to your bot)!
