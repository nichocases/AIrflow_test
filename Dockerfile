FROM apache/airflow:2.2.4

WORKDIR ${AIRFLOW_HOME}

RUN mkdir ${AIRFLOW_HOME}/tmp

COPY airflow-master-3f991488292a.json .

RUN pip install --upgrade pip \
  && pip install 'apache-airflow-providers-google'



USER airflow
