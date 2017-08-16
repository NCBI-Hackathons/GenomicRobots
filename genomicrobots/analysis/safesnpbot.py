import yaml
import uuid
import subprocess as sp
from flask import current_app as app
import os


def safe_snp_bot(rsids):
    yaml_file = app.config['ROBOTS_CONFIG']
    with open(yaml_file) as f:
        robot_config = yaml.load(f)

    SESSION_ID = str(uuid.uuid4())

    # create temp dir
    dir_name = robot_config['tmp_pattern'].format(SESSION_ID=SESSION_ID)
    os.mkdir(dir_name)

    # create input file
    with open(os.path.join(dir_name, "rsid.txt"), 'w') as o:
        for rs in rsids:
            o.write("{}\n".format(rs))

    try:
        sp.check_call(['/home/ubuntu/snakemake-robot/bin/snakemake', '--use-conda', '-j', '4'], )
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
