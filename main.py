import os, sys
PLAY32DEV_PATH = "/run/media/dreagonmon/Data/Code/Python/play32-dev"
sys.path.append(PLAY32DEV_PATH)
import play32env
if __name__ == "__main__":
    app_dir = os.path.dirname(os.path.abspath(__file__))
    play32env.setup(app_dir)
    # >>>> test <<<<
    play32env.start()
    # play32env.start_app(app_name, *app_args, **app_kws)
