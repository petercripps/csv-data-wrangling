import yaml
import sys

yfile = "config.yaml"

def init_config():
    try:
        with open(yfile) as f:
            return (yaml.load(f, Loader=yaml.FullLoader))
    except:
        print(f"ERROR YAML file error: {yfile}")
        sys.exit("FATAL ERROR Cannot continue")
        return {}


configdict = init_config()


if __name__ == "__main__":
    # execute only if run as a script
    print("Testing...")
    
    if True:
        print(configdict)