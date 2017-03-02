#!/usr/bin/env python3
# encoding: utf-8

import argparse
import logging
import sys

from .logging import init_logging
from .logging import set_root_log_level
from .session import init_session

module = sys.modules['__main__'].__file__
log = logging.getLogger(module)

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-p', '--profile',
        default=None,
        help='AWS credentials profile to use')
    parser.add_argument(
        '-r', '--region',
        default='us-west-1',
        help='AWS region to connect to')
    parser.add_argument(
        '-v', '--verbose', dest='verbosity',
        action='count', default=0,
        help='Increases log verbosity (can be specified multiple times).')
    return parser.parse_args()

def core():
    args = parse_args()
    set_root_log_level(args.verbosity)
    session = init_session(args.profile)
    ### EXAMPLE CODE FOLLOWS - REPLACE WITH YOUR LOGIC ###
    # A general boto pattern to grab a client/resource is:
    #   resource/client = session.resource/client('name', region_name=args.region)
    client = session.client('sts', region_name=args.region)
    caller_id = client.get_caller_identity()
    del caller_id['ResponseMetadata']
    print(caller_id)
    ### END EXAMPLE CODE ###

def main():
    init_logging()
    try:
        return core()
    except KeyboardInterrupt:
        log.error('Received SIGINT')
    finally:
        logging.shutdown()

if __name__ == '__main__':
    sys.exit(main())
