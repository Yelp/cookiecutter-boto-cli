This is a [cookiecutter][cookiecutter] template for quickly creating CLI-driven python apps to interact with the AWS APIs (via [boto3][boto3]).

With cookiecutter installed, starting a new app from the template is as simple as:
```
cookiecutter gh:yelp/cookicutter-boto-cli
```
After following the prompts, you can immediatly run `make venv` and start editing `main.py`.

Features include:

 * Pre-configured argument parsing
 * Pre-configured logging
 * Boto pre-configured to share the same assume-role session cache as [awscli][awscli]
 * Boto pre-configured to return Arrow objects
 * A Makefile target to bundle your code into a [PEX][PEX] file

[awscli]: https://aws.amazon.com/cli/
[boto3]: https://boto3.readthedocs.io/en/latest/
[cookiecutter]: https://github.com/audreyr/cookiecutter
[PEX]: https://pex.readthedocs.io/en/stable/
