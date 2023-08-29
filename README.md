### ⇨  Install Script Di Termux
```
$ apt update
$ apt upgrade
$ termux-setup-storage  
   • Enter  
   • Ketik y Atau Pilih Izinkan
$ pkg install python
$ pkg install git
$ git clone https://github.com/noe999x/AutoCreateFB
```
### ⇨  Menjalankan Script
```
$ cd AutoCreateFB
$ pip install -r requirements.txt
$ git pull
$ python create.py
```
### ⇨ Note
The code is unofficial, forked from <a href="https://github.com/Dapunta/AutoCreateFB">AutoCreateFB</a>.
**Mr.Dapunta** has full access to this code, we just added some necessary elements to make the code more tailored to your bot's needs.

Greetz to Mr.Dapunta, and You♥️.

### ⇨ Changelog
> ***29 August 2023***
- Added 2 lists of countries that generate random names:
  * Vietnam                  [VN]
  * Philippines              [PH]
<br>(If you attempt to add random names from countries or lists of your own, make sure to import the key names from your `names.py` into the main `create.py` code.)

- When the code executes phone numbers for account registration, I've added new phone numbers from 3 countries:
  * +1    [USA]
  * +91   [INDIA]
  * +880  [BANGLADESH]
<br>(Implementing changes and additions to this new code doesn't make significant alterations; I'm merely introducing more varied elements.)

- Modified the password generation function which no longer employs random values as the account password. Now, the function generates a random password based on the account name, followed by random numbers.
  * Password example: `@accountname666`

- Made changes to the images used for profile and cover photos of successfully created accounts.
  * You can modify the URL `https://picsum.photos/` to create profile and cover images of your own.

- Adjusted some lines of code.
  * The code will automatically execute when you inadvertently input characters other than numbers in the delay section.
    * Replace `input` with `int(input`.
  * When attempting to recheck a successfully created account, you may have encountered issues with the code not functioning as intended.
    * Therefore, I've made the `title` being searched for more specific during the recheck of "LIVE" accounts, and this issue should now be resolved.
  * etc.

- Removed `realtime.py` as I believed it was a flaw that needed to be eliminated.

> ***15 August 2023***
- Fixed several TypeError issues: 'NoneType' object is not subscriptable.

- Added several additional customized account activity elements to make the output appear more lively. (You can adjust the bot's target settings in the source code to suit your needs.)

- Implemented the option to generate random names from various available countries, including:
  * United States of America [US]
  * India                    [IN]
  * Indonesia                [ID]
  * Pakistan                 [PK]
  * Russia                   [RU]
  * Japan                    [JP]
  * China                    [CN]
  * Zimbabwe                 [ZW]
  * Spain                    [ES]
  * Brazil                   [BR]
  <br>(You can modify and edit the list of names in `names.py` according to your requirements.)

- I made some slight modifications to the appearance, excluding the banner. The banner serves as Mr.Dapunta's personal identification, and I hope you understand that it shouldn't be altered.

- Trimmed unnecessary code that doesn't contribute significantly to the code's execution. (This is my mistake and not recommended to be imitated. However, it seems that Mr.Dapunta doesn't mind it, isn't it? Idk, I apologize for that.)

I have written these updates to fulfill my personal needs. If you turn them into an "issue," I cannot be held responsible for it. This code is authored by Mr.Dapunta, and all copyrights belong to him.

### ⇨ Example
<img src="https://raw.githubusercontent.com/21sysai/21sysai/main/images/IMG_20230815_125804.jpg">

### ⇨ End 🖐️
***
I have written these updates to fulfill my personal needs. If you turn them into an "issue," I cannot be held responsible for it. This code is authored by <a href="https://github.com/Dapunta">**Mr.Dapunta**</a>, and all copyrights belong to him.
***
