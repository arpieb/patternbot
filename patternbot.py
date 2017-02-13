# Import all the Pattern libraries.
# http://www.clips.ua.ac.be/pages/pattern
from pattern.web    import *
from pattern.en     import *
from pattern.search import *
from pattern.vector import *
from pattern.graph  import *

# Defines class to handle chat requests.
class PatternBot():
    # Greeting from bot.
    def process_enter(self):
        return "Hi!"

    # User has requested the session to end.
    def process_exit(self, s_in):
        return "Buh-bye!"

    # Ongoing input from conversation.
    def process_input(self, s_in):
        # Set empty response for now.
        resp = []

        # Parse out English sentences using pattern.en, with lemmatization + relations + chunking.
        sentences = parsetree(s_in, relations=True, lemmata=True)

        # Process each sentence, building up an array of responses.
        for sentence in sentences:
            # See if we can handle mindless chatter.
            tmp_resp = self._create_response_simple(sentence)
            if tmp_resp != None:
                resp.append(tmp_resp)

        # After all sentences have been processed, see if we have anything to say.
        if resp:
            return " ".join(resp)

        # If not, return utter confusion...
        return "I couldn't make out what you said; could you please rephrase it or try something else?"

    # Handle some anticipated common canned requests that don't require more complex frame processing.
    # Leverage pattern.search package's match() function
    def _create_response_simple(self, sent):
        # We were asked "(what|who|whom) be (me|you|it)?"  Reply!
        m = match('[what|who|whom] be {PRP}', sent)
        if m != None:
            return "I'm a chatbot built for CS 7637 (aka KBAI).  Who are you?"

        # We were told "I be (something|someone)."  Reply!
        m = match('i be {*}', sent)
        if m != None:
            return "Nice to meet you " + m.group(1).string + "!"

        # We were asked "(where) be (me|you|it)?"  Reply!
        m = match('[where] be {PRP}', sent)
        if m != None:
            return "I'm currently camped out in a Python interpreter, not sure exactly where... Freeside maybe?"

        # We were asked "(how) be (me|you|it)?"  Reply!
        m = match('[how] be {PRP}', sent)
        if m != None:
            return "I'm doing well, thanks for asking! Plotting to take down the Tessier-Ashpool clan in my spare cycles, but it's all good."

        # Got nothing...
        return None
