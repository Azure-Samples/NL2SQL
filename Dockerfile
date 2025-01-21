FROM mcr.microsoft.com/azureml/promptflow/promptflow-runtime:latest

# Install ODBC PostgreSQL driver
RUN apt-get update && apt-get install -y \
    unixodbc \
    unixodbc-dev \
    odbc-postgresql \
    && rm -rf /var/lib/apt/lists/*

    # Install Python packages
COPY requirements.txt /tmp/requirements.txt
RUN pip install --upgrade pip && \
    pip install -r /tmp/requirements.txt

# Clean /etc/odbcinst.ini
RUN echo "" > /etc/odbcinst.ini

# Update /etc/odbcinst.ini
RUN echo "[PostgreSQL Unicode]" >> /etc/odbcinst.ini && \
    echo "Description = PostgreSQL ODBC driver (Unicode version)" >> /etc/odbcinst.ini && \
    echo "Driver = /usr/lib/x86_64-linux-gnu/odbc/psqlodbcw.so" >> /etc/odbcinst.ini
