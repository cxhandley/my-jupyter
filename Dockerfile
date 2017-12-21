FROM kaggle/python:latest

ADD .jupyter/jupyter_notebook_config.py /root/.jupyter/

RUN pip install s3contents

ADD start_jupyter /opt/bin/
ENV PATH="$PATH:/opt/bin"
RUN chmod 755 /opt/bin/start_jupyter
EXPOSE 8888
CMD ["/bin/bash", "start_jupyter"]
