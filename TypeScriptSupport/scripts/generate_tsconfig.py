import platform
import requests
import subprocess
from templateframework.metadata import Metadata

def run(metadata: Metadata = None):
    # inputs = metadata.all_inputs()
    inputs_local = metadata.inputs
    # inputs_computed_local = metadata.computed_inputs
    # inputs_global = metadata.global_inputs
    # inputs_computed_global = metadata.global_computed_inputs
    target_path = metadata.target_path
    # component_path = metadata.component_path
    # stack_path = metadata.stack_path
    
    print("- Gerando tsconfig.json...\n")

    if(inputs_local["use_tsconfig_base"] == True):
        tsconfig_file_name = inputs_local["tsconfig_base"].lower()
        url = f"https://raw.githubusercontent.com/tsconfig/bases/main/bases/{tsconfig_file_name}.json"

        response = requests.get(url, allow_redirects=True, verify=False)

        output_file = f"{target_path}/tsconfig.json"
        open(output_file, "wb").write(response.content)
    else:
        command = {
            "Linux": "npx -p typescript tsc --init", 
            "Windows": "cmd /C npx -p typescript tsc --init",
            "Darwin": "npx -p typescript tsc --init"
            }
        subprocess.run(command[platform.system()], shell=True)

    print("- Arquivo tsconfig.json gerado com sucesso!\n")