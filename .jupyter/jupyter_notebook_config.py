import os
import IPython.lib

from s3contents import S3ContentsManager

c = get_config()

### Password protection ###
# http://jupyter-notebook.readthedocs.io/en/latest/security.html
passwd = os.environ['JUPYTER_NOTEBOOK_PASSWORD']
c.NotebookApp.password = IPython.lib.passwd(passwd)
c.NotebookApp.iopub_data_rate_limit=1.0e10

if os.environ.get('AWS_BUCKET_NAME'):
    c.NotebookApp.contents_manager_class = S3ContentsManager
    c.S3ContentsManager.access_key_id = os.environ.get('AWS_ACCESS_KEY_ID')
    c.S3ContentsManager.secret_access_key = os.environ.get('AWS_SECRET_ACCESS_KEY')
    c.S3ContentsManager.bucket = os.environ.get('AWS_BUCKET_NAME')
