from asciinema.commands.command import Command
from asciinema.api import APIError


class UploadCommand(Command):

    def __init__(self, api, filename, insecure):
        Command.__init__(self)
        self.api = api
        self.filename = filename
        self.insecure = insecure

    def execute(self):
        try:
            if self.insecure:
                self.print("NOTICE: Insecure mode selected.  All SSL Checks will be suppressed")

            url, warn = self.api.upload_asciicast(self.filename)

            if warn:
                self.print_warning(warn)

            #TODO Need to fix this to reflect env API endpoint
            self.print(url)

        except OSError as e:
            self.print_error("upload failed: %s" % str(e))
            return 1

        except APIError as e:
            self.print_error("upload failed: %s" % str(e))
            self.print_error("retry later by running: asciinema upload %s" % self.filename)
            return 1

        return 0
