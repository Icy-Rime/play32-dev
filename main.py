import os, sys
PLAY32DEV_PATH = "D:\CODE\Python\play32_dev"
sys.path.append(PLAY32DEV_PATH)
import play32env
if __name__ == "__main__":
    app_dir = os.path.dirname(os.path.abspath(__file__))
    play32env.setup(app_dir)
    # >>>> test <<<<
