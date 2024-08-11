<pre>
🟦🟦🟦🟦🟦🟦⬜⬜⬜⬜⬜⬜⬜
🟦🟦🟦🟦🟦🟦⬜🟥🟥🟥🟥🟥🟥
🟦🟦🟦🟦🟦🟦⬜⬜⬜⬜⬜⬜⬜
⬜🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥
⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥
⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥
⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
</pre>
#EN autoupdategit - your helper in the server managment!
Automatically update your repository on server (Ubuntu) every day.

Now you can autoupdate your scripts on server without any activities on your side!

❗IMPORTANT❗ 
Please read a Settings section.

❓ How to use it?

Use this steps:
* Download the main file (autoupdate.py) and place it in the directory of your repository.
* Run the file by executing the command "python autoupdate.py".
* To test the functionality, you can use the "forceupdate" command. This command updates your repository without any wait time.
* Your repository will update at 00:00 local time every day.

🛠️ Commands / Settings:

* forceupdate - update your repo without waiting
* countdown - time until next update from git

* In script you have a Settings class, in which you can change foldername and URL (SSH, if your repo has a private visibility) of your repo

📃 Note:

If the script cannot find your repository, it will clone it to the folder containing the autoupdate script.

🖼️ Example with picture (you need to put autoupdate file like this):

![image](https://github.com/sekalYT/autoupdategit/assets/80056228/d1505c63-f3d3-4772-b52f-ce53c98b76e6)


------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

<pre>
⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦
🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦
🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥
</pre>
#RU autoupdategit - ваш помощник в менеджменте сервера!
Автоматическое обновление на сервере (ОС: Ubuntu) каждый день.

Теперь вы можете обновлять свои скрипты на сервере без каких-либо действий с вашей стороны!

❗ВАЖНО❗ 
Пожалуйста прочитайте секцию Настройки.

❓ Как использовать?

Следуйте этим шагам:
* Скачайте основной файл (autoupdate.py) и расположите его в директорию со скриптом.
* Запустите файл с помощью команды "python autoupdate.py" на вашем сервере.
* Для теста, вы можете использовать команду "forceupdate". Эта команда обновит ваш репозиторий без ожидания времени.
* Ваш репозиторий будет обновляться в 00:00 локального времени каждый день.

🛠️ Команды / Настройки:

* forceupdate - обновить репозиторий без ожидания
* countdown - время до следующего обновления

* В скрипте прописан класс Settings, в котором вы можете изменить название папки (в которую хотите установить и проверять обновления репозитория), а также ссылку URL (SSH, если репозиторий приватный) на репозиторий.

📃 Примечание:

Если скрипт не смог найти репозиторий, то он склонирует его в папку, где сам находится

🖼️ Пример с картинкой (вам нужно расположить файл autoupdate как здесь):

![image](https://github.com/sekalYT/autoupdategit/assets/80056228/d1505c63-f3d3-4772-b52f-ce53c98b76e6)
