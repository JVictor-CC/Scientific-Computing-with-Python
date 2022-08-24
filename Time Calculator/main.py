# This entrypoint file to be used in development. Start by reading README.md
from time_calculator import add_time
from unittest import main


print(add_time("11:36 PM", "27:50","moNday"))


# Run unit tests automatically
main(module='test_module', exit=False)