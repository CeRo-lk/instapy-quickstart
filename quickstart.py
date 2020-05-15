from instapy import InstaPy
from instapy import smart_run

# get a session!
session = InstaPy(username='cly.dez', password='')

photo_comments = []

# let's go! :>
with smart_run(session):
    # settings
    session.set_user_interact(amount=3, randomize=True, percentage=100,
                              media='Photo')
    session.set_relationship_bounds(enabled=True,
                                    potency_ratio=None,
                                    delimit_by_numbers=True,
                                    max_followers=3000,
                                    max_following=1500,
                                    min_followers=50,
                                    min_following=50)
    session.set_simulation(enabled=True, percentage=66)
    session.set_do_like(enabled=True, percentage=69)
    session.set_ignore_users([])
    session.set_do_comment(enabled=False, percentage=35)
    session.set_do_follow(enabled=True, percentage=25, times=1)
    session.set_comments(photo_comments)
    session.set_ignore_if_contains([])
    session.set_action_delays(enabled=True, like=40)
    session.set_action_delays(enabled=True, like=3, comment=5, follow=100, unfollow=40)
    session.set_skip_users(skip_private=True, private_percentage=100, skip_no_profile_pic=False, no_profile_pic_percentage=100, skip_business=True, business_percentage=100)

    # activity
    session.interact_user_followers(['bhanoob','kelum_devanarayana'], amount=340)
