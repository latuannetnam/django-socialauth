from socialauth.models import UserProfile
import logging
logger = logging.getLogger(__name__)
def get_profile(
    backend,
    user,
    response,
    details,
    is_new=False,
    *args,
    **kwargs
    ):
    img_url = None

    #Get photo
    if backend.name == 'facebook':
        img_url = 'http://graph.facebook.com/%s/picture?type=large' \
            % response['id']
    elif backend.name == 'twitter':
        img_url = response.get('profile_image_url', '').replace('_normal', '')
    if backend.name == 'google-oauth2':
        if response.get('image') and response['image'].get('url'):
            img_url = response['image'].get('url')

    logger.debug("Image url:%s" % img_url)
    profile = UserProfile.objects.get_or_create(user = user)[0]

    logger.debug("details:%s" % details)
    #logger.debug("response:%s" % response)
    profile.username = details['username']
    profile.fullname = details['fullname']
    profile.first_name = details['first_name']
    profile.last_name = details['last_name']
    profile.email = details['email']
    profile.photo = img_url
    profile.key = backend.strategy.session_get('key')
    profile.backend= backend.name
    profile.save()




    # profile1 = user.profile
    # attrs = vars(profile1)
    # logger.debug("profile1:%s" % attrs)





