import datetime
import logging
import sys

import arrow
import boto3
import botocore
import botocore.exceptions

from .assumerole import JSONFileCache
log = logging.getLogger(__name__)

class AlternativeDateTime(arrow.Arrow, datetime.datetime):
    """Arrow already implements the full datetime interface.
    However, in a few places boto does and isinstance(datetime.datetime) check.
    So, this is an Arrow object with datetime.datetime in its class heirarchy.
    Gross? yes
    Solves my problems? also yes
    """
    pass

def configure_timestamp_parser(session):
    """Change boto timestamp parsing to return Arrow objects"""
    arrow_factory = arrow.ArrowFactory(AlternativeDateTime)
    parser_factory = session.get_component('response_parser_factory')
    parser_factory.set_parser_defaults(timestamp_parser=arrow_factory.get)

def configure_awscli_credential_cache(session):
    """Have the assume-role provider use the awscli session cache"""
    component = session.get_component('credential_provider')
    provider = component.get_provider('assume-role')
    provider.cache = JSONFileCache()

def init_session(profile=None):
    """Create a customized boto3.session

    The session will use the same assume-role cache as awscli,
    and it will return timestamps as Arrow objects.
    """
    core_session = botocore.session.Session(profile=profile)
    try:
        configure_awscli_credential_cache(core_session)
        configure_timestamp_parser(core_session)
        session = boto3.Session(botocore_session=core_session)
    except botocore.exceptions.ProfileNotFound:
        log.error(f'Could not find profile: "{profile}"')
        log.error(f'Available profiles: {core_session.available_profiles}')
        sys.exit(1)
    if not session.get_credentials():
        log.error("Boto couldn't find any AWS credentials.\n"
                  "Try using --profile or putting creds in your ENV")
        sys.exit(1)
    return session
