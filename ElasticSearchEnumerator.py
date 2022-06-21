#!/usr/bin/env python3

import requests
import sys
import json
import re
import itertools

def elk():

    ip =  sys.argv[1]
    port = sys.argv[2]
    protocol = sys.argv[3]
    f_host = f"{protocol}://{ip}:{port}"
    url = re.sub('\?|\!|\'|\n|\'|\;', '', f_host)
    print (url)

    catinfo = [
    "/_cat/segments",
    "/_cat/shards",
    "/_cat/repositories",
    "/_cat/recovery",
    "/_cat/plugins",
    "/_cat/pending_tasks",
    "/_cat/nodes",
    "/_cat/tasks",
    "/_cat/templates",
    "/_cat/thread_pool",
    "/_cat/ml/trained_models",
    "/_cat/transforms/_all",
    "/_cat/aliases",
    "/_cat/allocation",
    "/_cat/ml/anomaly_detectors",
    "/_cat/count",
    "/_cat/ml/data_frame/analytics",
    "/_cat/ml/datafeeds",
    "/_cat/fielddata",
    "/_cat/health",
    "/_cat/indices",
    "/_cat/master",
    "/_cat/nodeattrs",
    "/_cat/nodes"]

    clusterinfo = [
    "/_cluster/allocation/explain",
    "/_cluster/settings","/_cluster/health",
    "/_cluster/state",
    "/_cluster/stats",
    "/_cluster/pending_tasks",
    "/_nodes",
    "/_nodes/usage",
    "/_nodes/hot_threads",
    "/_nodes/stats","/_tasks",
    "/_remote/info"]

    securityinfo = [
    "/_security/user",
    "/_security/privilege",
    "/_security/role_mapping",
    "/_security/role",
    "/_security/api_key"]

    paths = list(itertools.chain(catinfo,clusterinfo,securityinfo))

    for path in paths:

        try:
            f_url = f"{url}{path}?format=json&pretty"
            print(f_url)
            r = requests.request("GET",f_url, verify=False)
            print('===================================================================\n')
            decoded_r = json.loads(r.text)
            print('===================================================================\n')
            print(json.dumps(decoded_r, sort_keys=True, indent=3))

        except:
            print ('Could not execute the following request.')
            sys.exit()

elk()
