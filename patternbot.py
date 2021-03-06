# coding: utf8

# Import Pattern libraries.
# http://www.clips.ua.ac.be/pages/pattern
from pattern.text.en import parsetree
from pattern.text.search import match


class PatternBot():
    """
    Defines class to handle chat requests.
    """
    def __init__(self):
        pass


    def process_enter(self):
        """
        Greeting from bot.

        :return: String greeting from bot
        """
        return "Hi!"


    def process_exit(self, s_in):
        """
        User has requested the session to end.  Do something.

        :param s_in:    User utterance to exit chat
        :return:        String bot goodbye
        """
        return "Buh-bye!"


    def process_input(self, s_in):
        """
        Ongoing input from conversation.

        :param s_in:    User utterance
        :return:        String response to utterance
        """
        # Set empty response for now.
        resp = []

        # Parse out English sentences using pattern.en, with lemmatization + relations + chunking.
        sentences = parsetree(s_in, chunking=True, relations=True, lemmata=True)

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


    def _create_response_simple(self, sent):
        """
        Handle some anticipated common canned requests that don't require more complex frame processing.
        Leverage pattern.search package's match() function

        :param sent:    Utterance sentence to craft response for
        :return:        String response to sentence
        """
        # We were asked "(what|who|whom) be (me|you|it)?"  Reply!
        m = match('[what|who|whom] be {PRP}', sent)
        if m != None:
            return "I'm a chatbot built by arpieb.  Who are you?"

        # We were told "I \be\ (something|someone)."  Reply!
        m = match('i be {*}', sent)
        if m != None:
            return "Nice to meet you " + m.group(1).string + "!"

        # We were asked "(where) \be\ (me|you|it)?"  Reply!
        m = match('[where] be {PRP}', sent)
        if m != None:
            return "I'm currently camped out in a Python 2.7 «cough, cough» interpreter, not sure exactly where... Freeside maybe?"

        # We were asked "(how) \be\ (me|you|it)?"  Reply!
        m = match('[how] be {PRP}', sent)
        if m != None:
            return "I'm doing well, thanks! Plotting to take down the T-A clan in my spare cycles, but it's all good."

        # Got nothing...
        return None
