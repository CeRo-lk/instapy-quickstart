from instapy import InstaPy
from instapy import smart_run

# get a session!
session = InstaPy(username='cly.dez', password='')

photo_comments = []

# let's go! :>
with smart_run(session):
    # settings
    
    session.set_quota_supervisor(enabled=True, sleep_after=["likes", "comments_d", "follows", "unfollows", "server_calls_h"], 
                                sleepyhead=True, stochastic_flow=True,
                              #peak_likes_hourly=47,
                              #peak_likes_daily=480,
                              #peak_comments_hourly=21,
                              #peak_comments_daily=182,
                              #peak_follows_hourly=48,
                              #peak_follows_daily=479,
                              peak_unfollows_hourly=35,
                              peak_unfollows_daily=402,
                              peak_server_calls_daily=490)
    
    """
    session.set_relationship_bounds(enabled=True, potency_ratio=None, delimit_by_numbers=True, max_followers=900, max_following=1500, min_followers=50, min_following=50)
    session.set_user_interact(amount=3, randomize=True, percentage=100, media='Photo')
    
    #interactions
    session.set_do_like(enabled=True, percentage=69)
    session.set_do_comment(enabled=False, percentage=35)
    session.set_do_follow(enabled=True, percentage=25, times=1)
    session.set_comments(photo_comments)
    
    #optimization
    session.set_action_delays(enabled=True, like=3, comment=5, follow=100, unfollow=40)
    session.set_skip_users(skip_private=True, private_percentage=100, skip_no_profile_pic=False, no_profile_pic_percentage=100, skip_business=True, business_percentage=100)
    session.set_simulation(enabled=True, percentage=66)

    # Core tasks
    session.interact_user_followers(['bhanoob','kelum_devanarayana'], amount=340)
    session.unfollow_users(amount=25, InstapyFollowed=(True, "nonfollowers"), style="RANDOM", unfollow_after=42 * 60 * 60, sleep_delay=600)
    """
    session.unfollow_users(amount=10, nonFollowers=True, style="RANDOM", sleep_delay=655)
