# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AccountPCountry(models.Model):
    country_id = models.CharField(primary_key=True, max_length=250)
    sort_name = models.CharField(max_length=250)
    country = models.CharField(max_length=250)

    class Meta:
        managed = False
        db_table = 'account_p_country'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group_id = models.IntegerField()
    permission_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'


class AuthPermission(models.Model):
    name = models.CharField(max_length=50)
    content_type_id = models.IntegerField()
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class BlogComment(models.Model):
    blog_comment_id = models.AutoField(primary_key=True)
    queries = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'blog_comment'


class CitationParams(models.Model):
    firstname = models.CharField(max_length=255, blank=True, null=True)
    lastname = models.CharField(max_length=255, blank=True, null=True)
    nickname = models.CharField(max_length=255, blank=True, null=True)
    gender = models.CharField(max_length=255, blank=True, null=True)
    day = models.CharField(max_length=255, blank=True, null=True)
    month = models.CharField(max_length=255, blank=True, null=True)
    year = models.CharField(max_length=255, blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    mobile = models.CharField(max_length=255, blank=True, null=True)
    website = models.CharField(max_length=255, blank=True, null=True)
    password = models.CharField(max_length=255, blank=True, null=True)
    confirm_password = models.CharField(max_length=255, blank=True, null=True)
    street_address = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=255, blank=True, null=True)
    state = models.CharField(max_length=255, blank=True, null=True)
    pincode = models.CharField(max_length=255, blank=True, null=True)
    country = models.CharField(max_length=255, blank=True, null=True)
    business_title = models.CharField(max_length=255, blank=True, null=True)
    business_desc = models.TextField(blank=True, null=True)
    business_country = models.CharField(max_length=255, blank=True, null=True)
    business_category = models.CharField(max_length=255, blank=True, null=True)
    categories = models.CharField(max_length=255, blank=True, null=True)
    years_of_estd = models.CharField(max_length=255, blank=True, null=True)
    no_of_emp = models.CharField(max_length=255, blank=True, null=True)
    annual_turn_over = models.CharField(max_length=255, blank=True, null=True)
    total_income = models.CharField(max_length=255, blank=True, null=True)
    currency_type = models.CharField(max_length=255, blank=True, null=True)
    ownership_type = models.CharField(max_length=255, blank=True, null=True)
    image = models.CharField(max_length=255, blank=True, null=True)
    logo = models.CharField(max_length=255, blank=True, null=True)
    local_time = models.DateTimeField(blank=True, null=True)
    blog = models.TextField(blank=True, null=True)
    faxnumber = models.CharField(max_length=80, blank=True, null=True)
    twitter = models.CharField(max_length=25, blank=True, null=True)
    skype = models.CharField(max_length=25, blank=True, null=True)
    msn = models.CharField(max_length=25, blank=True, null=True)
    business_tag = models.CharField(max_length=25, blank=True, null=True)
    company_founded_month = models.IntegerField(blank=True, null=True)
    company_founded_year = models.IntegerField(blank=True, null=True)
    company_email = models.TextField(blank=True, null=True)
    facebook = models.CharField(max_length=50, blank=True, null=True)
    youtube = models.CharField(max_length=50, blank=True, null=True)
    pinterest = models.CharField(max_length=50, blank=True, null=True)
    linkedin = models.CharField(db_column='linkedIn', max_length=50, blank=True, null=True)  # Field name made lowercase.
    keywords = models.TextField(blank=True, null=True)
    designation = models.TextField(blank=True, null=True)
    language = models.TextField(blank=True, null=True)
    sector = models.TextField(blank=True, null=True)
    price = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'citation_params'


class DjangoContentType(models.Model):
    name = models.CharField(max_length=100)
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class FirstAppPState1(models.Model):
    state_id = models.IntegerField()
    state = models.CharField(max_length=30)
    country_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'first_app_p_state1'


class Frequency(models.Model):
    frequency_id = models.AutoField(primary_key=True)
    frequency = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'frequency'


class Keyword(models.Model):
    keyword_id = models.AutoField(primary_key=True)
    website_id = models.IntegerField(blank=True, null=True)
    keyword = models.CharField(unique=True, max_length=255, blank=True, null=True)
    call_success = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'keyword'


class LDirectoryDetail(models.Model):
    directory_id = models.IntegerField(primary_key=True)
    domain_authority = models.IntegerField(blank=True, null=True)
    page_authority = models.IntegerField(blank=True, null=True)
    spam_score = models.IntegerField(blank=True, null=True)
    domain_age = models.TextField(blank=True, null=True)
    is_domain_up = models.IntegerField(blank=True, null=True)
    is_domain_expired = models.IntegerField(blank=True, null=True)
    majestic_trustflow = models.IntegerField(blank=True, null=True)
    alexa_global_ranking = models.IntegerField(blank=True, null=True)
    alexa_traffic_country = models.IntegerField(blank=True, null=True)
    majestic_citationflow = models.IntegerField(blank=True, null=True)
    niche = models.CharField(max_length=45, blank=True, null=True)
    country = models.CharField(max_length=45, blank=True, null=True)
    is_https = models.IntegerField(blank=True, null=True)
    is_dofollow = models.IntegerField(blank=True, null=True)
    update_date = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'l_directory_detail'


class LDirectoryList(models.Model):
    directory_id = models.AutoField(primary_key=True)
    website = models.CharField(max_length=55, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'l_directory_list'


class MyPreference(models.Model):
    id = models.IntegerField(primary_key=True)
    country = models.CharField(max_length=45, blank=True, null=True)
    city = models.CharField(db_column='City', max_length=45, blank=True, null=True)  # Field name made lowercase.
    location = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'my_preference'


class PBusinessCategory(models.Model):
    business_category_id = models.AutoField(primary_key=True)
    business_category = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'p_business_category'


class PBusinessSubCategory(models.Model):
    business_sub_category_id = models.AutoField(primary_key=True)
    business_sub_category = models.CharField(max_length=455, blank=True, null=True)
    business_category = models.ForeignKey(PBusinessCategory, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'p_business_sub_category'


class PCity(models.Model):
    city_id = models.AutoField(primary_key=True)
    country = models.ForeignKey('PCountry', models.DO_NOTHING, blank=True, null=True)
    state = models.ForeignKey('PState', models.DO_NOTHING, blank=True, null=True)
    city = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'p_city'


class PCompanyType(models.Model):
    company_type_id = models.AutoField(primary_key=True)
    company_type = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'p_company_type'


class PCountry(models.Model):
    country_id = models.AutoField(primary_key=True)
    shortname = models.CharField(unique=True, max_length=255, blank=True, null=True)
    country = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'p_country'


class PCurrency(models.Model):
    currency_id = models.AutoField(primary_key=True)
    currency = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'p_currency'


class PCurrencyType(models.Model):
    currency_type_id = models.AutoField(primary_key=True)
    currency_type = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'p_currency_type'


class PEmployees(models.Model):
    employee_id = models.AutoField(primary_key=True)
    employee_strength = models.CharField(max_length=60, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'p_employees'


class PLocation(models.Model):
    location_id = models.AutoField(primary_key=True)
    location = models.CharField(max_length=255, blank=True, null=True)
    state = models.ForeignKey('PState', models.DO_NOTHING, blank=True, null=True)
    country = models.ForeignKey(PCountry, models.DO_NOTHING, blank=True, null=True)
    city = models.ForeignKey(PCity, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'p_location'


class PLogo(models.Model):
    logo_url = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'p_logo'


class POffice(models.Model):
    office_type_id = models.AutoField(primary_key=True)
    office_type = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'p_office'


class PState(models.Model):
    state_id = models.AutoField(primary_key=True)
    state = models.CharField(max_length=255, blank=True, null=True)
    country = models.ForeignKey(PCountry, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'p_state'


class Plan(models.Model):
    plan_id = models.AutoField(primary_key=True)
    plan = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'plan'


class QIndustryQuestionAnswer(models.Model):
    iqa_id = models.AutoField(primary_key=True)
    queries = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'q_industry_question_answer'


class QOtherQuestionAnswer(models.Model):
    oqa_id = models.AutoField(primary_key=True)
    queries = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'q_other_question_answer'


class RankCheckFrequency(models.Model):
    frequency_id = models.IntegerField(primary_key=True)
    frequency = models.CharField(max_length=255, blank=True, null=True)
    plan_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rank_check_frequency'


class RankTracker(models.Model):
    website_id = models.CharField(max_length=255, blank=True, null=True)
    keyword_id = models.CharField(max_length=255, blank=True, null=True)
    last_rank = models.CharField(max_length=255, blank=True, null=True)
    last_date = models.DateTimeField(blank=True, null=True)
    present_rank = models.CharField(max_length=255, blank=True, null=True)
    present_date = models.DateTimeField(blank=True, null=True)
    rank_difference = models.CharField(max_length=255, blank=True, null=True)
    result_url = models.CharField(max_length=500, blank=True, null=True)
    local_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rank_tracker'
        unique_together = (('website_id', 'keyword_id'),)


class SerpRankfactor(models.Model):
    website_id = models.IntegerField(primary_key=True)
    domain_authority = models.IntegerField(blank=True, null=True)
    page_authority = models.IntegerField(blank=True, null=True)
    total_backlinks = models.CharField(max_length=55, blank=True, null=True)
    quality_backlinks = models.CharField(max_length=55, blank=True, null=True)
    percentage_quality_backlinks = models.IntegerField(blank=True, null=True)
    moz_trust = models.TextField(blank=True, null=True)
    spam_score = models.IntegerField(blank=True, null=True)
    offpage_seo_score = models.IntegerField(blank=True, null=True)
    alexa_global_ranking = models.IntegerField(blank=True, null=True)
    majestic_trust_flow = models.IntegerField(blank=True, null=True)
    majestic_citatiion_flow = models.IntegerField(blank=True, null=True)
    majestic_indexed_url = models.IntegerField(blank=True, null=True)
    majestic_dofollow_backlinks = models.IntegerField(blank=True, null=True)
    majestic_nofollow_backlinks = models.IntegerField(blank=True, null=True)
    domain_name = models.CharField(max_length=55, blank=True, null=True)
    domain_purchase_date = models.CharField(max_length=55, blank=True, null=True)
    domain_age = models.CharField(max_length=55, blank=True, null=True)
    domain_updated_date = models.CharField(max_length=55, blank=True, null=True)
    domain_expiration_date = models.CharField(max_length=55, blank=True, null=True)
    registrar = models.CharField(max_length=55, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'serp_rankfactor'


class SocialAuthAssociation(models.Model):
    server_url = models.CharField(max_length=255)
    handle = models.CharField(max_length=255)
    secret = models.CharField(max_length=255)
    issued = models.IntegerField()
    lifetime = models.IntegerField()
    assoc_type = models.CharField(max_length=64)

    class Meta:
        managed = False
        db_table = 'social_auth_association'
        unique_together = (('server_url', 'handle'),)


class SocialAuthCode(models.Model):
    email = models.CharField(max_length=254)
    code = models.CharField(max_length=32)
    verified = models.IntegerField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'social_auth_code'
        unique_together = (('email', 'code'),)


class SocialAuthNonce(models.Model):
    server_url = models.CharField(max_length=255)
    timestamp = models.IntegerField()
    salt = models.CharField(max_length=65)

    class Meta:
        managed = False
        db_table = 'social_auth_nonce'
        unique_together = (('server_url', 'timestamp', 'salt'),)


class SocialAuthPartial(models.Model):
    token = models.CharField(max_length=32)
    next_step = models.PositiveSmallIntegerField()
    backend = models.CharField(max_length=32)
    data = models.TextField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'social_auth_partial'


class SocialAuthUsersocialauth(models.Model):
    provider = models.CharField(max_length=32)
    uid = models.CharField(max_length=255)
    extra_data = models.TextField()
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'social_auth_usersocialauth'
        unique_together = (('provider', 'uid'),)


class SpComment(models.Model):
    comment_id = models.AutoField(primary_key=True)
    comment = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sp_comment'


class SpCountry(models.Model):
    country_id = models.IntegerField(primary_key=True)
    country = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sp_country'


class SpDate(models.Model):
    date_id = models.AutoField(primary_key=True)
    date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sp_date'


class SpDay(models.Model):
    date_id = models.IntegerField(primary_key=True)
    date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sp_day'


class SpDayOfWeek(models.Model):
    day_of_week_id = models.IntegerField(primary_key=True)
    day_of_week = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sp_day_of_week'


class SpFestival(models.Model):
    festival_id = models.AutoField(primary_key=True)
    festival = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sp_festival'


class SpGreetingPhrase(models.Model):
    greeting_phrase_id = models.IntegerField(primary_key=True)
    greeting_phrase = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sp_greeting_phrase'


class SpImage(models.Model):
    image_id = models.AutoField(primary_key=True)
    image_url = models.TextField(db_column='Image_url', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'sp_image'


class SpInternationalDay(models.Model):
    international_day_id = models.AutoField(primary_key=True)
    international_day = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sp_international_day'


class SpPost(models.Model):
    post_id = models.AutoField(primary_key=True)
    festival_id = models.IntegerField(blank=True, null=True)
    post_type_id = models.IntegerField(blank=True, null=True)
    date_id = models.IntegerField(blank=True, null=True)
    international_day_id = models.IntegerField(blank=True, null=True)
    image_id = models.IntegerField(blank=True, null=True)
    country_id = models.IntegerField(blank=True, null=True)
    day_of_week_id = models.IntegerField(blank=True, null=True)
    state_id = models.IntegerField(blank=True, null=True)
    comment_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sp_post'


class SpPostType(models.Model):
    post_type_id = models.IntegerField(primary_key=True)
    post_type = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sp_post_type'


class SpState(models.Model):
    state_id = models.IntegerField(primary_key=True)
    state = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sp_state'


class SpWebsitePost(models.Model):
    id = models.IntegerField(primary_key=True)
    website_id = models.IntegerField(blank=True, null=True)
    date_id = models.DateField(blank=True, null=True)
    post_url = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sp_website_post'


class SpecialMaster(models.Model):
    day = models.CharField(max_length=255, blank=True, null=True)
    special_name = models.TextField(blank=True, null=True)
    rocognize_by = models.CharField(max_length=255, blank=True, null=True)
    local_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'special_master'


class State(models.Model):
    state_id = models.IntegerField(blank=True, null=True)
    state = models.TextField(blank=True, null=True)
    country_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'state'


class Website(models.Model):
    website_id = models.AutoField(primary_key=True)
    website = models.CharField(unique=True, max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'website'


class WebsiteFields(models.Model):
    country = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=255, blank=True, null=True)
    area = models.CharField(max_length=255, blank=True, null=True)
    category = models.CharField(max_length=255, blank=True, null=True)
    offer_type = models.CharField(max_length=255, blank=True, null=True)
    registered_by = models.CharField(max_length=255, blank=True, null=True)
    employees_strength = models.CharField(max_length=255, blank=True, null=True)
    industry = models.CharField(max_length=255, blank=True, null=True)
    industry_type = models.CharField(max_length=255, blank=True, null=True)
    state = models.CharField(max_length=255, blank=True, null=True)
    currency = models.CharField(max_length=255, blank=True, null=True)
    currency_type = models.CharField(max_length=255, blank=True, null=True)
    sub_category = models.CharField(max_length=255, blank=True, null=True)
    office_type = models.CharField(max_length=255, blank=True, null=True)
    url = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'website_fields'


class WebsiteKeywordTable(models.Model):
    website_id = models.CharField(max_length=255, blank=True, null=True)
    keyword_id = models.CharField(max_length=255, blank=True, null=True)
    call_success = models.IntegerField(blank=True, null=True)
    local_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'website_keyword_table'
