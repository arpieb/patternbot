# PatternBot

**PatternBot** is a Python-based chatbot agent built using the [CLiPS Pattern](http://www.clips.ua.ac.be/pages/pattern) library.
It is currently hardwired for English, even though the Pattern library supports several languages out of the box.

# Installation

1. Clone this repo
2. Alternatively initalize a [virtual environment](http://docs.python-guide.org/en/latest/dev/virtualenvs/)
3. Install dependencies using `pip install -r requirements.txt`

# Usage

The bot is encapsulated in a class called **PatternBot** located in `patternbot.py`.  To test it from a terminal or command line, execute `python main.py` and have fun!

To exit, type something like `quit` or `exit` or just hit `Ctrl-D`.

```bash
$ python main.py
PatternBot OCP (20170212)
To end the session, type `exit`, `quit` or hit Ctrl-D.

Hi!
> who are you?
< I'm a chatbot built for CS 7637 (aka KBAI).  Who are you?
> i'm rob
< Nice to meet you rob!
> where are you?
< I'm currently camped out in a Python interpreter, not sure exactly where... Freeside maybe?
> how are you?
< I'm doing well, thanks! Plotting to take down the T-A clan in my spare cycles, but it's all good.
> do you like green eggs and ham?
< I couldn't make out what you said; could you please rephrase it or try something else?
> bye
< Buh-bye!
```

# Customizing

The **PatternBot** class implements three required methods:

| Method | Description |
| ------ | ----------- |
|process_enter|Called by the controlling application to allow the 'bot to greet the user.|
|process_exit|Called by the controlling application to allow the 'bot to say good bye.|
|process_input|Main workhorse of the agent, this method takes the input string from the controlling application and expects a string to be returned.|

Customizing the behavior of these methods is what will give your 'bot not only a personality, but core functionality.

# Useful data sources

To support OMSCS course information, the following low-hanging data sources might come in handy:

* [Georgia Tech Course Catalog (JSON)](https://raw.githubusercontent.com/GatechVIP/Courses/master/app/json/GatechCourses.json)
* [OMSCS Course Surveys API](https://omscentral.com/about/faq) (under _How can I access the data?_)
* The bundled [pattern.web](http://www.clips.ua.ac.be/pages/pattern-web) module has support for a variety of search engines, Wikipedia, and a targeted crawler engine
