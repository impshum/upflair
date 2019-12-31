import praw
import configparser
import datetime
import schedule
from time import sleep
from halo import Halo


def get_days_ago(days_back):
    time_limit = datetime.datetime.now() - datetime.timedelta(days=days_back)
    return int(time_limit.timestamp())



class C:
    W, G, R, P, Y, C = '\033[0m', '\033[92m', '\033[91m', '\033[95m', '\033[93m', '\033[36m'



def runner(config, spinner):
    reddit_user = config['REDDIT']['reddit_user']
    reddit_pass = config['REDDIT']['reddit_pass']
    client_id = config['REDDIT']['client_id']
    client_secret = config['REDDIT']['client_secret']
    target_subreddit = config['SETTINGS']['target_subreddit']
    target_score = int(config['SETTINGS']['target_score'])
    time_limit = int(config['SETTINGS']['time_limit'])
    flair_text = config['SETTINGS']['flair_text']
    flair_css_class = config['SETTINGS']['flair_css_class']
    verbose_mode = config['SETTINGS'].getboolean('verbose_mode')
    test_mode = config['SETTINGS'].getboolean('test_mode')

    if not verbose_mode:
        spinner.start()

    reddit = praw.Reddit(
        username=reddit_user,
        password=reddit_pass,
        client_id=client_id,
        client_secret=client_secret,
        user_agent='Upflair (by u/impshum)'
    )

    days_ago = get_days_ago(time_limit)
    sub = reddit.subreddit(target_subreddit)

    for submission in sub.new(limit=None):
        score = submission.score
        saved = submission.saved
        author = submission.author.name
        created = submission.created_utc

        if created >= days_ago and not saved:
            if score >= target_score:
                c = C.G
                if not test_mode:
                    sub.flair.set(author, flair_text, css_class=flair_css_class)
                    submission.save()
            else:
                c = C.Y
        else:
            if score >= target_score:
                c = C.P
            else:
                c = C.R
            if not test_mode:
                submission.save()

        if verbose_mode:
            print(f'{c}{author} {score}{C.W}')
        else:
            msg = f'{c}{author} {score}{C.W}'
            spinner.text = msg
            sleep(.3)
    spinner.text = ''



def main():
    config = configparser.ConfigParser()
    config.read('conf.ini')
    test_mode = config['SETTINGS'].getboolean('test_mode')
    verbose_mode = config['SETTINGS'].getboolean('verbose_mode')
    sleep_time = int(config['SETTINGS']['sleep_time'])
    spinner = Halo(text='', spinner='dots')

    tm = ''
    if test_mode:
        tm = f'{C.R}TEST MODE{C.Y}'

    print(f"""{C.Y}
╦ ╦╔═╗╔═╗╦  ╔═╗╦╦═╗
║ ║╠═╝╠╣ ║  ╠═╣║╠╦╝ {tm}
╚═╝╩  ╚  ╩═╝╩ ╩╩╩╚═ {C.C}v1.0 {C.G}impshum{C.W}
    """)

    runner(config, spinner)
    schedule.every(sleep_time).seconds.do(runner, config, spinner)
    while True:
        schedule.run_pending()
        sleep(1)


if __name__ == '__main__':
    main()
