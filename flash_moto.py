import xml.etree.ElementTree as ET
import subprocess

def run():
    try:
        tree = ET.parse('flashfile.xml')
        root = tree.getroot()
        steps = root.find('steps')
        
        for step in steps.findall('step'):
            op = step.get('operation')
            part = step.get('partition')
            file = step.get('filename')
            var = step.get('var')
            
            cmd = ["fastboot"]
            if op == 'flash' and part and file:
                cmd += ["flash", part, file]
            elif op == 'erase' and part:
                cmd += ["erase", part]
            elif op == 'oem' and var:
                cmd += ["oem", var]
            elif op == 'getvar' and var:
                cmd += ["getvar", var]
            else:
                continue
                
            print(f"Executando: {' '.join(cmd)}")
            subprocess.run(cmd)
            
    except Exception as e:
        print(f"Erro: {e}")

if __name__ == "__main__":
    run()
