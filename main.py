import os, sys
PLAY32DEV_PATH = "D:\CODE\Python\play32_dev"
sys.path.append(PLAY32DEV_PATH)
import play32env
if __name__ == "__main__":
    current_app_dir_path = os.path.dirname(os.path.abspath(__file__))
    app_name = play32env.setup(current_app_dir_path)
    # >>>> init <<<<
    from play32sys import app
    app.run_app(app_name)
    # >>>> test <<<<
