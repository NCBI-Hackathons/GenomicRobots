import yaml
import uuid
import os
import os.path
import subprocess as sp
from flask import current_app as app
import copy


def safe_snp_bot(rsids):
    yaml_file_name = app.config['ROBOTS_CONFIG']
    with open(yaml_file_name) as f:
        robot_config = yaml.load(f)

    SESSION_ID = str(uuid.uuid4())

    rsid_file_name = robot_config['tmp_pattern'].format(SESSION_ID=SESSION_ID)

    # create temp dir
    dir_name = os.path.dirname(rsid_file_name)
    os.mkdir(dir_name)

    # create input file
    with open(rsid_file_name, 'w') as o:
        for rs in rsids:
            o.write("{}\n".format(rs))

    try:
        snakemake_file_name = os.path.dirname(yaml_file_name) + '/Snakefile'
        snake_env = copy.copy(os.environ)
        snake_env['SESSION_ID'] = SESSION_ID
        sp.check_call(
            ['/home/ubuntu/snakemake-robot/bin/snakemake',
                '-s', snakemake_file_name,
                '-d', os.path.dirname(yaml_file_name),
                '--configfile', yaml_file_name,
                '--use-conda',
                '-j', '16'], env=snake_env)
    except sp.CalledProcessError:
        return

    reported_rsids = []
    with open(os.path.join(dir_name, "output.txt")) as f:
        for line in f:
            reported_rsids.append(line.strip())

    results = []
    for rs in rsids:
        results.append({
            'rs': rs,
            'status': "YES" if rs in reported_rsids else "NO",
        })

    return results
