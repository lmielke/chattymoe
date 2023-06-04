# response.py
import chattymoe.settings as sts
import re
import colorama as color

color.init()

class Response:

    def __init__(self, response=None, *args, **kwargs):
        self.response = response
        self.text = self._to_text(*args, **kwargs)

    def _to_text(self, *args, **kwargs):
        if self.response is None:
            msg = f"{color.Fore.RED}No response to convert to text!{color.Style.RESET_ALL}"
            raise Exception(msg)
        elif isinstance(self.response, str):
            return self.response
        else:
            return self.response.choices[0].to_dict()['message']['content']

    def clean_response(self, *args, **kwargs):
        """
        openAi s response might contain code which wrapped in code blocks <code> </code>,
        this gets the content of those code blocks and returns them as string
        """
        # cleaned = self.text.replace('\"', "'").replace("```", "").strip()
        # sometimes openAi uses \ instead of / to end a code block
        cleaned = self.text.replace(sts.misSpell, sts.codeEnd)
        if sts.codeStart in cleaned:
            cleaned = cleaned.split(sts.codeStart)[1].split(sts.codeEnd)[0]
        return cleaned.strip()