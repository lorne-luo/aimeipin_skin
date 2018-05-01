# -*- coding: utf-8 -*-
import os
import logging
import shlex
import redis
import subprocess
from celery.task import periodic_task, task

log = logging.getLogger(__name__)
r = redis.StrictRedis(host='localhost', port=6379, db=0)


def run_shell_command(command_line):
    """ accept shell command and run"""
    command_line_args = shlex.split(command_line)
    log.info('Subprocess: "' + ' '.join(command_line_args) + '"')

    try:
        command_line_process = subprocess.Popen(
            command_line_args, shell=False, stdout=subprocess.PIPE, stderr=subprocess.STDOUT
        )

        command_line_process.communicate()
        command_line_process.wait()
    except (OSError, subprocess.CalledProcessError) as exception:
        log.info('Exception occured: ' + str(exception))
        log.info('Subprocess failed')
        return False
    else:
        # no exception was raised
        log.info('Subprocess finished')
    return True


@task
def guetzli_compress_image(image_path):
    GUETZLI_CMD = '/opt/guetzli/bin/Release/guetzli'

    if os.path.exists(GUETZLI_CMD):
        cmd = '%s --quality 84 %s %s' % (GUETZLI_CMD, image_path, image_path)
        run_shell_command(cmd)
