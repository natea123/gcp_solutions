#!/usr/bin/env python

# Copyright 2019 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the 'License');
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

#Lists all projects that the caller has access to view and then loops through and lists all GCS buckets within that project

from google.cloud import storage
from google.cloud import resource_manager

def list_projects():
    projs = []
    client = resource_manager.Client()

    # List all projects you have access to and returns them as an array of strings
    for project in client.list_projects():
        projs.append(project.project_id)

    return projs


def list_buckets(x):
    """Lists all buckets in project x."""

    storage_client = storage.Client(project=x)
    buckets = storage_client.list_buckets()

    print("~~~ALL BUCKETS IN PROJECT: {}~~~".format(x))
    for bucket in buckets:
        print(bucket.name)




if __name__ == "__main__":

    projects = list_projects()
    for p in projects:
        list_buckets(p)

