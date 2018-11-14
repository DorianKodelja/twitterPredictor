from twitter_collect import twitter_connection_setup

#garantie que la fonction twitter_connection_setup renvoit un objet non nul
def test_connection():
    assert twitter_connection_setup.twitter_setup() is not None