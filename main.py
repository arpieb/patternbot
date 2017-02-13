from patternbot import PatternBot

# Main callback for application.
def main():
    # Print application header.
    print "PatternBot OCP (20170212)"
    print "To end the session, type `exit`, `quit` or hit Ctrl-D."
    print

    # Initialize locals.
    s_in = ""
    exits = [
        "exit",
        "quit",
        "q",
        "bye",
    ]

    # Initialize the bot and give it a chance to greet the user.
    bot = PatternBot()
    print "<", bot.process_enter()

    try:
        # Go into input loop.
        while s_in not in exits:
            # Ask for input.
            s_in = raw_input("> ").strip()

            # Check for an exit phrase.
            if s_in in exits:
                s_out = bot.process_exit(s_in)
            else:
                s_out = bot.process_input(s_in)

            # Print the response from the bot.
            print "<", s_out

    except EOFError:
        print "\nending session"

if __name__ == "__main__":
    main()
