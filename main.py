from patternbot import PatternBot

# Main callback for application.
def main():
    bot = PatternBot()
    s_in = ""
    exits = [
        "exit",
        "quit",
        "q",
        "bye",
    ]

    # Greet the user.
    print bot.process_enter()

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

            print "<", s_out
    except EOFError:
        print "ending session"

if __name__ == "__main__":
    main()
