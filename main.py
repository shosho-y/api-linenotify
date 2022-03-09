import requests
import tweepy

def notify_message(message):
    token="NSM5ITw6xSDWMT58WUTRaMqSQxtcitHDafjt9TWyGxr"
    url="https://notify-api.line.me/api/notify"
    headers={"Authorization":"Bearer "+token}
    data={'message':message}
    requests.post(url, headers=headers, data=data)
    

def get_n_followers():
    consumer_key='oNZcJAx89cmCMfjcVVD8CrEuS'
    consumer_secret='7zRctquMRyEyJxgQZsX5WMPzIHhhQeBD8ZqjY9sj8bjMR7qAHI'
    access_token='1416707687761420290-YR2r0XMztYYln2ju1umGmqJGxM9pXH'
    access_token_secret='Z6AtbjP68E0YJijytr9k2ENHin2InNkUm5Mnn3A9OssRt'

    auth=tweepy.OAuthHandler(consumer_key,consumer_secret)
    auth.set_access_token(access_token,access_token_secret)

    api=tweepy.API(auth)

    user=api.get_user(screen_name='@NetflixJP')
    n_followers=user.followers_count

    return n_followers

def main():
    n_followers=get_n_followers()
    message=f'本日のフォロワー数は{n_followers}です!'
    notify_message(message)
    
if __name__=='__main__':
    main()