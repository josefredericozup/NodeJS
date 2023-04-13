import os
from templateframework.metadata import Metadata

def run(metadata: Metadata = None):
    path = './package_json'
    metadata.computed_inputs.update({ "package_json_exists": os.path.exists(path)})
    return metadata