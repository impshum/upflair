## Upflair

Assigns a chosen flair when submission get to n score

![](ss.jpg)

### Instructions

-   Install requirements `pip install -r requirements.txt`
-   Create Reddit (script) app at https://www.reddit.com/prefs/apps/ and get keys
-   Edit conf.ini with your details
-   Run it `python run.py`

#### Settings Info

-   `target_subreddit` - Bot account must be mod
-   `target_score` - Minimum score to trigger flair assignment
-   `time_limit` - How many days to reach target score
-   `sleep_time` - Seconds between runs
-   `flair_text` - The flair text
-   `flair_css_class` - Assign class in Reddit CSS stylesheet (OLD REDDIT)
-   `verbose_mode` - List results or not???
-   `test_mode` - Run the script without any actions

### CSS flair class (OLD REDDIT)

Add this to your CSS stylesheet and edit to your liking.

    .flair-winner {
        background-color: #19572a;
        color: #fff;
        padding: 2px 19px;
        font-weight: 600;
    }

---

BTC - 1AYSiE7mhR9XshtS4mU2rRoAGxN8wSo4tK
