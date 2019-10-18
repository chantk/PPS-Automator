Idea comes from [lihkg](s://lihkg.com/thread/1637669/)

This program help you pay your bill one dollar each time on the pps webpage.

Developing with Python3 and Selenium web driver

**Before you begin**

   1. Use it at your own risk.
   2. Start with a small amount and see if it works.
   3. You need to register the bill before using this automator.
   4. Check the version of your Chrome browser. (**Make sure the web driver you download be compatible with the chrome brwoser on your PC otherwise something wrong might happen.**)
   5. **__Do not minimize the Chrome windows in the background (the process will be crashed__**
   
### Step 1: [Download chrome driver](https://chromedriver.chromium.org/)

### Step 2: install Dependencies
```
pip install -r requirements.txt
```

### Step 3: Run the main script
```
python3 main.py
```

### Todo

- [ ] Migrate to QT5
- [ ] Auto download browser drivers
- [ ] Add support to firefox
- [ ] Refactor codebase


### FAQ

How does it work?


> The program does not relay any message to third parties, it first collect the information about the bill type and the bill no., then evoke the chromdriver to create a programmable browser (chrome) instance. The user will then login to the PPS website as usual, once the program detects the login has been done (by checking the redirected URL in the browser), it will send commands to break down your bill, and pay 1.01-1.09 each time until the target amount is reached (usually a little bit over, less than 2 dollars). No data will be stored in the program.


### Can I just run it without using the program?

> Yes, there's a related project written in chrome extension. [check it out](https://github.com/freehk-developer/chrome-ppshk-pay-bot)


This program may be not working once PPS HK updates the website, please submit issues if there're any problems










