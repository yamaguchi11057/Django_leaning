from .settings_common import *

#デバッグモードをゆうこにするか否か
DEBUG = False

#許可するホスト名のリスト
ALLOWED_HOSTS = [os.environ.get('ALLOWED_HOSTS')]

#静定期ファイルを配置する場所
STATIC_ROOT = '/usr/share/nginx/html/static'
MEDIA_ROOT = '/usr/share/nginx/html/media'

#AmazonSES関連設定
AWS_SES_ACCESS_KEY_ID = os.environ.get('AWS_SES_ACCESS_KEY_ID')
AWS_SES_SCRETE_ACCESS_KEY =os.environ.get('AWS_SES_SECRETE_ACCES_KEY')
EMAIL_BACKEND = 'django_ses.SESBackend'

#ロギング
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,

    #ロガーの設定
    'loggers':{
        #Djangoの利用するロガー
        'django':{
            'handlers':['file'],
            'level':'INFO',
        },

        'tobuyapp':{
            'handlers':['file'],
            'level':'INFO'
        },
    },

    #ハンドラの設定
    'handlers':{
        'file':{
            'level':'INFO',
            'class':'logging.handlers.TimedRotatingFileHandler',
            'filename':os.path.join(BASE_DIR, 'logs/django.log'),
            'formatter':'prod',
            'when':'D',#ログローテーション（新しいファイルへの切り替え）間隔の単位（D=日）
            'interval': 1,#ログローテーション間隔（1日）
            'backupCount': 7,#保存しておくログファイル数
        },
    },

    #フォーマッタの設定
    'formatters':{
        'prod':{
            'format':'  '.join([
                '%(asctime)s',
                '[%(levelname)s]'
                '%(pathname)s(Line:%(lineno)d',
                '%(message)s'
            ])
        },
    }
}